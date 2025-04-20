from django.contrib import admin
from .models import Category, AnonymousUser, Confession, Comment, Report

# Register your models here.

admin.site.register(Category)
admin.site.register(AnonymousUser)
admin.site.register(Confession)
admin.site.register(Comment)
admin.site.register(Report)