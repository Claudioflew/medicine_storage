'''
General comments: Superior coding and superior use of a table of functions! You
should be very happy with your midterm coding.

Rubric:
1. Menu loop: ✅
2. Menu processing: ✅
3. Dictionary comprehension with zip(): ✅
4. List comprehension or enumerate(): ✅
5. Columns: ✅
6. Output formatting: ✅
7. Input validation for menu: ✅
8. Input validation for medication number: ✅
9. Input validation for no negative entries: ✅
10. Input validation for preventing negative balance: ✅
11. Output loop: ✅
'''

def main():
  medName = [
      "Asprin", "Tylenol", "Lipitor", "Prilosec", "Gloucophage", "Zocor",
      "Toprol", "Zithromax", "Zoloft", "Xanax", "Wellbotrin", "Flexeril",
      "Prozac", "Effexor", "Adderall"
  ]

  medQty = [15, 20, 18, 24, 19, 29, 32, 42, 25, 42, 52, 19, 100, 40, 20]

  funcTable = [displayMed, addMed, removeMed]

  dict1 = {name: qty for name, qty in zip(medName, medQty)}
  dict2 = {ind: name for ind, name in enumerate(medName)}

  choice = chooseMenu()
  while choice != 4:
    funcTable[int(choice) - 1](dict1, dict2)
    choice = chooseMenu()
  print("Program ending. Have a superior day.")


def chooseMenu():
  choice = input("""
  **** Main Menu ****
  Press 1: medication status
        2: add medication to inventory
        3: remove medication from inventory
        4: quit  --> """)

  while choice not in [str(i) for i in range(1, 5)]:
    choice = input("Invalid entry.. Please enter 1 to 4: ")

  return int(choice)


def displayMed(dict1, dict2):
  displayStr = """
  --------------------
  Medication inventory
  --------------------
   ## Name        Qty   ## Name        Qty   ## Name        Qty   ## Name        Qty
"""

  for ind, name in dict2.items():
    if ind % 4 == 3:
      displayStr += "   {0:2} {1:11} {2:3}\n".format(ind + 1, name, dict1[name])
    else:
      displayStr += "   {0:2} {1:11} {2:3}".format(ind + 1, name, dict1[name])

  print(displayStr)

def addMed(dict1, dict2):
  displayMed(dict1, dict2)

  print("\nWhich medication do you want to deposit?")
  medChoice = input("Enter the medication number: ")
  while medChoice not in [str(i) for i in range(1, 16)]:
    medChoice = input("Invalid entry.. Please enter 1 to 15: ")
  medChoice = int(medChoice) - 1

  addQty = input(f"How many pills of {dict2[medChoice]} to add? --> ")
  while True:
    if addQty.isdigit():
      if int(addQty) <= 0:
        addQty = input("Invalid entry.. Please enter a positive int: ")
      else:
        break
    else:
      addQty = input("Invalid entry.. Please enter a positive int: ")

  dict1[dict2[medChoice]] += int(addQty)
  print(f"\tUPDATE: {dict2[medChoice]} new balance: {dict1[dict2[medChoice]]}")


def removeMed(dict1, dict2):
  displayMed(dict1, dict2)

  print("\nWhich medication do you want to remove?")
  medChoice = input("Enter the medication number: ")
  while medChoice not in [str(i) for i in range(1, 16)]:
    medChoice = input("Invalid entry.. Please enter 1 to 15: ")
  medChoice = int(medChoice) - 1

  if dict1[dict2[medChoice]] == 0:
    print(f"We don't have any {dict2[medChoice]}..")
    return

  print(f"How many pills of {dict2[medChoice]} to remove? \
        \n\tMaximum available is: {dict1[dict2[medChoice]]}")
  removeQty = input("Enter amount here: ")
  while True:
    if removeQty.isdigit():
      if (int(removeQty) <= 0) or (int(removeQty) > dict1[dict2[medChoice]]):
        removeQty = input(
            f"Invalid entry.. Please enter 1 to {dict1[dict2[medChoice]]}: ")
      else:
        break
    else:
      removeQty = input(
          f"Invalid entry.. Please enter 1 to {dict1[dict2[medChoice]]}: ")

  dict1[dict2[medChoice]] -= int(removeQty)
  print(f"\tUPDATE: {dict2[medChoice]} new balance: {dict1[dict2[medChoice]]}")


if __name__ == "__main__":
  main()
