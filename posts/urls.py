from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PostViewSet, UserViewSet

# here we're using rest_framework router
router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls



# from .views import PostListView, PostDetailView, UserList, UserDetail
# urlpatterns = [
#     path('user/', UserList.as_view()),
#     path('user/<int:pk>/', UserDetail.as_view()),
#     path('<int:pk>/', PostDetailView.as_view()),
#     path('', PostListView.as_view()),
# ]
