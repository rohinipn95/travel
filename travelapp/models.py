from django.db import models

# Create your models here.
class meet_team(models.Model):
    name = models.CharField(max_length=256)
    photo=models.ImageField(upload_to='pic')
    about=models.TextField()

    def __str__(self):
        return self.name

