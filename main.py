alive = True
currentRoom = 1
caveMap = {
  1: [2, 3, 8],
  2: [1, 3, 13],
  3: [1, 2, 5],
  4: [1, 2, 3],
  5: [1, 6, 14],
  6: [5, 9, 10],
  7: [5, 8, 9],
  8: [7, 10, 4],
  9: [6, 7, 10],
  10: [12, 6, 9, 8],
  11: [13, 8, 6],
  12: [10, 2, 13, 14],
  13: [11, 4, 2],
  14: []
}

def niceExitList(roomExits):
  global alive
  numExits = len(roomExits)
  
  if numExits == 0:
    alive = False
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

def look():
  print(f"bestie ur in room {currentRoom}")
  print(niceExitList(caveMap[currentRoom]))

def move():
  global currentRoom
  nextRoom = int(input("where ru going"))
  if nextRoom not in caveMap[currentRoom]:
    print(f"silly goose u cant get to room {nextRoom} from here")
    return
  if nextRoom not in caveMap:
    print(f"{nextRoom} doesnt exist smh")
    return
  currentRoom = nextRoom
  
print("ur mom")
print()

while alive:
  look()
  if not alive: 
    break
  nextAction = input("\nwhats next")

  if nextAction.lower()[0] == "m":
    move()
    continue

  if nextAction.lower()[0] == "q":
    break
  
  print(f"bruh wtheck ru doing idk how to do '{nextAction}'.'")
  print("i stoopid ik how to quit")