import json
import os

from googleapiclient.discovery import build

import isodate

api_key: str = os.getenv('API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""
    dict_hw = {}

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

        channel = Channel.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()

        self.title = channel['items'][0]['snippet']['title']
        self.description = channel['items'][0]['snippet']['description']
        self.url = channel['items'][0]['snippet']['thumbnails']["default"]['url']
        self.subscriberCount = channel['items'][0]['statistics']['subscriberCount']
        self.video_count = channel['items'][0]['statistics']['videoCount']
        self.viewCount = channel['items'][0]['statistics']['viewCount']

    def __str__(self):
        return f'{self.title}, {self.url}'

    def __add__(self, other):
        return int(self.subscriberCount) + int(other.subscriberCount)

    def __sub__(self, other):
        return int(self.subscriberCount) - int(other.subscriberCount)

    def __gt__(self, other):
        return int(self.subscriberCount) > int(other.subscriberCount)

    def __ge__(self, other):
        return int(self.subscriberCount) >= int(other.subscriberCount)

    def __lt__(self, other):
        return int(self.subscriberCount) < int(other.subscriberCount)

    def __le__(self, other):
        return int(self.subscriberCount) <= int(other.subscriberCount)

    def __eq__(self, other):
        return int(self.subscriberCount) == int(other.subscriberCount)

    def print_info(self, channel_id) -> None:
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        """Класс-метод возвращающий объект для работы с YouTube API"""
        api_key: str = os.getenv('API_KEY')
        object_get = build('youtube', 'v3', developerKey=api_key)
        return object_get

    def to_json(self, file_name):
        """Мохраняющий в файл значения атрибутов экземпляра `Channel`"""
        self.dict_hw['id'] = self.channel_id
        self.dict_hw['title'] = self.title
        self.dict_hw['description'] = self.description
        self.dict_hw['url'] = self.url
        self.dict_hw['subscriberCount'] = self.subscriberCount
        self.dict_hw['video_count'] = self.video_count
        self.dict_hw['viewCount'] = self.viewCount

        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(self.dict_hw, f, indent=2, ensure_ascii=False)


moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
moscowpython.print_info(moscowpython.channel_id)