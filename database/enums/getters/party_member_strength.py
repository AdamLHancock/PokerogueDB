from enum import Enum

from database import utils

def get_party_member_strength_enum(base_url: str) -> Enum:
    response_text = utils.get_response_text(f'{base_url}/src/enums/party-member-strength.ts')

    party_member_strength = filter(lambda x: "{" not in x and "}" not in x and x != "", response_text.split('\n'))
    party_member_strength = map(utils.strip_and_remove_commas, party_member_strength)
    party_member_strength = list(party_member_strength)

    PartyMemberStrength = Enum('PartyMemberStrength', party_member_strength, start=0)

    return PartyMemberStrength

if __name__ == "__main__":
    repo = 'pagefaultgames/pokerogue/main'
    base = f'https://raw.githubusercontent.com/{repo}'
    strength = get_party_member_strength_enum(base)
    print([e.name for e in strength])
