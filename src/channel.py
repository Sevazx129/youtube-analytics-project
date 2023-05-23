import json
import os

from googleapiclient.discovery import build

import isodate
api_key: str = os.getenv('API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self, channel_id) -> None:
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
moscowpython.print_info(moscowpython.channel_id)