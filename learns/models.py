from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

from django.db import models
from django.db.models import indexes

private_storage = FileSystemStorage(location=settings.PRIVATE_STORAGE_ROOT)

class Post(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = 'Posts'

    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey('MyProfile', on_delete=models.CASCADE, related_name='posts', null=True)
    upload = models.FileField(storage=private_storage, null=True)
    image = models.ImageField(upload_to='poster/', null=True)

    def __str__(self):
        return self.title

class MyProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    home_page = models.URLField(max_length=255, blank=True)
    icq = models.IntegerField(null=True)

    def __str__(self):
        return self.home_page
