from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Note


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = fields = "__all__"
        extra_kwargs = {"author": {"read_only": True}}


#        fields = "__all__"
