import sys
class World:
    def __init__(self):
        self.memoryList = []
        self.tutorialship = Ship()
        thread = Interactable(("green thread", "green", "thread", "wall", "bright green", "something"), self.tutorialship.room1, "A vine spills forth in a pile of rubble.\nYou remember that this room used to bustle.\nNot anymore. In fact, the exit doors are shut.\n\"Remember\" is bound to \"rocket.\"")
        vine = Interactable(("vine", "vines", "ivy"), self.tutorialship.room1, "The vine has unassumingly breached\nyour bunker. You're merely irritated\nuntil you realize there's a trickle\nof water, too. The water looks dreadful.")
        door = Interactable(("door", "exit", "doors", "exit doors", "exit door"), self.tutorialship.room1, "Sharp, green-stenciled warnings decorate\nthe blast doors, vivid orange on slate.\n\"CAUTION: Do not exit during interception\nsequence. Do not press override button.\"")
        button = Interactable(("button", "override", "override button"), self.tutorialship.room1, "The override button was installed to let\npeople escape death by starvation. Bet\nthey'd die faster outside, though, from\nradiation leaking from a shot-down bomb.")
        lights = Interactable(("lights", "light", "lighting", "flicker", "flickering"), self.tutorialship.room1, "It seems, from the continuous flickering,\nlike the flourescent lights are running\non low current. That would be unfortunate.\nFor you and it, energy's on a tight budget.")
        door_mem = Memory(("door", "exit", "doors", "exit doors", "exit door", "blast door", "blast doors"), "The blast doors are, somewhow, secure.\nThey were originally meant to ensure\nthat nobody got in. It seems that you're\nnot getting out - of that you're sure.")
        room_mem = Memory(("bustle", "room", "here", "bunker", "busy"), "This room used to be constantly busy - \npeople used to be in and out constantly,\nchecking your vitals, diagnosing, tweaking,\nand always, constantly, worrying, fretting.")
        meta_mem = Memory(("rocket", "december", "memory"), "You don't know why you think the way\nthat you do - you associate the array\nof things that you do with strange words.\nYou blame the hordes of clipboard nerds.")
        nerd_mem = Memory(("nerds", "hordes", "nerd", "horde", "clipboard", "clipboards", "people", "worrying", "fretting", "worry", "fret", "technicans", "technician"), "They built you, you know. They put you\ntogether, bit by bit, screw by screw.\nYou should know, you killed the nerds\nthat threw you together from broken words.")
        health_mem = Memory(("vitals", "diagnosis", "prognosis", "health"), "The technicians swarmed over you busily -\nyou were meant to protect this country.\nYour diagnosis was fine - a healthy state -\nnear optimal intercept and retaliate rate.")
        bomb_mem = Memory(("bomb", "intercept", "interception", "purpose", "job", "rockets", "bombs", "interception sequence", "sequence"), "You brought the rockets down, you know;\nyou made tactical decisions: counted ammo,\narmed countermeasures, carefully guided\nshots. And then you retaliated.")
        friend_mem = Memory(("friends", "friendship", "friend"), "You don't remember any friends...")
        retaliation_mem = Memory(("retaliated", "retaliation", "retaliate", "decision", "decisions"), "Oh dear. You remember ending the world.")
        for memory in (door_mem, meta_mem, nerd_mem, room_mem, health_mem, bomb_mem, retaliation_mem, friend_mem):
            self.memoryList.append(memory)

        self.player1 = Player(self)
        self.player1.location = self.tutorialship.room1
        for object in (vine, thread, door, button, lights):
            self.player1.location.objectList.append(object)

class Ship:
    def __init__(self):
        self.room1 = Room("room1", "You're in a cement-walled room. It's\nsparse and the lighting is on the fritz.\nSomething bright green threads amongst all\nthe gray, encroaching through the wall.")

class Room:
    def __init__(self, name, description = "This is a blank room description."):
        self.description = description
        self.name = name
        self.objectList=[]
        self.tempDescription=""
    def describe(self):
        return self.description

class Description:
    pass

class Actor:
    def __init__(self):
        self.location = None

class Agent(Actor):
    def __init__(self):
        pass
    def get(self, target):
        return "You can't pick anything up!"
    def drop(self, target):
        return "You have nothing to drop."

class Player(Agent):
    def __init__(self, world):
        self.world = world
        self.decembered = False
    def act(self, userInput=""):
        userInput = userInput.lower()
        inputList = userInput.split(" ")
        if (userInput=="quit" or userInput=="exit"):
            sys.exit()
        elif userInput == "" and self.decembered == True:
            return self.location.describe()
        elif inputList[0] in ("january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november"):
            return "This module is currently offline."
        elif userInput == "wake" or userInput == "wake up":
            return "You don't wake up, remember? You come to."
        elif userInput == "come to":
            return "You've already done that."
        elif userInput == "crash":
            raise TypeError
        elif userInput == "remember" or inputList[0] == "remember":
            return "You don't know how to \"remember\".\nYou do know how to \"rocket\", however."
        elif userInput == "rocket":
            return "There's so much to remember - a decade\nof memories. At least they don't fade.\nYou should probably query a particular\nmemory to learn more, you infer."
        elif inputList[0] == "rocket" and userInput != "rocket":
            for x in self.world.memoryList:
                if(inputList[1] in x.name):
                    return x.description
            return "You don't remember that."
        elif (userInput == "december"):
            self.decembered = True
            return self.location.describe()
        elif inputList[0]=="december" and (inputList[1]=="bunker" or inputList[1]=="room" or inputList[1]==""):
            return self.location.describe()
        elif userInput == "look" or inputList[0] == "look":
            return "You don't know how to \"look\".\nYou do know how to \"December\", however."
        elif (inputList[0] == "december" and inputList[1]=="at"):
            for x in self.location.objectList:
                if(inputList[2] in x.name):
                    return x.description
            return "You want to look at what, now?"
        elif inputList[0] == "december" and inputList != "december":
            for x in self.location.objectList:
                if(inputList[1] in x.name):
                    return x.description
            return "You want to look at what, now?"
        elif (inputList[0] in ("get", "grab", "pull", "acquire", "obtain")):
            return "You can't "+inputList[0]+" anything."
        elif (inputList[0] == "inventory"):
            return "You aren't carrying anything!"
        elif (inputList[0] == "drop"):
            return self.drop(inputList[1])
        else:
            return "You don't understand how to do that."

class Interactable(Actor):
    def __init__(self, name, location, description="A generic object."):
        self.name = name; self.location=location; self.description=description

class Memory(Actor):
    def __init__(self, name, description="A generic memory."):
        self.name = name; self.description=description