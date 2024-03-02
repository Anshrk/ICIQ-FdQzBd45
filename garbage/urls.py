from django.urls import path

from . import views
app_name = "garbage"
urlpatterns = [
    path("<int:garbage_id>/", views.detail, name="details"),
    path("", views.index, name="index"),
    path("signup", views.signup, name="register")
]