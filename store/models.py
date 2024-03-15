from django.db import models

# Create your models here.
class Promotion(models.Model):
    description = models.CharField(max_length = 255)
    descount = models.FloatField()

class Collection(models.Model):
    title = models.CharField(max_length = 255)


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6 , decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection , on_Delete = models.PROTECT)
    promotion = models.ManyToManyField(Promotion)


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_CHOICES = [
        ('MEMBERSHIP_BRONZE' , 'Bronze'),
        ('MEMBERSHIP_SILVER' , 'Silver'),
        ('MEMBERSHIP_GOLD' , 'Gold'),
        ]
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(unique = True)
    phone_number = models.CharField(max_length = 255)
    birth_date = models.DateField(null = True)
    membership = models.CharField(max_length = 1 , choices = MEMBERSHIP_CHOICES, default = 'MEMBERSHIP_BRONZE') 

class Order(models.Model):
    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLETE = 'C'
    PAYMENT_FAILED = 'F'
    PAYMENT_CHOICES = [
        ('PAYMENT_PENDING' , 'Pending'),
        ('PAYMENT_COMPLETE' , 'Pending'),
        ('PAYMENT_FAILED' , 'Pending'),
    ]
    placed_at = models.DateTimeField(auto_now_add = True)
    payment_status = models.CharField(max_length = 1 , choices = PAYMENT_CHOICES , default = PAYMENT_PENDING) 
    customer = models.ForeignKey(Customer , on_Delete = models.PROTECT )         

# One to One relationship between a Customer and Address models haha
class Address(models.Model):
    street = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    customer = models.OneToOneField(Customer , on_Delete = models.CASCADE , primary_key = True)



    # ########################################
# One to Many relationship between a Customer and Address models haha
# class Address(models.Model):
#     street = models.CharField(max_length = 255)
#     city = models.CharField(max_length = 255)
#     customer = models.ForeignKey(Customer , on_Delete = models.CASCADE)
    # ########################################



class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add = 255)


class OrderItem(models.Model):
    order = models.ForeignKey(Order , on_Delete = models.PROTECT)
    cart = models.ForeignKey(Cart , on_Delete = models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits = 6 , decimal_places = 2)

class cartItem(models.Model):
    cart = models.ForeignKey(Cart , on_Delete = models.CASCADE)
    product = models.ForeignKey(Product , on_Delete = models.CASCADE)
    quantity = models.PositiveSmallIntegerField()