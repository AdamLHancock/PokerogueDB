from enum import Enum

from database import utils

def get_egg_source_type_enum(base_url: str) -> Enum:
    response_text = utils.get_response_text(f'{base_url}/src/enums/egg-source-types.ts')
    egg_source_type = filter(lambda x: "{" not in x and "}" not in x and x != "", response_text.split('\n'))
    egg_source_type = map(utils.strip_and_remove_commas, egg_source_type)
    egg_source_type = list(egg_source_type)

    EggSourceType = Enum('EggSourceType', egg_source_type, start=0)

    return EggSourceType

if __name__ == "__main__":
    repo = 'pagefaultgames/pokerogue/main'
    base = f'https://raw.githubusercontent.com/{repo}'
    egg_source_type = get_egg_source_type_enum(base)
    print([e.name for e in egg_source_type])
    print([e.value for e in egg_source_type])
