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

def get_passive_enum(base_url: str) -> Enum:
    response_text = utils.get_response_text(f'{base_url}/src/enums/passive.ts')

    passive = filter(lambda x: "{" not in x and "}" not in x and x != "", response_text.split('\n'))
    passive = map(utils.strip_and_remove_commas, passive)
    passive = list(passive)
    passive = clean_comments(passive)
    passive = process_list(passive)

    Passive = Enum('Passive', passive)

    return Passive

if __name__ == "__main__":
    repo = 'pagefaultgames/pokerogue/main'
    base = f'https://raw.githubusercontent.com/{repo}'
    passive = get_passive_enum(base)
    print([e.name for e in passive])
    print([e.value for e in passive])
