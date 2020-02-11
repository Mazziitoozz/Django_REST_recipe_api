from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipeApp import views


router = DefaultRouter()
router.register('tags', views.TagViewSet)

app_name = 'recipeApp'

urlpatterns = [
    path('', include(router.urls)),
]