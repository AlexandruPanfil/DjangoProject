from django.db import models
from django.urls import reverse


# Create your models here.

class PC(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_created = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Category")
    #it's cat_id (category id) and _id is added by Django
    #why 'Category' and not simple Category, bcz Django will understand where to be forwarded without
    #moving all code below
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug':self.slug})

    class Meta:
        # This class is showing the data in admin pannel and some of them in our site
        verbose_name = "All About PC"
        verbose_name_plural = "All About PCs"
        ordering = ["time_update", "title"]

class Category(models.Model):
    name = models.CharField(max_length=120, db_index=True)
    # db_index -> means that this field will be indexed
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})
        # return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["id"]
