from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters
from .filters import VacancyFilter
from rest_framework.decorators import action, permission_classes
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


from .models import (Location, Skill, ProfessionalArea, Speciality, Resume,
                     Vacancy, Responses, Chat, Massage, EXPERIANCE, EDUCATION,
                     SCHEDULE, TYPE_EMPLOYMENT, STATUS)
from .serializers import (LocationSerializer, SkillSerializer,
                          ProfessionalAreaSerializer, SpecialitySerializer,
                          ResumeSerializer,VacancySerializer,
                          ResponsesSerializer, ChatSerializer, MassageSerializer
                          )
from users.serializers import CustomUserSerializer


User = get_user_model()


def create_dict(value, name, items = []):
    dict_prams = {
        'value': value,
        'name': name,
        'items': []
    }
    for item in items:
        dict_prams['items'].append(
            {
                'id': item[0],
                'name': item[1],
            }
        )
    return dict_prams


class FilterParams(ListAPIView):

    def get(self, request, *args, **kwargs):
        params = {
            'radio': [],
            'switch_elements': []
        }
        params['radio'].append(
            create_dict('experience', 'Опыт работы', EXPERIANCE)
        )
        params['radio'].append(
            create_dict('education', 'Образование', EDUCATION)
        )
        params['radio'].append(
            create_dict('work_schedule', 'График работы', SCHEDULE)
        )
        params['radio'].append(
            create_dict('type_employment', 'Тип занятости', TYPE_EMPLOYMENT)
        )
        params['switch_elements'].append(
            create_dict('remote_work', 'Удаленная работа')
        )
        return Response(params)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

    # TODO предлеать результат для вывода значения при авторизации
    @action(methods=['GET'], detail=False)
    def me(self, request, *args, **kwargs):
        instance = request.user
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    # TODO Настроить фронт под поиск
    pagination_class = None


class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class ProfessionalAreaViewSet(ModelViewSet):
    queryset = ProfessionalArea.objects.all()
    serializer_class = ProfessionalAreaSerializer


class SpecialityViewSet(ModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer
    # TODO Настроить фронт под поиск
    pagination_class = None


class ResumeViewSet(ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # Получение списка своих резюме
    @action(methods=['get'], detail=False,
            permission_classes=[permissions.IsAuthenticated])
    def my(self, request, *args, **kwargs):
        print(request.user)
        resumes = Resume.objects.filter(author=request.user).all()
        serializer = ResumeSerializer(resumes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class VacancyViewSet(ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = VacancyFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

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

    @action(detail=False, methods=['get'],
            permission_classes=[permissions.IsAuthenticated])
    def my(self, request, *args, **kwargs):
        responses = Responses.objects.filter(resume__author=request.user).order_by('-id').all()
        queryset = self.filter_queryset(responses)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



class ChatViewSet(ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class MassageViewSet(ModelViewSet):
    queryset = Massage.objects.all()
    serializer_class = MassageSerializer


