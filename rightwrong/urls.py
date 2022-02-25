from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("statistics", views.statistics),
    path("reset", views.reset, name="reset"),

    # API Routes
    path("<word_id>", views.updateScore)

]
