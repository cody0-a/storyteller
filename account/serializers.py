from rest_framework import serializers
from .models import Notification
class PhoneNumberSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    country_code = serializers.CharField()



class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'