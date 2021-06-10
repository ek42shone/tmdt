
from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.utils.safestring import mark_safe


class Address(models.Model):
    fullAddress = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.fullAddress + ', ' + self.city + ', ' + self.country
class User(AbstractUser):
    address=models.OneToOneField(Address,on_delete=models.CASCADE)

class Payment(models.Model):
    amount = models.FloatField(max_length=100)
    additionalFee = models.FloatField(max_length=100)


class Fullname(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname + " " + self.lastname


class CreditCard(models.Model):
    creditNumber = models.BigIntegerField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)


class CreditCardPayment(Payment):
    creditCard = models.ForeignKey(CreditCard, on_delete=models.CASCADE)


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    ad = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " " + str(self.ad)


class Product(models.Model):
    TYPE = (
        ('1','Quần Áo'),
        ('2','Sách'),
        ('3','Điện Tử')
    )
    STATUS = (
        ('True', 'Đang Kinh Doanh'),
        ('False', 'Ngừng Kinh Doanh'),
    )

    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    type = models.CharField(max_length=10 , choices=TYPE)
    status = models.CharField(max_length=10 , choices=STATUS)

    def __str__(self):
        return self.name
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format('/static'+self.image.url))
        else:
            return ""
    # def category(self):
    #     if self.TYPE

class BookStatus(models.Model):
    status = models.CharField(max_length=100)


class BookDescription(models.Model):
    font = models.IntegerField()
    paperSize = models.CharField(max_length=100)
    colorFont = models.CharField(max_length=100)
    bookStatus = models.OneToOneField(BookStatus, on_delete=models.CASCADE)


class Book(Product):
    bookDescription = models.ForeignKey(BookDescription, on_delete=models.CASCADE)


class Author(models.Model):
    sex = models.CharField(max_length=100)
    age = models.IntegerField()
    fullname = models.ForeignKey(Fullname, on_delete=models.CASCADE)
    organization = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class ProductImage(models.Model):
    image = models.ImageField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Storage(models.Model):
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    # chưa nối quan hệ trong bd class

    def __str__(self):
        return str(self.address)


class Item(models.Model):
    saleOff = models.FloatField()
    price = models.FloatField()
    product = models.OneToOneField(Product, on_delete=models.CASCADE)


class ProductInStock(models.Model):
    stock = models.IntegerField()
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.CharField(max_length=100)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)


class Cart(models.Model):
    STATUS = (
        (1, 'active'),
        (2, 'inactive'),
    )

    cartType = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.IntegerField(max_length=10,choices=STATUS)



class OrderStatus(models.Model):
    status = models.CharField(max_length=100)


class Order(models.Model):
    saleOff = models.FloatField()
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)



class ItemInCart(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()


class Credit(Payment):
    creditNumber = models.BigIntegerField()


class Bill(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


class Shipment(models.Model):
    dateShip = models.DateTimeField(max_length=100)
    receiveDate = models.DateTimeField(max_length=100)
    bill = models.OneToOneField(Bill, on_delete=models.CASCADE)


class ShipmentStatus(models.Model):
    status = models.CharField(max_length=100)
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)


class DomesticShip(Shipment):
    distance = models.BigIntegerField()
    district = models.CharField(max_length=100)


class GlobalShip(Shipment):
    country = models.CharField(max_length=100)
    typeDelivery = models.CharField(max_length=100)


class Notification(models.Model):
    content = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)

    ''''''


class Genre(models.Model):
    genre = models.CharField(max_length=100)


class BookGenre(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    bookDescription = models.ForeignKey(BookDescription, on_delete=models.CASCADE)


class Electronic(Product):
    desc = models.CharField(max_length=100)


class Appliance(Electronic):
    width = models.CharField(max_length=100)
    height = models.FloatField()
    length = models.FloatField()
    type_of_appliance = models.CharField(max_length=100)


class Mobile(Electronic):
    dimension = models.FloatField()
    device_type = models.CharField(max_length=100)


class ClothingType(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Clothing(Product):
    material = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    type_of_clothing = models.ForeignKey(ClothingType, on_delete=models.CASCADE)


class Staff(User):
    workAddress = models.ForeignKey(Address, on_delete=models.CASCADE)


class StorageStaff(Staff):
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)


class OrderStatusLogs(models.Model):
    orderStatus = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)


class BusinessStaff(Staff):
    test = models.CharField(max_length=100)


class OrderStatusChangeLogs(models.Model):
    businessStaff = models.ForeignKey(BusinessStaff, on_delete=models.CASCADE)
    orderStatusLogs = models.ForeignKey(
        OrderStatusLogs, on_delete=models.CASCADE)
