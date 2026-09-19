import random

heads = 0
tails = 0

coin_sides = ["Heads", "Tails"]

tosses = int(input("Enter the number of times you want to toss the coin: "))

while tosses > 0:
    coin = random.choice(coin_sides)

    if coin == "Heads":
        heads += 1
        print("Heads came up!")
    else:
        tails += 1
        print("I swear, it really came up Tails—seriously, I mean it, it came up Tails. Believe me, it didn't come up anything else. I'm telling you, it really came up TAILSSSSSSSSSSSSS!! You have to take a picture of this moment, get your camera ready right now—COME ONNNNNNNNNNNNNNNNNNNNNN, what are you waiting for? Look, it really came up Tails, not Heads—Tails!!")

    tosses -= 1

print(f"Heads Number: {heads}\nTails Number: {tails}")
