**Will Pratt**
# Alpha Testing
## Rooms
* Prevent Early Event Access
  * Out of the three room types that I have within my game which are empty, combat and event, the event room type is the most complicated. One bug that I had earlier on in my        project when first trying to implement how I would have the event rooms function was that the player could activate them earlier than when it should be possible. Event rooms      function through the use of listeners waiting for specific strings, and if the word for that listener was typed in then they could activate them sooner than they should.          However, the player would need to have prior knowledge of what the words are for the listeners before having the ability to activate them. In order to correct I made my program    check if the player is in the right room and if the room is an event room.
* Event Room Repeat
  * Earlier on in the project the player would have been able to cause an event room to repeat over and over again if they remembered the word that would call the listener for the     event. This caused me to implement another check for the room. Not only did I make sure that the player was in the right room I needed to make sure that the room was set to be
    in an "event" state. After the event had been called the state of the current room the player is in would then become "empty" so that even if they might remember the word(s)       for the event it would not be called again.
## Combat
* word
## Travel
* word
# Ad Hoc Testing
* word
