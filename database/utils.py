import requests
import os
from enum import Enum
from database.enums.getters import (
    abilities, arena_tag_type, battler_tag_type,
    battle_spec, battle_style, berry_type, 
    biome, challenges, color, 
    ease_type, egg_source_type, egg_type, 
    moves, party_member_strength, passive, 
    player_gender, species, time_of_day, 
    trainer_type, ui_theme, variant_tier, variant_tiers
)

def get_response_text(url: str) -> str:
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    return ""

def get_response_json(url: str) -> dict:
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    return {}

def strip_and_remove_commas(s):
    return s.strip().replace(",", "")

def strip_and_remove_quotes(s):
    return s.strip().replace('"', "")

def get_base_path() -> str:
    return os.path.dirname(os.path.abspath(__file__)).split("database")[0] + "database"

def write_enum(name: str, enum: Enum):
    path = f'{get_base_path()}/enums/{name.lower()}.py'
    enum_entries = [f"\t{entry.name} = {entry.value}" for entry in enum]
    enum_code = "\n".join(enum_entries)

    enum_definition = f"class {name}(Enum):\n{enum_code}\n"

    with open(path, 'w+') as f:
        f.write(f"from enum import Enum\n\n{enum_definition}")

def write_string_enum(name: str, enum: list):
    path = f'{get_base_path()}/enums/{name.lower()}.py'
    enum_entries = [f"\t{entry.name} = \"{entry.value}\"" for entry in enum]
    enum_code = "\n".join(enum_entries)

    enum_definition = f"class {name}(Enum):\n{enum_code}\n"

    with open(path, 'w+') as f:
        f.write(f"from enum import Enum\n\n{enum_definition}")

def write_color_enum(name: str, colors: list):
    path = f'{get_base_path()}/enums/{name.lower()}.py'
    with open(path, 'w+') as f:
        f.write(f'from enum import Enum\n\n')
        for color in colors:
            f.write(f"class {name}(Enum):\n")
            for entry in color:
                f.write(f"\t{entry.name} = \"{entry.value}\"\n")
            f.write('\n')

def write_all_enums(base_url: str):
    enums = {
        "Ability": abilities.get_ability_enum(base_url),
        "ArenaTagType": arena_tag_type.get_arena_tag_type_enum(base_url),
        "BattleSpec": battle_spec.get_battle_spec_enum(base_url),
        "BattleStyle": battle_style.get_battle_style_enum(base_url),
        "BattlerTagType": battler_tag_type.get_battler_tag_type_enum(base_url),
        "BerryType": berry_type.get_berry_type_enum(base_url),
        "Biome": biome.get_biome_enum(base_url),
        "Challenge": challenges.get_challenges_enum(base_url),
        "Color": color.get_all_color_enums(base_url),
        "EaseType": ease_type.get_ease_type_enum(base_url),
        "EggSourceType": egg_source_type.get_egg_source_type_enum(base_url),
        "EggType": egg_type.get_egg_type_enum(base_url),
        "Moves": moves.get_moves_enum(base_url),
        "PartyMemberStrength": party_member_strength.get_party_member_strength_enum(base_url),
        "Passive": passive.get_passive_enum(base_url),
        "PlayerGender": player_gender.get_player_gender_enum(base_url),
        "Species": species.get_species_enum(base_url),
        "TimeOfDay": time_of_day.get_time_of_day_enum(base_url),
        "TrainerType": trainer_type.get_trainer_type_enum(base_url),
        "UITheme": ui_theme.get_ui_theme_enum(base_url),
        "VariantTier": variant_tier.get_variant_tier_enum(base_url),
        "VariantTiers": variant_tiers.get_variant_tiers_enum(base_url)
    }
    str_enums = ["ArenaTagType", "BattlerTagType", "EaseType", ]
    for key in enums.keys():
        if key == "Color":
            write_color_enum(key, enums[key])
        elif key in str_enums:
            write_string_enum(key, enums[key])
        else:
            write_enum(key, enums[key])

if __name__ == "__main__":
    repo = 'pagefaultgames/pokerogue/main'
    base = f'https://raw.githubusercontent.com/{repo}'
    write_all_enums(base)
