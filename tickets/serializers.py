from dataclasses import field
from rest_framework import serializers
from .models import *

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['pk' , 'name' , 'mobile' , 'reservation']

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'        