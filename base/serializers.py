from rest_framework import serializers
from .models import student




class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'


    def validate(self,data):
            if data['roll'] <20:
                raise serializers.ValidationError({'msg':'roll canot be less than 20'})
            

            if data['name']:
             for n in data['name']:
              if n.isdigit():
                raise serializers.ValidationError({'msg':'Name cannot be numeric.'})



            return data    
                       