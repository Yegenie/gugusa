from rest_framework import viewsets
from .models import Portfolio
from .serializer import PortfolioSerializer

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
