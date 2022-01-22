"""
Name(s): Joshua Chong and Ethan Wang
Name of Project: Hangman
"""
import random
import wordlist
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

while 1 == 1:
  print("CS-9 Final Project: Hangman\nBy: Joshua Chong and Ethan Wang")
  word = random.choice(wordlist.wordlist)

  alreadyGuessed = []

  win = False

  numberOfGuesses = 7

  underscores = []

  print("Word:")
  for i in range (0, len(word)):
    print("_", end = " ")
    underscores.insert(0,'_ ')

  list(word)

  while numberOfGuesses > 0: 
    guessedLetter = input("\nEnter a guess: ")
    guessedLetter = guessedLetter.lower()
    for i in range(len(underscores)):
      if guessedLetter == word[i]:
        underscores[i] = guessedLetter + ' '
    if guessedLetter not in word:
      numberOfGuesses = numberOfGuesses - 1
      print("That letter is not in the word")

    newString = ''

    newString = newString.join(underscores)
    print(newString)
    if guessedLetter == "":
      print("Please enter a letter:")
    elif len(guessedLetter) !=1:
      print("Please enter one letter only:")
      numberOfGuesses += 1
    elif guessedLetter not in 'abcdefghijklmnopqrstuvwxyz':
      print("Please enter a letter:")
      numberOfGuesses += 1
    elif guessedLetter in alreadyGuessed:
      if guessedLetter in word:
        print("You've already guessed that letter: ")
      elif guessedLetter not in word:
        print("You've already guessed that letter: ")
        numberOfGuesses += 1
    alreadyGuessed.insert(0, guessedLetter)
    print("Guesses left: " + str(numberOfGuesses))
    if '_' not in newString:
      print("Congratulations! You have guessed the word!")
      break

  if numberOfGuesses == 0:
    print("You lose!")
    print("The word was: " + word)

  playAgain = input("Do you want to play again? ")
  playAgain.lower()

  while playAgain not in ['yes', 'no']:
      print("Please type 'yes' or 'no': ")
      playAgain = input("Do you want to play again? ")
      playAgain = playAgain.lower()
  if playAgain == 'yes':
    clearConsole()
  elif playAgain == 'no':
    break

