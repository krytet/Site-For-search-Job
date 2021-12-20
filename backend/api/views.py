from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters
from .filters import VacancyFilter


from .models import (Location, Skill, ProfessionalArea, Speciality, Resume,
                     Vacancy, Responses, Chat, Massage)
from .serializers import (LocationSerializer, SkillSerializer,
                          ProfessionalAreaSerializer, SpecialitySerializer,
                          ResumeSerializer,VacancySerializer,
                          ResponsesSerializer, ChatSerializer, MassageSerializer
                          )


USer = get_user_model()


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class ProfessionalAreaViewSet(ModelViewSet):
    queryset = ProfessionalArea.objects.all()
    serializer_class = ProfessionalAreaSerializer


class SpecialityViewSet(ModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer


class ResumeViewSet(ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer


class VacancyViewSet(ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = VacancyFilter



class ResponsesViewSet(ModelViewSet):
    queryset = Responses.objects.all()
    serializer_class = ResponsesSerializer


class ChatViewSet(ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class MassageViewSet(ModelViewSet):
    queryset = Massage.objects.all()
    serializer_class = MassageSerializer


