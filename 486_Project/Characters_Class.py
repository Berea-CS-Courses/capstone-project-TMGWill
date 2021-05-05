class Warrior:
    """
    warrior class for player
    """
    def __init__(self):
        # [strength, dexterity, intelligence, constitution]
        self.base_stats = [7, 5, 5, 7]

        # weapon
        self.weapon = [1, 0, 0, 1, "Ole Trusty Sword"]

        # total stats geekforgeeks.com
        self.stats = [self.base_stats[i] + self.weapon[i] for i in range(len(self.base_stats))]

        # will be used to determine total armor
        self.warrior_head = 0
        self.warrior_chest = 1
        self.warrior_hands = 1
        self.warrior_legs = 1

        # total armor
        self.warrior_armor = self.warrior_head + self.warrior_chest + self.warrior_hands + self.warrior_legs

        # health points
        self.warrior_max_hp = self.stats[3] * 4
        self.warrior_hp = self.warrior_max_hp

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

        # player skill cooldowns
        self.big_cdt = 4
        self.big_cd = 0
        self.double_cdt = 3
        self.double_cd = 0

        # will contain players items
        self.player_items = ["Small Health Potion"]

    # idea is to be used when player changes their constitution stat value
    def new_max_hp(self):
        self.warrior_max_hp = self.stats[3] * 4

    # function for when player gets new weapon
    def new_weapon(self):
        pass


class Bad_warrior:
    """
    class for enemy
    """
    def __init__(self):
        # the name for the enemy character
        self.name = "Bad Warrior"

        # [strength, dexterity, intelligence, constitution]
        self.stats = [5, 5, 5, 7]

        # armor for this enemy
        self.bad_warrior_armor = 2

        # health points
        self.bad_warrior_max_hp = self.stats[3] * 4
        self.bad_warrior_hp = self.bad_warrior_max_hp

        # enemy menu for choices during combat
        self.bad_warrior_menu = ["attack", "defend", "skills"]

        # enemy skills to use during combat
        self.bad_warrior_skills = ["big swing", "double swing"]

        # enemy skill cooldowns
        self.enemy_big_cdt = 4
        self.enemy_big_cd = 0
        self.enemy_double_cdt = 3
        self.enemy_double_cd = 0


class Wolf:
    """
    class for enemy
    """
    def __init__(self):
        # the name for the enemy character
        self.name = "Wolf"

        # [strength, dexterity, intelligence, constitution]
        self.stats = [3, 6, 3, 5]

        # armor for this enemy
        self.wolf_armor = 1

        # health points
        self.wolf_max_hp = self.stats[3] * 4
        self.wolf_hp = self.wolf_max_hp

        # enemy menu for choices during combat
        self.wolf_menu = ["attack", "defend", "skills"]

        # enemy skills to use during combat
        self.wolf_skills = ["maul", "rend"]

        # enemy skill cooldowns
        self.enemy_maul_cdt = 5
        self.enemy_maul_cd = 0
        self.enemy_rend_cdt = 3
        self.enemy_rend_cd = 0
