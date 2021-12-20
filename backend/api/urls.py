from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter


from .views import (LocationViewSet, SkillViewSet, ProfessionalAreaViewSet,
                    SpecialityViewSet, ResumeViewSet, VacancyViewSet,
                    ResponsesViewSet, ChatViewSet, MassageViewSet
                    )

router = DefaultRouter()
router.register('locations', LocationViewSet, basename='locations')
router.register('skills', SkillViewSet, basename='skills')
router.register('prof-areas', ProfessionalAreaViewSet, basename='prof-areas')
router.register('specialists', SpecialityViewSet, basename='specialists')
router.register('resumes', ResumeViewSet, basename='resumes')
router.register('vacancies', VacancyViewSet, basename='vacancies')
router.register('responses', ResponsesViewSet, basename='responses')
router.register('chats', ChatViewSet, basename='chats')
router.register('massages', MassageViewSet, basename='massages')


urlpatterns = [
    path('', include(router.urls))
]