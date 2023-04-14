from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from user_app.views import UserViewSets, ProfileViewSet
from phrase_app.views import PhraseViewSet
from post_app.views import PostViewSet
from note_app.views import NoteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', UserViewSets, basename='user')
router.register('profile', ProfileViewSet, basename='profile')
router.register('post', PostViewSet, basename='post')
router.register('phrase', PhraseViewSet, basename='phrase')
router.register('note', NoteViewSet, basename='note')
''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/', include(router.urls)),
    path('api/v1/post/<str:pk>/phrase_list/', PostViewSet.as_view({'get': 'phrase_list'}), name='post-phrase-list'),
    path('api/v1/post/<str:pk>/note_list/',PostViewSet.as_view({'get': 'note_list'}), name='post-note-list' ),
    path('api/v1/profile/<str:pk>/post_list/',ProfileViewSet.as_view({'get': 'post_list'}), name='post-list' ),
]

