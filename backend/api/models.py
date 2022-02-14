from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

EXPERIANCE = (
    (1, 'Нет опыта'),
    (2, 'До 1 года'),
    (3, 'От 1 до 3 лет'),
    (4, 'От 3 до 6 лет'),
    (5, 'Более 6 лет'),
)

EDUCATION = (
    (1, 'Среднее'),
    (2, 'Среднее спецальное'),
    (3, 'Неполное высшие'),
    (4, 'Высшее'),
)

SCHEDULE = (
    (1, 'Полный день'),
    (2, 'Сменный режим'),
    (3, 'Гибкий график'),
    (4, 'Вахтовый метод'),
)

TYPE_EMPLOYMENT = (
    (1, 'Полная занятость'),
    (2, 'Частичная занятость'),
    (3, 'Стажировка'),
    (4, 'Проектная работа'),
    (5, 'Волонтерство'),
)

STATUS = (
    (1, 'Не просмотрен'),
    (2, 'Просмотрен'),
    (3, 'Отказ'),
    (4, 'Приглашен'),
    (5, 'Архив'),
)

class Location(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название города')

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположение'
    
    def __str__(self):
        return f"{self.pk} {self.name}"
        

class Skill(models.Model):
    name = models.CharField(max_length=255, verbose_name='Навык')

    class Meta:
        verbose_name = 'Навыки'
        verbose_name_plural = 'Навыки'
    
    def __str__(self):
        return self.name


class ProfessionalArea(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название облости')

    class Meta:
        verbose_name = 'Професианальная облость'
        verbose_name_plural = 'Професианальная облость'
    
    def __str__(self):
        return self.name


class Speciality(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name='Название спецальности')
    professional_area = models.ForeignKey(
        ProfessionalArea, on_delete=models.CASCADE, related_name='speciality',
        verbose_name='Професианальная область'
    )

    class Meta:
        verbose_name = 'Спецализация'
        verbose_name_plural = 'Спецализация'
    
    def __str__(self):
        return f'{self.name} в {self.professional_area.name}'


class Resume(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='resume')
    name = models.CharField(max_length=255, verbose_name='Название должности')
    location = models.ForeignKey(
        Location, on_delete=models.PROTECT, related_name='resume',
        verbose_name='Метоположение'
    )
    salary = models.IntegerField(null=True, verbose_name='Зарплата', blank=True)
    skills = models.ManyToManyField(Skill, related_name='resume',
                                    verbose_name='Навыки')
    speciality = models.ForeignKey(
        Speciality, on_delete=models.PROTECT, related_name='resume',
        verbose_name='Спецальность'
    )
    experience = models.IntegerField(choices=EXPERIANCE,
                                     verbose_name='Опыт работы')
    education = models.IntegerField(choices=EDUCATION,
                                    verbose_name='Образование')
    type_employment = models.IntegerField(choices=TYPE_EMPLOYMENT, 
                                          verbose_name='Тип занятости')
    work_schedule = models.IntegerField(choices=SCHEDULE,
                                        verbose_name='График работы')
    remote_work = models.BooleanField(default=False,
                                      verbose_name='Удаленная работа')

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'
    
    def __str__(self):
        return f'{self.author.get_full_name()} с резюме {self.name}'


class Vacancy(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='vacancy',
                               verbose_name='Автор вакансии')
    name = models.CharField(max_length=255, verbose_name='Название вакансии')
    short_discription = models.CharField(max_length=255, blank=True,
                                         verbose_name='Короткое описание')
    discription = models.TextField(verbose_name='Описание вакансии')
    location = models.ForeignKey(
        Location, on_delete=models.PROTECT, related_name='vacancy',
        verbose_name='Метоположение'
    )
    salary = models.IntegerField(null=True, verbose_name='Зарплата')
    skills = models.ManyToManyField(Skill, related_name='vacancy',
                                    verbose_name='Навыки')
    speciality = models.ForeignKey(
        Speciality, on_delete=models.PROTECT, related_name='vacancy',
        verbose_name='Спецальность'
    )
    experience = models.IntegerField(choices=EXPERIANCE,
                                     verbose_name='Опыт работы')
    education = models.IntegerField(choices=EDUCATION,
                                    verbose_name='Образование')
    type_employment = models.IntegerField(choices=TYPE_EMPLOYMENT, 
                                          verbose_name='Тип занятости')
    work_schedule = models.IntegerField(choices=SCHEDULE,
                                        verbose_name='График работы')
    remote_work = models.BooleanField(default=False,
                                      verbose_name='Удаленная работа')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансия'
        ordering = ['-id']
    
    def __str__(self):
        return f'{self.author.get_full_name()} с резюме {self.name}'

    
class Responses(models.Model):
    resume = models.ForeignKey(
        Resume, on_delete=models.PROTECT, related_name='respomses',
        verbose_name='Резюме'
    )
    vacancy = models.ForeignKey(
        Vacancy, on_delete=models.CASCADE, related_name='responses',
        verbose_name='Вакансия'
    )
    status = models.IntegerField(choices=STATUS, verbose_name='Статус отклика',
                                 default=1)

    class Meta:
        verbose_name = 'Отклики'
        verbose_name_plural = 'Отклики'
    
    def __str__(self):
        return f'Отклик {self.resume} на {self.vacancy} - {self.status}'


class Chat(models.Model):
    members = models.ManyToManyField(User, related_name='chat',
                                     verbose_name='участкника чата')

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чат'

    def __str__(self):
        string = ''
        for member in self.members.all():
            string = string + str(member) + ', '
        return string
    

class Massage(models.Model):
    chat = models.ForeignKey(
        Chat, on_delete=models.CASCADE, related_name='massage',
        verbose_name='Чат'
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='message', null=True,
        verbose_name='Автор Сообщения'
    )
    text = models.TextField(verbose_name='Текст сообщения')

    class Meta:
        verbose_name = 'Сообщения'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return f'От {self.author}, где участники ({self.chat}),  сообщение {self.text}'
        