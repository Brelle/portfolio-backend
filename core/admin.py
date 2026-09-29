from django.contrib import admin
from .models import Skill, Project, Experience, Education, ContactMessage


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'level')
    list_filter = ('category',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'technologies', 'created_at')
    search_fields = ('name', 'description')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'company', 'order')
    ordering = ('order',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'school', 'order')
    ordering = ('order',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'sujet', 'envoye_le', 'lu')
    list_filter = ('lu',)
    readonly_fields = ('envoye_le',)