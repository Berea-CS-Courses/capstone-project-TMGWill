#dndbeyond

class Warrior:
    """
    warrior class for player
    """
    def __init__(self):
        # [strength, dexterity, intelligence, constitution]
        self.base_stats = [6, 4, 4, 6]

        # weapon
        self.weapon = [1, 0, 0, 1, "Ole Trusty Sword"]

        # total stats geekforgeeks.com
        self.stats = [self.base_stats[i] + self.weapon[i] for i in range(len(self.base_stats))]

        # will be used to determine total armor
        self.head = 0
        self.chest = 1
        self.hands = 1
        self.legs = 1

        # total armor
        self.armor = self.head + self.chest + self.hands + self.legs

        # health points
        self.max_hp = self.stats[3] * 4
        self.hp = self.max_hp

        # will be used to display player menu
        self.player_menu = '''
        [1]Attack
        [2]Defend
        [3]Skills
        [4]Items
        '''

        # will be used to display player skills
        self.player_skills = '''
        [1]Big Swing
        [2]Double Swing
        '''
        # counter

        # player skill cooldowns
        self.big_cdt = 4
        self.big_cd = 0
        self.double_cdt = 3
        self.double_cd = 0

        # will contain players items
        self.player_items = ["Small Health Potion"]

    # idea is to be used when player changes their constitution stat value
    def new_max_hp(self):
        self.max_hp = self.stats[3] * 4

    # function for when player gets new weapon
    def new_weapon(self):
        pass


class Corrupted_swordsman:
    """
    class for enemy
    """
    def __init__(self):
        # the name for the enemy character
        self.name = "Corrupted Swordsman"

        # [strength, dexterity, intelligence, constitution]
        self.stats = [7, 6, 5, 7]

        # armor for this enemy
        self.enemy_armor = 2

        # health points
        self.enemy_max_hp = self.stats[3] * 4
        self.enemy_hp = self.enemy_max_hp

        # enemy menu for choices during combat
        self.enemy_menu = ["attack", "defend", "skills"]

        # enemy skills to use during combat
        self.enemy_skills = ["big swing", "double swing"]

        # enemy skill cooldowns
        self.enemy_big_cdt = 4
        self.enemy_big_cd = 0
        self.enemy_double_cdt = 3
        self.enemy_double_cd = 0


class Corrupted_knight:
    """
    class for enemy
    """
    def __init__(self):
        # the name for the enemy character
        self.name = "Corrupted Knight"

        # [strength, dexterity, intelligence, constitution]
        self.stats = [8, 4, 5, 8]

        # armor for this enemy
        self.enemy_armor = 2

        # health points
        self.enemy_max_hp = self.stats[3] * 4
        self.enemy_hp = self.enemy_max_hp

        # enemy menu for choices during combat
        self.enemy_menu = ["attack", "defend", "skills"]

        # enemy skills to use during combat
        self.enemy_skills = ["pommel strike", "lunge"]

        # enemy skill cooldowns
        # str + dex?
        self.enemy_lunge_cdt = 4
        self.enemy_lunge_cd = 0
        # str? feint, blah...?
        self.enemy_pommel_cdt = 3
        self.enemy_pommel_cd = 0


class Corrupted_acolyte:
    """
    class for enemy
    """
    def __init__(self):
        # the name for the enemy character
        self.name = "Corrupted Acolyte"

        # [strength, dexterity, intelligence, constitution]
        self.stats = [4, 7, 8, 6]

        # armor for this enemy
        self.enemy_armor = 2

        # health points
        self.enemy_max_hp = self.stats[3] * 4
        self.enemy_hp = self.enemy_max_hp

        # enemy menu for choices during combat
        self.enemy_menu = ["attack", "defend", "skills"]

        # enemy skills to use during combat
        self.enemy_skills = ["fire bolt", "chaos bolt"]

        # enemy skill cooldowns
        self.enemy_fireb_cdt = 3
        self.enemy_fireb_cd = 0
        self.enemy_chaosb_cdt = 3
        self.enemy_chaosb_cd = 0


class Wolf:
    """
    class for enemy
    """
    def __init__(self):
        # the name for the enemy character
        self.name = "Wolf"

        # [strength, dexterity, intelligence, constitution]
        self.stats = [4, 6, 4, 5]

        # armor for this enemy
        self.enemy_armor = 1

        # health points
        self.enemy_max_hp = self.stats[3] * 4
        self.enemy_hp = self.enemy_max_hp

        # enemy menu for choices during combat
        self.enemy_menu = ["attack", "defend", "skills"]

        # enemy skills to use during combat
        self.enemy_skills = ["maul", "rend"]

        # enemy skill cooldowns
        # str?
        self.enemy_maul_cdt = 2
        self.enemy_maul_cd = 0
        # dex?
        self.enemy_rend_cdt = 3
        self.enemy_rend_cd = 0


class Giant_lizard:
    """
    class for enemy
    """
    def __init__(self):
        # the name for the enemy character
        self.name = "Giant Lizard"

        # [strength, dexterity, intelligence, constitution]
        self.stats = [4, 5, 4, 7]

        # armor for this enemy
        self.enemy_armor = 2

        # health points
        self.enemy_max_hp = self.stats[3] * 4
        self.enemy_hp = self.enemy_max_hp

        # enemy menu for choices during combat
        self.enemy_menu = ["attack", "defend", "skills"]

        # enemy skills to use during combat
        self.enemy_skills = ["tail whip", "ram"]

        # enemy skill cooldowns
        # dex?
        self.enemy_tail_cdt = 3
        self.enemy_tail_cd = 0
        # str
        self.enemy_ram_cdt = 3
        self.enemy_ram_cd = 0


