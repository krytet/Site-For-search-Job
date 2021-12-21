from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters
from .filters import VacancyFilter
from rest_framework.decorators import action, permission_classes
from rest_framework import permissions, status
from rest_framework.response import Response


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

    # Получение списка своих резюме
    @action(methods=['get'], detail=False,
            permission_classes=permissions.IsAuthenticated)
    def my(self, request, *args, **kwargs):
        resumes = Resume.objects.filter(author=request.user).all()
        serializer = ResponsesSerializer(resumes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class VacancyViewSet(ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = VacancyFilter

    @action(detail=True, methods=['post'],
            permission_classes=[permissions.IsAuthenticated])
    def response(self, request, *args, **kwargs):
        data = {
            'resume': int(request.data['resume']),
            'vacancy': int(kwargs['pk'])
        }
        serializer = ResponsesSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ResponsesViewSet(ModelViewSet):
    queryset = Responses.objects.all()
    serializer_class = ResponsesSerializer


class ChatViewSet(ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class MassageViewSet(ModelViewSet):
    queryset = Massage.objects.all()
    serializer_class = MassageSerializer


