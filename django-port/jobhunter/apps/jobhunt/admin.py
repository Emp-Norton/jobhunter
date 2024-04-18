from django.contrib import admin
from .models import Company, Application, Resume, Role, CoverLetter


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company')

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'coverletter', 'resume', 'role', 'date_submitted')

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'body')

class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'description')

class CoverLetterAdmin(admin.ModelAdmin):
    list_display = ('id', 'body', 'name')

admin.site.register(Company)
admin.site.register(Application)
admin.site.register(Resume)
admin.site.register(Role)
admin.site.register(CoverLetter)