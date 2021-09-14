from django.http import HttpResponse
from django.shortcuts import render
from listings.choices import price_choices, house_choices, state_choices
from listings.models import Listing
from agents.models import Agent
from pages.models import CampusSchool


def index(request):
    compusSchool = CampusSchool.objects.all()
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'house_choices': house_choices,
        'compusSchool': compusSchool,
        'price_choices': price_choices
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Get all agents
    agents = Agent.objects.order_by('-joined_date')

    # Get IS BEST
    best_agents = Agent.objects.all().filter(is_best=True)

    context = {
        'realtors': agents,
        'mvp_realtors': best_agents
    }

    return render(request, 'pages/about.html', context)
