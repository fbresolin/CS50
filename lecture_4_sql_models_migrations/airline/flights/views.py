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
    return(render(request, "flights/flight.html", {
        "flight": Flight.objects.get(id=flight_id),
        "passengers": Flight.objects.get(id=flight_id).passengers.all(),
    }))


def book(request, flight_id):
    if request.method == "POST":
        passenger = Passenger.objects.get(id=request.POST["passenger_id"])
        flight = Flight.objects.get(id=flight_id)
        passenger.flights.add(flight)
        passenger.save()
        return HttpResponseRedirect(reverse("flight", args=flight_id))
    else:
        return(render(request, "flights/book.html", {
            "flight": Flight.objects.get(id=flight_id),
            "passengers": Passenger.objects.all(),
        }))
