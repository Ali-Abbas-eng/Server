# Generated by Django 4.0.1 on 2024-03-23 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_scenarios', '0002_chatscenario_background_chatscenario_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatscenario',
            name='language',
            field=models.CharField(default='english', max_length=100),
            preserve_default=False,
        ),
    ]
