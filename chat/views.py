from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Room, Message
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
            User.objects.get(username__iexact=usern)
        except User.DoesNotExist:
            User.objects.create_user(username=usern, password=None, email='')
            
        try:
            User.objects.get(username__iexact=contact)
        except User.DoesNotExist:
            User.objects.create_user(username=contact, password=None, email='')
        
        tmp = Room.objects.filter(Q(user1=usern, user2=contact)|Q(user1=contact, user2=usern))
        if tmp.exists():
            roomId = str(tmp.first().room_id)
        else:
            roomId = str(Room.objects.count())
            Room.objects.create(room_id=roomId, user1=contact, user2=usern)

        return redirect("chat", contact_name=contact, username=usern, roomId=roomId)
    return render(request, "HomePage.html")
        
def ChatView(request, contact_name, username, roomId):
    # if request.method == 'POST' :
    #     new_message = request.POST['message_input']
    #     # print ("the new message is:", new_message)
    #     tmp = Message.objects.create(receiver=contact_name, sender=username, message=new_message)
    #     print("the new message is: ", new_message, "||", )
    #     return redirect("chat", contact_name=contact_name, username=username)
    # try:
    #     contactObj = User.objects.get(username__iexact=contact_name)
    # except User.DoesNotExist:
    #     return HttpResponse("Contact not found", status=404)
    # try:
    #     userObj = User.objects.get(username__iexact=username)
    # except User.DoesNotExist:
    #     return HttpResponse("Contact not found", status=404)
    get_messages = Message.objects.filter(Q(receiver=username, sender=contact_name) | Q(receiver=contact_name, sender=username))
    context = {
        "messages": get_messages,
        "user": username,
        "contact": contact_name,
        "room_id": roomId
    }
    return render(request, "ChatPage.html", context)