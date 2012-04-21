import sys

class World:
    def __init__(self):
        self.memoryList = []
        self.tutorialship = Ship()
        thread = Interactable(("green thread", "green", "thread", "wall", "bright green"), self.tutorialship.room1, "A vine spills forth in a pile of rubble.\nYou remember that this room used to bustle.\nNot anymore. In fact, the exit doors are shut.\n\"Remember\" is bound to \"rocket.\"")
        vine = Interactable(("vine", "vines", "ivy"), self.tutorialship.room1, "asdf")
        door_mem = Memory(("door", "exit", "doors", "exit doors", "exit door"), "The blast doors are, somewhow, secure.\nThey were originally meant to ensure\nthat nobody got in. It seems that you're\nnot getting out - of that you're sure.")
        room_mem = Memory(("bustle", "room", "here"), "This room used to be constantly busy - \npeople used to be in and out constantly,\nchecking your vitals, diagnosing, tweaking,\nand always, constantly, worrying, fretting.")
        meta_mem = Memory(("rocket", "december", "memory"), "You don't know why you think the way\nthat you do - you associate the array\nof things that you do with strange words.\nYou blame the hordes of clipboard nerds.")
        nerd_mem = Memory(("nerds", "hordes", "nerd", "horde", "clipboard", "clipboards"), "They built you, you know. They put you\ntogether, bit by bit, screw by screw.\nI would know - I was one of the nerds\nthat threw you together from broken words.")
        for memory in (door_mem, meta_mem, nerd_mem, room_mem):
            self.memoryList.append(memory)

        self.player1 = Player(self)
        self.player1.location = self.tutorialship.room1
        self.player1.location.objectList.append(vine)
        self.player1.location.objectList.append(thread)

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
        return "You want to pick up what?"
    def drop(self, target):
        return "You want to drop what?"

class Player(Agent):
    def __init__(self, world):
        self.world = world
    def act(self, userInput=""):
        userInput = userInput.lower()
        inputList = userInput.split(" ")
        if (inputList[0]=="quit"):
            sys.exit()
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
            return "Woopsy! I don't recognize that command."

class Interactable(Actor):
    def __init__(self, name, location, description="A generic object."):
        self.name = name; self.location=location; self.description=description

class Memory(Actor):
    def __init__(self, name, description="A generic memory."):
        self.name = name; self.description=description