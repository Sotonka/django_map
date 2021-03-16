from django.db import models
from django.contrib.auth.models import User
import uuid


class UnverifiedTag(models.Model):
    """
    Метка от неавторизованного пользователя
    name: название метки
    description: описание
    image: адрес изображения
    location: местоположение
    x_coord: координата x
    y_coord: координата y
    username: имя пользователя
    email:  email ользователя
    """
    def images_directory_path(instance, filename):
        return '/'.join(['images', str(uuid.uuid4().hex + ".png")])

    name = models.CharField('Название', max_length=30)
    description = models.TextField('Описание', max_length=100)
    image = models.FileField('Изображение', upload_to=images_directory_path,
                             default="no pic", blank=True)
    location = models.CharField('Местоположение', max_length=30)
    x_coord = models.FloatField('Координата X')
    y_coord = models.FloatField('Координата Y')
    username = models.CharField('Имя пользователя', max_length=30)
    email = models.EmailField('Email', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Метка(неавторизованный)'
        verbose_name_plural = 'Метки(неавторизованный)'


class Tag(models.Model):
    """
    Метка от авторизованного пользователя
    name: название метки
    description: описание
    image: адрес изображения
    location: местоположение
    x_coord: координата x
    y_coord: координата y
    user: внешний ключ
    """
    def images_directory_path(instance, filename):
        return '/'.join(['images', str(uuid.uuid4().hex + ".png")])

    name = models.CharField('Название', max_length=30)
    description = models.TextField('Описание', max_length=100)
    image = models.ImageField('Изображение', upload_to=images_directory_path,
                              default="no pic")
    location = models.CharField('Местоположение', max_length=30)
    x_coord = models.FloatField('Координата X')
    y_coord = models.FloatField('Координата Y')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Метка'
        verbose_name_plural = 'Метки'
