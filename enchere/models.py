from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

class Utilisateur(AbstractUser):
	id = models.AutoField(primary_key=True)
	email = models.EmailField(max_length=255, unique=True)
	solde = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

	class Meta:
		db_table='utilisateur'
	
	def __str__(self):
		return self.username

class Article(models.Model):
	STATUT_CHOICES = [
		('OUVERT', 'Ouvert'),
	    ('CLOTURE', 'Clôturé'),
	    ('VENDU', 'Vendu'),
	]

	id_article = models.AutoField(primary_key=True)
	vendeur = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,blank=True,related_name='articles_vendus')
	gagnant_actuel = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,blank=True,related_name='articles_gagnes')
	nom = models.CharField(max_length=255)
	description = models.TextField()
	prix_depart = models.DecimalField(max_digits=10, decimal_places=2)
	prix_actuel = models.DecimalField(max_digits=10, decimal_places=2)
	date_creation = models.DateTimeField(auto_now_add=True)
	date_debut = models.DateTimeField()
	date_fin = models.DateTimeField() 
	statut = models.CharField(max_length=50, choices=STATUT_CHOICES)
	
	class Meta:
	    indexes = [
	        models.Index(fields=['date_fin']),
	        models.Index(fields=['vendeur']),
	    ]

	def __str__(self):
	    return self.nom

class Enchere(models.Model):
	id_enchere = models.BigAutoField(primary_key=True)
	article = models.ForeignKey(Article,related_name='encheres',on_delete=models.CASCADE)
	encherisseur = models.ForeignKey(Utilisateur,related_name='encheres',on_delete=models.CASCADE)
	montant = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
	date_enchere = models.DateTimeField(auto_now_add=True)
	class Meta:
        indexes = [
            models.Index(fields=['article', '-date_enchere']),
        ]

	def __str__(self):
	    return f"Enchère {self.montant} sur {self.article.nom}"




