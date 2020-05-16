from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

# Create your views here.


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        realtor_email = request.POST['realtor_email']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        user_id = request.POST['user_id']

        contact = Contact(listing=listing, listing_id=listing_id,  name=name, email=email, user_id=user_id,
                          message=message)
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already placed an enquiry for this listing ')
                return redirect('/listings/' + listing_id)

            else:
                contact.save()
                send_mail(
                    'testing',
                    'listing.',
                    'kabiaofficial@gmail.com',
                    [realtor_email, 'kabiamohamed1997@gmail.com'],
                    fail_silently=False
                )
                messages.success(request, 'submitted ')
                return redirect('/listings/' + listing_id)
