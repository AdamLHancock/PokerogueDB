import requests

def get_urls(lang: str = 'en', repo: str = 'pagefaultgames/pokerogue/main') -> dict:
    return {
        'main': f'https://raw.githubusercontent.com/{repo}',
        'baseStats': '/src/data/pokemon-species.ts',
        'masterList': '/public/images/pokemon/variant/_masterlist.json',
        'abilities': f'/src/locales/{lang}/ability.ts',
        'abilitiesFlags': '/src/data/ability.ts',
        'moves': '/src/data/move.ts',
        'moveDescriptions': f'/src/locales/{lang}/move.ts'
    }

def get_response_text(url: str) -> str:
    return requests.get(url).text

def get_response_json(url: str) -> dict:
    return requests.get(url).json()
