from django.urls import path
from notesapp import views

namespace = "notesapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("notes/", views.notespage, name="notes"),
]
