from asyncio import tasks
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.template import RequestContext
from django.urls import reverse


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# Create your views here.


def index(request):
    ## to create a new tasks list if this is a new session (a new user for example)
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })


def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })


def removeTask(request, taskindex):
    if taskindex < len(request.session["tasks"]):
        request.session["tasks"].pop(taskindex)
        request.session.modified = True
    return HttpResponseRedirect(reverse("tasks:index"))


def remove(request):
    form = NewTaskForm(initial={'task': 'que coisa'})
    return render(request, f"tasks/remove.html", {
        "form": form
    })
