import random
write = 0
head = 0

monetary_surface = ["Head" , "Write"]
thrownmoney = int(input("Enter the number of times you want to toss the coin:"))
while thrownmoney > 0:
  money = random.choice(monetary_surface)
  if money  == "Head":
    head +=1
    print("Hade comed")
  else:
    write += 1
    print("I swear, it really came up Tails—seriously, I mean it, it came up Tails. Believe me, it didn't come up anything else. I'm telling you, it really came up TAILSSSSSSSSSSSSS!! You have to take a picture of this moment, get your camera ready right now—COME ONNNNNNNNNNNNNNNNNNNNNN, what are you waiting for? Look, it really came up Tails, not Heads—Tails!!")

  thrownmoney -=1
print(f"Write Number: {write}\n Head Number: {head}")
