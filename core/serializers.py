from rest_framework import serializers
from .models import Skill, Project, Experience, Education, ContactMessage


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'nom', 'email', 'sujet', 'message']
        extra_kwargs = {
            'sujet': {'required': True, 'allow_blank': False},
            'nom': {'required': True, 'allow_blank': False},
            'message': {'required': True, 'allow_blank': False},
        }