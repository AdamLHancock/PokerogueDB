from enum import Enum

from database import utils

def get_ease_type_enum(base_url: str) -> Enum:
    response_text = utils.get_response_text(f'{base_url}/src/enums/ease-type.ts')

    ease_type = filter(lambda x: "{" not in x and "}" not in x and x != "", response_text.split('\n'))
    ease_type = map(utils.strip_and_remove_commas, ease_type)
    ease_type = map(utils.strip_and_remove_quotes, ease_type)
    ease_type_dict = {}

    for entry in ease_type:
        if entry == "NONE":
            ease_type_dict[entry] = "NONE"
        else:
            key, value = entry.split('=')
            ease_type_dict[key.strip()] = value.strip()

    EaseType = Enum('EaseType', ease_type_dict)

    return EaseType

if __name__ == "__main__":
    repo = 'pagefaultgames/pokerogue/main'
    base = f'https://raw.githubusercontent.com/{repo}'
    ease_type = get_ease_type_enum(base)
    print([e.name for e in ease_type])
    print([e.value for e in ease_type])
