from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType


# Create your models here.

def get_product_url(obj, viewname):
    ct_model = obj.__class__._meta.model_name
    return reversed(viewname, kwargs={'ct_model': ct_model, 'slug': obj.slug})

class LatestProductManager:
    def get_pruducts_for_main_page(self, *args, **kwargs):
        with_respect_to = kwargs.get('with_respect_to')
        pruducts = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_pruducts = ct_model.model_class()._base_manager.all().order_by('-id')[:5]
            pruducts.extend(model_pruducts)
        if with_respect_to:
            ct_model = ContentType.objects.filter(model=with_respect_to)
            if ct_model.exists():
                if with_respect_to in args:
                    return sorted(
                        pruducts, key=lambda x: x.__class__._meta.model_name.startwith(with_respect_to), reverse=True
                    )
        return pruducts

class LatestProduct:
    objects = LatestProductManager()

class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=20, unique=True)
    
    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('products:product_list_by_category', args=[self.slug])
    

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = ProductManager()
    
    def __str__(self):
        return self.name
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url= ''
        return url
    
    class Meta:
        ordering = ('-created', )
        index_together = (('id', 'slug'), )
        
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("products:product_detail", args=[self.id, self.slug])
    