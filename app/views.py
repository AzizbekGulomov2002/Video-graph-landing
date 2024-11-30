from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Slide, Service, Statistic, Team, Blog, AboutUs, TypePortfolio, Portfolio, Gallery
from .forms import MessageForm

# Index view for all classes
def index(request):
    context = {
        'slides': Slide.objects.all(),
        'services': Service.objects.all(),
        'statistics': Statistic.objects.all(),
        'teams': Team.objects.all(),
        'blogs': Blog.objects.all(),
        'about_us': AboutUs.objects.first(),
        'type_portfolios': TypePortfolio.objects.all(),
        'portfolios': Portfolio.objects.all(),
        'gallery':Gallery.objects.all()
    }
    return render(request, 'index.html', context)

# Detail views for each class
def slides(request):
    slides = Slide.objects.all()
    return render(request, 'slides.html', {'slides': slides})

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def contacts(request):
    contacts = AboutUs.objects.all()
    return render(request, 'contact.html', {'contacts': contacts})


def statistics(request):
    # Fetch all statistics from the Statistic model
    statistics = Statistic.objects.all()
    return render(request, 'statistics.html', {'statistics': statistics})

def teams(request):
    # Fetch all the team members from the Team model
    team_members = Team.objects.all()
    return render(request, 'teams.html', {'team_members': team_members})

def blogs(request):
    # Fetch all blogs from the database
    blogs = Blog.objects.all()
    return render(request, 'blogs.html', {'blogs': blogs})


def about_us(request):
    about_us = get_object_or_404(AboutUs)
    return render(request, 'about.html', {'about_us': about_us})

def portfolios(request):
    portfolios = Portfolio.objects.all()  # Fetch all portfolio items
    distinct_types = portfolios.values_list('type__name', flat=True).distinct()  # Get distinct type names
    return render(request, 'portfolio.html', {
        'portfolios': portfolios,
        'distinct_types': distinct_types
    })


def message_form(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'message_success.html')
    else:
        form = MessageForm()
    return render(request, 'message_form.html', {'form': form})

def gallery_view(request):
    gallery_items = Gallery.objects.all()
    return render(request, 'gallery.html', {'gallery_items': gallery_items})



# View to handle the form submission
def submit_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()  # Save the message to the database
            return redirect('success')  # Redirect to a success page (you can create one)
        else:
            return HttpResponse('Form is not valid', status=400)

    # If it's a GET request, just display the form
    form = MessageForm()
    return render(request, 'index.html', {'form': form})

