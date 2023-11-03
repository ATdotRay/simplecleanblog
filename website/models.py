from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.text import slugify
# import uuidmanage
# from django import forms
# from django.forms import Textarea

# Create your models here.
class HomePage(models.Model):
    about1 = RichTextField(null=True)
    about2 = RichTextField(null=True)

    testimonial1 = RichTextField(null=True)
    testimonial2 = RichTextField(null=True)

    def __str__(self):
        return "Home Page"
    
    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Page"
    


class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='article_images/', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("article-post", args=[self.id])



class Service(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='service_images/', null=True, blank=True)
    slug = models.SlugField(editable=False, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    # def get_absolute_url(self):
    #     return reverse("service-page", args=[self.id])
    
    def __str__(self):
        return self.title
