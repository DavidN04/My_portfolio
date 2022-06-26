from django.db import models
from django.urls import reverse

class Project(models.Model):
	name = models.CharField(max_length=80, unique=True, help_text="Имя проекта", verbose_name="Имя проекта")
	slug = models.SlugField(max_length=80, unique=True, help_text="Slug проекта", verbose_name="Slug проекта")
	url_repository = models.URLField(max_length=500, help_text="Ссылка на репозиторий проекта", verbose_name="Ссылка на репозиторий проекта")
	description = models.TextField(help_text="Описание проекта", verbose_name="Описание проекта")
	created = models.DateTimeField(auto_now_add=True)
	status = models.BooleanField(default=True, help_text="Опубликовать проект?", verbose_name="Статус проекта")

	class Meta:
		ordering = ('created', )
		verbose_name = "Проект"
		verbose_name_plural = "Проекты"

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		pass

class Image(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE, help_text="Проект", verbose_name="Проект")
	name = models.CharField(max_length=60, unique=True, help_text="Подпись к изображению", verbose_name="Подпись к изображению")
	image = models.ImageField(upload_to="project_image", help_text="Изображение к проекту", verbose_name="Изображение к проекту")
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('name', )
		verbose_name = "Изображение к проекту"
		verbose_name_plural = "Изображения к проектам"

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		pass
# Create your models here.
