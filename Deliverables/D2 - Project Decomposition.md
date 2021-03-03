**Name: Will Pratt** 

* Objective
  * Journey to defeat the Big Bad
* Non-combat menu
    * Start menu
      * start game
        * Option to start and play the main game 
      * tutorial
        * Will teach player about game and their options
* Combat menu
    * Attack
      * Random number within a certain range
    * Defend
      * Damage reduction percentage based on class
    * Skills 
      * Cooldowns, option to explain skill
    * Item(s)
      * Non-skill that benefits player e.g. healing
* Turn-based
  * Checks speed to see who goes first in turn order
  * Player goes
    * They get one action to do:
      * Attack
      * Defend
      * Skill
      * Item
  * Enemy goes
    * They get one action to do:
      * Attack
      * Defend
      * Skill
  * Checks health for enemy
    * If 0 then combat ends
    * If not checks player health
  * Checks health for player
    * If 0 then combat ends and player loses
    * If not then combat continues
  * Loops
* Stats
  * They will impact players health, skills, and damage 
    * Each class will have starting stats that can be improved with points at 
      the beginning and weapon in use
  * Strength
    * Will affect damage for Warrior class
  * Dexterity
    * Will determine who's first
    * Will affect damage for Rougue class if implemented
  * Intelliegence
    * Will affect magic defense
    * Will affect damage for Mage class if implemented 
  * Constitution
    * Will affect all classes with health
* Theme for Areas
  * E.g. one area could be humans, another area could be animals, and so on and so forth
    * This will influence their stats, weapons, armor, and other things related to character
* Enemies
  * Will be similar to player but more limited in options
    * Will have attack, defend, skill(s), probably not items?
* Layout
  * Create structure for enemies, empty rooms, events
  * Events
* Traversal
  * Give player options to move in a certain direction
    * Left, Right, Forward, Back
  * Keep track of position
  *  Find appropiate spots to restrict player movement and when to implement them
     *  When moving to a different zone
     *  After doing an event  
* Class(es)
  * Will determine skills and starting stats
* Skills
  * Make available all from begining or unlocking after progression?
  * Abilities that can affect enemy or player
    * Damage
    * Heal
      * Possible additions
        *  Buffs
        *  Debuffs
* Equipment
  * Weapons
    * Increase and/or decrease stats
  * Armor
    * Damage reduction flat
  * Way to view? 
* Items
  * Healing 
  * Possible additions
    *  Buffs