class Giant_eagle:
    """
    class for enemy
    """
    def __init__(self):
        # the name for the enemy character
        self.name = "Giant Eagle"

        # [strength, dexterity, intelligence, constitution]
        self.stats = [5, 7, 4, 4]

        # armor for this enemy
        self.enemy_armor = 2

        # health points
        self.enemy_max_hp = self.stats[3] * 4
        self.enemy_hp = self.enemy_max_hp

        # enemy menu for choices during combat
        self.enemy_menu = ["attack", "defend", "skills"]

        # enemy skills to use during combat
        self.enemy_skills = ["dive bomb", "talons"]

        # enemy skill cooldowns
        # dex?
        self.enemy_dive_cdt = 4
        self.enemy_dive_cd = 0
        # str?
        self.enemy_talons_cdt = 3
        self.enemy_talons_cd = 0


class Ogre:
    """
    class for enemy
    """
    def __init__(self):
        # the name for the enemy character
        self.name = "Ogre"

        # [strength, dexterity, intelligence, constitution]
        self.stats = [10, 6, 5, 9]

        # armor for this enemy
        self.enemy_armor = 2

        # health points
        self.enemy_max_hp = self.stats[3] * 4
        self.enemy_hp = self.enemy_max_hp

        # enemy menu for choices during combat
        self.enemy_menu = ["attack", "defend", "skills"]

        # enemy skills to use during combat
        self.enemy_skills = ["smash", "bash"]

        # enemy skill cooldowns
        self.enemy_smash_cdt = 4
        self.enemy_smash_cd = 0
        self.enemy_bash_cdt = 3
        self.enemy_bash_cd = 0


class Bugbear:
    """
    class for enemy
    """
    def __init__(self):
        # the name for the enemy character
        self.name = "Bugbear"

        # [strength, dexterity, intelligence, constitution]
        self.stats = [10, 7, 5, 8]

        # armor for this enemy
        self.enemy_armor = 2

        # health points
        self.enemy_max_hp = self.stats[3] * 4
        self.enemy_hp = self.enemy_max_hp

        # enemy menu for choices during combat
        self.enemy_menu = ["attack", "defend", "skills"]

        # enemy skills to use during combat
        self.enemy_skills = ["club", "charge"]

        # enemy skill cooldowns
        self.enemy_club_cdt = 4
        self.enemy_club_cd = 0
        self.enemy_charge_cdt = 3
        self.enemy_charge_cd = 0


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Goblin:
    """
    class for enemy
    """
    def __init__(self):
        # the name for the enemy character
        self.name = "Goblin"

        # [strength, dexterity, intelligence, constitution]
        self.stats = [8, 11, 5, 6]

        # armor for this enemy
        self.enemy_armor = 2

        # health points
        self.enemy_max_hp = self.stats[3] * 4
        self.enemy_hp = self.enemy_max_hp

        # enemy menu for choices during combat
        self.enemy_menu = ["attack", "defend", "skills"]

        # enemy skills to use during combat
        self.enemy_skills = ["lil hit", "mace knee"]

        # enemy skill cooldowns
        self.enemy_lil_cdt = 4
        self.enemy_lil_cd = 0
        self.enemy_knee_cdt = 3
        self.enemy_knee_cd = 0


# class Death_dog:
#     """
#     class for enemy
#     """
#     def __init__(self):
#         # the name for the enemy character
#         self.name = "Death Dog"
#
#         # [strength, dexterity, intelligence, constitution]
#         self.stats = [7, 10, 5, 8]
#
#         # armor for this enemy
#         self.enemy_armor = 2
#
#         # health points
#         self.enemy_max_hp = self.stats[3] * 4
#         self.enemy_hp = self.enemy_max_hp
#
#         # enemy menu for choices during combat
#         self.enemy_menu = ["attack", "defend", "skills"]
#
#         # enemy skills to use during combat
#         self.enemy_skills = ["death maul", "death rend"]
#
#         # enemy skill cooldowns
#         self.enemy_dmaul_cdt = 4
#         self.enemy_dmaul_cd = 0
#         self.enemy_drend_cdt = 3
#         self.enemy_drend_cd = 0


class Dragon:
    """
    class for enemy
    """
    def __init__(self):
        # the name for the enemy character
        self.name = "Dragon"

        # [strength, dexterity, intelligence, constitution]
        self.stats = [9, 7, 9, 9]

        # armor for this enemy
        self.enemy_armor = 2

        # health points
        self.enemy_max_hp = self.stats[3] * 4
        self.enemy_hp = self.enemy_max_hp

        # enemy menu for choices during combat
        self.enemy_menu = ["attack", "defend", "skills"]

        # enemy skills to use during combat
        self.enemy_skills = ["claws", "tail whip", "breathe fire"]

        # enemy skill cooldowns
        self.enemy_claws_cdt = 4
        self.enemy_claws_cd = 0
        self.enemy_tail_cdt = 3
        self.enemy_tail_cd = 0
        self.enemy_breathe_cdt = 3
        self.enemy_breathe_cd = 0


