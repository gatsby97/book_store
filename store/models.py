from django.db import models
from django.core.validators import MinLengthValidator , MaxLengthValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def full_name(self):
        return self.first_name+self.last_name
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinLengthValidator(1),MaxLengthValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE,null=True)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default='',blank=True,null=False,db_index=True) #harry-potter-1



    def get_absolute_url(self):
        return reverse("book_detail", args=[self.slug])


    
    def __str__(self):
        return f"{self.title}({self.rating})"


