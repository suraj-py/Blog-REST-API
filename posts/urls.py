from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    path('<int:pk>/', PostDetailView.as_view()),
    path('', PostListView.as_view()),
]
