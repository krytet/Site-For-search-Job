from collections import OrderedDict
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import (Location, Skill, ProfessionalArea, Speciality, Resume,
                     Vacancy, Responses, Chat, Massage, EXPERIANCE, EDUCATION,
                     SCHEDULE, TYPE_EMPLOYMENT, STATUS)


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email',
                  'number']


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = '__all__'


class ProfessionalAreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProfessionalArea
        fields = '__all__'


class SpecialitySerializer(serializers.ModelSerializer):
    professional_area = ProfessionalAreaSerializer()

    class Meta: 
        model = Speciality
        fields = '__all__'


class ShowResumeSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    location = LocationSerializer()
    skills = SkillSerializer(many=True)
    speciality = SpecialitySerializer()
    experience = serializers.SerializerMethodField()
    education = serializers.SerializerMethodField()
    type_employment = serializers.SerializerMethodField()
    work_schedule = serializers.SerializerMethodField()

    class Meta:
        model = Resume
        fields = '__all__'

    def api_choices(self, id, name):
        dic = {
            'id' : id,
            'name' : name
        }
        return dic

    def get_experience (self, obj):
        result = self.api_choices(EXPERIANCE[obj.experience-1][0],
                                  EXPERIANCE[obj.experience-1][1])
        return result

    def get_education (self, obj):
        result = self.api_choices(EDUCATION[obj.education-1][0],
                                  EDUCATION[obj.education-1][1])
        return result

    def get_type_employment (self, obj):
        result = self.api_choices(TYPE_EMPLOYMENT[obj.type_employment-1][0],
                                  TYPE_EMPLOYMENT[obj.type_employment-1][1])
        return result

    def get_work_schedule (self, obj):
        result = self.api_choices(SCHEDULE[obj.work_schedule-1][0],
                                  SCHEDULE[obj.work_schedule-1][1])
        return result
    


class ResumeSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Resume
        fields = '__all__'

    def to_representation(self, data):
        fields = ShowResumeSerializer(data, context=self.context)
        return OrderedDict(fields.data)


class ShowVacancySerializer(serializers.ModelSerializer):
    author = UserSerializer()
    location = LocationSerializer()
    skills = SkillSerializer(many=True)
    speciality = SpecialitySerializer()
    experience = serializers.SerializerMethodField()
    education = serializers.SerializerMethodField()
    type_employment = serializers.SerializerMethodField()
    work_schedule = serializers.SerializerMethodField()

    class Meta:
        model = Vacancy
        fields = '__all__'   

    def api_choices(self, id, name):
        dic = {
            'id' : id,
            'name' : name
        }
        return dic
    
    def get_experience (self, obj):
        result = self.api_choices(EXPERIANCE[obj.experience-1][0],
                                  EXPERIANCE[obj.experience-1][1])
        return result

    def get_education (self, obj):
        result = self.api_choices(EDUCATION[obj.education-1][0],
                                  EDUCATION[obj.education-1][1])
        return result

    def get_type_employment (self, obj):
        result = self.api_choices(TYPE_EMPLOYMENT[obj.type_employment-1][0],
                                  TYPE_EMPLOYMENT[obj.type_employment-1][1])
        return result

    def get_work_schedule (self, obj):
        result = self.api_choices(SCHEDULE[obj.work_schedule-1][0],
                                  SCHEDULE[obj.work_schedule-1][1])
        return result


class VacancySerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        queryset=Location.objects.all(),
        slug_field='name'
    )
    speciality = serializers.SlugRelatedField(
        queryset=Speciality.objects.all(),
        slug_field='name'
    )
    # TODO настроить под сериализатор skills
    skills = serializers.ListField()

    class Meta:
        model = Vacancy
        fields = ['name', 'location', 'skills', 'speciality', 'experience',
                  'education', 'type_employment', 'work_schedule', 'salary',
                  'remote_work', 'discription', 'short_discription']
    
    def validate_skills(self, data):
        for num_skill in range(len(data)):
            data[num_skill], _ = Skill.objects.get_or_create(name=data[num_skill])
        return data

    def to_representation(self, data):
        fields = ShowVacancySerializer(data, context=self.context)
        return OrderedDict(fields.data)


class ShowResponsesSerializer(serializers.ModelSerializer):
    resume = ResumeSerializer()
    vacancy = VacancySerializer()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Responses
        fields = '__all__'

    def get_status(self, obj):
        result = {
            'id': obj.status,
            'name': ''
        }
        for item in STATUS:
            if item[0] == result['id']:
                result['name'] = item[1]
                break
        return result


class ResponsesSerializer(serializers.ModelSerializer):
    #resume = ResumeSerializer()
    #vacancy = VacancySerializer()

    class Meta:
        model = Responses
        fields = '__all__'

    def to_representation(self, data):
        fields = ShowResponsesSerializer(data, context=self.context)
        return OrderedDict(fields.data)


class MassageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Massage
        fields = '__all__'


class ChatSerializer(serializers.ModelSerializer):
    massage = MassageSerializer(many=True)
    members = UserSerializer(many=True)

    class Meta:
        model = Chat
        fields = '__all__'


