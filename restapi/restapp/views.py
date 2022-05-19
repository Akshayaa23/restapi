from django.shortcuts import render
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework import status
#from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
#from rest_framework.authentication import SessionAuthentication, BasicAuthentication
#from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

#@api_view(['GET', 'POST'])
#def drink_list(request):
#    if request.method == 'GET':
#       drinks = Drink.objects.all()
#        serializer = DrinkSerializer(drinks, many=True)
#   return Response(serializer.data)

#    elif request.method == 'POST':
#       serializer = DrinkSerializer(data=request.data)
#       if serializer.is_valid():
#          serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#@api_view(['GET','PUT','DELETE'])
#def drink_detail(request,id,format=None):
#  try:
#       drink = Drink.objects.get(pk=id)
#   except Drink.DoesNotExist:
#      return Response(status=status.HTTP_404_NOT_FOUND)

#   if request.method == 'GET':
#      serializer = DrinkSerializer(drink)
#      return Response(serializer.data)  
#   elif  request.method == 'PUT':
#       serializer=DrinkSerializer(drink, data=request.data)
#       if serializer.is_valid():
#          serializer.save()
#        return Response(serializer.data, status=status.HTTP_201_CREATED)
#   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#  elif request.method == 'DELETE':
#      drink.delete()
#   return Response(status=status.HTTP_204_NO_CONTENT)
    
    
#class based APIView()
class drinkAPIView(APIView):
    def get(self,request,format=None):
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return Response(serializer.data)

    def post(self, request,format=None):
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class drinklist(APIView):
    def get_object(self,id):
        try:
            return Drink.objects.get(id=id)
        except Drink.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id,format=None):
        drink=self.get_object(id)
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)  
    
    def put(self,request,id,format=None):
        drink=self.get_object(id)
        serializer=DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id,format=None):
        drink=self.get_object(id)
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GenericAPIView(mixins.ListModelMixin,  mixins.CreateModelMixin,  mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin, mixins.RetrieveModelMixin ,generics.GenericAPIView):
    queryset =  Drink.objects.all()
    serializer_class = DrinkSerializer

    lookup_field='id'
    permission_classes = [IsAuthenticated]

    def get(self, request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request,id=None):
        return self.create(request)

    def put(self, request,id=None):
        return self.update(request,id)

    def delete(self, request, id=None):
        return self.destroy(request,id)



        

