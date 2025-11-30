from django.db import models

# Create your models here.
class Category(models.Model):
    """
    Класс - категорії (групи) товарів
    """
    mame = models.CharField(max_length=150, unique=True,
                            verbose_name='Назва категорії (групи)')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True,
                            verbose_name='URL категорії (групи)')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.mame


class Product(models.Model):
    """
    Клаа - товар (головні атрібути)
    """
    mame = models.CharField(max_length=150, unique=True,
                            verbose_name='Назва товара')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True,
                            verbose_name='URL товара')
    description = models.TextField(blank=True, null=True,
                                   verbose_name='Опис товару')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2,
                                verbose_name='Вартість')
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2,
                                verbose_name='Знижка (%)')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Кількість')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE,
                                 verbose_name='Категорія')

    class Meta:
        db_table = 'product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'

    def __str__(self):
        return self.mame