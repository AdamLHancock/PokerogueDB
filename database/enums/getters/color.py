from enum import Enum
from typing import List

from database import utils

def process_entry(entry):
    key, value = entry.split('=')
    return (key.strip(), value.strip())

def get_color_enum(raw_text: str) -> Enum:
    color_list = filter(lambda x: "{" not in x and "}" not in x and x != "", raw_text.split('\n'))
    color_list = map(utils.strip_and_remove_commas, color_list)
    color_list = map(utils.strip_and_remove_quotes, color_list)
    color_list = map(process_entry, color_list)
    color_list = dict(color_list)

    Color = Enum('Color', color_list)

    return Color

def get_type_color_enum(raw_text: str) -> Enum:
    type_color_list = filter(lambda x: "{" not in x and "}" not in x and x != "", raw_text.split('\n'))
    type_color_list = map(utils.strip_and_remove_commas, type_color_list)
    type_color_list = map(utils.strip_and_remove_quotes, type_color_list)
    type_color_list = map(process_entry, type_color_list)
    type_color_list = dict(type_color_list)

    TypeColor = Enum('TypeColor', type_color_list)

    return TypeColor

def get_type_shadow_enum(raw_text: str) -> Enum:
    type_shadow_list = filter(lambda x: "{" not in x and "}" not in x and x != "", raw_text.split('\n'))
    type_shadow_list = map(utils.strip_and_remove_commas, type_shadow_list)
    type_shadow_list = map(utils.strip_and_remove_quotes, type_shadow_list)
    type_shadow_list = map(process_entry, type_shadow_list)
    type_shadow_list = dict(type_shadow_list)

    TypeShadow = Enum('TypeShadow', type_shadow_list)

    return TypeShadow

def get_shadow_color_enum(raw_text: str) -> Enum:
    shadow_color_list = filter(lambda x: "{" not in x and "}" not in x and x != "", raw_text.split('\n'))
    shadow_color_list = map(utils.strip_and_remove_commas, shadow_color_list)
    shadow_color_list = map(utils.strip_and_remove_quotes, shadow_color_list)
    shadow_color_list = map(process_entry, shadow_color_list)
    shadow_color_list = dict(shadow_color_list)

    ShadowColor = Enum('ShadowColor', shadow_color_list)

    return ShadowColor

def get_all_color_enums(base_url: str) -> List[Enum]:
    color_list = utils.get_response_text(f'{base_url}/src/enums/color.ts')
    color_list = filter(lambda x: x != '', color_list.split('export enum'))
    color_list = list(color_list)
    
    return [get_color_enum(color_list[0]), get_type_color_enum(color_list[1]), get_type_shadow_enum(color_list[2]), get_shadow_color_enum(color_list[3])]

if __name__ == "__main__":
    repo = 'pagefaultgames/pokerogue/main'
    base = f'https://raw.githubusercontent.com/{repo}'
    all_color_enums = get_all_color_enums(base)
    for color_enum in all_color_enums:
        print(color_enum)
        print([e.name for e in color_enum])
        print([e.value for e in color_enum])
