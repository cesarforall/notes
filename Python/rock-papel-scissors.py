import random
import os

options = ('piedra', 'papel', 'tijeras')
rounds = 1
user_wins = 0
computer_wins = 0

while True:
  print('-' * 20)
  print('ROUND', rounds)
  print('-' * 20)
  print('User wins: ', user_wins)
  print('Computer wins: ', computer_wins)
  
  user_option = input('piedra, papel o tijeras: ').lower()
  computer_option = random.choice(options)
  
  print('User option =>', user_option)
  print('Computer option =>', computer_option)
  
  if not user_option in options:
    print(f"{user_option} no es una opción válida")
  
  if user_option == computer_option:
    print('Empate')
  elif user_option == 'piedra':
    if computer_option == 'papel':
      print('papel gana a piedra')
      print('computer ganó!')
      computer_wins += 1
    else:
      print('piedra gana a tijeras')
      print('user ganó!')
      user_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('user ganó!')
      user_wins += 1
    else:
      print('piedra gana a tijeras')
      print('computer ganó!')
      computer_wins += 1
  elif user_option == 'tijeras':
    if computer_option == 'piedra':
      print('piedra ganaa tijeras')
      print('computer ganó!')
      computer_wins += 1
    else:
      print('tijeras ganan a papel')
      print('user ganó!')
      user_wins += 1

  rounds += 1
  
  if computer_wins == 2:
    print('Computer wins!')
    break
    
  if user_wins == 2:
    print('User wins!')
    break