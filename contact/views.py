from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.conf import settings
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
    """
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            subject = serializer.validated_data.get('subject', 'No Subject')
            message = serializer.validated_data['message']

            # Save to database
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )

            # Send email
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            send_mail(
                f"Portfolio Contact from {name}",
                body,
                settings.EMAIL_HOST_USER,   # From
                [settings.EMAIL_HOST_USER], # To
                fail_silently=False,
            )

            return Response({"success": "Message sent successfully!"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ---------------- Project Views ----------------
class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# ---------------- Category Views ----------------
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# ---------------- Stack Views ----------------
class StackListCreateView(generics.ListCreateAPIView):
    queryset = Stack.objects.all()
    serializer_class = StackSerializer


class StackDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stack.objects.all()
    serializer_class = StackSerializer


# ---------------- Project Image Views ----------------
class ProjectImageListCreateView(generics.ListCreateAPIView):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer


class ProjectImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer
