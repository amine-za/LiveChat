import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.contact = f"room_{self.scope['url_route']['kwargs']['contact']}"
        await self.channel_layer.group_add(self.contact, self.channel_name)
        
        await self.accept()
        
    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.contact, self.channel_name)
        await super().disconnect(code)
        # self.close(code)
    
    async def receive(self, text_data):
        # This method will handle incoming WebSocket messages
        data = json.loads(text_data)
        message = data['message']
        contact = data['contact']
        sender = data['sender']
        print(f"Received message: --{message}-- from {sender} to {contact}")
        
    #     await self.channel_layer.group_send(
    #         self.contact,
    #         {
    #             'type': 'chat_message',
    #             'message': message,
    #             'sender': sender
    #         }
    #     )
        
    # async def chat_message(self, event):
    #     message = event['message']

    #     # Send message to WebSocket
    #     await self.send(text_data=json.dumps({
    #         'message': message
    #     }))