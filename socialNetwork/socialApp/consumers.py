import json
from channels.generic.websocket import AsyncWebsocketConsumer

# Consumer for chat application
class ChatConsumer(AsyncWebsocketConsumer):
    # connect to websocket
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    # disconnect from websocket
    async def disconnect(self,close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # recieves chat message
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        messageText = text_data_json['message']
        username = text_data_json['username']
        message = ('@'+ username + ': ' + messageText)


        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message
            }
        )

    # send chat message
    async def chat_message(self,event):
        message = event['message']
        username = self.scope["user"].username


        await self.send(text_data=json.dumps({
            'message':message,
            'username':username
        })
        ) 
