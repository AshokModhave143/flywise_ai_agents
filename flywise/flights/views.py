"""
Views for Flight and Prediction agents using upsonic.ai
"""
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from upsonic import Agent, Task
from upsonic.client.tools import Search

from .serializers import FlightSerializer
from .models import Flight


class FlightViewSet(viewsets.ModelViewSet):
    """
    Flight view set
    """
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    @action(detail=False, methods=['get'])
    def predict_prices(self, request):
        """
            Predict future flight prices using AI agents
        """

        # Initialize upsonic agent
        agent = Agent(job_title="Flight Price Predictor", tools=[Search()])

        # Define task
        task_description = "Predict flight prices for the next 30 days based on historical data."
        task = Task(description=task_description)

        # Execute the task
        result = agent.do(task)

        print(f"result: {result}")

        return Response({"prediction": result}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def best_deals(self, request):
        """
            Suggest best flight deals and alternative travel dates.
        """
        # Initialize Upsonic Agent
        agent = Agent(job_title="Best Deals Finder", tools=[Search()])

        # Define the task
        task_description = "Find the best flight deals and suggest alternative travel dates for cheaper options."
        task = Task(description=task_description)

        # Execute the task
        result = agent.do(task)

        return Response({"best_deals": result})
