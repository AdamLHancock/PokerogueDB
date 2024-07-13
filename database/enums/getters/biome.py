from enum import Enum

from database import utils

def get_biome_enum(base_url: str) -> Enum:
    response_text = utils.get_response_text(f'{base_url}/src/enums/biome.ts')
    
    biome = filter(lambda x: "{" not in x and "}" not in x and x != "", response_text.split('\n'))
    biome = map(utils.strip_and_remove_commas, biome)
    biome = list(biome)
    enum_dict = {}
    prev = 0
    for entry in biome:
        if '=' in entry:
            key, value = entry.split('=')
            enum_dict[key.strip()] = int(value.strip())
            prev = int(value.strip())
        else:
            enum_dict[entry.strip()] = prev + 1
            prev = enum_dict[entry.strip()]

    Biome = Enum('Biome', enum_dict)

    return Biome

if __name__ == "__main__":
    repo = 'pagefaultgames/pokerogue/main'
    base = f'https://raw.githubusercontent.com/{repo}'
    biome = get_biome_enum(base)
    print([e.name for e in biome])
    print([e.value for e in biome])
