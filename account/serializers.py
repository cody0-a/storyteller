from rest_framework import serializers
from .models import Notification, Story, StoryComment, SharedStory, SharedComment
class PhoneNumberSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    country_code = serializers.CharField()



class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'

class StoryCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryComment
        fields = '__all__'

class SharedStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedStory
        fields = '__all__'

class SharedCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedComment
        fields = '__all__'
