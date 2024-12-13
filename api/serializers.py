from rest_framework import serializers
from .models import student,teacher

class studentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=student
        fields='__all__'

    # name=serializers.CharField(validate='name_length')    

    #field level validation

    # def validate_name(self,value):
    #     if len(value)<2:
    #         raise serializers.ValidationError('name is too short') 
    #     else :
    #         return value    
        
    #object level validation

    def validate(self,data):
        if data['name']==data['place']:
            raise serializers.ValidationError('place and name  cant be same name andjuifhevbi')
        else:
            return data 
    def name_length(value):
        if len(value)<2:
            raise serializers.ValidationError('name too short')