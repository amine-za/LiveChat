import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Message, Room
from datetime import datetime


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = f"room_{self.scope['url_route']['kwargs']['room_id']}"
        print("connect function:" , self.room_name)
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()
        # self.contact = self.scope['url_route']['kwargs']['contact']
        # self.user = self.scope['url_route']['kwargs']['user']
        
        # self.room_name = f"{self.contact}_{self.user}"
        # self.room_name = f"chat_{self.roomId}"
        
    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)
        # await super().disconnect(code)
        # self.close(code)
    
    async def receive(self, text_data):
        data_json = json.loads(text_data)
        message = data_json
        print("receive function: ", message)
        
        sig = {'type': 'send_message',
               'message': message}
        
        await self.channel_layer.group_send(
            self.room_name, sig)
        
        
    async def send_message(self, event):
        message = event["message"]
        print("send_message function: ", message)
        await self.create_message(data = message)
        await self.send(text_data=json.dumps({"message": message}))
        # await self.channel_layer.group_send(
        #     self.room_name,
        #     {
        #         'type': 'chat_message',
        #         'message': message
        #     }
        # )
    
    # async def chat_message(self, event):
    #     print("chat message function")
    #     message = event['message']
    #     response = {
    #         "receiver": message["receiver"],
    #         "user": message["user"],
    #         "message": message["message"],
    #     }
    #     await self.send(text_data=json.dumps({"message": response}))

    @database_sync_to_async
    def create_message(self, data):
        print("create message function")
        Message.objects.create(
            message=data["message"],
            sender=data["user"],
            receiver=data["receiver"])