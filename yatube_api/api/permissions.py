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
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
