from rest_framework import serializers
from django.contrib.auth.models import User
from forum.models import Tag, Thread, Answer, Comment, Response, UserVoteThread, UserVoteAnswer

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('pk','keyword')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('body','created_at')

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = ('body','created_at')

class UserSerializer(serializers.ModelSerializer):
    # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    class Meta:
        model = User
        # fields = ('id', 'username', 'snippets')
        fields = ('id', 'username')

class AnswerSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Answer
        fields = ('description','vote','comment_set')

class UserVoteThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVoteThread
        fields = ('status','user')

class UserVoteAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVoteAnswer
        fields = ('status','user')

class ThreadSerializer(serializers.ModelSerializer):
    # answer_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Answer.objects.all())
    # response_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Response.objects.all())
    # tag_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
    
    answer_set = AnswerSerializer(many=True, read_only=True)
    response_set = ResponseSerializer(many=True, read_only=True)
    tag_set = TagSerializer(many=True, read_only=True)
    class Meta:
        model = Thread
        fields = ('pk','title','description','created_at', 'vote', 'tag_set','response_set','answer_set')

class ShortThreadSerializer(serializers.ModelSerializer):
    tag_set = TagSerializer(many=True, read_only=True)
    class Meta:
        model = Thread
        fields = ('pk','title','description','created_at', 'vote', 'tag_set')
