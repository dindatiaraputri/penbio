
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),

    path("materi/", views.daftar_materi, name="materi"),
    path("materi/<slug:slug>/", views.detail_materi, name="detail_materi"),

    path("video/", views.video, name="video"),
    path("kuis/", views.kuis, name="kuis"),
]
