from django.db import models
from django.shortcuts import reverse

from django.contrib.auth.models import User

class Client(models.Model):
    SEX = (
        ('M', 'Мужчина'),
        ('F', 'Женщина'),
    )
    first_name = models.CharField(verbose_name="Имя", max_length=50, db_index=True)
    last_name = models.CharField(verbose_name="Фамилия", max_length=50, db_index=True)
    patronymic = models.CharField(verbose_name="Отчество", max_length=50, blank=True)
    sex = models.CharField(verbose_name="Пол", max_length=1, choices=SEX, default='M')
    phone = models.CharField(verbose_name="Телефон", max_length=11, db_index=True)
    e_mail = models.CharField(verbose_name="E-mail", max_length=100, blank=True)
    label = models.TextField(verbose_name="Метка", max_length=150, blank=True)

    # def get_absolute_url(self):
    #     return reverse('client_detail_url', kwargs={'pk': self.pk})

    def __str__(self):
        return self.last_name

class Contractor(models.Model):
    contractor_name = models.CharField(verbose_name='Название поставщика', max_length=50)

    def __str__(self):
        return self.contractor_name

class Car(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name="Клиент")
    makes = models.CharField(verbose_name="Марка", max_length=80)
    model = models.CharField(verbose_name="Модель", max_length=80)
    year = models.CharField(verbose_name="Год", max_length=4, blank=True)
    vin = models.CharField(verbose_name="VIN", max_length=25, blank=True)
    hp = models.FloatField(verbose_name="Л/С", max_length=5, default=0)

    def __str__(self):
        return self.makes

class Product(models.Model):
    STATUS = (
        ('A', 'Не закуплен'),
        ('B', 'Ожидается'),
        ('C', 'В наличии'),
        ('D', 'Выдан'),
        ('E', 'Возврат'),
    )
    product_name = models.CharField(verbose_name="Название", max_length=80)
    vendor_code = models.CharField(verbose_name="Артикул", max_length=20)
    contractor = models.ForeignKey('Contractor', null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Поставщик")
    status = models.CharField(verbose_name="Статус", max_length=1, choices=STATUS, default='A')
    price = models.DecimalField(verbose_name="Цена закупки", max_digits=10, decimal_places=2)
    description = models.TextField(verbose_name="Описание", max_length=80)

    def __str__(self):
        return self.product_name

class Order(models.Model):
    STATUS = (
        ('A', 'В работе'),
        ('B', 'Завершен'),
    )
    date_create = models.DateTimeField(verbose_name="Дата", auto_now_add=True)
    date_end = models.DateTimeField(verbose_name="Дата", blank=True, null=True)
    status = models.CharField(verbose_name="Статус", max_length=1, choices=STATUS, default='A')
    client = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name="Клиент")
    worker = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Сотрудник")
    note = models.CharField(verbose_name="Заметка", max_length=150, blank=True)

    # def get_absolute_url(self):
    #     return reverse('order_detail_url', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def __str__(self):
        return '{}'.format(self.id)

class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name="Заказ")
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveIntegerField(verbose_name="Колличество", default='1')
    price_purchase = models.DecimalField(verbose_name="Цена закупки", max_digits=10, decimal_places=2)
    markup = models.DecimalField(verbose_name="Наценка", max_digits=4, decimal_places=2)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        added_price = (self.price_purchase * self.markup)/100
        return ((self.price_purchase + added_price) * self.quantity)
