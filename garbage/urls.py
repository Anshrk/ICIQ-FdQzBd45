from django.urls import path

from . import views
app_name = "garbage"
urlpatterns = [
    path("<int:garbage_id>/", views.detail, name="detail"),
    path("", views.index, name="index"),
]