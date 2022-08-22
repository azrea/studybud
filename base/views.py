from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm
# Create your views here.


def home(request):
    # Room model is an object and to access its methods .objects needs to be called
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    # renders the html document when method is called and passing in the context allows page to have much needed variables
    return render(request, 'base/home.html', context)


def room(request, pk):
    # from the object Room get a room where the id = pk(short for primary key)
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)


def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)
