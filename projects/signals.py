from django.db.models.signals import post_save
from .models import Project, Review


def create_review_vote(sender, instance, created, **kwargs):
    if created:
        project = instance.project
        project.update_vote_stats()


def set_default_image_on_clear(sender, instance, **kwargs):

    if not instance.project_image and instance.project_image.name != instance.DEFAULT_PROJECT_IMAGE_PATH :
        instance.project_image = instance.DEFAULT_PROJECT_IMAGE_PATH
        instance.save()

post_save.connect(create_review_vote, sender=Review)
post_save.connect(set_default_image_on_clear, sender=Project)