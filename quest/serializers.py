from rest_framework import serializers
from .models import Quest, QuestComplite

class QuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = "__all__"

class QuestCompliteSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestComplite
        fields = "__all__"