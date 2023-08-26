from rest_framework import serializers
from .models import *

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.username')
    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'created_at', 'comment']
        read_only_fields = ['post', 'user']


class BoardSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many = True)
    class Meta:
        model = Board
        fields = ['id', 'user', 'title', 'body', 'comments']

class CreateBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'user', 'title', 'body']
        read_only_fields = ['user']