from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets, permissions, filters
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Comment, Follow, Group, Post
from .permissions import IsAuthorOrReadOnly
from .serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer
)


class CreateListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """Кастомный ViewSet: создание и получение списка."""
    pass


class PostViewSet(viewsets.ModelViewSet):
    """Представление для модели Post."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        IsAuthorOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly
    )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Автоматическое указание автора при создании поста."""

        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Представление для модели Group."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (
        IsAuthorOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly
    )


class CommentViewSet(viewsets.ModelViewSet):
    """Представление для модели Comment."""

    serializer_class = CommentSerializer
    permission_classes = (
        IsAuthorOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly
    )

    def get_queryset(self):
        """
        Получение id поста из эндпоинта.
        Отбор комментариев к этому посту.
        """
        post_id = self.kwargs.get("post_id")
        new_queryset = Comment.objects.filter(post=post_id)
        return new_queryset

    def perform_create(self, serializer):
        """
        Автоматическое указание автора комментария и поста,
        к которому он относится при создании комментария.
        """
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(CreateListViewSet):
    """Представление для модели Follow."""

    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)
    pagination_class = None

    def get_queryset(self):
        """
        Получение пользователя из эндпоинта.
        """
        return self.request.user.follower

    def perform_create(self, serializer):
        """
        Автоматическое указание пользователя, создавшего подписку.
        """
        serializer.save(user=self.request.user)
