from enum import Enum

from database.enums import utils

def process_list(species: list) -> dict:
    prev = 0
    species_dict = {}
    for entry in species:
        if '=' in entry:
            key, value = entry.split('=')
            species_dict[key.strip()] = int(value.strip())
            prev = int(value.strip())
        else:
            species_dict[entry.strip()] = prev + 1
            prev = species_dict[entry.strip()]
    return species_dict

def get_species_enum(base_url: str) -> Enum:
    response_text = utils.get_response_text(f'{base_url}/src/enums/species.ts')

    species = filter(lambda x: "{" not in x and "}" not in x and x != "", response_text.split('\n'))
    species = map(utils.strip_and_remove_commas, species)
    species = list(species)
    species = process_list(species)

    Species = Enum('Species', species)

    return Species

if __name__ == "__main__":
    repo = 'pagefaultgames/pokerogue/main'
    base = f'https://raw.githubusercontent.com/{repo}'
    species = get_species_enum(base)
    print([e.name for e in species])
    print([e.value for e in species])
