from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import *
from app.serializers import *





class ProductCrud(APIView):
    def get(self,request,pk):
        LPO=Product.objects.all()#list product objects 
        MSPO=ProductMs(LPO,many=True)#model serializers product object
        return Response(MSPO.data)
    


    def post(self,request):
        rjd=request.data
        PDO=ProductMs(data=rjd)
        if PDO.is_valid():
            PDO.save()
            return Response({'success':'inserted successfully'})
        else:
            return Response({'failed':'insertion is not done please check it once'})
        


    def put(self,request,pk):# it is used for update the  data by default we need to give all the information else it will throw the errors
        rjd=request.data
        instance=Product.objects.get(pk=pk)
        LPO=ProductMs(instance,data=rjd)
        if LPO.is_valid():
            LPO.save()
            return Response({'updation':'is successfully done'})
        else:
            return Response({'failed':'not done check once please '})
        


    def patch(self,request,pk):# it is used for update the specific data from the instance
         rjd=request.data
         instance=Product.objects.get(pk=pk)
         LPO=ProductMs(instance,data=rjd,partial=True)
         if LPO.is_valid():
            LPO.save()
            return Response({'updation':'is successfully done'})
         else:
            return Response({'failed':'not done check once please '})
    
    
    
    
    
    def delete(self,request,pk):# it is used for delete the given instance  
        instance=Product.objects.get(pk=pk).delete()
        return Response({'delete':'deleted is successfully'})




# note: if we want to put,patch,delete then we need instance(or)objects to update or partially update or delete the data 
#note1: in put method we have to give all the information  of the given instance
#note 2: in patch we have to all information or else we need to give particular information.
#note 3: delete is used for delete the data

#imp naote:when we want to pass the data through url compulsory we need primary key and put it in angularbrackets ex:<pk>

    
