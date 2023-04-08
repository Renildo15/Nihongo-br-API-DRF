from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from user_app.views import UserViewSets, ProfileViewSet
from post_app.views import PostViewSet
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

router = DefaultRouter()
router.register('user', UserViewSets, basename='user')
router.register('profile', ProfileViewSet, basename='profile')
router.register('post', PostViewSet, basename='post')

urlpatterns += router.urls