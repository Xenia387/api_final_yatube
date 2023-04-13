from rest_framework.routers import DefaultRouter
from django.urls import include, path

from api.views import CommentViewSet, FollowViewSet, PostViewSet, GroupViewSet

router_1 = DefaultRouter()
router_1.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment'
)
router_1.register('groups', GroupViewSet, basename='groups')
router_1.register('posts', PostViewSet, basename='posts')
router_1.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router_1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
