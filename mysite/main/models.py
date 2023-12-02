from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField('Category name', max_length=50)
    image = models.ImageField('Category image', upload_to='logo')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Car(models.Model):

    COLOR_CHOICE = (
        ('White', 'white'),
        ('Black', 'Black'),
        ('Red', 'red'),
        ('Blue', 'Blue'),
        ('Purple', 'purple')
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat_prod')
    name = models.CharField('Car name', max_length=50)
    year = models.PositiveIntegerField('Year')
    color = models.CharField('Color', choices=COLOR_CHOICE, max_length=10)
    price = models.PositiveIntegerField('Car price')
    description = models.TextField('Car description')
    image = models.ImageField('Car image')

    def __str__(self) -> str:
        return self.name

