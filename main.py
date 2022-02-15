import random
from enum import Enum

class WumpusState(Enum):
  DEAD = 0
  AWAKE = 1
  ASLEEP = 2

gameState = {
  "alive": True,
  "wumpusState": WumpusState.ASLEEP,
  "currentRoom": 1,
  "wumpusRoom" : 1,
  "startleChance": .5,
  "sleepChance": .33,
  "numAmmo": 4,
  "caveMap": {
    1: [2, 3, 8],
    2: [1, 3, 13],
    3: [1, 2, 5],
    4: [1, 2, 3],
    5: [1, 6, 14],
    6: [5, 9, 10],
    7: [5, 8, 9],
    8: [4, 10, 7],
    9: [6, 7, 10],
    10: [12, 6, 9, 8],
    11: [13, 8, 6],
    12: [10, 2, 13, 14],
    13: [11, 4, 2],
    14: []
  }
}

def numOfRooms(state):
  count = 0
  for room in state["caveMap"]:
    count += 1
  return count

def safeRandomRoom(state):
  while True:
    room = random.randint(1, numOfRooms(state))
    roomExits =state["caveMap"][room]
    if len(roomExits) > 0:
      break
  return room      

def newGame(state):
  if numOfRooms(state) < 2:
    print("a game that only has one room is not supported")
    raise SystemExit
  while state["wumpusRoom"] == state["currentRoom"]:
    state["wumpusRoom"] = safeRandomRoom(state)
    state["currentRoom"] = safeRandomRoom(state)
  return

def niceAmmoList(numAmmo):
  if numAmmo == 0:
    return "leave u ran out stoopid"
  if numAmmo == 1:
    return "u got one round dawg"
  return f"u have {numAmmo} rounds left"

def niceExitList(state):
  currentRoom = state["currentRoom"]
  roomExits = state["caveMap"][currentRoom]
  numExits = len(roomExits)
  
  if numExits == 0:
    state["alive"] = False
    return "bahaha loser ur trapped and u ded"
  
  if numExits == 1:
    return "this room is special it only goes to {roomExits[0]}"
  
  if len(roomExits) == 2:
    return f"this room has exits to rooms {roomExits[0]} and {roomExits[1]}"
  
  niceList = "this room has exit to rooms: "
  for exitNum in range(numExits-1):
    niceList += f"{roomExits[exitNum]}, "
  niceList += f" and {roomExits[-1]}"
  
  return niceList

def sense(state):
  currentRoom = state["currentRoom"]
  print(f"bestie ur in room {currentRoom}")
  print(niceAmmoList(state["numAmmo"]))
  if currentRoom == state["wumpusRoom"]:
    if state["wumpusState"] == WumpusState.ASLEEP:
      print("wumpie dumpie is taking a phat nap")
    else:
      print("wumpie dumpie is lookin at uuu")
  for exitNumber in state["caveMap"][state["currentRoom"]]:
      if state["wumpusRoom"] == exitNumber:
        print("yummy yummy wumpie dumpie tooted")
  print(niceExitList(state))

def move(state):
  currentRoom = state["currentRoom"]
  nextRoom = int(input("where ru going"))
  if nextRoom not in state["caveMap"][currentRoom]:
    print(f"silly goose u cant get to room {nextRoom} from here")
    return
  if nextRoom not in state["caveMap"]:
    print(f"{nextRoom} doesnt exist smh")
    return
  state["currentRoom"] = nextRoom
  
def encounter(state):
  if state["currentRoom"] == state["wumpusRoom"] and state["wumpusState"] == WumpusState.ASLEEP:
    print("smh my head wumpie dumpie wants to eat u")
    state["wumpusState"] = WumpusState.AWAKE
    if (random.random() < state["startleChance"]):
      roomExits = state["caveMap"][state["currentRoom"]]
      if len(roomExits) == 0:
        print('u scared wumpie dumpie but u cant get out lol')
      else:
        print('arent u one lucky gal u scared wumpie dumpie and he ran out an exit')
        state["wumpusRoom"] = random.choice(roomExits)
  if state["currentRoom"] == state["wumpusRoom"] and state["wumpusState"] == WumpusState.AWAKE:
    print("nom nom nom wumpie dumpie ate u")
    state["alive"] = False

def updateHazards(state):
  if state["wumpusState"] == WumpusState.AWAKE:
    roomExits = state["caveMap"][state["currentRoom"]]
    if random.random() <state["sleepChance"]:
      print("hint: wumpie dumpie is napping bro shhh")
      state["wumpusState"] = WumpusState.ASLEEP
    elif len(roomExits) > 0:
      state["wumpusRoom"] = random.choice(roomExits)

newGame(gameState)
print("ur mom")
print()

while gameState["alive"]:
  updateHazards(gameState)
  print("hint: the wumpus is in room {wumpusRoom}".format_map(gameState))
  sense(gameState)
  encounter(gameState)
  if not gameState["alive"]: 
    break
  nextAction = input("\nwhats next")

  if nextAction.lower()[0] == "m":
    move(gameState)
    continue

  if nextAction.lower()[0] == "q":
    break
  
  print(f"bruh wtheck ru doing idk how to do '{nextAction}'.'")
  print("i stoopid ik how to quit")