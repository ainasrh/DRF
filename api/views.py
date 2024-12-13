from django.shortcuts import render
from .models import student,teacher
from rest_framework.response import Response  
from .serializers import studentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics,mixins
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle,ScopedRateThrottle
#serialization

#normal view api

def student_data(request,pk):
    if request.method =="GET":
        stu = student.objects.get(id=pk)
        print(stu)
        serialized=studentSerializer(stu)
        print(serialized)
        print(serialized.data)
        json_data=JSONRenderer().render(serialized.data)
     
        return HttpResponse(json_data,content_type='application/json')
    

 # api functional view (apo)   

# @api_view(['GET','POST'])
# def StudentList(request):
#     if request.method=='GET':
#         stu=student.objects.all()
#         serialized=studentSerializer(stu,many=True)
#         print(stu)
#         return Response(serialized.data)
#     if request.method=='POST':
#         return HttpResponse('its post method')


class student_details(APIView):
   
    def get(self,request,pk):
        data=student.objects.filter(teacher=pk)
        serialized=studentSerializer(data,many=True)
        return Response(serialized.data)   

    def post(self,request,pk):
        data=studentSerializer(data=request.data)
        if data.is_valid():
            student.objects.create(name=data.validated_data['name'],
                                   roll=data.validated_data['roll'],
                                   place=data.validated_data['place'],
                                   teacher=data.validated_data['teacher'])
            return Response('succesful')
        return Response('check the data correctly')
    

    
    def put(self,request,pk):
        student_obj=student.objects.get(id=pk)
        data=studentSerializer(student_obj,data=request.data)
        if data.is_valid():
            student_obj.name=data.validated_data['name']
            student_obj.roll=data.validated_data['roll']
            student_obj.place=data.validated_data['place']
            student_obj.teacher=data.validated_data['teacher']

            student_obj.save()
            return Response('succeeded')
        return Response('unsucceful')   
    
    def delete(self,request,pk):
        student.objects.get(id=pk).delete()
        return Response(status=status.HTTP_200_OK)
    


class ListMixinStudent(mixins.ListModelMixin,generics.GenericAPIView):
    
    queryset=student.objects.all()
    serializer_class=studentSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
class DetailedProductMixin(mixins.RetrieveModelMixin,
                           mixins.CreateModelMixin,
                           mixins.DestroyModelMixin,
                           mixins.UpdateModelMixin,
                           generics.GenericAPIView):
        
        queryset=student.objects.all()
        serializer_class=studentSerializer

        def get(self,request,*args,**kwargs):
            return self.retrieve(request,*args,**kwargs)
        def put(self,request,*args,**kwargs):
            return self.update(request,*args,**kwargs)
        
class student_generic(generics.ListAPIView,generics.CreateAPIView):
    queryset=student.objects.all()
    serializer_class=studentSerializer

class generic_delete(generics.DestroyAPIView,generics.UpdateAPIView):
    queryset=student.objects.all()
    serializer_class=studentSerializer

class studentViewSet(viewsets.ModelViewSet):

    queryset=student.objects.all()
    serializer_class=studentSerializer

    authentication_classes=[SessionAuthentication]
    # permission_classes=[AllowAny]
    # permission_classes=[IsAdminUser]
    # permission_classes=[IsAuthenticated]
    # permission_classes=[IsAuthenticatedOrReadOnly]
    # permission_classes=[DjangoModelPermissions]
    permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
    throttle_classes=[AnonRateThrottle,UserRateThrottle]

class sampleStudent(APIView):

    def get(self,request,pk):
        data=student.objects.all()
        serialized=studentSerializer(data)
        return Response(serialized.data)
    
    def post(self,request):
        data=studentSerializer(data=request.data)
        if data.is_valid():
            data.validated_data.save()

    def put(self,request):
        data=student.objects.get(id=pk)
        data.objects.update(name=request.data['name'],place=request.data['place'],roll=['roll'],teacher=request.data['teacher'])        



