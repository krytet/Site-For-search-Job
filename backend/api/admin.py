from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Location)
admin.site.register(models.Skill)
admin.site.register(models.ProfessionalArea)
admin.site.register(models.Speciality)
admin.site.register(models.Resume)
admin.site.register(models.Vacancy)
admin.site.register(models.Responses)
admin.site.register(models.Chat)
admin.site.register(models.Massage)