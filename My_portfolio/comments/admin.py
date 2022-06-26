from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
	fields = ["user_name", "project", "text"]
	list_filter = ["user_name", "project"]
	search_fields = ["text"]

admin.site.register(Comment, CommentAdmin)
# Register your models here.
