from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("brian", views.brian, name="brian"),
    path("<str:name>", views.greet, name="greet")
]
