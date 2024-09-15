from django.shortcuts import render, redirect
from .models import Room, Message
# Create your views here.


def HomeView(request):
    if request.method == 'POST' :
        usern = request.POST['username']
        room = request.POST['room']
        try:
            existing_room = Room.objects.get(room_name__icontains=room)
        except Room.DoesNotExist:
            r = Room.objects.create(room_name=room)
        return redirect("room", room_name=room, username=usern)
    return render(request, "home.html")
        

def RoomView(request, room_name, username):
    try:
        RoomModel = Room.objects.get(room_name=room_name)
    except Room.DoesNotExist:
        return (HttpResponse("Room not found", status=404))
    get_messages = Message.objects.filter(room=RoomModel)
    context = {
        "messages": get_messages,
        "user": username,
        "room_name": RoomModel
    }
    return render(request, "room.html", context)