from enum import Enum

from database import utils

def get_battle_style_enum(base_url: str) -> Enum:
    response_text = utils.get_response_text(f'{base_url}/src/enums/battle-style.ts')
    
    battle_style = filter(lambda x: "{" not in x and "}" not in x and "*" not in x and x != "", response_text.split('\n'))
    battle_style = map(utils.strip_and_remove_commas, battle_style)
    battle_style = list(battle_style)

    BattleStyle = Enum('BattleStyle', battle_style, start=0)

    return BattleStyle

if __name__ == "__main__":
    repo = 'pagefaultgames/pokerogue/main'
    base = f'https://raw.githubusercontent.com/{repo}'
    battle_style = get_battle_style_enum(base)
    print([e.name for e in battle_style])
