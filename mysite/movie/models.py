from django.db import models

from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, null=False)
    image = models.ImageField(name="image", upload_to='category_images')

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"Category # {self.id}({self.name})"


class Product(models.Model):
    category_id = models.ForeignKey(Category, name="category", null=False, on_delete=models.CASCADE)
    image = models.ImageField(name="image", upload_to='product_images')
    name = models.CharField(max_length=50, null=False)
    shelflife_date = models.DateField(null=False, name="date", auto_now=True)
    amount_in_stock = models.IntegerField(name="amount_in_stock", default=0)
    price = models.IntegerField(name="price", null=False)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return f"Product # {self.id}"

class Provider(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=225, null=False)
    next_delivery_date = models.DateField(auto_now=True, null=False)

    class Meta:
        verbose_name = "Provider"
        verbose_name_plural = "Providers"

    def __str__(self):
        return f"Provider # {self.id} of {self.category.name} category"


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, null=False)
    avatar = models.ImageField(name="avatar", upload_to='avatars')

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customer"

    def __str__(self):
        return f"User # {self.id} ({self.user.first_name} {self.user.last_name})"


class PaymentInfo(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=20, name="cc_number")
    expiration_date = models.CharField(max_length=10, name="expiration")

    class Meta:
        verbose_name = "PaymentInfo"
        verbose_name_plural = "PaymentInfo's"

    def __str__(self):
        return f"Payment info of {self.owner.first_name} {self.owner.last_name}"


class DeliveryAddress(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=225, null=False)
    city = models.CharField(max_length=225, null=False)
    street = models.CharField(max_length=225, null=False)
    building_number = models.IntegerField(name="building_number", null=False)
    floor = models.IntegerField(name="floor", default=1)
    apartments = models.CharField(max_length=50, name="apartments", null=False)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"Delivery address of {self.owner.first_name} {self.owner.last_name}"


class Order(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    total = models.IntegerField(null=False)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Order of {self.owner.first_name} {self.owner.last_name} for {self.total}$"
