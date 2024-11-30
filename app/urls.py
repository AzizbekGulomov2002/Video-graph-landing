from django.urls import path
from . import views
from app.views import submit_message
from config import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('slides/', views.slides, name='slides'),
    path('services/', views.services, name='services'),
    path('contact/', views.contacts, name='contacts'),
    path('team/', views.teams, name='teams'),
    path('statistics/', views.statistics, name='statistics'),
    path('blogs/', views.blogs, name='blogs_list'),  
    path('about/', views.about_us, name='about'),
    path('portfolio/', views.portfolios, name='portfolios'),
    path('message/', views.message_form, name='message_form'),
    path('submit-message/', submit_message, name='submit_message'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
 
