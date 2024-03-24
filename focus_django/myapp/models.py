from django.db import models

# Create your models here.


class URLSummary(models.Model):
    url = models.TextField()
    prompt = models.TextField()


    # summary = models.TextField()

class Project(models.Model):
    # intent = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    urls_and_summaries = models.ManyToManyField('myapp.URLSummary', related_name='urls_and_summaries')
    # urls_and_clean_summaries = models.ManyToManyField('myapp.URLSummary', related_name='urls_and_clean_summaries')
    # executive_summary = models.TextField()