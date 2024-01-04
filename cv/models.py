from django.db import models

class ProfessionalExperience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    skills = models.CharField(max_length=200)

    def __str__(self):
        return self.title    

    def current_position(self):
        if end_date:
            return False
        else:
            return "Present"

