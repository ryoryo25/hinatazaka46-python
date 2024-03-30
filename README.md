# hinatazaka46-python

This package supplies some utilities for developing tools of hinatazaka46.

The following features are included:
- Converting member's ID to her name in both Japanese and Romaji.
- Getting hash tags of members' blog, official message app, and instagram from member's ID.

## How to install

Run the following command to install this package.
```bash
pip install git+https://github.com/ryoryo25/hinatazaka46-python.git@v0.0.2
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

### `id_to_name`

Converts member's ID to her name.

**Arguments:**
| VAR: TYPE | default value | description|
| ---------- | :-----------: | ---------- |
| `id: int` | - | Member's id |
| `en: bool` | `False` | Name in Romaji or not |
| `case: StringCase` | `StringCase.Plain` | Select string case such as camel case ... |

**Return value:** member's name

### `name_to_id`

Converts member's name to her ID.

**Arguments:**
| VAR: TYPE | default value | description|
| ---------- | :-----------: | ---------- |
| `name: str` | - | Member's name |
| `en: bool` | `False` | Name in Romaji or not |

**Return value:** member's ID

### `id_to_blog_tag`

Gets member's ID to her blog hash tag.

**Arguments:**
| VAR: TYPE | default value | description|
| ---------- | :-----------: | ---------- |
| `id: int` | - | Member's ID |

**Return value:** member's blog hash tag starts with '#'

### `id_to_talk_tag`

Gets member's ID to her official message app hash tag.

**Arguments:**
| VAR: TYPE | default value | description|
| ---------- | :-----------: | ---------- |
| `id: int` | - | Member's ID |

**Return value:** member's official message app hash tag starts with '#'

### `id_to_instagram_tag(id: int)`

Gets member's ID to her instagram hash tag.

**Arguments:**
| VAR: TYPE | default value | description|
| ---------- | :-----------: | ---------- |
| `id: int` | - | Member's ID |

**Return value:** member's instagram hash tag starts with '#'

**NOTE:** *returns empty string if the member doesn't have a official instagram account.*
