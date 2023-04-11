from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]

# from api.views import CommentViewSet, GroupViewSet, PostViewSet
# router = routers.DefaultRouter()

# router.register(
#     r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment'
# )
# router.register(r'groups', GroupViewSet, basename='groups')
# router.register(r'posts', PostViewSet, basename='posts')