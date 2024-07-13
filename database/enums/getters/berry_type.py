from enum import Enum

from database import utils

def get_berry_type_enum(base_url: str) -> Enum:
    response_text = utils.get_response_text(f'{base_url}/src/enums/berry-type.ts')
    
    berry_type = filter(lambda x: "{" not in x and "}" not in x and x != "", response_text.split('\n'))
    berry_type = map(utils.strip_and_remove_commas, berry_type)
    berry_type = list(berry_type)

    BerryType = Enum('BerryType', berry_type, start=0)

    return BerryType

if __name__ == "__main__":
    repo = 'pagefaultgames/pokerogue/main'
    base = f'https://raw.githubusercontent.com/{repo}'
    berry_type = get_berry_type_enum(base)
    print([e.name for e in berry_type])
