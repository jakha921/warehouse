from django.db import models


# Create your models here.
class Reception(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Mahsulot nomi')
    product_count = models.IntegerField(verbose_name='Mahsulot soni')
    product_price = models.FloatField(verbose_name='Mahsulot narxi', blank=True, null=True)
    sender = models.CharField(max_length=100, verbose_name='Jo\'natuvchi')
    receiver = models.CharField(max_length=100, verbose_name='Qabul qiluvchi')
    receiver_date = models.DateField(verbose_name='Qabul qilingan sana')

    image = models.ImageField(upload_to='images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product_name} - {self.product_count}'

    class Meta:
        verbose_name = 'Qabul qilingan mahsulot'
        verbose_name_plural = 'Qabul qilingan mahsulotlar'
        ordering = ['-receiver_date', 'product_name']
        db_table = 'reception'
        indexes = [
            models.Index(fields=['receiver_date', 'product_name']),
        ]


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Mahsulot nomi')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Mahsulot'
        verbose_name_plural = 'Mahsulotlar'
        ordering = ['name']
        db_table = 'product'
        indexes = [
            models.Index(fields=['name']),
        ]


class Staff(models.Model):
    name = models.CharField(max_length=100, verbose_name='FIO', unique=True)
    department = models.CharField(max_length=100, verbose_name='Bo\'limi', blank=True, null=True)
    position = models.CharField(max_length=100, verbose_name='Lavozimi', blank=True, null=True)
    phone = models.CharField(max_length=100, verbose_name='Telefon raqami', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.department or ""} '

    class Meta:
        verbose_name = 'Xodim'
        verbose_name_plural = 'Xodimlar'
        ordering = ['name']
        db_table = 'staff'


class Warehouse(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Mahsulot')
    count = models.IntegerField(verbose_name='Mahsulot soni')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product} - {self.count}'

    class Meta:
        verbose_name = 'Ombor'
        verbose_name_plural = 'Omborlar'
        ordering = ['product']
        db_table = 'warehouse'
        indexes = [
            models.Index(fields=['product']),
        ]


class Transmitting(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Mahsulot')
    count = models.IntegerField(verbose_name='Mahsulot soni')
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name='Qabul qiluvchi xodim', blank=True, null=True)
    # receiver = models.CharField(max_length=100, verbose_name='Qabul qiluvchi', blank=True, null=True)
    receiver_date = models.DateField(verbose_name='Qabul qilingan sana')
    comment = models.TextField(blank=True, null=True, verbose_name='Izoh')
    department = models.CharField(max_length=100, verbose_name='Bo\'lim', blank=True, null=True)

    image = models.ImageField(upload_to='transmitting/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product} - {self.count}'

    class Meta:
        verbose_name = 'Jo\'natilgan mahsulot'
        verbose_name_plural = 'Jo\'natilgan mahsulotlar'
        ordering = ['-receiver_date', 'product']
        db_table = 'transmitting'
        indexes = [
            models.Index(fields=['receiver_date', 'product']),
        ]
