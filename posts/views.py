from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework import viewsets
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer


# Single view for our post and user model using rest_framework viewsets
# using it to avoid repetitive code

class PostViewSet(viewsets.ModelViewSet):
    # here comma(,) is necessary after IsAuthorOrReadOnly
    # or else you will get BasePermissionMetaclass' object is not iterable error
    permission_classes = (IsAuthorOrReadOnly, permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


# class PostListView(generics.ListCreateAPIView):
#     # permission_classes = (permissions.IsAuthenticated,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer



