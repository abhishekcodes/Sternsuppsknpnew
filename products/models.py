import random
import os
from django.db import models
from django.db.models.signals import pre_save,post_save
from django.urls import reverse
from .utils import unique_slug_generator

def get_filename_ext(filename):
	base_name =os.path.basename(filename)
	name, ext = os.path.splitext(base_name)
	return name,ext

def upload_image_path(instance,filename):
	print(instance)
	print(filename)
	new_filename= random.randint(1,3910209312)
	name, ext = get_filename_ext(filename)
	final_filename = '{new_filename}{ext}',format(new_filename=new_filename, ext=ext)
	return "products/{new_filename}/{final_filename}".format(
		new_filename=new_filename,
		final_filename=final_filename
		)

class ProductQuerySet(models.query.QuerySet):
	def active(self):
		return self.filter(active=True)

	def featured(self):
		return self.filter(featured=True, active=True)

	def search(self,query):
		lookups = (Q(title_icontains=query) |
					Q(description_icontains=query) |
					Q(price_icontains=query) |
					Q(tag_title_icontains=query))
		return self.filter(lookups).distinct() #if you avoid distinct then one result comes over and over



class ProductManager(models.Manager):
	def get_queryset(self):
		return ProductQuerySet(self.model, using=self._db)

	def all(self):
		return self.get_queryset().active()

	def featured(self):
		return self.get_queryset().filter()

	def get_by_id(self,id):
		qs = self.get_queryset().filter(id=id) #products.objects==self.get_by_id
		if qs.count()==1:
			return qs.first()
		return None

# Create your models here.
class Product(models.Model):
	title 		= models.CharField(max_length=120)
	slug		= models.SlugField(blank=True,unique=True)
	description = models.TextField()
	price 		= models.DecimalField(decimal_places=2,max_digits=10,default=39.99)
	image		= models.FileField(upload_to='products/',null=True,blank=True)
	featured	= models.BooleanField(default=False)
	active		= models.BooleanField(default=False)
	timestamp	= models.DateTimeField(auto_now_add=True)

	objects 	= ProductManager()

	def get_absolute_url(self):
		#return "/products/{slug}/".format(slug=self.slug)
		return reverse("products:detail", kwargs={"slug":self.slug})

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title

def product_pre_save_receiver(sender,instance,*args,**kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver,sender=Product)	