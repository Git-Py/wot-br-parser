import struct
from dictpackers import *


class FLAG_ACTION:
    PICKED_UP_FROM_BASE = 0
    PICKED_UP_FROM_GROUND = 1
    CAPTURED = 2
    RANGE = (PICKED_UP_FROM_BASE, PICKED_UP_FROM_GROUND, CAPTURED)


VEHICLE_DEVICE_TYPE_NAMES = ('engine',
                             'ammoBay',
                             'fuelTank',
                             'radio',
                             'track',
                             'gun',
                             'turretRotator',
                             'surveyingDevice')
VEHICLE_TANKMAN_TYPE_NAMES = ('commander',
                              'driver',
                              'radioman',
                              'gunner',
                              'loader')

VEH_INTERACTION_DETAILS = (('spotted', 'B', int, 0),
                           ('deathReason', 'b', int, -1),
                           ('directHits', 'H', int, 0),
                           ('explosionHits', 'H', int, 0),
                           ('piercings', 'H', int, 0),
                           ('damageDealt', 'H', int, 0),
                           ('damageAssistedTrack', 'H', int, 0),
                           ('damageAssistedRadio', 'H', int, 0),
                           ('crits', 'I', int, 0),
                           ('fire', 'H', int, 0),
                           ('damageBlockedByArmor', 'I', int, 0),
                           ('damageReceived', 'H', int, 0),
                           ('rickochetsReceived', 'H', int, 0),
                           ('noDamageDirectHitsReceived', 'H', int, 0),
                           ('targetKills', 'B', int, 0))

# VEH_INTERACTION_DETAILS = (('spotted', 'B', 1, 0),
#                            ('deathReason', 'b', 10, -1),
#                            ('directHits', 'H', 65535, 0),
#                            ('explosionHits', 'H', 65535, 0),
#                            ('piercings', 'H', 65535, 0),
#                            ('damageDealt', 'H', 65535, 0),
#                            ('damageAssistedTrack', 'H', 65535, 0),
#                            ('damageAssistedRadio', 'H', 65535, 0),
#                            ('crits', 'I', 4294967295L, 0),
#                            ('fire', 'H', 65535, 0),
#                            ('damageBlockedByArmor', 'I', 4294967295L, 0),
#                            ('damageReceived', 'H', 65535, 0),
#                            ('rickochetsReceived', 'H', 65535, 0),
#                            ('noDamageDirectHitsReceived', 'H', 65535, 0),
#                            ('targetKills', 'B', 255, 0))

_VEH_CELL_RESULTS_PUBLIC = Meta(('health', int, 0, None),
                                ('credits',int, 0, None),
                                ('xp', int, 0, None),
                                ('achievementCredits', int, 0, None),
                                ('achievementXP', int, 0, None),
                                ('achievementFreeXP', int, 0, None),
                                ('shots', int, 0, None),
                                ('directHits', int, 0, None),
                                ('directTeamHits', int, 0, None),
                                ('explosionHits', int, 0, None),
                                ('piercings', int, 0, None),
                                ('damageDealt', int, 0, None),
                                ('sniperDamageDealt', int, 0, None),
                                ('damageAssistedRadio', int, 0, None),
                                ('damageAssistedTrack', int, 0, None),
                                ('damageReceived', int, 0, None),
                                ('damageBlockedByArmor', int, 0, None),
                                ('directHitsReceived', int, 0, None),
                                ('noDamageDirectHitsReceived', int, 0, None),
                                ('explosionHitsReceived', int, 0, None),
                                ('piercingsReceived', int, 0, None),
                                ('tdamageDealt', int, 0, None),
                                ('tdestroyedModules', int, 0, None),
                                ('tkills', int, 0, None),
                                ('isTeamKiller', bool, False, None),
                                ('capturePoints', int, 0, None),
                                ('capturingBase', None, None, None),
                                ('droppedCapturePoints', int, 0, None),
                                ('mileage', int, 0, None),
                                ('lifeTime', int, 0, None),
                                ('killerID', int, 0, None),
                                ('achievements', list, [], None),
                                ('potentialDamageReceived', int, 0, None),
                                ('rolloutsCount', int, 0, None),
                                ('deathCount', int, 0, None),
                                ('flagActions', tuple, (0,) * len(FLAG_ACTION.RANGE), None),
                                ('winPoints', int, 0, None),
                                ('resourceAbsorbed', int, 0, None),
                                ('stopRespawn', bool, False, None)
                               )

