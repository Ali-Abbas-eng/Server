import json
from channels.generic.websocket import AsyncWebsocketConsumer
from gptengine.SpeakingSessionManager import SpeakingSessionManager
from gptengine.conversationalists.general_conversationalist import GeneralConversationalist
from django.conf import settings
import os


class SpeakingSessionConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.ai_processor = None
        self.user_id = None
        self.path_template = None

    def session_initialiser(self):
        session_type = self.scope['query_string'].decode('utf-8').split('=')[1]
        self.ai_processor = SpeakingSessionManager(session_type)
        self.user_id = '0'
        self.path_template = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT, 'audios', self.user_id)
        os.makedirs(self.path_template, exist_ok=True)

    async def connect(self):
        self.session_initialiser()
        await self.accept()
        await self.send(text_data=json.dumps({"type": "connection_established",
                                              "message": "You are now connected"}))

    async def receive(self, text_data=None, bytes_data=None):
        input_audio_file_path = None
        output_audio_file_path = os.path.join(self.path_template, '0_out')
        if bytes_data:
            input_audio_file_path = os.path.join(self.path_template, '0_in.wav')
            with open(input_audio_file_path, 'wb') as audio_file:
                audio_file.write(bytes_data)
                audio_file.close()

        response = self.ai_processor(input_audio_file_path, output_audio_file_path)
        response['audio'] = response['audio'].replace(settings.MEDIA_ROOT, "http://127.0.0.1:8000/media")
        await self.send(text_data=json.dumps(response))
