from django.urls import include, path
from rest_framework import routers

from api.views import (CommentViewSet, GroupViewSet, PostViewSet)


app_name = 'api'
router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('groups', GroupViewSet, basename='group')
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comm'
)


urlpatterns = [
    path('v1/', include(router.urls)),
]
