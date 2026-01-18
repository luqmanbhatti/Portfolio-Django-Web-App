from django.contrib import admin
from .models import Project, Photography, Videography, ContactMessage, Profile

# ----------------------------
# Portfolio Models
# ----------------------------
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')      # Columns to show in list view
    search_fields = ('title', 'description')    # Add search box
    list_filter = ('created_at',)               # Filter by date

@admin.register(Photography)
class PhotographyAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)

@admin.register(Videography)
class VideographyAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description', 'url')
    list_filter = ('created_at',)

# ----------------------------
# Contact Messages
# ----------------------------
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('created_at',)

# ----------------------------
# User Profiles
# ----------------------------
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
    search_fields = ('user__username', 'bio')
