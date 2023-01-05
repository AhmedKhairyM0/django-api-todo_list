from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

class ListTodoView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailsTodoView(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
