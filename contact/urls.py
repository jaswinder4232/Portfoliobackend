from django.urls import path
from .views import ContactAPIView, ProjectListCreateView, ProjectDetailView, CategoryListCreateView, CategoryDetailView, StackListCreateView, StackDetailView, ProjectImageListCreateView, ProjectImageDetailView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path("contact/", ContactAPIView.as_view(), name="contact"),
    path("projects/", ProjectListCreateView.as_view(), name="project-list-create"),
    path("projects/<int:pk>/", ProjectDetailView.as_view(), name="project-detail"),

    # Categories
    path("categories/", CategoryListCreateView.as_view(), name="category-list-create"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),

    # Stacks
    path("stacks/", StackListCreateView.as_view(), name="stack-list-create"),
    path("stacks/<int:pk>/", StackDetailView.as_view(), name="stack-detail"),

    # Project Images
    path("images/", ProjectImageListCreateView.as_view(), name="image-list-create"),
    path("images/<int:pk>/", ProjectImageDetailView.as_view(), name="image-detail"),

    # Spectacular
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
