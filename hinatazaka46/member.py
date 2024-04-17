from enum import Enum, auto

class StringCase(Enum):
    Plain = auto()
    CamelCase = auto()
    SnakeCase = auto()
    KebabCase = auto()

class Name:
    def __init__(self, ja: str, en: str) -> None:
        self.ja = ja
        self.en = en

class Tags:
    def __init__(self, blog: str, talk: str = None, instagram: str = None) -> None:
        self.blog = blog
        self.talk = talk
        self.instagram = instagram

class Accounts:
    def __init__(self, instagram: str) -> None:
        self.instagram = instagram

class Member:
    def __init__(self, id: int, name: Name, tags: Tags, accounts: Accounts = None) -> None:
        self.id = id
        self.name = name
        self.tags = tags
        self.accounts = accounts

    def get_name(self, sep = '', en = False) -> str:
        pass