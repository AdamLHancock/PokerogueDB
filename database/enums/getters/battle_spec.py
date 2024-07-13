from enum import Enum

from database import utils

def get_battle_spec_enum(base_url: str) -> Enum:
    response_text = utils.get_response_text(f'{base_url}/src/enums/battle-spec.ts')
    
    battle_spec = filter(lambda x: "{" not in x and "}" not in x and x != "", response_text.split('\n'))
    battle_spec = map(utils.strip_and_remove_commas, battle_spec)
    battle_spec = list(battle_spec)

    BattleSpec = Enum('BattleSpec', battle_spec, start=0)

    return BattleSpec

if __name__ == "__main__":
    repo = 'pagefaultgames/pokerogue/main'
    base = f'https://raw.githubusercontent.com/{repo}'
    battle_spec = get_battle_spec_enum(base)
    print([e.name for e in battle_spec])
