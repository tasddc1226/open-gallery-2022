from django.urls import path
from . import views

urlpatterns = [
    path("", views.survey.survey_list_create, name="survey-list-create"),
    path("<int:pk>/", views.survey.detail, name="survey-detail"),
    path("<int:pk>/delete/", views.survey.delete, name="survey-delete"),
    path("<int:pk>/edit/", views.survey.edit, name="survey-edit"),
    path(
        "<int:pk>/question/",
        views.survey.question_create,
        name="survey-question-create",
    ),
    path(
        "<int:survey_pk>/question/<int:question_pk>/delete/",
        views.survey.question_delete,
        name="survey-question-delete",
    ),
    path(
        "<int:survey_pk>/question/<int:question_pk>/choice/",
        views.survey.choice_create,
        name="survey-choice-create",
    ),
    path("<int:pk>/start/", views.survey.start, name="survey-start"),
    path(
        "<int:survey_pk>/submit/<int:sub_pk>/",
        views.survey.submit,
        name="survey-submit",
    ),
    path("<int:pk>/thanks/", views.survey.thanks, name="survey-thanks"),
    path("search/", views.survey.search, name="survey-search"),
    path("<int:pk>/download/", views.survey.download, name="survey-download"),
]
