from django.urls import path
from .views import ListTodoView, DetailsTodoView

urlpatterns = [
    path("", ListTodoView.as_view(), name="list-todo"),
    path("<int:pk>", DetailsTodoView.as_view(), name="details-todo"),

]
