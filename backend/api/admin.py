from django.contrib import admin
from . import models


class ResumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'salary')
    list_filter = ('experience', 'education', 'type_employment',
                   'work_schedule', 'remote_work', )
    search_fields = ('id', 'name')


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'salary')
    list_filter = ('experience', 'education', 'type_employment',
                   'work_schedule', 'remote_work', )
    search_fields = ('id', 'name', 'author')


class ResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'resume', 'vacancy', 'status')
    list_filter = ('status', )


admin.site.register(models.Location)
admin.site.register(models.Skill)
admin.site.register(models.ProfessionalArea)
admin.site.register(models.Speciality)
admin.site.register(models.Resume, ResumeAdmin)
admin.site.register(models.Vacancy, VacancyAdmin)
admin.site.register(models.Responses, ResponseAdmin)
admin.site.register(models.Chat)
admin.site.register(models.Massage)