from django.db.models.signals import post_save
from .models import Project, Review

def create_review_vote(sender, instance, created, **kwargs):
    if created:
        project = instance.project
        project.update_vote_stats()

post_save.connect(create_review_vote, sender=Review)