import random
# This is a simple coin flip game.
heads = 0
tails = 0
# I think Ctrl+C is the standard way to stop a loop in Python.
while True:
    try:
        input("Press Enter to flip the coin (or Ctrl+C to stop): ")
    except KeyboardInterrupt:
        print("\nGame stopped.")
        break
# Flip the coin
    coin = random.choice(["Heads", "Tails"])
    print("You got:", coin)
# Update the score
    if coin == "Heads":
        heads += 1
    else:
        tails += 1
# Print the current score
    print("Score → Heads:", heads, "| Tails:", tails)
