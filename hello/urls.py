# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomLoginView, UserRegistrationView, ActivityViewSet

router = DefaultRouter()
router.register(r'activity', ActivityViewSet, basename='activity')

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),  # Custom login view
    path('', include(router.urls)),
]
