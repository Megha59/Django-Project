from rest_framework import serializers
from .models import doctor,patient
   
class doctorsSerializer(serializers.ModelSerializer):
   
	class Meta:
		model = doctor
		fields = '__all__'
	   
class patientsSerializer(serializers.ModelSerializer):
   
	class Meta:
		model = patient
		fields = '__all__'