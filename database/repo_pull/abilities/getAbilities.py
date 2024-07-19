from database.utils import get_urls, get_response_text
from database.repo_pull.abilities.abilitiesParser import parseAbilities, parseAbilitiesFlags
import json

class AbilityObject:
    def __init__(self, name: str, inGameName: str, description: str, flags: list, generation: int):
        self.name = name
        self.inGameName = inGameName
        self.description = description
        self.flags = flags
        self.generation = generation

    def get_name(self) -> str:
        return self.name
    
    def get_inGameName(self) -> str:
        return self.inGameName
    
    def get_description(self) -> str:
        return self.description
    
    def get_flags(self) -> list:
        return self.flags
    
    def get_generation(self) -> int:
        return self.generation

def getAbilities() -> dict:
    urls = get_urls()
    abilitiesUrl = f'{urls["main"]}{urls["abilities"]}'

    abilitiesText = get_response_text(abilitiesUrl)

    return parseAbilities(abilitiesText)

def getAbilitiesFlags(abilities: dict) -> str:
    urls = get_urls()
    abilitiesFlagsUrl = f'{urls["main"]}{urls["abilitiesFlags"]}'

    abilitiesFlagsText = get_response_text(abilitiesFlagsUrl)

    return parseAbilitiesFlags(abilitiesFlagsText, abilities)

def buildAbilityObjectList(abilities: dict) -> list:
    abilityObjectList = []
    for ability in abilities:
        if "PARTIAL" in abilities[ability]["flags"]:
            abilities[ability]["inGameName"] = abilities[ability]["inGameName"] + " (P)"
        elif "UNIMPLEMENTED" in abilities[ability]["flags"]:
            abilities[ability]["inGameName"] = abilities[ability]["inGameName"] + " (N)"
        abilityObjectList.append(AbilityObject(ability, abilities[ability]["inGameName"], abilities[ability]["description"], abilities[ability]["flags"], abilities[ability]["generation"]))

    return abilityObjectList

def getAbilityObjectFromList(name: str, abilityObjectList: list) -> AbilityObject:
    for ability in abilityObjectList:
        if ability.get_name() == name:
            return ability
    return None

if __name__ == '__main__':
    abilities = getAbilitiesFlags(getAbilities())
    with open('/home/ahancock/PokerogueDB/database/abilities.json', 'w+') as f:
        json.dump(abilities, f, indent=4, ensure_ascii=False)
