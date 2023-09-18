from django.shortcuts import render
""" from django.views import generic
from django.views import View """
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.

""" class Index(generic.TemplateView):
    template_name =  "todo/index.html"

class Create(generic.CreateView):
    template_name = "todo/index.html"
    model = Todo
    form_class = TitleForm """

""" class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request,"todo/index.html") """

class Index(APIView):
    def get(self, request):
        return render(request,"todo/index.html")

class List(APIView):
    def get(self,request):
        lista = Todo.objects.all().order_by('-id')
        serializer = TodoSerializer(lista, many=True)
        return Response(serializer.data)

class Create(APIView):
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteItem(APIView):
    def delete(self, request, pk):
        item = Todo.objects.get(id=pk)
        item.delete()
        return Response("Deleted successfully")
