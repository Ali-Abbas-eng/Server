from django.db import models


class ChatScenario(models.Model):
    id = models.AutoField(primary_key=True)
    socket_url = models.CharField(verbose_name="Socket URL", max_length=1000)
    name = models.CharField(max_length=255)
    description = models.TextField(default="")
    number_of_messages = models.IntegerField(default=15)

    def __str__(self):
        return self.name
