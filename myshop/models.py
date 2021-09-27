from django.db import models
from django.contrib.auth.models import User
class Order(models.Model):
    user=models.ForeignKey(User, on_delete=models.PROTECT)
    
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User, on_delete=models.PROTECT)
    name=models.CharField(max_length=20)
    email=models.EmailField()
    address=models.CharField(max_length=50)
  
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    zip=models.IntegerField()
    contact=models.IntegerField()
    
    def __str__(self):
        return 'Order {}'.format(self.id)




    
    
Product_choice=[('Electronics','Electronics'), ('Fashion','Fashion'),('Sports','Sports'),('Home & Furniture','Home & Furniture'),('Boooks','Books'),('Health & Nutritions','Health & Nutritions')]
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50, choices=Product_choice ,default="1")
    
    p_name = models.CharField(max_length=50, default="")
    p_date = models.DateField()
    desc = models.CharField(max_length=300, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.p_name

class Orderitem(models.Model):
    order=models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    quantity=models.IntegerField(default=1)

   

# Create your models here.
