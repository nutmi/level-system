from django.shortcuts import render
from .serializers import QuestSerializer, QuestCompliteSerializer
from .models import Quest, QuestComplite
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from core.models import UserProfile
from lvl.models import LevelInformation
# Create your views here.
class QuestViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = QuestSerializer
    queryset = Quest.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class QuestCompliteViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = QuestCompliteSerializer
    queryset = QuestComplite.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def create(self, request, *args, **kwargs):
        user = UserProfile.objects.get(user=request.user)
        # request.user.profile
        quest_id = request.data.get("quest")
        answer = request.data.get("answer")
        quest = Quest.objects.get(id=quest_id)
        if quest.quest_answer == answer:
            user.gained_xp += quest.xp
            level_info = LevelInformation.objects.first()
            lvl = user.gained_xp // level_info.needed_xp
            user.level += lvl
            if lvl >= 1:
                user.gained_xp -= level_info.needed_xp * lvl
            user.save()
            return super().create(request, *args, **kwargs)
        else:
            return Response("this answer is incorrect")
