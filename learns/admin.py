from django.contrib import admin

from learns.models import Post, MyProfile


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "body", 'author']

@admin.register(MyProfile)
class MyProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'home_page', 'icq']