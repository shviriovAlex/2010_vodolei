from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


@admin.register(Целевые, Членские, Электроэнергия)
class ViewAdmin(ImportExportModelAdmin):
    pass


@admin.register(Главная, ДоскаПозора)
class ForCommunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish')
    list_filter = ('publish',)
    search_fields = ('title', 'body')  # добавляем поиск
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ('publish',)


@admin.register(Тарифы_Электр_Газ)
class ElGAs(admin.ModelAdmin):
    list_display = ('дата_от', )


@admin.register(АдминистрацияСТ, Правление, Уполномоченные, РевизионнаяКомиссия, СчетнаяКомиссия)
class LeadershipAdmin(admin.ModelAdmin):
    list_display = ('title', 'ФИО', 'Должность')
    search_fields = ('title', 'ФИО', 'Должность')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Протоколы_Собраний)
class ProtocolsAdmin(admin.ModelAdmin):
    list_display = ('title', 'document',)
    search_fields = ('title', 'document')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(AllPhoto)
class BaseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Photo)
class BaseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
