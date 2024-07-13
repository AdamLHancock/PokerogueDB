from enum import Enum

from database import utils

def get_moves_enum(base_url: str) -> Enum:
    response_text = utils.get_response_text(f'{base_url}/src/enums/moves.ts')

    move_list = filter(lambda x: "{" not in x and "}" not in x and x != "" and "/**" not in x, response_text.split('\n'))
    move_list = map(utils.strip_and_remove_commas, move_list)
    move_list = list(move_list)

    cleaned_move_list = []
    comment = False
    for move in move_list:
        if "/*" in move:
            comment = True
        if not comment:
            cleaned_move_list.append(move)
        if "*/" in move:
            comment = False

    Move = Enum('Move', cleaned_move_list, start=0)

    return Move

if __name__ == "__main__":
    repo = 'pagefaultgames/pokerogue/main'
    base = f'https://raw.githubusercontent.com/{repo}'
    move = get_moves_enum(base)
    print([e.name for e in move])
