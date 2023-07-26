from django.db import models

# Create your models here.
class Women(models.Model):
    title = models.CharField(max_length=225)
    coutent = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='images')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

