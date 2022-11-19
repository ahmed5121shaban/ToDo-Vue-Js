from django.urls import path,include
from .api import TODOViewSet
from rest_framework import routers
from .views import todolist

app_name = 'todo'

router = routers.DefaultRouter()
router.register('todo',TODOViewSet)


urlpatterns = [
    path('api',include(router.urls)),
    path('',todolist)

]