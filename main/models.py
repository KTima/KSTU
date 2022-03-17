from tabnanny import verbose
from django.db import models

# Create your models here.


class News(models.Model):
    images = models.ImageField("Изображение статьи",blank=True,null=True)
    tittle = models.CharField("Название статьи",max_length=250)
    full_text = models.TextField("Статья")
    date = models.DateField("Дата публикации")

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

    def __str__(self) :
        return self.tittle

    class Meta:
        verbose_name = "Программа"
        verbose_name_plural = "Программы"