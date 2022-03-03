from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("statistics/<str:sort>", views.statistics, name="statistics"),
    path("reset", views.reset, name="reset"),

    # API Routes
    path("<word_id>", views.updateScore)

]
