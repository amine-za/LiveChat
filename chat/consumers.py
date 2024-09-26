import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Message, Room
from datetime import datetime

channel_layer = get_channel_layer()

class ChatConsumer(AsyncWebsocketConsumer):        
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_id']
        print("self is : ", self)
        print("connect function:" , self.room_name)
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()
    
    
    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    
    async def get_receiver_channel(self, receiver):
        channel_layer = get_channel_layer()
        return await channel_layer.get(f"user_channel_{receiver}")
    
    
    async def receive(self, text_data):
        data_json = json.loads(text_data)
        message = data_json['message']
        user = data_json.get("user")
        receiver = data_json.get("receiver")
        
        print("receive function: ", message, "the receiver: ")
        
        enent = {
            'type': 'send_message',
            'message': {"user": user, "receiver":receiver, "message":message},
            'time': datetime.now()
            }
        await self.channel_layer.group_send(self.room_name, enent)


    async def send_message(self, event):
        print("send_message function: ", event["message"])
        
        await self.create_message(data = event)
        await self.send(text_data=json.dumps({"message": event["message"]}))


    @database_sync_to_async
    def create_message(self, data):
        message = data["message"]
        print("create_message function:", message)
        if not (Message.objects.filter(time_stamp=data["time"], message=message["message"], sender=message["user"], receiver=message["receiver"]).exists()):
            Message.objects.create(
                sender=message["user"],
                receiver=message["receiver"],
                message=message["message"],
                time_stamp=data["time"])
