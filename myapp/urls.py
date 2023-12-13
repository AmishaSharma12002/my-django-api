# myapp/urls.py
from django.urls import path
from .views import UserRegistrationView, UserLoginView
from .views import UserRegistrationView, UserLoginView, ContentGenerationView
from .views import UserRegistrationView, UserLoginView, ContentGenerationView, ImageRecognitionView


urlpatterns = [
    path('api/register/', UserRegistrationView.as_view(), name='register'),
    path('api/login/', UserLoginView.as_view(), name='login'),
    path('api/content-generation/', ContentGenerationView.as_view(), name='content_generation'),
    path('api/image-recognition/', ImageRecognitionView.as_view(), name='image_recognition'),


]
