from enum import Enum


class APIRoutes(str, Enum):
    AUTH = '/auth'
    INFO = '/info'
    CAST = '/cast'
    EPISODES = '/episodes'
    QUESTIONS = '/questions'
    INVENTORY = '/inventory'
    CHARACTERS = '/characters'

    OBJECTS = '/objects'

    BREEDS = '/breeds'
    VOTES = '/votes'
    CATEGORIES = '/categories'
    def __str__(self) -> str:
        return self.value