_VEH_CELL_RESULTS_PRIVATE = Meta(('repair', int, 0, None),
                                 ('freeXP', int, 0, None),
                                 ('details', None, '', None)
                                )

_VEH_CELL_RESULTS_SERVER = Meta(('potentialDamageDealt', int, 0, None),
                                ('soloHitsAssisted', int, 0, None),
                                ('isEnemyBaseCaptured', bool, False, None),
                                ('stucks', list, [], DeltaPacker(roundToInt)),
                                ('autoAimedShots', int, 0, None),
                                ('presenceTime', int, 0, None),
                                ('spotList', list, [], None),
                                ('ammo', list, [], None),
                                ('crewActivityFlags', list, [], None),
                                ('series', dict, {}, None),
                                ('tkillRating', float, 0.0, None),
                                ('tkillLog', dict, {}, None),
                                ('destroyedObjects', dict, {}, None),
                                ('discloseShots', list, [], DeltaPacker()),
                                ('guerrillaShots', list, [], DeltaPacker()),
                                ('critsCount', int, 0, None),
                                ('aimerSeries', int, 0, None),
                                ('critsByType', dict, {},
                                 DictPacker(('destroyed', dict, {},
                                 SimpleDictPacker(int, VEHICLE_DEVICE_TYPE_NAMES)),
                                ('critical', dict, {},
                                 SimpleDictPacker( int, VEHICLE_DEVICE_TYPE_NAMES)),
                                ('tankman', dict, {},
                                 SimpleDictPacker(int, VEHICLE_TANKMAN_TYPE_NAMES)))),
                                ('innerModuleCritCount', int, 0, None),
                                ('innerModuleDestrCount', int, 0, None),
                                ('isAnyOurCrittedInnerModules', int, 0, None),
                                ('killsAssistedTrack', int, 0, None),
                                ('killsAssistedRadio', int, 0, None),
                                ('damagedVehicleCntAssistedTrack', int, 0, None),
                                ('damagedVehicleCntAssistedRadio', int, 0, None),
                                ('isNotSpotted', bool, True, None),
                                ('isAnyHitReceivedWhileCapturing', bool, False, None),
                                ('damageAssistedRadioWhileInvisible', int, 0, None),
                                ('damageAssistedTrackWhileInvisible', int, 0, None),
                                ('damageEventList', dict, {}, None),
                                ('multiDamageEvents', dict, {}, None),
                                ('inBattleMaxSniperSeries', int, 0, None),
                                ('inBattleMaxKillingSeries', int, 0, None),
                                ('inBattleMaxPiercingSeries', int, 0, None),
                                ('firstDamageTime', int, 0, None),
                                ('consumedAmmo', None, None, None)
                               )

_VEH_BASE_RESULTS_PUBLIC = Meta(('accountDBID', int, 0, None),
                                ('typeCompDescr', int, 0, None),
                                ('deathReason', int, -1, None),
                                ('fortBuilding', None, None, None),
                                ('fortResource', int, 0, None),
                                ('influencePoints', None, None, None),
                                ('team', int, 1, None),
                                ('kills', int, 0, None),
                                ('spotted', int, 0, None),
                                ('damaged', int, 0, None)
                               )

_VEH_BASE_RESULTS_PRIVATE = Meta(('xpPenalty', int, 0, None),
                                 ('creditsPenalty', int, 0, None),
                                 ('creditsContributionIn', int, 0, None),
                                 ('creditsContributionOut', int, 0, None),
                                 ('creditsToDraw', int, 0, None),
                                 ('club', None, None, None),
                                 ('enemyClub', None, None, None),
                                 ('damageBeforeTeamWasDamaged', int, 0, None),
                                 ('killsBeforeTeamWasDamaged', int, 0, None),
                                 ('percentFromTotalTeamDamage', float, 0.0, None),
                                 ('percentFromSecondBestDamage', float, 0.0, None),
                                 ('killedAndDamagedByAllSquadmates', int, 0, None),
                                 ('damagedWhileMoving', int, 0, None),
                                 ('damagedWhileEnemyMoving', int, 0, None),
                                 ('committedSuicide', bool, False, None)
                                )

