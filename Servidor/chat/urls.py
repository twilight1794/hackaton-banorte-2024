from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("unitaxx", views.process_text, name='process_text')
]