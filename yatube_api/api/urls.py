from rest_framework.routers import DefaultRouter
# from rest_framework import routers
from django.urls import include, path

from api.views import CommentViewSet, FollowViewSet, PostViewSet, GroupViewSet

router = DefaultRouter()
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment'
)
router.register('groups', GroupViewSet, basename='groups')
router.register('posts', PostViewSet, basename='posts')
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
