from rest_framework import viewsets, generics
from rest_framework.exceptions import APIException
from django.core.mail import send_mail
from django.conf import settings
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

    def perform_create(self, serializer):
        instance = serializer.save()

        sujet_mail = f"[Portfolio] Nouveau message : {instance.sujet}"
        corps_mail = (
            f"Nom : {instance.nom}\n"
            f"Email : {instance.email}\n"
            f"Sujet : {instance.sujet}\n"
            f"Date : {instance.envoye_le.strftime('%d/%m/%Y %H:%M')}\n\n"
            f"Message :\n{instance.message}"
        )

        try:
            send_mail(
                sujet_mail,
                corps_mail,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL_RECEIVER],
                fail_silently=False,
            )
        except Exception:
            # L'email a échoué : le message reste enregistré en base (visible dans l'admin),
            # mais on informe le visiteur que l'envoi n'a pas abouti.
            raise APIException("L'envoi de l'email a échoué. Le message a été enregistré mais non transmis.")