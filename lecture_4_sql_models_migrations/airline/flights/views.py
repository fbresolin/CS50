from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Flight, Passenger
from django.urls import reverse


# Create your views here.


def index(request):
    return(render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    }))


def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    return(render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
    }))


def book(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    if request.method == "POST":
        passenger = Passenger.objects.get(id=request.POST["non_passenger_id"])
        passenger.flights.add(flight)
        passenger.save()
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
    else:
        return(render(request, "flights/book.html", {
            "flight": flight,
            "non_passengers": Passenger.objects.exclude(flights=flight),
        }))
