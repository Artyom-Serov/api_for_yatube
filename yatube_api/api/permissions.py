from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешение для проверки прав доступа к объектам,
    ограничивающее изменение чужих объектов.
    """
    message = 'Изменение чужого контента запрещено!'

    def has_object_permission(self, request, view, obj):
        """
        Проверка наличия прав доступа к указанному объекту.
        """
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
