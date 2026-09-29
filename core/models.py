from django.db import models


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('Développement', 'Développement'),
        ('Outils', 'Outils'),
        ('Marketing digital', 'Marketing digital'),
    ]

    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, help_text="Nom de l'icône react-icons, ex: FaReact")
    level = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    problem = models.TextField()
    technologies = models.CharField(max_length=255, help_text="Séparées par des virgules")
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    demo_link = models.URLField(blank=True)
    github_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Experience(models.Model):
    role = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    period = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0, help_text="Ordre d'affichage")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.role} — {self.company}"


class Education(models.Model):
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=150, blank=True)
    period = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.degree


class ContactMessage(models.Model):
    nom = models.CharField(max_length=150)
    email = models.EmailField()
    sujet = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    envoye_le = models.DateTimeField(auto_now_add=True)
    lu = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nom} — {self.sujet or 'Sans sujet'}"