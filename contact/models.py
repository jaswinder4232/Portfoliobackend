from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Stack(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class ProjectImage(models.Model):
    title = models.CharField(max_length=255)
    file = models.ImageField(upload_to="project_images/")
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    live_link = models.URLField(blank=True, null=True)
    git_hub_link = models.URLField(blank=True, null=True)

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="projects"
    )
    stacks = models.ManyToManyField(Stack, related_name="projects")
    images = models.ManyToManyField(ProjectImage, related_name="projects")

    def __str__(self):
        return self.name