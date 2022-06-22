from django.urls import reverse
from django.db import models
from mainapp.models import Project

class Comment(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE, help_text="Проект", verbose_name="Проект")
	user_name = models.CharField(max_length=255, help_text="Имя автора", verbose_name="Имя автора")
	text = models.TextField(help_text="Текст комментария", verbose_name="Текст комментария")
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ("created", )
		verbose_name = "Комментарий"
		verbose_name_plural = "Комментарии"

	def __str__(self):
		return user_name

# Create your models here.
