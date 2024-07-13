from enum import Enum

from database import utils

def get_battler_tag_type_enum(base_url: str) -> Enum:
    response_text = utils.get_response_text(f'{base_url}/src/enums/battler-tag-type.ts')

    battler_tag_type = filter(lambda x: "{" not in x and "}" not in x and x != "", response_text.split('\n'))
    battler_tag_type = map(utils.strip_and_remove_commas, battler_tag_type)
    battler_tag_type = map(utils.strip_and_remove_quotes, battler_tag_type)
    battler_tag_dict = {}

    for entry in battler_tag_type:
        key, value = entry.split('=')
        battler_tag_dict[key.strip()] = value.strip()

    BattlerTagType = Enum('BattlerTagType', battler_tag_dict)

    return BattlerTagType

if __name__ == "__main__":
    repo = 'pagefaultgames/pokerogue/main'
    base = f'https://raw.githubusercontent.com/{repo}'
    battler_tag_type = get_battler_tag_type_enum(base)
    print([e.name for e in battler_tag_type])
    print([e.value for e in battler_tag_type])
