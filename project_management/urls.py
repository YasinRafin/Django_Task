from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProjectViewSet, TaskViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('projects/<int:project_id>/tasks/', 
         TaskViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('tasks/<int:task_id>/comments/', 
         CommentViewSet.as_view({'get': 'list', 'post': 'create'})),
]
