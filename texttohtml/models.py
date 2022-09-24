from django.db import models

# Create your models here.

from ckeditor.fields import RichTextField

class Post(models.Model):
    body = RichTextField(blank=True,null=True) 