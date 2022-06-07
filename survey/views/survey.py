from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from ..models import Survey, Question, Choice, Submission


@login_required
def survey_list(request):
    objs = (
        Survey.objects.filter(author=request.user).order_by("-created_at").all()
    )
    return render(request, "survey/list.html", {"surveys": objs})


@login_required
def detail(request):
    pass


@login_required
def create(request):
    pass


@login_required
def delete(request):
    pass


@login_required
def edit(request):
    pass
