from django.urls import path
from . import views

urlpatterns = [
    path("", views.survey.survey_list, name="survey-list"),
    path("<int:pk>/", views.survey.detail, name="survey-detail"),
    path("create/", views.survey.create, name="survey-create"),
    path("<int:pk>/delete/", views.survey.delete, name="survey-delete"),
    path("<int:pk>/edit/", views.survey.edit, name="survey-edit"),
]
