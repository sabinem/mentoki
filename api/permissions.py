from rest_framework import permissions

from apps_data.course.models import Course

class CourseIsOwnerOrReadOnly(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        print "=============="
        print "in permissons"
        print obj.is_owner(request.user)
        print obj.id
        print request.user
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if obj.is_owner(request.user):
                return True
        return False


class CoursePartIsOwnerOrReadOnly(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if obj.course.is_owner(request.user):
                return True
        return False


class IsOwnerOrAdminStaffReadOnly(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        elif request.user.is_staff and request.method in permissions.SAFE_METHODS:
            return True
        else:
            if obj.is_owner(request.user):
                return True
        return False