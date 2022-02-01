from django.urls import path
from . import views

app_name = "tasks"
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("removeTask/<int:taskindex>/", views.removeTask, name="removeTask"),
    path("remove", views.remove, name="remove")
]
