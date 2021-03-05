**Name: Will Pratt** 

* Objective
  * Defeat the Big Bad
    * Journey that will have combat and various encounters or events that will end with a final boss
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
      * Cooldown time depending on skill used 
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
    * Will affect certain skills
  * Dexterity
    * Will determine who's first
    * Will affect damage for Rougue class if implemented
    * Will affect certain skills
  * Intelliegence
    * Will affect magic defense
    * Will affect damage for Mage class if implemented
    * Will affect certain skills 
  * Constitution
    * Will affect all classes with health
    * Will affect certain skills
* Traversal
  * Give player options to move in a certain direction
    * Left, Right, Forward, Back
  * Keep track of position
    * This will determine what options they have depending on where they are
  *  Find appropiate spots to restrict player movement and when to implement them
     *  When moving to a different area and not allowing player to go back
     *  After doing an event and not allowing player to go back
* Theme for Areas
  * E.g. one area could be humans, another area could be animals, and so on and so forth
    * This will influence how I determine their stats, weapons, armor, and other things related to character
* Enemies
  * Will be similar to player but more limited in options
    * Will have attack, defend, skill(s)
* Layout
  * The general idea is that one area will have various rooms 
  * Create structure and determine where to have rooms that will either have enemies, be empty, or events for the player to traverse
    * Enemies
      * A room that will involve combat
    * Empty
      * A room that will be empty and uneventful
    * Events
      * A room that could be combat, a treasure (something that will benefit the player), or maybe something that has no impact beyond entertainment purposes
* Class(es)
  * Will determine skills and starting stats
  * Warrior
    * First class to be implemented and guarenteed to be involved
  * Rogue
    * Possible class idea to be implemented
  * Mage
    * Possible class idea to be implemented
* Skills
  * Make available all from begining or unlocking after progression?
  * Provide way to allow player to get explaination of skill?
  * Abilities that can affect enemy or player
    * Damage
    * Heal
      * Possible additions
        * Buffs
          * Gives player an advantage 
        * Debuffs
          * Gives enemy a disadvantage
* Equipment
  * Weapons
    * Increase and/or decrease stats
  * Armor
    * Damage reduction flat
    * Affects stats?
  * Way to view?
    *  Provide way for player to view stats and info from equipment?
* Items
  * Healing 
  * Possible additions
    *  Buffs
* Narrative
  * Needed for story-telling
    * Will tell player about overall story at certain point(s)
    * Will tell player about areas at certain point(s)
    * Will be involved with certain events at certain point(s)
