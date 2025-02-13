from django.db import models

    
class Category(models.Model):
    Category_Name=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.Category_Name

class Product(models.Model):
    
    Category_Reference=models.ForeignKey(Category,null=True,on_delete=models.SET_NULL)
    product_name=models.CharField(max_length=200,null=True)
    code=models.CharField(max_length=200,null=True)
    price=models.FloatField(default=0)

    def __str__(self):
        return self.product_name
    