_VEH_BASE_RESULTS_SERVER = Meta(('spottedBeforeWeBecameSpotted', int, 0, None),
                                ('spottedAndDamagedSPG', int, 0, None),
                                ('damageList', list, [], None),
                                ('killList', list, [], None),
                                ('vehLockTimeFactor', float, 0.0, None),
                                ('misc', dict, {}, None),
                                ('cybersportRatingDeltas', tuple, (0.0, 0.0), None),
                                ('clanDBID', int, 0, None),
                                ('vehsByClass', list, [], None)
                               )

_AVATAR_CELL_RESULTS_PRIVATE = Meta(('ammo', list, [], None),
                                    ('damageEventList', set, set(), None)
                                   )

_AVATAR_CELL_RESULTS_PUBLIC = Meta(('damageDealt', int, 0, None),
                                   ('kills', int, 0, None)
                                  )

_AVATAR_BASE_PRIVATE_RESULTS = Meta(('isPrematureLeave', bool, False, None),
                                    ('fairplayViolations', tuple, (0, 0, 0), None)
                                   )

_AVATAR_BASE_PUBLIC_RESULTS = Meta(('damaged', int, 0, None),
                                   ('totalDamaged', int, 0,None)
                                  )

VEH_FULL_RESULTS_UPDATE = Meta(('originalCredits', int, 0, None),
                               ('creditsReplay', str, '', ValueReplayPacker()),
                               ('originalXP', int, 0, None),
                               ('xpReplay', str, '', ValueReplayPacker()),
                               ('originalFreeXP', int, 0, None),
                               ('freeXPReplay', str,  '', ValueReplayPacker()),
                               ('originalTMenXP', int, 0, None),
                               ('tmenXPReplay', str, '', ValueReplayPacker()),
                               ('tmenXP', int, 0, None),
                               ('originalGold', int, 0, None),
                               ('goldReplay', str, '', ValueReplayPacker()),
                               ('gold', int, 0, None),
                               ('originalFortResource', int, 0, None),
                               ('fortResourceReplay', str, '', ValueReplayPacker()),
                               ('factualXP', int, 0, None),
                               ('factualFreeXP', int, 0, None),
                               ('factualCredits', int, 0, None),
                               ('subtotalCredits', int, 0, None),
                               ('subtotalXP', int, 0, None),
                               ('subtotalFreeXP', int, 0, None),
                               ('subtotalTMenXP', int, 0, None),
                               ('subtotalGold', int, 0, None),
                               ('subtotalFortResource', int, 0, None),
                               ('eventCreditsList', list, [], None),
                               ('eventXPList', list, [], None),
                               ('eventFreeXPList', list, [], None),
                               ('eventTMenXPList', list, [], None),
                               ('eventGoldList', list, [], None),
                               ('eventFortResourceList', list, [], None),
                               ('eventCreditsFactor10List', list, [], None),
                               ('eventXPFactor10List', list, [], None),
                               ('eventFreeXPFactor10List', list, [], None),
                               ('eventTMenXPFactor10List', list, [], None),
                               ('eventGoldFactor10List', list, [], None),
                               ('eventFortResourceFactor10List', list, [], None),
                               ('eventCredits', int, 0, None),
                               ('eventXP', int, 0, None),
                               ('eventFreeXP', int, 0, None),
                               ('eventTMenXP', int, 0, None),
                               ('eventGold', int, 0, None),
                               ('eventFortResource', int, 0, None),
                               ('originalXPPenalty', int, 0, None),
                               ('originalCreditsPenalty', int, 0, None),
                               ('originalCreditsContributionIn', int, 0, None),
                               ('originalCreditsContributionOut', int, 0, None),
                               ('premiumVehicleXP', int, 0, None),
                               ('premiumVehicleXPFactor10', int, 0, None),
                               ('premiumXPFactor10', int, 0, None),
                               ('appliedPremiumXPFactor10', int, 0, None),
                               ('premiumCreditsFactor10', int, 0, None),
                               ('appliedPremiumCreditsFactor10', int, 0, None),
                               ('dailyXPFactor10', int, 0, None),
                               ('igrXPFactor10', int, 0, None),
                               ('aogasFactor10', int, 0, None),
                               ('refSystemXPFactor10', int, 0, None),
                               ('fairplayFactor10', int, 0, None),
                               ('orderCredits', int, 0, None),
                               ('orderXP', int, 0, None),
                               ('orderFreeXP', int, 0, None),
                               ('orderTMenXP', int, 0, None),
                               ('orderFortResource', int, 0, None),
                               ('boosterCredits', int, 0, None),
                               ('boosterXP', int, 0, None),
                               ('boosterFreeXP', int, 0, None),
                               ('boosterTMenXP', int, 0, None),
                               ('boosterCreditsFactor100', int, 0, None),
                               ('boosterXPFactor100', int, 0, None),
                               ('boosterFreeXPFactor100', int, 0, None),
                               ('boosterTMenXPFactor100', int, 0, None),
                               ('isPremium', bool, False,None),
                               ('xpByTmen', list, [], None),
                               ('autoRepairCost', int, 0, None),
                               ('autoLoadCost', tuple, (0, 0), None),
                               ('autoEquipCost', tuple, (0, 0), None),
                               ('histAmmoCost', tuple, (0, 0), None),
                               ('prevMarkOfMastery', int, 0, None),
                               ('markOfMastery', int, 0, None),
                               ('dossierPopUps', list, [], None),
                               ('vehTypeLockTime', int, 0, None),
                               ('serviceProviderID', int, 0, None),
                               ('marksOnGun', int, 0, None),
                               ('movingAvgDamage', int, 0, None),
                               ('damageRating', int, 0, None),
                               ('battleNum', int, 0, None)
                              )

