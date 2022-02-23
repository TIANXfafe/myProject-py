from django.contrib import admin
from .models import Classify, Tag, Detail


# Register your models here.
@admin.register(Classify)
class ClassifyAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent_id', 'name', 'creator', 'createdAt')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'creator', 'createdAt')


@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'classify', 'creator', 'createdAt', 'updateAt', 'status')
