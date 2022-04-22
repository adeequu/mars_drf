from django.db import models
from django.conf import settings


def upload_images(instance, filename):
    return 'post/{user}/{filename}'.format(user=instance.user, filename=filename)


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.title

