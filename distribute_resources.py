from random import random

institutions = []

def add_institution(name, amout_needed, urgency):
  # name, amount_needed, urgency, prob, received
  institutions.append([name, amout_needed, urgency, 0, 0])

def compute_weights():
  global institutions
  for ins in institutions:
    ins[3] = 1 * ins[2]

if __name__ == "__main__":
  print()
  print("This program simulates a biased algorithm that distributes resources among institutions.")
  print("=" * 50)
  
  resources = int(input("(?) How many items are available? "))
  count = int(input("(?) How many institutions do you want to add? "))
  print("(?) Enter an institution's need and urgency (0 to 1): e.g 20, 0.24")

  for i in range(count):
    need, urgency = eval(input("> "))
    add_institution(chr(65 + i), need, urgency)

  # add_institution("Old Cargo", 30, 0.45)
  # add_institution("Nissan", 50, 1)
  # add_institution("Unilever", 35, 0.6)
  # add_institution("UNILAG", 10, 0.2)

  compute_weights()

  print("Resources available:", resources)

  total_prob = sum(map(lambda ins: ins[3], institutions))
  institutions.sort(key=lambda ins: ins[3], reverse=True)

  time = 0

  while resources >= 0:
    prev = resources
    if time == 0:
      debt = resources / 2
      resources -= debt
    for i, ins in enumerate(institutions):
      amt = ins[3] / total_prob * resources
      amt = round(min(ins[1] - ins[4], amt))
      ins[4] += amt
      resources -= amt
    time += 1
    if time == 1:
      resources += debt
    if prev == resources:
      # give the last one
      least = [ins for ins in institutions if ins[4] == institutions[-1][4]]
      for ins in least:
        amt = round(resources / len(least))
        ins[4] += amt
        resources -= amt
      break

  spent = 0
  for ins in institutions:
    spent += ins[4]
    print(ins[0], "received", ins[4], "out of", ins[1], "items. Urgency was", ins[2] * 100, "%")

  print("Resources spent:", spent)
  print("Resources left:", resources)

  # print(institutions)
