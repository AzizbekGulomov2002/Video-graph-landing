from rest_framework import viewsets
from .models import (
    Slide, Service, Statistic, Team, Blog, AboutUs,
    TypePortfolio, Portfolio, Message, Gallery
)
from .serializers import (
    SlideSerializer, ServiceSerializer, StatisticSerializer,
    TeamSerializer, BlogSerializer, AboutUsSerializer, 
    TypePortfolioSerializer, PortfolioSerializer, 
    MessageSerializer, GallerySerializer
)

class SlideViewSet(viewsets.ModelViewSet):
    queryset = Slide.objects.all()
    serializer_class = SlideSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class StatisticViewSet(viewsets.ModelViewSet):
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class TypePortfolioViewSet(viewsets.ModelViewSet):
    queryset = TypePortfolio.objects.all()
    serializer_class = TypePortfolioSerializer


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
