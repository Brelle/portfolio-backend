from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    SkillViewSet, ProjectViewSet, ExperienceViewSet,
    EducationViewSet, ContactMessageCreateView
)

router = DefaultRouter()
router.register('skills', SkillViewSet)
router.register('projects', ProjectViewSet)
router.register('experiences', ExperienceViewSet)
router.register('educations', EducationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('contact/', ContactMessageCreateView.as_view(), name='contact-create'),
]