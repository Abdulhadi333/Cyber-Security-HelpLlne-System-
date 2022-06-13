from dataclasses import field
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Scan_Vul, Certification, Comment, Profile, reatingProfile


"""
Serializers allow complex data such as querysets and model instances 
to be converted to native Python datatypes that can then be easily 
rendered into JSON

"""

class Scan_VulSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scan_Vul
        fields = '__all__'


class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ReatingProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = reatingProfile
        fields = '__all__'


