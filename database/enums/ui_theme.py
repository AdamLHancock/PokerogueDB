from enum import Enum

from database.enums import utils

def get_ui_theme_enum(base_url: str) -> Enum:
    response_text = utils.get_response_text(f'{base_url}/src/enums/ui-theme.ts')

    species = filter(lambda x: "{" not in x and "}" not in x and x != "", response_text.split('\n'))
    species = map(utils.strip_and_remove_commas, species)
    species = list(species)

    Species = Enum('Species', species)

    return Species

if __name__ == "__main__":
    repo = 'pagefaultgames/pokerogue/main'
    base = f'https://raw.githubusercontent.com/{repo}'
    species = get_ui_theme_enum(base)
    print([e.name for e in species])
