# hinatazaka46-python

This package supplies some utilities for developing tools of hinatazaka46.

The following features are included:
- Converting member's ID to her name in both Japanese and Romaji.
- Getting hash tags of members' blog, official message app, and instagram from member's ID.

## How to install

Run the following command to install this package.
```bash
pip install "git+https://github.com/ryoryo25/hinatazaka46-python.git@$(curl -s https://api.github.com/repos/ryoryo25/hinatazaka46-python/releases/latest | jq -r '.tag_name')"
```

## How to use

Simply import this package like this:
```python
import hinatazaka46 as hinata
```

# Features

## Classes

The following classes are added.

### `StringCase`

Enum class of case of string. This enum has the following items.
- `Plain`
- `CamelCase`
- `SnakeCase`
- `KebabCase`

## Functions

The following functions are supported.

### `id_to_name(id: int, en: bool = False, case: StringCase = StringCase.Plain) -> str`

Converts member's ID to her name.

**Arguments:**
| VAR: TYPE | default value | description|
| ---------- | :-----------: | ---------- |
| `id: int` | - | Member's id |
| `en: bool` | `False` | Name in Romaji or not |
| `case: StringCase` | `StringCase.Plain` | Select string case such as camel case ... |

**Return value:** member's name

### `name_to_id(name: str, en: bool = False) -> int`

Converts member's name to her ID.

**Arguments:**
| VAR: TYPE | default value | description|
| ---------- | :-----------: | ---------- |
| `name: str` | - | Member's name |
| `en: bool` | `False` | Name in Romaji or not |

**Return value:** member's ID

### `id_to_blog_tag(id: int) -> str`

Gets member's blog hash tag from her ID.

**Arguments:**
| VAR: TYPE | default value | description|
| ---------- | :-----------: | ---------- |
| `id: int` | - | Member's ID |

**Return value:** member's blog hash tag starts with '#'

### `id_to_talk_tag(id: int) -> str`

Gets member's her official message app hash tag from her ID.

**Arguments:**
| VAR: TYPE | default value | description|
| ---------- | :-----------: | ---------- |
| `id: int` | - | Member's ID |

**Return value:** member's official message app hash tag starts with '#'

### `id_to_instagram_tag(id: int) -> str`

Gets member's instagram hash tag from her ID.

**Arguments:**
| VAR: TYPE | default value | description|
| ---------- | :-----------: | ---------- |
| `id: int` | - | Member's ID |

**Return value:** member's instagram hash tag starts with '#'

**NOTE:** *returns empty string if the member doesn't have a official instagram account.*

### `id_to_instagram_account(id: int) -> str`

Gets member's instagram username from her ID.

**Arguments:**
| VAR: TYPE | default value | description|
| ---------- | :-----------: | ---------- |
| `id: int` | - | Member's ID |

**Return value:** member's instagram username

**NOTE:** *returns `None` if the member doesn't have a official instagram account.*

### `instagram_accounts()`

Generates all existing instagram accounts.

**Arguments:**
None

**Return value:** generator for instagram accounts

### `get_nth_phase_list(n: int, en: bool = False) -> list[str]`

Generates a list of member's names within the `n`-th phase.

**Arguments:**
| VAR: TYPE | default value | description|
| ---------- | :-----------: | ---------- |
| `n: int` | - | Phase |
| `en: bool` | `False` | Name in Romaji or not |

**Return value:** a list of member's names with in the `n`-th phase