from rest_framework import viewsets, generics
from .models import Skill, Project, Experience, Education, ContactMessage
from .serializers import (
    SkillSerializer, ProjectSerializer, ExperienceSerializer,
    EducationSerializer, ContactMessageSerializer
)


class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ExperienceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class EducationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class ContactMessageCreateView(generics.CreateAPIView):
    """Permet uniquement l'envoi (POST) d'un message, pas la lecture publique."""
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer