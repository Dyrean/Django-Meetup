from django.shortcuts import render, redirect

from .models import MeetUp, Participant
from .forms import RegistrationForm

from datetime import datetime
# Create your views here.


def index(request):
    meetups = MeetUp.objects.all()
    return render(request, 'meetups/index.html', {
        "meetups": meetups
    })


def meetup_details(request, slug):
    try:
        meetup = MeetUp.objects.get(slug=slug)
        registration_form = RegistrationForm()

        if request.method == "POST":
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                meetup.participants.add(participant)
                return redirect("confirm-registration", slug=slug)

        return render(request, 'meetups/meetup-details.html', {
                'meetup_found': True,
                'meetup': meetup,
                'form': registration_form
            })
    except Exception as exc:
        print(exc)
        return render(request, "meetups/meetup-details.html", {
            'meetup_found': False
        })

def confirm_registration(request, slug):
    meetup = MeetUp.objects.get(slug=slug)
    return render(request, 'meetups/registration-success.html', {
        'organizer_email': meetup.organizer
    })