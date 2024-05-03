import csv


def intro():
  print(
      'Welcome to the Spanish and French tranlator app.\nPlease enter an English word and press the "Enter" key.'
  )
  print('\nType "done" at any time to exit')


def exit():
  print('\nThanks for using the tranlator app. Have a great day!')


translations = {}

with open("translations.csv", "r") as words:
  reader = csv.DictReader(words, delimiter=",")
  for line in reader:
    english = line["English"].lower()
    spanish = line["Spanish"].lower()
    french = line["French"].lower()
    translations[english] = [spanish, french]

done = False

intro()

while not done:
  word = input(
      "\nType in an English word to translate to Spanish and French: ")
  word = word.lower()
  if word == "done":
    done = True
  elif word in translations:
    print(f'\nSpanish: {translations[word][0]}')
    print(f'\nFrench: {translations[word][1]}')
  else:
    print("\nThe translation for that word is unkown")

exit()
