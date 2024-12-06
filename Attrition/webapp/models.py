from django.db import models

# Create your models here.

class company(models.Model):
	name=models.CharField(max_length=159);
	email=models.CharField(max_length=159);
	pass_word=models.CharField(max_length=159);
	phone=models.CharField(max_length=159);
	address=models.CharField(max_length=559);
	city=models.CharField(max_length=159);
	stz=models.CharField(max_length=159);

	
class performance(models.Model):
    alg_name = models.CharField(max_length=100)
    sc1 = models.FloatField()
    sc2 = models.FloatField()
    sc3 = models.FloatField()
    sc4 = models.FloatField()


class feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    file = models.CharField(max_length=100)
    