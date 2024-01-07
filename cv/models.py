from django.db import models

class Personal(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

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

class AcademicExperience(models.Model):
    level = models.CharField(max_length=200)
    field = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    skills = models.CharField(max_length=200)

    def __str__(self):
        return self.field   

    def currently_studying(self):
        if end_date:
            return False
        else:
            return "Present"

class Links(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    logo = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title