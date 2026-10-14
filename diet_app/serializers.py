from rest_framework import serializers
from diet_app.models import *


class UserSerializer(serializers.ModelSerializer):
    profile=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=CustomUser
        fields=["id","username","email","password","phone","profile"]
        read_only_fields=["id"]
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
    def get_profile(self,obj):
        profile_obj=UserProfile.objects.get(owner=obj)
        serailzer_instance=UserProfileSerializer(profile_obj)
        return serailzer_instance.data
        
#CreateApiView[serializer_class]-->UserSerializer--POST-->UserSerializerObject.save()--->UserSerializer[create]--->User.objects.create()

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields="__all__"
        read_only_fields=["id","bmr","owner"]
        

class FoodLogSerializer(serializers.ModelSerializer):
    class Meta:
        model=FoodLog
        fields="__all__"
        read_only_fields=["id","owner","created_at"]