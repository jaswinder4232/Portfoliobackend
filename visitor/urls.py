from django.urls import path
from .views import notify_visit

urlpatterns = [
    path('notify-visit/', notify_visit, name='notify_visit'),
]
