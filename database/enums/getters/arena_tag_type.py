from enum import Enum

from database import utils

def get_arena_tag_type_enum(base_url: str) -> Enum:
    response_text = utils.get_response_text(f'{base_url}/src/enums/arena-tag-type.ts')

    arena_tag_type = filter(lambda x: "{" not in x and "}" not in x and x != "", response_text.split('\n'))
    arena_tag_type = map(utils.strip_and_remove_commas, arena_tag_type)
    arena_tag_type = map(utils.strip_and_remove_quotes, arena_tag_type)
    arena_tag_dict = {}

    for entry in arena_tag_type:
        key, value = entry.split('=')
        arena_tag_dict[key.strip()] = value.strip()

    ArenaTagType = Enum('ArenaTagType', arena_tag_dict)

    return ArenaTagType

if __name__ == "__main__":
    repo = 'pagefaultgames/pokerogue/main'
    base = f'https://raw.githubusercontent.com/{repo}'
    arena_tag_type = get_arena_tag_type_enum(base)
    print([e.name for e in arena_tag_type])
    print([e.value for e in arena_tag_type])
