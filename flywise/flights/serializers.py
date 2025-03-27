
""" Serializers for models """
from rest_framework import serializers

from .models import Flight, PricePrediction


class FlightSerializer(serializers.ModelSerializer):
    """
    Serializer for the Flight model.
    """
    class Meta:
        """ Serilizer fields for Flight """
        model = Flight
        fields = '__all__'


class PricePredictionSerializer(serializers.ModelSerializer):
    """ Serializer for Prediction model """
    class Meta:
        """ Serializer fields for Prediction """
        model = PricePrediction
        fields = '__all__'
