from django.db import models
import uuid
from django.utils.text import slugify
from users.models import Profile


class Project(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True,
                              on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    project_image = models.ImageField(null=True, blank=True,
                                      upload_to="projects/",
                                      default="projects/default.jpg", )
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField("Tag", blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)

    slug = models.SlugField(default="", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,
                          editable=False)


    def update_vote_stats(self):
        reviews = self.review_set.all()
        total_votes = reviews.count()

        up_vote = reviews.filter(value="up").count()
        ratio = (up_vote / total_votes) * 100
        print(ratio)
        self.vote_total = total_votes
        self.vote_ratio = ratio

        self.save()

    def reviewers(self):
        query_set = self.review_set.all().values_list("owner__id",flat=True)
        return query_set

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

        if self.slug is None:
            self.slug = slugify(self.title)
            self.save()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-vote_ratio", "-vote_total", "title"]


class Review(models.Model):
    VOTED = (
        ("up", "Up Vote"),
        ("down", "Down Vote"),
    )

    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTED)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    class Meta:
        unique_together = [["owner", "project"]]


    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,
                          editable=False)

    def __str__(self):
        return self.name
