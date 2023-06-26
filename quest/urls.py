from django.contrib import admin
from django.urls import path
from rest_framework import routers
from .views import QuestViewSet, QuestCompliteViewSet

router = routers.SimpleRouter()
router.register(r"quests", QuestViewSet, basename="quests")
router.register(r"questcomplite", QuestCompliteViewSet, basename="questcomplite")
urlpatterns = router.urls
urlpatterns += []