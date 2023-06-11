"""
Определение URL-адресов для API.

Импортированные модули:
- include: функция для включения других URL-адресов в текущий URL-адрес.
- path: функция для определения URL-адресов.
- DefaultRouter: класс для автоматического создания URL-адресов
для представлений Django REST Framework.

Импортированные представления:
- CommentViewSet: класс вида для модели Comment.
- GroupViewSet: класс вида для модели Group.
- PostViewSet: класс вида для модели Post.
"""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet


router = DefaultRouter()

router.register('posts', PostViewSet, basename='posts')
router.register(
    'posts/(?P<post_id>\\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register('groups', GroupViewSet, basename='groups')


urlpatterns = [
    path('v1/', include(router.urls)),
]

"""
Список URL-адресов для API.

- v1/posts/: список всех постов.
- v1/posts/<post_id>/comments/: список всех комментариев для данного поста.
- v1/groups/: список всех групп.
"""
