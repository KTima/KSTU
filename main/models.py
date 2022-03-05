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