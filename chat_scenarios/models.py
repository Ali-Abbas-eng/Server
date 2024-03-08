# chat_scenario/models.py
from django.db import models
from django.conf import settings

class ChatScenario(models.Model):
    id = models.AutoField(primary_key=True)
    socket_url = models.CharField(verbose_name="Socket URL", max_length=1000)
    name = models.CharField(max_length=255)
    description = models.TextField(default="")
    number_of_messages = models.IntegerField(default=15)
    background = models.ImageField(upload_to='chat_scenarios/background', null=True, blank=True)
    image = models.ImageField(upload_to='chat_scenarios/image', null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def background_url(self):
        if self.background and hasattr(self.background, 'url'):
            return self.background.url
        else:
            return ""

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return ""
