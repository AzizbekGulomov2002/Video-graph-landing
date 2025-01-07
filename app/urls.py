from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SlideViewSet, ServiceViewSet, StatisticViewSet, TeamViewSet,
    BlogViewSet, AboutUsViewSet, TypePortfolioViewSet, PortfolioViewSet,
    MessageViewSet, GalleryViewSet
)

router = DefaultRouter()
router.register('slides', SlideViewSet)
router.register('services', ServiceViewSet)
router.register('statistics', StatisticViewSet)
router.register('teams', TeamViewSet)
router.register('blogs', BlogViewSet)
router.register('about-us', AboutUsViewSet)
router.register('type-portfolios', TypePortfolioViewSet)
router.register('portfolios', PortfolioViewSet)
router.register('messages', MessageViewSet)
router.register('galleries', GalleryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
