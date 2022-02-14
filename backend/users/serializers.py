from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model


User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=150, required=True,
                                     write_only=True
                                     )


    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email',
                  'image', 'patronymic', 'is_company', 'number', 'password']
    
    # Проверка соотвествия пароля
    def validate_password(self, data):
        validate_password(password=data, user=User)
        return data

    # Создание аккауна пользователя
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
