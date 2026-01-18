from django.db import models
from django.contrib.auth.models import User

# ----------------------------
# Portfolio-related models
# ----------------------------

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    url = models.URLField("Project URL", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title


class Photography(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="photography/", blank=True, null=True)
    url = models.URLField("Image URL", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Photography"
        verbose_name_plural = "Photographies"

    def __str__(self):
        return self.title


class Videography(models.Model):
    title = models.CharField(max_length=200)
    video_file = models.FileField(upload_to="videos/", blank=True, null=True)
    url = models.URLField(
        "Video URL",
        blank=True, 
        null=True,
        help_text="Paste a video URL (Cloudinary, YouTube, Instagram, etc.)"
    )
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Videography"
        verbose_name_plural = "Videographies"

    def __str__(self):
        return self.title


# ----------------------------
# Contact form submissions
# ----------------------------

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    attachment = models.FileField("Attachment (optional)", blank=True, null=True)
    url = models.URLField("Attachment URL (optional)", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"{self.name} - {self.subject}"


# ----------------------------
# Optional: Extend user profile
# ----------------------------

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    avatar_url = models.URLField("Avatar URL", blank=True, null=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.user.username
