from django.db import models
from django.urls import reverse
# Create your models here.

class Furnitures(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    content = models.TextField(blank=True, verbose_name="Text")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Photo")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Create Time")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Update Time")
    is_published = models.BooleanField(default=True, verbose_name="Published")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Categories")


    def __str__(self):
       return self.title


    #  def get_absolute_url(self):
    #     return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Furnitures'
        verbose_name_plural = 'Furnitures'
        ordering = ['-time_create', 'title']



class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']

