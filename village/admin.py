from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


@admin.register(Целевые, Членские, Электроэнергия)
class ViewAdmin(ImportExportModelAdmin):
    pass


@admin.register(Base)
class BaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish')
    list_filter = ('publish',)
    search_fields = ('title', 'body')  # добавляем поиск
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ('publish',)


@admin.register(ForCommunity)
class ForCommunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish')
    list_filter = ('publish',)
    search_fields = ('title', 'body')  # добавляем поиск
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ('publish',)


@admin.register(MainPage)
class MainPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'text',)
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Leadership)
class LeadershipAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'name',)
    search_fields = ('title', 'name')
    prepopulated_fields = {'slug': ('title',)}




@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'document',)
    search_fields = ('title', 'document')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(RuleInside)
class RuleInsideAdmin(admin.ModelAdmin):
    list_display = ('title', 'document',)
    search_fields = ('title', 'document')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(AllPhoto)
class BaseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Photo)
class BaseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
