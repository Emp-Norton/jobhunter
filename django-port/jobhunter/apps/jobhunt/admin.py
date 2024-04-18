from django.contrib import admin
from .models import Company, Application, Resume, Role, CoverLetter


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company')

admin.site.register(Company)
admin.site.register(Application)
admin.site.register(Resume)
admin.site.register(Role)
admin.site.register(CoverLetter)