class warrior:
    """
    warrior class for player
    :return: none
    """
    def __init__(self):

        self.stats = [7, 5, 5, 7]
        self.warrior_head = 0
        self.warrior_chest = 1
        self.warrior_hands = 1
        self.warrior_legs = 1
        self.warrior_armor = self.warrior_head + self.warrior_chest + self.warrior_hands + self.warrior_legs
        self.warrior_max_hp = self.stats[3] * 4
        self.warrior_hp = self.warrior_max_hp
        self.player_menu = '''
        [1]Attack
        [2]Defend
        [3]Skills
        [4]Items
        '''
        self.player_skills = '''
        [1]Big Swing
        [2]Double Swing
        '''
        self.big_cdt = 4
        self.big_cd = 0
        self.double_cdt = 3
        self.double_cd = 0

        self.player_items = []

    def new_max_hp(self):
        self.max_hp = self.stats[3] * 4


class bad_warrior:
    """
    warrior class for player
    :return: none
    """
    def __init__(self):
        self.name = "Bad Warrior"
        self.stats = [5, 5, 5, 7]
        self.bad_warrior_armor = 2
        self.bad_warrior_max_hp = self.stats[3] * 4
        self.bad_warrior_hp = self.bad_warrior_max_hp
        self.bad_warrior_menu = ["attack", "defend", "skills"]
        self.bad_warrior_skills = ["big swing", "double swing"]


class wolf:
    """
    warrior class for player
    :return: none
    """
    def __init__(self):
        self.name = "Wolf"
        self.stats = [3, 6, 3, 5]
        self.wolf_armor = 1
        self.wolf_max_hp = self.stats[3] * 4
        self.wolf_hp = self.wolf_max_hp
        self.wolf_menu = ["attack", "defend", "skills"]
        self.wolf_skills = ["maul", "rend"]
