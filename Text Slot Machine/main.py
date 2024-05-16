import random
import requests

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100
ROWS = 3
COLS = 3


symbolCount = {"A":2,
                "B":4, 
                "C":6, 
                "D":8}

symbolValue = {"A":5,
                "B":4, 
                "C":3, 
                "D":2}

def checkWinnings(columns, lines, bet, values):
      winnings = 0
      winningLines = []
      for line in range(lines):
            symbol = columns[0][line]
            for column in columns:
                  symbolChecking = column[line]
                  if symbol != symbolChecking:
                        break
            else:
                  winnings += values[symbol] * bet
                  winningLines.append(line + 1)

      return winnings, winningLines

def slotMachineSpin(rows, cols, symbols):
      #First
      all_symbols = []
      for symbol, symbolCount in symbols.items():
            for _ in range(symbolCount):
                  all_symbols.append(symbol)

      my_columns = []
      for _ in range(cols):
            my_col = []
            current_symbols = all_symbols[:]
            for _ in range(rows):
                  value = random.choice(current_symbols)
                  current_symbols.remove(value)
                  my_col.append(value)
      
            my_columns.append(my_col)
      
      return my_columns

def print_slot_machine(columns):
      for row in range(len(columns[0])):
            for i, column in enumerate(columns):
                  if i != len(columns) - 1:
                        print(column[row], end=" | ")
                  else:
                        print(column[row], end="")

            print()

def deposit():
    while True:
                amount = input("How much would you like to deposit?>>")
                if amount.isdigit():
                        amount = int(amount)
                        if amount > 0:
                            break
                        else:
                            print("Amount required to be greater than 0.")
                else:
                    print("Please enter a number.")
    return amount

def getLinesNumber():
      while True:
            lines = input("Enter the number of lines to bet on (1 - "+ str(MAX_LINES) +" lines)>>")
            if lines.isdigit():
                  lines = int(lines)
                  if 1 <= lines <= MAX_LINES:
                        break
                  else:
                        print("Lines required to be greater than 0 and lesser than "+ str(MAX_LINES) +".") 
            else:
                  print("Please enter a number.")
      return lines

def getBet():
      while True:
            bet = input("Enter the amount you want to bet on each line>>")
            if bet.isdigit():
                  bet = int(bet)
                  if MIN_BET <= bet <= MAX_BET:
                        break
                  else:
                        print(f"Lines required to be {MIN_BET} at least and {MAX_BET} at most.") 
            else:
                  print("Please enter a number.")
      return bet

def game(balance):
      lines = getLinesNumber()
      while True:
            bet= getBet()
            totalBet=bet*lines

            if totalBet > balance:
                  print(f"You don't have enough to bet, your balance is: {balance}$")
            else:
                  break
            
      print(f"You are betting {bet}$ on {lines} lines. Total bet is equal to {totalBet}$")

      slots = slotMachineSpin(ROWS, COLS, symbolCount)
      print_slot_machine(slots)
      winnings, winningLines = checkWinnings(slots, lines, bet, symbolValue)
      print(f"You won {winnings}$ on", *winningLines)
      return winnings - totalBet

def main():
      print("Hello :=)")
      balance = deposit()   
      while True:
            print(f"Current balance is {balance}$")
            spin = input("Press 'ENTER' to play. Press 'q' to quit. >>")
            if spin == "q":
                  print("Thank you for playing, please have a nice day and bet responsibly :=)")
                  break
            
            balance += game(balance)
      

main()                          