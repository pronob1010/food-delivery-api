from dataclasses import fields
import email
from . models import User 
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=24)
    email = serializers.EmailField(max_length=80)
    phone_number = PhoneNumberField(allow_blank=False)
    password = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = ['username','email','phone_number','password']

    def validate(self, attrs):
        username_exists= User.objects.filter(username=attrs['username']).exists()

        if username_exists:
            raise serializers.ValidationError(detail="User already username exists")
        
        email_exists = User.objects.filter(email=attrs['email']).exists()
        if email_exists:
            raise serializers.ValidationError(detail="User already email exists")
        
        phone_number_exists = User.objects.filter(phone_number=attrs['phone_number']).exists()
        if phone_number_exists:
            raise serializers.ValidationError(detail="User already phone number exists")
        
        return super().validate(attrs)