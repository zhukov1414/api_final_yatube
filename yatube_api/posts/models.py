from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.deletion import CASCADE

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    slug = models.SlugField(max_length=18, unique=True, verbose_name="Ссылка")
    description = models.TextField(max_length=250, verbose_name="Описание")

    class Meta():
        ordering = ("id",)
        verbose_name_plural = "Группы"

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(verbose_name="Текст")
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name="Дата публикации")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Автор")

    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        related_name="posts",
        on_delete=models.SET_NULL,
        verbose_name="Группа")

    image = models.ImageField(
        "Картинка",
        upload_to="posts/",
        blank=True
    )

    class Meta():
        ordering = ['id',]
        verbose_name_plural = 'Посты'

    def __str__(self) -> str:
        return self.text


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Посты',
    )
    author = models.ForeignKey(
        User,
        on_delete=CASCADE,
        related_name='comments',
        verbose_name='Автор',
    )
    text = models.TextField(verbose_name='Текст')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=CASCADE,
        related_name='follower',
        verbose_name='Подписчик'
    )
    following = models.ForeignKey(
        User,
        on_delete=CASCADE,
        related_name="following",
        verbose_name="Подписан",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("user", "following"),
                name="unique_pair"
            ),]
