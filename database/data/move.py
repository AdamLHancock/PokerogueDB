"""
import { ChargeAnim, MoveChargeAnim, initMoveAnim, loadMoveAnimAssets } from "./battle-anims";
import { BattleEndPhase, MovePhase, NewBattlePhase, PartyStatusCurePhase, PokemonHealPhase, StatChangePhase, SwitchSummonPhase } from "../phases";
import { BattleStat, getBattleStatName } from "./battle-stat";
import { EncoreTag, SemiInvulnerableTag } from "./battler-tags";
import { getPokemonMessage, getPokemonNameWithAffix } from "../messages";
import Pokemon, { AttackMoveResult, EnemyPokemon, HitResult, MoveResult, PlayerPokemon, PokemonMove, TurnMove } from "../field/pokemon";
import { StatusEffect, getStatusEffectHealText, isNonVolatileStatusEffect, getNonVolatileStatusEffects} from "./status-effect";
import { Type } from "./type";
import { Constructor } from "#app/utils";
import * as Utils from "../utils";
import { WeatherType } from "./weather";
import { ArenaTagSide, ArenaTrapTag } from "./arena-tag";
import { UnswappableAbilityAbAttr, UncopiableAbilityAbAttr, UnsuppressableAbilityAbAttr, BlockRecoilDamageAttr, BlockOneHitKOAbAttr, IgnoreContactAbAttr, MaxMultiHitAbAttr, applyAbAttrs, BlockNonDirectDamageAbAttr, applyPreSwitchOutAbAttrs, PreSwitchOutAbAttr, applyPostDefendAbAttrs, PostDefendContactApplyStatusEffectAbAttr, MoveAbilityBypassAbAttr, ReverseDrainAbAttr, FieldPreventExplosiveMovesAbAttr, ForceSwitchOutImmunityAbAttr, BlockItemTheftAbAttr, applyPostAttackAbAttrs, ConfusionOnStatusEffectAbAttr, HealFromBerryUseAbAttr, IgnoreProtectOnContactAbAttr, IgnoreMoveEffectsAbAttr, applyPreDefendAbAttrs, MoveEffectChanceMultiplierAbAttr } from "./ability";
import { allAbilities } from "./ability";
import { PokemonHeldItemModifier, BerryModifier, PreserveBerryModifier } from "../modifier/modifier";
import { BattlerIndex } from "../battle";
import { Stat } from "./pokemon-stat";
import { TerrainType } from "./terrain";
import { SpeciesFormChangeActiveTrigger } from "./pokemon-forms";
import { ModifierPoolType } from "#app/modifier/modifier-type";
import { Command } from "../ui/command-ui-handler";
import i18next from "i18next";
import { Localizable } from "#app/interfaces/locales";
import { getBerryEffectFunc } from "./berry";
import { Abilities } from "#enums/abilities";
import { ArenaTagType } from "#enums/arena-tag-type";
import { BattlerTagType } from "#enums/battler-tag-type";
import { Biome } from "#enums/biome";
import { Moves } from "#enums/moves";
import { Species } from "#enums/species";
"""

from enum import Enum

def get_move_enums() -> dict:
    move_category = ["PHYSICAL", "SPECIAL", "STATUS"]
    move_target = [
        "USER",
        "OTHER",
        "ALL_OTHERS",
        "NEAR_OTHER",
        "ALL_NEAR_OTHERS",
        "NEAR_ENEMY",
        "ALL_NEAR_ENEMIES",
        "RANDOM_NEAR_ENEMY",
        "ALL_ENEMIES",
        "ATTACKER",
        "NEAR_ALLY",
        "ALLY",
        "USER_OR_NEAR_ALLY",
        "USER_AND_ALLIES",
        "ALL",
        "USER_SIDE",
        "ENEMY_SIDE",
        "BOTH_SIDES",
        "PARTY",
        "CURSE"
        ]
    move_flags = {
        "NONE": 0,
        "MAKES_CONTACT": 1 << 0,
        "IGNORE_PROTECT": 1 << 1,
        "IGNORE_VIRTUAL": 1 << 2,
        "SOUND_BASED": 1 << 3,
        "HIDE_USER": 1 << 4,
        "HIDE_TARGET": 1 << 5,
        "BITING_MOVE": 1 << 6,
        "PULSE_MOVE": 1 << 7,
        "PUNCHING_MOVE": 1 << 8,
        "SLICING_MOVE": 1 << 9,
        "RECKLESS_MOVE": 1 << 10,
        "BALLBOMB_MOVE": 1 << 11,
        "POWDER_MOVE": 1 << 12,
        "DANCE_MOVE": 1 << 13,
        "WIND_MOVE": 1 << 14,
        "TRIAGE_MOVE": 1 << 15,
        "IGNORE_ABILITIES": 1 << 16,
        "CHECK_ALL_HITS": 1 << 17
    }
    move_effect_trigger = ["PRE_APPLY", "POST_APPLY", "HIT", "POST_TARGET"]
    multi_hit_type = ["_2", "_2_TO_5", "_3", "_10", "BEAT_UP"]

    return {
        "move_category": move_category,
        "move_target": move_target,
        "MoveFlags": move_flags,
        "move_effect_trigger": move_effect_trigger,
        "multi_hit_type": multi_hit_type
    }

class MoveCategory(Enum):
    PHYSICAL = 0
    SPECIAL = 1
    STATUS = 2

class MoveTarget(Enum):
    USER = 0
    OTHER = 1
    ALL_OTHERS = 2
    NEAR_OTHER = 3
    ALL_NEAR_OTHERS = 4
    NEAR_ENEMY = 5
    ALL_NEAR_ENEMIES = 6
    RANDOM_NEAR_ENEMY = 7
    ALL_ENEMIES = 8
    ATTACKER = 9
    NEAR_ALLY = 10
    ALLY = 11
    USER_OR_NEAR_ALLY = 12
    USER_AND_ALLIES = 13
    ALL = 14
    USER_SIDE = 15
    ENEMY_SIDE = 16
    BOTH_SIDES = 17
    PARTY = 18
    CURSE = 19

class MoveFlags(Enum):
    NONE = 0
    MAKES_CONTACT = 1 << 0
    IGNORE_PROTECT = 1 << 1
    IGNORE_VIRTUAL = 1 << 2
    SOUND_BASED = 1 << 3
    HIDE_USER = 1 << 4
    HIDE_TARGET = 1 << 5
    BITING_MOVE = 1 << 6
    PULSE_MOVE = 1 << 7
    PUNCHING_MOVE = 1 << 8
    SLICING_MOVE = 1 << 9
    RECKLESS_MOVE = 1 << 10
    BALLBOMB_MOVE = 1 << 11
    POWDER_MOVE = 1 << 12
    DANCE_MOVE = 1 << 13
    WIND_MOVE = 1 << 14
    TRIAGE_MOVE = 1 << 15
    IGNORE_ABILITIES = 1 << 16
    CHECK_ALL_HITS = 1 << 17

class MoveEffectTrigger(Enum):
    PRE_APPLY = 0
    POST_APPLY = 1
    HIT = 2
    POST_TARGET = 3

class MultiHitType(Enum):
    _2 = 0
    _2_TO_5 = 1
    _3 = 2
    _10 = 3
    BEAT_UP = 4

