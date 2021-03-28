from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 100)
    techs = models.CharField(max_length = 75)
    description = models.TextField(max_length = 250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank = True)

    def __str__(self):
        return self.title


class About(models.Model):
    text = models.TextField()
