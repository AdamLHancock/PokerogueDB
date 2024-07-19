import re
import json
def parseAbilities(textAbilities: str) -> dict:
    abilitiesMatch = re.findall(".*?:.*?}", textAbilities, re.IGNORECASE | re.DOTALL)
    abilities = {}

    abilities["ABILITY_NONE"] = {}
    abilities["ABILITY_NONE"]["name"] = "ABILITY_NONE"
    abilities["ABILITY_NONE"]["ingameName"] = "None"
    abilities["ABILITY_NONE"]["description"] = ""
    abilities["ABILITY_NONE"]["flags"] = []

    if abilitiesMatch:
        for ability in abilitiesMatch:
            matches = re.search(r"\"?(\w+)\"?\s*:\s*{\s*\w+:\s+\"(.*?)\"\W+\w+:\W\"(.*?)\",\s*(?:\n|})", ability, re.I)
            if matches is not None:
                abilityName = 'ABILITY_' + re.sub(r"(\d+)", r" \g<1>", re.sub(r"([A-Z])", r" \g<1>", matches.group(1))).strip().replace(" ", "_").upper()
                inGameName = matches.group(2)
                description = matches.group(3).replace("\\n", " ")
                abilities[abilityName] = {
                    'name': abilityName,
                    'inGameName': inGameName,
                    'description': description,
                    'flags': [],
                    'generation': 0
                }
    return abilities

def parseAbilitiesFlags(textAbilitiesFlags: str, abilities: dict) -> dict:
    abilitiesFlagMatch = re.findall(r"new\sAbility\(Abilities\.\w+.*?(?=new\s*Ability.*?Abilities.*?,|;)", textAbilitiesFlags, re.I | re.DOTALL)

    if abilitiesFlagMatch:
        for abilityFlag in abilitiesFlagMatch:
            abilityData = re.search(r".*?(Abilities.\w+), (\d).*", abilityFlag, re.I | re.DOTALL)
            if abilityData is not None:
                abilityName = abilityData.group(1).upper().replace("ABILITIES.", "ABILITY_")
                abilityGeneration = int(abilityData.group(2))
                if abilityName in abilities:
                    abilities[abilityName]["generation"] = abilityGeneration
                    abilityFlagMatch = re.search(r".*?(\.unimplemented|\.partial).*", abilityFlag, re.I | re.DOTALL)
                    if abilityFlagMatch is not None:
                        abilities[abilityName]["flags"].append(abilityFlagMatch.group(1).replace(".", "").upper())
    return abilities
