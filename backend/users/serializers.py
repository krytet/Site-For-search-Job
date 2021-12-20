from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email',
                  'image', 'is_company', 'number']
        #fields = '__all__'
