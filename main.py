currentRoom = 1
caveMap = {
  1: [2, 3, 8],
  2: [1, 3, 13],
  3: [1, 2, 5],
  4: [1, 2, 3],
  5: [1, 6],
  6: [5, 9, 10],
  7: [5, 8, 9],
  8: [7, 10, 4],
  9: [6, 7, 10],
  10: [12, 6, 9, 8],
  11: [13, 8, 6],
  12: [10, 2, 13],
  13: [11, 4, 2]
}
  

def look():
  print(f"bestie ur in room {currentRoom}")
  if len(caveMap[currentRoom]) == 0:
    print("bahaha loser ur trapped")
  print(f"exits lead to room: {caveMap[currentRoom]}")

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

while True:
  look()
  nextAction = input("\nwhats next")

  if nextAction.lower()[0] == "m":
    move()
    continue

  if nextAction.lower()[0] == "q":
    break
  
  print(f"bruh wtheck ru doing idk how to do '{nextAction}'.'")
  print("i stoopid ik how to quit")