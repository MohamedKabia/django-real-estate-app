from django.shortcuts import render
from listings.models import Listing
from realters.models import Realtor
from listings.choices import price_choices, bedroom_choices, state_choices


def home(request):
    listings = Listing.objects.order_by('-list_date').filter(is_publish=True)

    context = {
        'listings': listings,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices
    }
    return render(request, 'pages/index.html', context)


def about(request):
    realtors = Realtor.objects.order_by('-date_hired')
    mvprealtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvprealtors': mvprealtors
    }
    return render(request, 'pages/about.html', context)
