from django.db import models
from django.utils import timezone

class Utilisateur(models.Model):
    id_utilisateur = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    mot_de_passe = models.CharField(max_length=128)
    solde = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.username


class Article(models.Model):
    STATUT_CHOICES = [
        ('OUVERT', 'Ouvert'),
        ('CLOTURE', 'Clôturé'),
        ('VENDU', 'Vendu'),
    ]

    id_article = models.AutoField(primary_key=True)
    vendeur = models.ForeignKey(Utilisateur,related_name="articles_vendus",on_delete=models.CASCADE)
    gagnant_actuel = models.ForeignKey(Utilisateur,related_name="articles_gagnes",on_delete=models.SET_NULL,null=True,blank=True)
    nom = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    prix_depart = models.DecimalField(max_digits=10, decimal_places=2)
    prix_actuel = models.DecimalField(max_digits=10, decimal_places=2)
    date_creation = models.DateTimeField(default=timezone.now)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    statut = models.CharField(max_length=50,choices=STATUT_CHOICES,default='OUVERT')

    def __str__(self):
        return self.nom

    class Meta:
        indexes = [
            models.Index(fields=['date_fin']),
            models.Index(fields=['vendeur']),
        ]


class Enchere(models.Model):
    id_enchere = models.AutoField(primary_key=True)
    article = models.ForeignKey(Article,related_name="encheres",on_delete=models.CASCADE)
    encherisseur = models.ForeignKey(Utilisateur,related_name="encheres",on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_enchere = models.DateTimeField(default=timezone.now)

    class Meta:
        indexes = [
            models.Index(fields=['article', '-date_enchere']),
        ]

    def __str__(self):
        return f"Enchère de {self.montant} sur {self.article}"
