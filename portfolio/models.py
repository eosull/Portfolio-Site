from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    date = models.DateField()
    description = models.TextField()
    code_link = models.URLField(max_length=200, blank=True)
    live_link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title
    
    def live(self):
        if live_link:
            return True
        else:
            return False