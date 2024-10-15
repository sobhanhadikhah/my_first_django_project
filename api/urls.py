from django.urls import path
from .views import BlogView

urlpatterns = [
    path("blogs/",BlogView.as_view(),name="blogs"),
    path("blogs/<int:pk>/",BlogView.as_view(),name="blog_detail"),
]