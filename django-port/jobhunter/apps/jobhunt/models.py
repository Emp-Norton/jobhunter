from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)

class Role(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)

class Resume(models.Model):
    body = models.TextField()
    name = models.CharField(max_length=255)

class CoverLetter(models.Model):
    body = models.TextField()
    name = models.CharField(max_length=255)

class Application(models.Model):
    coverletter = models.ForeignKey(CoverLetter, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    date_submitted = models.DateField()