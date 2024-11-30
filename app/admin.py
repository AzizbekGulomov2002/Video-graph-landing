from django.contrib import admin
from .models import Slide, Service, Statistic, Team, Blog, AboutUs, TypePortfolio, Portfolio, Message,Gallery

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')

@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ('name', 'count')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('email', 'address')

@admin.register(TypePortfolio)
class TypePortfolioAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'video', 'image')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'website', 'message')

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_url', 'size_class')
    list_filter = ('size_class', 'video_type')
    search_fields = ('title',)