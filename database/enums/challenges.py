from enum import Enum

from database.enums import utils

def get_challenge_enum(base_url: str) -> Enum:
    response_text = utils.get_response_text(f'{base_url}/src/enums/challenges.ts')
    
    challenge = filter(lambda x: "{" not in x and "}" not in x and x != "", response_text.split('\n'))
    challenge = map(utils.strip_and_remove_commas, challenge)
    challenge = list(challenge)

    Challenge = Enum('Challenge', challenge)

    return Challenge

if __name__ == "__main__":
    repo = 'pagefaultgames/pokerogue/main'
    base = f'https://raw.githubusercontent.com/{repo}'
    challenge = get_challenge_enum(base)
    print([e.name for e in challenge])