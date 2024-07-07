from django.db import models


class CarManager(models.Manager):
    def get_only_tesla(self):
        return self.filter(brand='tesla')

