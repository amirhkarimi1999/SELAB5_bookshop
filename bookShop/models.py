from django.db import models

EDUCATIONAL, NOVEL, MAGAZINE, OTHER = 0, 1, 2, 3
BOOK_CATEGORIES_CHOICES = (
    (EDUCATIONAL, 'educational'),
    (NOVEL, 'novel'),
    (MAGAZINE, 'magazine'),
    (OTHER, 'other'),
)

# Create your models here.
class Book(models.Model):
    created = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=BOOK_CATEGORIES_CHOICES, default=OTHER)
    price = models.IntegerField(default=0)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"{self.title} - {self.author} - {self.category}"
    
    def save(self, *args, **kwargs):
        super(Book, self).save(*args, **kwargs)