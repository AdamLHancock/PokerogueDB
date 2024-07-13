"""
import { MoveTarget, allMoves } from "./move";
import * as Utils from "../utils";
import PokemonSpecies, { PokemonForm, SpeciesFormKey, allSpecies } from "./pokemon-species";
import { GrowthRate } from "./exp";
import { Type } from "./type";
import { allAbilities } from "./ability";
import { pokemonFormLevelMoves } from "./pokemon-level-moves";
import { tmSpecies } from "./tms";
import { Abilities } from "#enums/abilities";
import { Moves } from "#enums/moves";
import { Species } from "#enums/species";

The list of imports for the api-generator.script.ts file. 
each import is an enum necessary for the resulting data structures that get created
"""

from enum import Enum

from database import utils
from database.data.move import MoveTarget
from database.data.exp import GrowthRate

def get_api_generator_data_structres() -> dict:
    targetMap = {
        "specific-move": MoveTarget.ATTACKER.value,
        "selected-pokemon-me-first": MoveTarget.NEAR_ENEMY.value,
        "ally": MoveTarget.NEAR_ALLY.value,
        "users-field": MoveTarget.USER_SIDE.value,
        "user-or-ally": MoveTarget.USER_OR_NEAR_ALLY.value,
        "opponents-field": MoveTarget.ENEMY_SIDE.value,
        "user": MoveTarget.USER.value,
        "random-opponent": MoveTarget.RANDOM_NEAR_ENEMY.value,
        "all-other-pokemon": MoveTarget.ALL_NEAR_OTHERS.value,
        "selected-pokemon": MoveTarget.NEAR_OTHER.value,
        "all-opponents": MoveTarget.ALL_NEAR_ENEMIES.value,
        "entire-field": MoveTarget.BOTH_SIDES.value,
        "user-and-allies": MoveTarget.USER_AND_ALLIES.value,
        "all-pokemon": MoveTarget.ALL.value,
        "all-allies": MoveTarget.NEAR_ALLY.value,
        "fainting-pokemon": MoveTarget.NEAR_OTHER.value
    }

    generationMap = {
        "generation-i": 1,
        "generation-ii": 2,
        "generation-iii": 3,
        "generation-iv": 4,
        "generation-v": 5,
        "generation-vi": 6,
        "generation-vii": 7,
        "generation-viii": 8,
        "generation-ix": 9
    }

    growthRateMap = {
        "slow-then-very-fast": GrowthRate.ERRATIC.value,
        "fast": GrowthRate.FAST.value,
        "medium": GrowthRate.MEDIUM_FAST.value,
        "medium-slow": GrowthRate.MEDIUM_SLOW.value,
        "slow": GrowthRate.SLOW.value,
        "fast-then-very-slow": GrowthRate.FLUCTUATING.value
    }

    regionalForms = [ "alola", "galar", "hisui", "paldea" ]

    ignoredForms = [ "gmax", "totem", "cap", "starter" ]

    generationDexNumbers = {
        1: 151,
        2: 251,
        3: 386,
        4: 494,
        5: 649,
        6: 721,
        7: 809,
        8: 905,
        9: 1010
    }

    versions = [ "scarlet-violet", "sword-shield", "sun-moon" ]

    return {
        "targetMap": targetMap,
        "generationMap": generationMap,
        "growthRateMap": growthRateMap,
        "regionalForms": regionalForms,
        "ignoredForms": ignoredForms,
        "generationDexNumbers": generationDexNumbers,
        "versions": versions
    }
