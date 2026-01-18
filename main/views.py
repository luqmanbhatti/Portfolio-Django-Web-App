from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings
from .models import Project, Videography, Photography

# ---------------------------
# Public Portfolio Pages
# ---------------------------

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def stack_tech(request):
    projects = Project.objects.all().order_by('created_at')  # oldest first
    return render(request, "stack_tech.html", {"projects": projects})

def videography(request):
    videos = Videography.objects.all().order_by('created_at')  # oldest first
    return render(request, "videography.html", {"videos": videos})

def photography_designs(request):
    photos = Photography.objects.all().order_by('created_at')  # oldest first
    return render(request, "photography_designs.html", {"photos": photos})

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message_text = request.POST.get("message")
        subject = f"New Contact Form Message from {name}"
        message_body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_text}"
        send_mail(subject, message_body, settings.DEFAULT_FROM_EMAIL, ['luqmansportfolio@gmail.com'])
        messages.success(request, "Your message has been sent successfully!")
        return render(request, "contact_success.html")
    return render(request, "contact.html")

# ---------------------------
# Authentication
# ---------------------------

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. Please log in.")
            return redirect("main:login")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user:
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}")
                return redirect("main:dashboard")
        messages.error(request, "Invalid login details.")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("main:home")

# ---------------------------
# Dashboard
# ---------------------------

@login_required
def dashboard(request):
    projects = Project.objects.all()
    videos = Videography.objects.all()
    photos = Photography.objects.all()
    return render(request, "dashboard.html", {
        "projects": projects,
        "videos": videos,
        "photos": photos
    })

# ---------------------------
# Stack Tech CRUD
# ---------------------------

@login_required
def add_stack_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        url = request.POST.get("url")
        Project.objects.create(title=title, description=description, image=image, url=url)
        messages.success(request, "Stack Tech post added successfully.")
        return redirect("main:dashboard")
    return render(request, "add_stack_post.html")

@login_required
def edit_stack_post(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        project.title = request.POST.get("title")
        project.description = request.POST.get("description")
        project.url = request.POST.get("url")
        if request.FILES.get("image"):
            project.image = request.FILES.get("image")
        project.save()
        messages.success(request, "Stack Tech post updated successfully.")
        return redirect("main:dashboard")
    return render(request, "edit_stack_post.html", {"project": project})

@login_required
def delete_stack_post(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        project.delete()
        messages.success(request, "Stack Tech post deleted successfully.")
        return redirect("main:dashboard")
    return render(request, "delete_stack_post.html", {"project": project})

# ---------------------------
# Videography CRUD
# ---------------------------

@login_required
def add_videography_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        url = request.POST.get("url")
        description = request.POST.get("description")
        video_file = request.FILES.get("video_file")
        Videography.objects.create(title=title, url=url, description=description, video_file=video_file)
        messages.success(request, "Videography post added successfully.")
        return redirect("main:dashboard")
    return render(request, "add_videography_post.html")

@login_required
def edit_videography_post(request, pk):
    video = get_object_or_404(Videography, pk=pk)
    if request.method == "POST":
        video.title = request.POST.get("title")
        video.url = request.POST.get("url")
        video.description = request.POST.get("description")
        if request.FILES.get("video_file"):
            video.video_file = request.FILES.get("video_file")
        video.save()
        messages.success(request, "Videography post updated successfully.")
        return redirect("main:dashboard")
    return render(request, "edit_videography_post.html", {"video": video})

@login_required
def delete_videography_post(request, pk):
    video = get_object_or_404(Videography, pk=pk)
    if request.method == "POST":
        video.delete()
        messages.success(request, "Videography post deleted successfully.")
        return redirect("main:dashboard")
    return render(request, "delete_videography_post.html", {"video": video})

# ---------------------------
# Photography CRUD
# ---------------------------

@login_required
def add_photography_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        url = request.POST.get("url")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        Photography.objects.create(title=title, url=url, description=description, image=image)
        messages.success(request, "Photography post added successfully.")
        return redirect("main:dashboard")
    return render(request, "add_photography_post.html")

@login_required
def edit_photography_post(request, pk):
    photo = get_object_or_404(Photography, pk=pk)
    if request.method == "POST":
        photo.title = request.POST.get("title")
        photo.url = request.POST.get("url")
        photo.description = request.POST.get("description")
        if request.FILES.get("image"):
            photo.image = request.FILES.get("image")
        photo.save()
        messages.success(request, "Photography post updated successfully.")
        return redirect("main:dashboard")
    return render(request, "edit_photography_post.html", {"photo": photo})

@login_required
def delete_photography_post(request, pk):
    photo = get_object_or_404(Photography, pk=pk)
    if request.method == "POST":
        photo.delete()
        messages.success(request, "Photography post deleted successfully.")
        return redirect("main:dashboard")
    return render(request, "delete_photography_post.html", {"photo": photo})

# ---------------------------
# SEO Views
# ---------------------------

def sitemap(request):
    return render(request, "sitemap.xml", content_type="application/xml")

def robots(request):
    return render(request, "robots.txt", content_type="text/plain")

