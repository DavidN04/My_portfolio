from django.contrib import admin
from .models import Project, Image

class ImageInline(admin.StackedInline):
	model = Image
	extra = 2

class ProjectAdmin(admin.ModelAdmin):
	model = Project
	list_display = ["name", "slug", "url_repository", "description", "status"]
	fields = ["name", "slug", "url_repository", "description", "status"]
	list_display_links = ["name", "slug"]
	list_editable = ["status"]
	list_filter = ["created", "name", "slug", "status"]
	search_fields = ["name", "slug", "description"]

	inlines = [ImageInline]

class ImageAdmin(admin.ModelAdmin):
	fields = ["name", "project", "image"]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Image, ImageAdmin)

# Register your models here.
