from enum import Enum

from database import utils

def clean_comments(passives: list) -> list:
    cleaned_passives = []
    comment = False
    for entry in passives:
        if "/*" in entry:
            comment = True
        if not comment:
            cleaned_passives.append(entry)
        if "*/" in entry:
            comment = False
    return cleaned_passives

def process_list(passives: list) -> dict:
    prev = 0
    passive_dict = {}
    for entry in passives:
        if '=' in entry:
            key, value = entry.split('=')
            passive_dict[key.strip()] = int(value.strip())
            prev = int(value.strip())
        else:
            passive_dict[entry.strip()] = prev + 1
            prev = passive_dict[entry.strip()]
    return passive_dict

def get_player_gender_enum(base_url: str) -> Enum:
    response_text = utils.get_response_text(f'{base_url}/src/enums/player-gender.ts')

    player_gender = filter(lambda x: "{" not in x and "}" not in x and x != "", response_text.split('\n'))
    player_gender = map(utils.strip_and_remove_commas, player_gender)
    player_gender = list(player_gender)
    player_gender = clean_comments(player_gender)

    PlayerGender = Enum('PlayerGender', player_gender)

    return PlayerGender

if __name__ == "__main__":
    repo = 'pagefaultgames/pokerogue/main'
    base = f'https://raw.githubusercontent.com/{repo}'
    player_gender = get_player_gender_enum(base)
    print([e.name for e in player_gender])
