from enum import Enum, auto

class StringCase(Enum):
    Plain = auto()
    CamelCase = auto()
    SnakeCase = auto()
    KebabCase = auto()

class Name:
    def __init__(self, ja_full: str, en_full: str) -> None:
        ja_split = ja_full.split()
        en_split = en_full.split()
        if len(ja_split) == 2:
            self._family = (ja_split[0], en_split[1])
            self._given = (ja_split[1], en_split[0])
        else: # for Poka
            self._family = (None, None)
            self._given = (ja_split[0], en_split[0])

    def get_full_name(self, en: bool = False, case: StringCase = StringCase.Plain) -> str:
        name_list = self.get_full_name_as_list(en)

        if case == StringCase.CamelCase:
            return self._concat_name_list(name_list, "")
        elif case == StringCase.SnakeCase:
            return self._concat_name_list(name_list, sep="_", lower=True)
        elif case == StringCase.KebabCase:
            return self._concat_name_list(name_list, sep="-", lower=True)
        return self._concat_name_list(name_list)

    def _concat_name_list(self, name_list: list[str], sep: str = " ", lower: bool = False) -> str:
        if lower:
            name_list = [n.lower() for n in name_list]
        return sep.join(name_list)

    def get_full_name_as_list(self, en: bool = False) -> list[str]:
        family = self.get_family_name(en)
        given = self.get_given_name(en)
        if family is None:
            result = [given]
        else:
            result = [family, given]
        return reversed(result) if en else result

    def get_family_name(self, en: bool = False) -> str | None:
        return self._family[int(en)]

    def get_given_name(self, en: bool = False) -> str:
        return self._given[int(en)]

class Tags:
    def __init__(self, blog: str, talk: str = None, instagram: str = None) -> None:
        self.blog = blog
        self.talk = talk
        self.instagram = instagram

class Accounts:
    def __init__(self, instagram: str) -> None:
        self.instagram = instagram

class Member:
    def __init__(self, id: int, gen: int, name: Name, tags: Tags, accounts: Accounts = None) -> None:
        self.id = id
        self.gen = gen
        self.name = name
        self.tags = tags
        self.accounts = accounts