_VEH_FULL_RESULTS_PRIVATE = Meta(('questsProgress', dict, {},None))

VEH_FULL_RESULTS_SERVER = Meta(('eventGoldByEventID', dict, {}, None))

PLAYER_INFO = Meta(('name', str, '', None),
                   ('clanDBID', int, 0, None),
                   ('clanAbbrev', str, '', None),
                   ('prebattleID', int, 0, None),
                   ('team', int, 1, None),
                   ('igrType', int, 0, None)
                  )

COMMON_RESULTS = Meta(('arenaTypeID', int, 0, None),
                      ('arenaCreateTime', int, 0, None),
                      ('winnerTeam', int, 0, None),
                      ('finishReason', int, 0, None),
                      ('duration', int, 0, None),
                      ('bonusType', int, 0, None),
                      ('guiType', int, 0, None),
                      ('vehLockMode', int, 0, None),
                      ('division', None, None, None)
                     )

VEH_INTERACTIVE_STATS = ('xp',
                         'damageDealt',
                         'capturePts',
                         'flagActions',
                         'winPoints',
                         'deathCount',
                         'resourceAbsorbed',
                         'stopRespawn',
                         'equipmentDamage',
                         'equipmentKills'
                        )

AVATAR_PUBLIC_RESULTS = _AVATAR_CELL_RESULTS_PUBLIC +\
                        _AVATAR_BASE_PUBLIC_RESULTS

AVATAR_FULL_RESULTS = _AVATAR_CELL_RESULTS_PUBLIC +\
                      _AVATAR_CELL_RESULTS_PRIVATE +\
                      _AVATAR_BASE_PUBLIC_RESULTS +\
                      _AVATAR_BASE_PRIVATE_RESULTS

VEH_CELL_RESULTS = _VEH_CELL_RESULTS_PUBLIC +\
                   _VEH_CELL_RESULTS_PRIVATE +\
                   _VEH_CELL_RESULTS_SERVER

VEH_BASE_RESULTS = _VEH_CELL_RESULTS_PUBLIC +\
                   _VEH_BASE_RESULTS_PUBLIC +\
                   _VEH_CELL_RESULTS_PRIVATE +\
                   _VEH_BASE_RESULTS_PRIVATE +\
                   _VEH_CELL_RESULTS_SERVER +\
                   _VEH_BASE_RESULTS_SERVER

VEH_PUBLIC_RESULTS = _VEH_CELL_RESULTS_PUBLIC +\
                     _VEH_BASE_RESULTS_PUBLIC

VEH_FULL_RESULTS = _VEH_CELL_RESULTS_PUBLIC +\
                   _VEH_BASE_RESULTS_PUBLIC +\
                   _VEH_CELL_RESULTS_PRIVATE +\
                   _VEH_BASE_RESULTS_PRIVATE +\
                   VEH_FULL_RESULTS_UPDATE +\
                   _VEH_FULL_RESULTS_PRIVATE

