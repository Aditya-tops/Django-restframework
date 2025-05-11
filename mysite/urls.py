from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from moviesApp.views import MovieViewSet

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), 
]
