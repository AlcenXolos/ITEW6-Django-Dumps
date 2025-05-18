from django.db import models
class BookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(pages__gt=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13)
    pages = models.IntegerField()
    objects = BookManager()
    
    def __str__(self):
        return self.title
    
class Meta:
    verbose_name = "book"
    ordering = ["title"]
    db_table = "book"