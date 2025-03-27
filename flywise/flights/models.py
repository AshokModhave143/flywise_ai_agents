"""
Models for Flight, Prediction
"""
from django.db import models


class Flight(models.Model):
    """ Model for Flight object """
    airline = models.CharField(max_length=100)
    departure_city = models.CharField(max_length=100)
    arrival_city = models.CharField(max_length=100)
    departure_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.airline} {self.departure_city} -> {self.arrival_city} (${self.price})"


class PricePrediction(models.Model):
    """ Model for Predictions object """
    flight = models.ForeignKey(
        Flight, on_delete=models.CASCADE, related_name='predictions')
    predicted_price = models.FloatField()
    predicted_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Prediction: {self.flight} - ${self.predicted_price}"
