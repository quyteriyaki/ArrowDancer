from enum import Enum

# ArrowDirection tells us where other witches need to be
class ArrowDirection(Enum):
  BOTTOM_LEFT = 1
  BOTTOM_CENTER = 2
  BOTTOM_RIGHT = 3
  MIDDLE_LEFT = 4
  CENTER = 5
  MIDDLE_RIGHT = 6
  TOP_LEFT = 7
  TOP_CENTER = 8
  TOP_RIGHT = 9

  # For the FGC enthusiast (imo feels more comfy to use this type of notation)
  @staticmethod
  def num(number: int): return ArrowDirection(int(number))

  # For rendering
  @staticmethod
  def emoji(direction):
    if direction == ArrowDirection.BOTTOM_LEFT: return  "↙️"
    if direction == ArrowDirection.BOTTOM_CENTER: return "⬇️"
    if direction == ArrowDirection.BOTTOM_RIGHT: return "↘️"
    if direction == ArrowDirection.MIDDLE_LEFT: return "⬅️"
    if direction == ArrowDirection.CENTER: return "⏺️"
    if direction == ArrowDirection.MIDDLE_RIGHT: return "➡️"
    if direction == ArrowDirection.TOP_LEFT: return "↖"
    if direction == ArrowDirection.TOP_CENTER: return "⬆️"
    if direction == ArrowDirection.TOP_RIGHT: return "↗️"

    return None

# ArrowType tells us whether it's a bonk or a pointer
class ArrowType(Enum):
  BONK = "B"
  POINT = "P"

  @staticmethod
  def let(letter):
    return ArrowType(str(letter))

# ? We could limit bonks depending on the direction (2,4,6,8)?
class Arrow():
  def __init__(self, direction: ArrowDirection, type: ArrowType):
    
    # Value check (bonks)
    if type == ArrowType.BONK and direction.value not in [2,4,6,8]:
      raise ValueError("Found a corner bonk in Dance Formation.")

    self.direction = direction
    self.type = type 
  
  # The main thing when we check if arrows are equal to each other are the directions.
  def __eq__(self, other):
    return self.direction == other.direction

  def __str__(self):
    return str(self.direction.value) + str(self.type.value)

  # Shorthand arrow notation (SAN)
  @staticmethod
  def short(notation: str):
    if len(notation) != 2:
      raise ValueError("Notation has incorrect length")

    return Arrow(ArrowDirection.num(notation[0]), ArrowType.let(notation[1]))

class DanceFormation:
  def __init__(self, *args):
    # Existence check (arrows)
    if len(args) == 0:
      raise ValueError("A Dance Formation cannot have 0 arrows.")

    # Type check (if list, break out)
    if isinstance(args[0], list):
      args = [i for i in args[0]]
    
    # Type check (arrows)
    for i in args:
      if not isinstance(i, Arrow): raise TypeError("Caught an argument not of type Arrow in Dance Formation")

    # Existence check (duplicates)
    seen = set()
    dupes = [x for x in args if x.direction in seen or seen.add(x.direction)]
    if len(dupes) > 0:
      raise ValueError("Multiple arrows in same direction found in Dance Formation")

    # Value check (impossible bonk + point combo) (e.g. 1P, 2B)
    self.arrows: list[Arrow] = args

  # Make multiple arrows with SAN
  # ? Input format: "2B, 6P" or ["2B", "6P"]
  @staticmethod
  def multiShort(notation:str | list | tuple):

    if type(notation) == str:
      # Delete all spaces
      notation = notation.replace(" ", "")
      notation = notation.split(",")

    if type(notation) == list or tuple:
      return DanceFormation([Arrow.short(i) for i in notation])
  
  def getTypeAtPosition(self, direction):
    for i in self.arrows:
      if i.direction == direction:
        return i.type
    return None

  def __str__(self):
    return "Formation: " + ",".join([str(i) for i in self.arrows])

class DanceSequence(list):
  def __init__(self, *args, **kwargs):
    if args: super().__init__(*args, **kwargs)
    else: super().__init__(list())
  
  @staticmethod
  def fromStringList(sequence: list):
    return DanceSequence([DanceFormation.multiShort(i) for i in sequence])

  def __str__(self):
    return "Dance:\n" + "\n".join([str(i) for i in self])

class DanceVisual:
  @staticmethod 
  def buildFormation(formation: DanceFormation):
    data = ["◻"] * 9
    for i in range(9):
      dir = ArrowDirection.num(i + 1)
      t = formation.getTypeAtPosition(dir)
      if t == ArrowType.POINT:
        data[i] = ArrowDirection.emoji(dir)
      elif t == ArrowType.BONK:
        data[i] = ArrowDirection.emoji(ArrowDirection.CENTER)
    
    return (data[6:9], data[3:6], data[0:3])

  @staticmethod
  def buildSequence(sequence: DanceSequence):
    data = [DanceVisual.buildFormation(i) for i in sequence]
    return data

  @staticmethod
  def showFormation(formation: DanceFormation):
    output = DanceVisual.buildFormation(formation)
    for i in output: print("".join(i))

  @staticmethod
  def showSequence(sequence: DanceSequence, style: str = "wide"):
    if style == "wide":
      output = DanceVisual.buildSequence(sequence)
      for i in range(3):
        line = "   ".join(["".join(j[i]) for j in output])
        print(line)
    elif style == "long":
      for i in sequence:
        DanceVisual.showFormation(i)
        print("\n")

if __name__ == "__main__":
  apples = DanceSequence.fromStringList([
    ("2P", "8P"),
    ("3P", "9P"),
    ("4B"),
    ("2P", "8P")
  ])
  print(apples)
  DanceVisual.showSequence(apples)