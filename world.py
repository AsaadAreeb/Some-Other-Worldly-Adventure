from player import Player
# import logging
import random
import time


class World:

    classes = {}

    def __init__(self):
        self.player = Player()
    
    def performRitual(self):
        print("""
                You performed the profession ritual!
                Your soul is being looked upon, you will be given a profession that your soul is able to bear.
""")
        self.player.profession = random.choice(["Guard", "Swordsman", "Thief", "Summoner", "Mage"])
        

        print(f"""
                {self.player.profession} profession has been bestowed upon you!
                NEVER GO AGAINST WHAT HAS BEEN CHOSEN BY FATE FOR YOU.
                ELSE IT END GOOD FOR YOU.
        """)
        World.classes[len(World.classes) + 1] = self.player.profession
        # return self.player.profession
    
    def performAction(self):
        action = ''
        while action !='1' and action !='2' and action !='3' and action !='4':
            action = input()

        return action

    
    def start(self):
        run=True
        while run==True:
            try:
                print("Choose you name!\n")
                self.player.name = input()
                # if self.player.name == 'q':
            except ValueError:
                print("Not a string, try again")

            {time.sleep(1)}
            print(f"""
                    Welcome to Some Other Worldly Adventure!
                    So.....?.. {self.player.name} ah yes.

                    You are one day away from your awakening!
                    You fate will be decided and you will become a functioning member of society.
                    Tommorow will be the most special day for you.
                    Well, not only for you but for all those who will be turning 18.
                    But you get the sentiments right....right?
                    Anyways, you got one day more to waste, but don't wander out of town ok?
                    At this time of the year those guards are more proactive than normal.
                    They are not to blame though, we can't have someone with cursed profession get away can we?
                """)
            {time.sleep(5)}
            print(f"""


                1) Return home and sleep till tommorow          2) Try to go outside the village
                3) Roam village                                 4) Visit your friends house
                """)

            action = self.performAction()
            if action == '1':
                print("""
                        You returned home and slept till the ritual.
                        Your friends enjoyed the whole night in excitement of tommorow's ritual.
                        When you got to know about it you were quite upset and cursed the oldman
                        for getting the stupid idea inside your head.
                    """)
            
            
            # World.classes[len(World.classes) + 1] = self.performRitual()
            # print(World.classes)
            run=False
            
        


world = World()
world.start()







