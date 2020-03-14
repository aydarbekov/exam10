from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from api_v1 import views

router = routers.DefaultRouter()
router.register(r'files', views.FileViewSet)
# router.register(r'comments', views.CommentViewSet)
# router.register(r'likes', views.LikeViewSet)
# router.register(r'statuses', views.StatusViewSet)

app_name = 'api_v1'

urlpatterns = [
    path('', include(router.urls)),
    # path('like/', like_view, name='like'),
    # path('login/', obtain_auth_token, name='api_token_auth')
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))]