AVATAR_PRIVATE_STATS = ('ragePoints',)
AVATAR_PRIVATE_STATS_INDICES = dict(((x[1], x[0]) for x in enumerate(AVATAR_PRIVATE_STATS)))
VEH_INTERACTIVE_STATS_INDICES = dict(((x[1], x[0]) for x in enumerate(VEH_INTERACTIVE_STATS)))
VEH_INTERACTION_DETAILS_NAMES = [x[0] for x in VEH_INTERACTION_DETAILS]
VEH_INTERACTION_DETAILS_MAX_VALUES = dict(((x[0], x[2]) for x in VEH_INTERACTION_DETAILS))
VEH_INTERACTION_DETAILS_INIT_VALUES = [x[3] for x in VEH_INTERACTION_DETAILS]
VEH_INTERACTION_DETAILS_LAYOUT = ''.join([x[1] for x in VEH_INTERACTION_DETAILS])
VEH_INTERACTION_DETAILS_INDICES = dict(((x[1][0], x[0]) for x in enumerate(VEH_INTERACTION_DETAILS)))


class UNIT_CLAN_MEMBERSHIP:
    NONE = 0
    ANY = 1
    SAME = 2

def dictToList(indices, d):
    l = [None] * len(indices)
    for name, index in indices.items():
        l[index] = d[name]
    return l

def listToDict(names, l):
    d = {}
    for x in enumerate(names):
        d[x[1]] = l[x[0]]
    return d


class _VehicleInteractionDetailsItem(object):
    def __init__(self, values, offset):
        self.__values = values
        self.__offset = offset

    def __getitem__(self, key):
        return self.__values[self.__offset + VEH_INTERACTION_DETAILS_INDICES[key]]

    def __setitem__(self, key, value):
        self.__values[self.__offset +\
                      VEH_INTERACTION_DETAILS_INDICES[key]] = \
                      min(int(value), VEH_INTERACTION_DETAILS_MAX_VALUES[key])

    def __str__(self):
        return str(dict(self))

    def __iter__(self):
        return zip(VEH_INTERACTION_DETAILS_NAMES, self.__values[self.__offset:])


class VehicleInteractionDetails(object):
    def __init__(self, uniqueVehIDs, values):
        self.__uniqueVehIDs = uniqueVehIDs
        self.__values = values
        size = len(VEH_INTERACTION_DETAILS)
        self.__offsets = dict(((x[1], x[0] * size) for x in enumerate(uniqueVehIDs)))

    @staticmethod
    def fromPacked(packed):
        count = len(packed) / struct.calcsize(''.join(['<2I', VEH_INTERACTION_DETAILS_LAYOUT]))
        packedVehIDsLayout = '<%dI' % (2 * count,)
        packedVehIDsLen = struct.calcsize(packedVehIDsLayout)
        flatIDs = struct.unpack(packedVehIDsLayout, packed[:packedVehIDsLen])
        uniqueVehIDs = []
        for i in xrange(0, len(flatIDs), 2):
            uniqueVehIDs.append((flatIDs[i], flatIDs[i + 1]))

        values = struct.unpack('<' + VEH_INTERACTION_DETAILS_LAYOUT * count, packed[packedVehIDsLen:])
        return VehicleInteractionDetails(uniqueVehIDs, values)

    def __getitem__(self, uniqueVehID):
        if not type(uniqueVehID) == tuple:
            raise AssertionError
            offset = self.__offsets.get(uniqueVehID, None)
            offset is None and self.__uniqueVehIDs.append(uniqueVehID)
            offset = len(self.__values)
            self.__values += VEH_INTERACTION_DETAILS_INIT_VALUES
            self.__offsets[uniqueVehID] = offset
        return _VehicleInteractionDetailsItem(self.__values, offset)

    def __contains__(self, uniqueVehID):
        raise type(uniqueVehID) == tuple or AssertionError
        return uniqueVehID in self.__offsets

    def __str__(self):
        return str(self.toDict())

    def pack(self):
        count = len(self.__uniqueVehIDs)
        flatIDs = []
        for uniqueID in self.__uniqueVehIDs:
            flatIDs.append(uniqueID[0])
            flatIDs.append(uniqueID[1])

        packed = struct.pack(('<%dI' % (2 * count)), *flatIDs) + struct.pack(
            ('<' + VEH_INTERACTION_DETAILS_LAYOUT * count), *self.__values)
        return packed

    def toDict(self):
        return dict([((vehID, vehTypeCompDescr), dict(_VehicleInteractionDetailsItem(self.__values, offset))) for
                     (vehID, vehTypeCompDescr), offset in self.__offsets.items()])
