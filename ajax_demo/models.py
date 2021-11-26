from django.db import models


class Post(models.Model):
    posted_by = models.CharField(max_length=50)
    caption = models.TextField(null=True, blank=True)

    def __str__(self):
       return self.posted_by
