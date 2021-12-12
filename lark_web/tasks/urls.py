from django.urls import path, include
from rest_framework import routers

from .api import TaskTmplViewSet, TaskViewSet

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'task_tmpl', TaskTmplViewSet)
router.register(r'task', TaskViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
