from enum import Enum

from database import utils

def get_egg_type_enum(base_url: str) -> Enum:
    response_text = utils.get_response_text(f'{base_url}/src/enums/egg-type.ts')

    egg_type = filter(lambda x: "{" not in x and "}" not in x and x != "", response_text.split('\n'))
    egg_type = map(utils.strip_and_remove_commas, egg_type)
    egg_type = list(egg_type)

    EggType = Enum('EggType', egg_type, start=0)

    return EggType

if __name__ == "__main__":
    repo = 'pagefaultgames/pokerogue/main'
    base = f'https://raw.githubusercontent.com/{repo}'
    egg_type = get_egg_type_enum(base)
    print([e.name for e in egg_type])
    print([e.value for e in egg_type])
