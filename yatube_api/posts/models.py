from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import F, Q
from django.db.models.constraints import (
    CheckConstraint,
    UniqueConstraint
)

User = get_user_model()


class Group(models.Model):
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name='Слаг'
    )
    title = models.CharField(
        max_length=200,
        verbose_name='Название группы'
    )
    description = models.TextField(verbose_name='Описание группы')

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Группа'
    )

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Пользователь на которого подписались'
    )

    class Meta:
        constraints = [
            CheckConstraint(
                check=~Q(user=F('following')),
                name='could_not_follow_itself'
            ),
            UniqueConstraint(
                fields=['user', 'following'],
                name='unique_following'
            ),
        ]
