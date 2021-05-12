# from Characters_Class import *
class Story:

    def __init__(self):
        pass

    # def select_class(self):
    #     player_class = None
    #     choice = input("Choose your class.")
    #
    #     if choice == "warrior":
    #         player_class = Warrior()
    #
    #     # else:
    #     #     print("nope")
    #
    #     return player_class

    def intro(self):
        # There are countless stories within this world, each with their own kind of ending whether it be good, bad, or somewhere in-between.
        # Out of those there is a kind of story about a chosen one who was destined to save the world or right some kind of wrong.
        # This however, isn't one of those stories. This story is yours. You're a nobody who decides to become a somebody and
        # make a name for yourself. The path to becoming a brave hero where you begin your journey and become a part of a tale as old
        # as time of good versus evil. In order to save this land you must overcome many trials and tribulations to
        # have the chance to defeat the dragon that plagues us, corrupting the land and it's inhabitants.
        #
        print("""Brave hero, you are about to begin your journey and become a part of a tale as old as time of good versus evil. 
In order to save the land you must defeat the dragon that plagues us, corrupting the land and it's inhabitants.""")

    def epilogue(self):
        pass

    # idea was to use this for the Dragon_Intro room but might not be used
    def final_dialogue(self):
        pass

    def title(self):
        print("""
 $$$$$$\                                                                                                                             
$$  __$$\                                                                                                                            
$$ /  \__|$$\   $$\  $$$$$$\   $$$$$$\   $$$$$$\                                                                                     
\$$$$$$\  $$ |  $$ |$$  __$$\ $$  __$$\ $$  __$$\                                                                                    
 \____$$\ $$ |  $$ |$$ /  $$ |$$$$$$$$ |$$ |  \__|                                                                                   
$$\   $$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |                                                                                         
\$$$$$$  |\$$$$$$  |$$$$$$$  |\$$$$$$$\ $$ |                                                                                         
 \______/  \______/ $$  ____/  \_______|\__|                                                                                         
                    $$ |                                                                                                             
                    $$ |                                                                                                             
                    \__|                                                                                                             
 $$$$$$\                                                                                                                             
$$  __$$\                                                                                                                            
$$ /  $$ |$$\  $$\  $$\  $$$$$$\   $$$$$$$\  $$$$$$\  $$$$$$\$$$$\   $$$$$$\                                                         
$$$$$$$$ |$$ | $$ | $$ |$$  __$$\ $$  _____|$$  __$$\ $$  _$$  _$$\ $$  __$$\                                                        
$$  __$$ |$$ | $$ | $$ |$$$$$$$$ |\$$$$$$\  $$ /  $$ |$$ / $$ / $$ |$$$$$$$$ |                                                       
$$ |  $$ |$$ | $$ | $$ |$$   ____| \____$$\ $$ |  $$ |$$ | $$ | $$ |$$   ____|                                                       
$$ |  $$ |\$$$$$\$$$$  |\$$$$$$$\ $$$$$$$  |\$$$$$$  |$$ | $$ | $$ |\$$$$$$$\                                                        
\__|  \__| \_____\____/  \_______|\_______/  \______/ \__| \__| \__| \_______|                                                       
                                                                                                                                                                                                                                                                         
$$$$$$$$\                    $$\            $$$$$$\        $$\                                 $$\                                   
\__$$  __|                   $$ |          $$  __$$\       $$ |                                $$ |                                  
   $$ | $$$$$$\  $$\   $$\ $$$$$$\         $$ /  $$ | $$$$$$$ |$$\    $$\  $$$$$$\  $$$$$$$\ $$$$$$\   $$\   $$\  $$$$$$\   $$$$$$\  
   $$ |$$  __$$\ \$$\ $$  |\_$$  _|        $$$$$$$$ |$$  __$$ |\$$\  $$  |$$  __$$\ $$  __$$\ _$$  _|  $$ |  $$ |$$  __$$\ $$  __$$\ 
   $$ |$$$$$$$$ | \$$$$  /   $$ |          $$  __$$ |$$ /  $$ | \$$\$$  / $$$$$$$$ |$$ |  $$ | $$ |    $$ |  $$ |$$ |  \__|$$$$$$$$ |
   $$ |$$   ____| $$  $$<    $$ |$$\       $$ |  $$ |$$ |  $$ |  \$$$  /  $$   ____|$$ |  $$ | $$ |$$\ $$ |  $$ |$$ |      $$   ____|
   $$ |\$$$$$$$\ $$  /\$$\   \$$$$  |      $$ |  $$ |\$$$$$$$ |   \$  /   \$$$$$$$\ $$ |  $$ | \$$$$  |\$$$$$$  |$$ |      \$$$$$$$\ 
   \__| \_______|\__/  \__|   \____/       \__|  \__| \_______|    \_/     \_______|\__|  \__|  \____/  \______/ \__|       \_______|
   """)
