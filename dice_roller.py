import random
def main():
  dice_rolls = 2
  dice_sum = 0
  for i in range(0, dice_rolls):
    roll = random.randint(1,6)
    dice_sum += roll
    if roll == 1 : 
      print('You rolled a', roll, " gamer fail")
    elif roll == 6:
      print("You rolled a", roll, " gamer success")
    else:
      print("you rolled a", roll)
    print("you have rolled total of", dice_sum)
if __name__== "__main__":
  main()
