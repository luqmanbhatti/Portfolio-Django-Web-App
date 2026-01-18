from django.urls import path
from django.views.generic.base import RedirectView
from . import views

app_name = "main"  # Recommended for namespacing URLs

urlpatterns = [
    path("favicon.ico", RedirectView.as_view(url="/static/images/fi.ico", permanent=True)),
    # Portfolio pages
    path("", views.home, name="home"),                      
    path("about/", views.about, name="about"),
    path("stack-tech/", views.stack_tech, name="stack_tech"),
    path("videography/", views.videography, name="videography"),
    path("photography-designs/", views.photography_designs, name="photography_designs"),
    path("contact/", views.contact, name="contact"),

    # Authentication-related (✅ now only your custom views)
    path("login/", views.login_view, name="login"),          # Login page
    path("logout/", views.logout_view, name="logout"),       # Logout action
    path("register/", views.register, name="register"),      # Registration page
    path("dashboard/", views.dashboard, name="dashboard"),   # User dashboard

    # CRUD routes for posts (Stack Tech, Videography, Photography)
    path("stack-tech/add/", views.add_stack_post, name="add_stack_post"),
    path("stack-tech/edit/<int:pk>/", views.edit_stack_post, name="edit_stack_post"),
    path("stack-tech/delete/<int:pk>/", views.delete_stack_post, name="delete_stack_post"),

    path("videography/add/", views.add_videography_post, name="add_videography_post"),
    path("videography/edit/<int:pk>/", views.edit_videography_post, name="edit_videography_post"),
    path("videography/delete/<int:pk>/", views.delete_videography_post, name="delete_videography_post"),

    path("photography/add/", views.add_photography_post, name="add_photography_post"),
    path("photography/edit/<int:pk>/", views.edit_photography_post, name="edit_photography_post"),
    path("photography/delete/<int:pk>/", views.delete_photography_post, name="delete_photography_post"),
    
    # SEO
    path("sitemap.xml", views.sitemap, name="sitemap"),
    path("robots.txt", views.robots, name="robots"),
]

