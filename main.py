# Name - Krisha Hemani
#      - Justin Ha
# Program - Practice
# Date - 02/15/2024
# Module 3 - Capital Quiz
# Purpose - Create a 10 question quiz on US states and capitals

import random

def read_file(file_name):
  """Reads a file and returns a 2d matrix with states and capitals"""
  file = open(file_name, "r")
  list2d = []
  for row in file:
    items = row.strip().split(",")
    list2d.append(items)
  return list2d


def get_random_state(states):
  """Get random state"""
  state = random.choice(states)
  return state

def get_random_choices(state, correct_capital):
  """Get 3 random choices and the correct choice"""
  choices = [correct_capital]
  while len(choices) < 4:
    capital = random.choice(state)
    if capital[1] not in choices:
      choices.append(capital[1])
  random.shuffle(choices)
  return choices

def ask_question(correct_state, possible_answers):
  """Ask question and returns an answer by converting A-D to 0-3"""  
  print("The capital of", correct_state[0], "is:")
  print("\tA.", possible_answers[0], end = " ")
  print("\tB.", possible_answers[1], end = " ")
  print("\tC.", possible_answers[2], end = " ")
  print("\tD.", possible_answers[3])
  answer = input("Enter selection: ")
  while answer.upper() not in "ABCD":
    print("Invalid input. Input choice A-D.")
    answer = input("Enter selection: ")
    continue 
  if answer.upper() == "A":
    answernum = 0
  elif answer.upper() == "B":
    answernum = 1
  elif answer.upper() == "C":
    answernum = 2
  else:
    answernum = 3
  return answernum

def main():
  """Main function"""
  print("- State Capitals Quiz -")
  state = read_file("statecapitals.txt")
  correct_answer = 0
  previous_states = []
  for i in range (10):
    correct_state = get_random_state(state)
    while correct_state in previous_states:
      correct_state = get_random_state(state)
      continue
    previous_states.append(correct_state)
    correct_capital = correct_state[1]
    possible_answers = get_random_choices(state, correct_capital)
    print(str(i+1) + ".", end = " ")
    answer = ask_question(correct_state, possible_answers)
    if possible_answers[answer] == correct_state[1]:
      print("Correct!\n")
      correct_answer += 1
    else:
      print("Incorrect! The correct answer is:", correct_state[1], "\n")
  print("End of test. You got " + str(correct_answer) + " correct.")


main()