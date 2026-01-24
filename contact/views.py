from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .serializers import (
    ContactSerializer, 
    ProjectSerializer, 
    CategorySerializer, 
    StackSerializer, 
    ProjectImageSerializer
)
from .models import ContactMessage, Project, Category, Stack, ProjectImage


# ---------------- Contact API ----------------
@method_decorator(csrf_exempt, name='dispatch')
class ContactAPIView(APIView):
    """
    Contact API endpoint
    CSRF exempt for cross-origin requests
    Saves contact message to database only
    """
    def post(self, request):
        serializer = ContactSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()  # Save directly to DB

            return Response(
                {"success": "Message saved successfully!"},
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# ---------------- Projects ----------------
class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# ---------------- Categories ----------------
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# ---------------- Stacks ----------------
class StackListCreateView(generics.ListCreateAPIView):
    queryset = Stack.objects.all()
    serializer_class = StackSerializer


class StackDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stack.objects.all()
    serializer_class = StackSerializer


# ---------------- Project Images ----------------
class ProjectImageListCreateView(generics.ListCreateAPIView):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer


class ProjectImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer
