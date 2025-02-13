from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *

class ProductView(APIView):
    def get(self,request):
        all_products=Product.objects.all()
        serialized_products=Products_Serializer(all_products,many=True).data
        # products_data=[]
        # for product in all_products:
        #     singleproduct={
        #         'id':product.id,
        #         'product_name' :product.product_name,
        #         'code':product.code,
        #         'price':product.price 
        #     }
        #     products_data.append(singleproduct)
        return Response(serialized_products)
    def post(self,request):
        new_product=Products_Serializer(data=request.data)
        if new_product.is_valid():
            new_product.save()
            return Response('data saved')
        else:  
            return Response(new_product.errors)  
        # new_product=Product(product_name=request.data['product_name'],code=request.data['code'],price=request.data['price'],Category_Name=request.data['Category_Name'])
        # print(request.data)
        # new_product.save()
        
        # return Response('data saved')
class Product_ViewById(APIView):
    def get(self,request,id):      #
        product=Product.objects.get(id=id)
        Single_product=Products_Serializer(product).data #with serializer
        # singleproduct={
        #         'id':product.id,
        #         'product_name' :product.product_name,
        #         'code':product.code,
        #         'price':product.price             without serializer

        #     }
            
        return Response(Single_product)
    def patch(self,request,id):

        product= Product.objects.filter(id=id)

        new_values=Products_Serializer(product,data=request.data,partial=True)

        if new_values.is_valid():
            new_values.save()
            return Response('New Values are saved')
        else:
            return Response(new_values.errors)
        
        # product.update(product_name=request.data['product_name'],code=request.data['code'],price=request.data['price'],Category_Reference=request.data['Category_Reference_id'])

        # return Response('updated')
    def delete(self,request,id):
        product=Product.objects.get(id=id)
        product.delete()

        return Response('deleted')
    
class CategoryView(APIView):
    def get(self,request):
        all_category=Category_Serializer(Category.objects.all(),many=True).data

        return Response(all_category)    
    
    def post(self,request):

        new_category=Category_Serializer(data=request.data)
        

        if new_category.is_valid():
            new_category.save()

            return Response('data sAVED')
        else:
            return Response(new_category.errors)
        
class CateoryGetById(APIView):
    def get(self,request,id):
        category=Category.objects.get(id=id)
        
        category_serialized=Category_Serializer(category).data
        print(category_serialized)
        return Response(category_serialized)
    def delete(self,request,id):
        category=Category.objects.get(id=id)
        category.delete()
        return Response('deleted')  

    def patch(self,request,id):
        category=Category.objects.get(id=id)

        category_serializes=Category_Serializer(category,data=request.data,partial=True)

        if category_serializes.is_valid():
            category_serializes.save()
            return Response('updated')

        else:
            return Response(category_serializes.errors)  
        
       