from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Contact, Message
from django.db.models import Q
from django.contrib import messages  # Import this to send error messages to the template

def HomeView(request):
    if request.method == 'POST' :
        usern = request.POST['username']
        contact = request.POST['Contact']
        
        if usern == contact:
            messages.error(request, "Username and Contact cannot be the same.")
            return render(request, "home.html")
        
        try:
            existing_contact1 = User.objects.get(username__iexact=usern)
        except User.DoesNotExist:
            User.objects.create_user(username=usern, password=None, email='')
            
        try:
            existing_contact2 = User.objects.get(username__iexact=contact)
        except User.DoesNotExist:
            User.objects.create_user(username=contact, password=None, email='')
        
        return redirect("chat", contact_name=contact, username=usern)
    return render(request, "home.html")
        

<<<<<<< HEAD
def ChatView(request, contact_name, username):
    if request.method == 'POST' :
        new_message = request.POST['message_input']
        print ("the new message is:", new_message)
        Message.objects.create(receiver=contact_name, sender=username, message=new_message)
        return redirect("chat", contact_name=contact_name, username=username)
    try:
        contactObj = User.objects.get(username__iexact=contact_name)
    except User.DoesNotExist:
        return HttpResponse("Contact not found", status=404)
    try:
        userObj = User.objects.get(username__iexact=username)
    except User.DoesNotExist:
        return HttpResponse("Contact not found", status=404)
    get_messages = Message.objects.filter(Q(receiver=userObj, sender=contactObj) | Q(receiver=contactObj, sender=userObj))
    context = {
        "messages": get_messages,
        "user": userObj,
        "contact": contactObj
=======
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
>>>>>>> f9d18dff2f4bf56ee7940e54f4f5135ea41e6319
    }
    return render(request, "ChatPage.html", context)