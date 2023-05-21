import os

from django.db import models
from django.dispatch import receiver


class MyPost(models.Model):
    text = models.TextField(default=None, null=True, blank=True)
    file = models.FileField(default=None, null=True, blank=True, upload_to='uploaded_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    ip = models.TextField(default=None, null=True, blank=True)


@receiver(models.signals.post_delete, sender=MyPost)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)
