from rest_framework import serializers
from .models import Project, ProjectImage, Category, Stack

class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    message = serializers.CharField()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class StackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = ["id", "name"]


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ["id", "title", "file", "link"]


class ProjectSerializer(serializers.ModelSerializer):
    # Category
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source="category", write_only=True
    )

    # Stacks
    stacks = StackSerializer(many=True, read_only=True)
    stack_ids = serializers.PrimaryKeyRelatedField(
        queryset=Stack.objects.all(), many=True, source="stacks", write_only=True
    )

    # Images
    images = ProjectImageSerializer(many=True, read_only=True)
    image_ids = serializers.PrimaryKeyRelatedField(
        queryset=ProjectImage.objects.all(), many=True, source="images", write_only=True
    )

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "description",
            "live_link",
            "git_hub_link",
            "category",      # full object
            "category_id",   # only ID
            "stacks",        # full objects
            "stack_ids",     # only IDs
            "images",        # full objects
            "image_ids",     # only IDs
        ]
