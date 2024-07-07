import os
from uuid import uuid1

from core.dataclasses.user_dataclass import ProfileDataClass


class FileService:
    @staticmethod
    def upload_avatar(instance: ProfileDataClass, file: str):
        ext = file.split('.')[-1]
        return os.path.join(instance.last_name, 'avatars', f'{uuid1()}.{ext}')

    @staticmethod
    def upload_car_photo(instance, file: str):
        ext = file.split('.')[-1]
        return os.path.join('cars_photo', f'{uuid1()}.{ext}')
