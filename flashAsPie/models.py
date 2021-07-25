import _datetime
from django.db import models



class CategoryManager(models.Manager):
    def create_category(self, category_name):
        category = self.create(category_name=category_name)
        category.save(using=self._db)
        # do something with the book
        return category

class QuantityManager(models.Manager):
    def create_quantity(self, measure):
        quantity = self.create(measure=measure)
        # do something with the book
        quantity.save()
        return quantity

class ProductManager(models.Manager):
    def create_product(self, product_name, brand_name,units, quantity_id):
        product =  self.create(
            product_name=product_name,
            brand_name=brand_name,
            quantity_id=quantity_id,
            units=units
            )
        product.save()
        return product

class NewUserManager(models.Manager):
    def create_user (self, username,email, first_name, last_name, position, phone,  password=None ):
        user = self.model(
            username = username,
            password = password,
            email = email,
            first_name = first_name,
            last_name = last_name,
            position = position,
            phone = phone
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, password, email, position, first_name, phone, last_name):
        user = self.create_user(username, password, position, email, first_name, last_name, phone)
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class SupplierManager(models.Manager):
    def create_usage(self, supplier_name):
         supplier = self.create( supplier_name=supplier_name)
         supplier.save()
         return supplier

class OrderManager(models.Manager):
    def create_order(self, date, supplier_id, user_id, product, quantity, units, is_ordered):
        order = self.create(date=date,supplier_id=supplier_id,user_id=user_id, product=product, quantity=quantity, units=units, is_ordered=is_ordered)
        order.save()
        return order

class Quantity (models.Model):
    quantity_id = models.AutoField(primary_key=True)
    measure = models.CharField(max_length = 15)
    objects = QuantityManager()
    class Meta:
        verbose_name = "Quantity"
        verbose_name_plural = 'Quantity'
    def __str__(self):
        return self.measure

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length = 20)
    objects = CategoryManager()
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = 'Category'
    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_id = models.AutoField(primary_key=True, verbose_name="ID")
    product_name = models.CharField(max_length= 50)
    brand_name = models.CharField(max_length = 20)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    units = models.IntegerField()
    quantity = models.ForeignKey(Quantity, on_delete=models.SET_NULL, null=True)
    objects = ProductManager()
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = 'Products'
    def __str__(self):
        return self.product_name


class User (models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 15, unique = True)
    password = models.CharField(max_length = 35)
    email = models.EmailField()
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    dob = models.DateField()
    position = models.CharField(max_length = 25)
    phone = models.CharField(max_length=35)
    is_admin = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name', 'last_name']
    objects = NewUserManager()

    def __str__(self):
        return (self.first_name + " " + self.last_name)

    def has_perm(self,perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Supplier (models.Model):
    supplier_id = models.AutoField(primary_key = True)
    supplier_name = models.CharField(max_length = 30)
    objects = SupplierManager()
    def __str__(self):
        return self.supplier_name  

class Order (models.Model):
    order_id = models.AutoField(primary_key = True)
    date = models.DateTimeField(auto_now_add = True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    units = models.IntegerField()
    quantity = models.ForeignKey(Quantity, on_delete=models.SET_NULL, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default = False)
    
    objects = OrderManager()

    #time when order placed
    def __str__(self):
        return self.date.strftime('%d-%m-%y Placed at : %H:%M')
