from dancer import *

class Witch:
  def __init__(self, name):
    self.name = name
    self.mainDance = None
    self.altDance = None

    self.selectedDance = "Main"

  def setMainDance(self, dance: DanceSequence):
    self.mainDance = dance

  def setAltDance(self, dance: DanceSequence):
    self.altDance = dance

  def chooseDance(self, option: str):
    self.selectedDance = option

  def getCurrentDance(self):
    if self.selectedDance == "Main":
      return self.mainDance
    elif self.selectedDance == "Alt":
      return self.altDance
    else: return None

  # ? Do we really need to remove dances

class Team:
  def __init__(self):
    self.members: list[Witch] = []

  def addMember(self, member: Witch):
    self.members.append(member)

  def showDances(self):
    for i in self.members:
      print(i.name, "\n") 
      print("Main")
      DanceVisual.showSequence(i.mainDance)
      print("\n")
      print("Alt")
      DanceVisual.showSequence(i.altDance)
      print("\n")

if __name__ == "__main__":
  myTeam = Team()

  a = Witch("DPS")
  a.setMainDance(DanceSequence.fromStringList([
    ("2P", "8P"),
    ("3P", "9P"),
    ("4B"),
    ("2P", "8P"),
  ]))
  
  a.setAltDance(DanceSequence.fromStringList([
    ("2P", "8P"),
    ("3P", "9P")
  ]))

  b = Witch("Debuff")
  b.setMainDance(DanceSequence.fromStringList([
    "9P, 6P",
    "8P",
    "7P",
    "6B",
    "4P,1P"
  ]))

  b.setAltDance(DanceSequence.fromStringList([
    ("4B", "3P"),
    ("6P"),
    ("9P")
  ]))


  c = Witch("Buff")
  c.setMainDance(DanceSequence.fromStringList([
    ("3P"),
    ("6P"),
    ("9P"),
    ("8P")
  ]))

  c.setAltDance(DanceSequence.fromStringList([
    ("8B", "2P"),
    ("1P", "3P")
  ]))

  myTeam.addMember(a)
  myTeam.addMember(b)
  myTeam.addMember(c)

  myTeam.showDances()