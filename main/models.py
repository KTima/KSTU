from cgitb import text
from datetime import datetime
from tabnanny import verbose
from django.db import models

# Create your models here.


class News(models.Model):
    images = models.ImageField("Изображение статьи",blank=True,null=True)
    tittle = models.CharField("Название статьи",max_length=250)
    full_text = models.TextField("Статья")
    date = models.DateTimeField("Дата публикации",auto_now_add=True,null=True,blank=True)

    def __str__(self) :
        return self.tittle

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Programms(models.Model):
    set_choices = [
        ("открыт", 'открыт'),
        ("закрыт", 'закрыт'),
    ]
    tittle = models.CharField("Название программы",max_length=250)
    date = models.DateField("Начало")
    length = models.CharField("Длительность",max_length=155)
    location = models.CharField("Местоположение",max_length=150)
    set = models.CharField("Набор",max_length=50,choices=set_choices,default="закрыт")
    text = models.TextField("Описание")

    def __str__(self) :
        return self.tittle

    class Meta:
        verbose_name = "Программа"
        verbose_name_plural = "Программы"


class Consulting(models.Model):
    name = models.CharField("Имя",max_length=255)
    email = models.EmailField("Почта")
    phone = models.IntegerField("Номер")
    text = models.TextField("Описание")
    date = models.DateTimeField("Время",auto_now_add=True,null=True,blank=True)
    answer = models.BooleanField('Ответ',default=False)

    def __str__(self) :
        return self.name,self.email

    class Meta:
        verbose_name = "Консультация"
        verbose_name_plural = "Консультации"

