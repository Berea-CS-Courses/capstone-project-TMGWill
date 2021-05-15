**Will Pratt**
# Alpha Testing
## Travel
* Invalid Direction/Typo Crash
  * For my project I made use of parts of the adventurelib library for my game. I mainly used the Room class and the start() function that uses a while loop to run functions from     its library. In the earlier stages of my project I was used the Room class and my own while loop to try and run the game. When I did this, if the player entered a word that       wasnn't north, south, east, or west or made some kind of typo then it would crash. After implementing the start() function that is apart of the adventurelib library the crash     issue that came from not inputing a valid direction or a typo would no longer occur since there are checks already in place if something like that were to happen.
* Invalid Direction Bug
  * After implementing the start() function from adventurelib a different bug occurred when traveling between rooms. If the player would enter a direction that was not one of the     given exits then the game would still run but they would be given a blank response which was awkward to occur while playing. The player would still be able to travel between       rooms with no issue as long as that direction is one of the given exits. To counteract that possible situation from arising I put in a check that if the direction given is not     one of the available exits then the player would be given the response "You can't go that way." and have the current room the player is in print back to the screen so that the     flow doesn't seem broken or awkward and have the room description and exits readily present.
## Rooms
* Prevent Early Event Access
  * Out of the three room types that I have within my game which are empty, combat and event, the event room type is the most complicated. One bug that I had earlier on in my        project when first trying to implement how I would have the event rooms function was that the player could activate them earlier than when it should be possible. Event rooms      function through the use of listeners waiting for specific strings, and if the word for that listener was typed in then they could activate them sooner than they should.          However, the player would need to have prior knowledge of what the words are for the listeners before having the ability to activate them. In order to correct I made my program    check if the player is in the right room and if the room is an event room.
* Event Room Repeat
  * Earlier on in the project the player would have been able to cause an event room to repeat over and over again if they remembered the word that would call the listener for the     event. This caused me to implement another check for the room. Not only did I make sure that the player was in the right room I needed to make sure that the room was set to be
    in an "event" state. After the event had been called the state of the current room the player is in would then become "empty" so that even if they might remember the word(s)       for the event it would not be called again.
## Combat
* word
# Ad Hoc Testing
* word
