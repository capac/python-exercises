from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    def enter(self):
        print("This scene is not defined")
        print("Subclass it and implement enter")
        exit(1)

class Engine(Scene):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            # be sure to print the last scene
        current_scene.enter()

class Death(Scene):

    quips = ["You died. You kinda suck at this.",
    "Your mum would be proud... if she were smarter.", "Such a loser",
     "I have a small puppy that's better at this",
     "You're worse than your dad's jokes"]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips))-1])
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print(dedent("""The Gothons of planet Percal No25 have invaded your ship and destroyed 
        your crew. You are the sole survivor, and your last mission is to get the neutron destruct bomb
        from the Weapon Armory, put it in the Bridge and blow the ship up
        after escaping into the escape Pod.

        You're running down the central corridor to the weapon armory when a Gothon
        jumps out, red scaly skin, dark grimy teeth, and evil clown costume
        flowing around his hate filled body. He's blocking the door to the
        Armory and about to pull a weapon to blast you.""" ))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""Quick on the draw you yank out your blaster and fire it at the Gothon.
            His clown costume is flowing and moving around his body, which throws off
            your aim. Your laser hits his costume but misses him entirely.
            This completely ruins his brand new costume his motherbought him
            which makes him fly into an in sane rage and blast you repeatedly
            in the face until you are dead. Then he eats you. """))
            return 'death'

        elif action == "dodge":
            print(dedent("""Like a world class boxer you dodge, weave, slip and slide right
            as the Gothon's  blaster cranks a laser past your head.
            In the middle of your artful dodge your foot slips and you bang your head on the
            metal wall and pass out. You wake up shortly after only to die as the Gothon stomps
            on your head and eats you. """))
            return 'death'

        elif action == "tell a joke":
            print(dedent("""Lucky for you they made you learn Gothon insults in the academy.
            You tell one Gothon joke you know: tnah foeaw gow annf slklll.
            The Gothon stops, tries not to laugh, then bursts out laughing
            and cannot move.  You run up and shoot him square in the head
            putting him down, then jump through the Weapon Armory door."""))
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!!")
            return 'central_corridor'


class LaserWeaponArmory(Scene):
    def enter(self):
        print(dedent("""You do a dive roll into the Weaon Armory, crouch
        and scan the room for more Gothons that might be hiding.
        It's dead quiet, too quiet. You stand up and run to the far side
        of the room and find the bomb in its container.
        There's a keypad lock on the box and you need to the code
        to get the bomb out.
        If you get the sode wrong 10 times, then the lock closes
        forever and you cannot get the bomb.
        The code is three digits."""))

        code = '123' # f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]>")
        guesses = 0

        while guess != code and guesses <9:
            print("BZZZZZEEDDDD!")
            guesses += 1
            guess = input("[keypad]>")

        if guess == code:
            print(dedent("""The container clics open and the seal breaks.
            You grab the bomb and run to the bridge, where you must
            place it in the right spot."""))
            return 'the_bridge'
        else:
            print(dedent("""The lock buzzes one last itme and then
            you hear a sickening melting sound as the mechanism fuses
            together. You decide to sit there, and finally
            the Gothins blow up the ship from their ship
            and you die."""))
            return 'death'

class TheBridge(Scene):
    def enter(self):
        print(dedent("""You burst onto the bridge with the bomb
        nd surprise 5 Gothons who are trying to take control of the
        ship. They haven't pulled their weapon, as they see the bomb
        under your arm and don't want to set it off. """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""In a panic you throw the bomb at the Gothons
            and make a leap to the door. Right as you throw it, a Gothons
            shoots you and you die. """))
            return 'death'

        elif action == "slowly place the bomb":
            print(dedent("""The Gothins see the  bomband start sweating.
            You inch backward to the door, open it, and carefully
            place the bomb to the floor.  You jump back and close the door.
            Then blast the door so the Gothins cannot escape.
            You then run to the escape pod. """))

            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"

class EscapePod(Scene):
    def enter(self):
        print(dedent("""You rush through the ship trying to make it
        to the escape pod before the ship explodes. You arrive at the chamber
        and need to pick one escape pod. Some of them could be damaged,
        but you have no time to look.  There are five pods,
        which one will you take? """))
        good_pod = randint(1,5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent("""You jump into pod """f"{guess}"""" and hit the eject
            buttin. The pod escapes out into the void, then
            implodes as the hull ruptures, crushing your body
            into jam jelly."""))
            return 'death'
        else:
            print(dedent("""You jump into pod """f"{guess}"""" and hit the eject
            button. The pod slides easily into the void heading
            you to the planet below.
            You look back and see you ship explode taking
            the Gothins with her. You WON!"""))

            return 'finished'

class Finished(Scene):
    def enter(self):
        print("You won! Well done!")
        return 'finished'

class Map(object):

    scenes = {'central_corridor': CentralCorridor(), 'laser_weapon_armory': LaserWeaponArmory(),
    'the_bridge': TheBridge(), 'escape_pod': EscapePod(), 'death': Death(), 'finished': Finished()}

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)
        
    def last_scene(self):
        pass

if __name__ == "__main__":
    a_map = Map('central_corridor')
    a_game = Engine(a_map)
    a_game.play()
