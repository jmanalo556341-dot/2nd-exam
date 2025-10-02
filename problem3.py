import random

def lottery_game():
    # Generate 6 unique winning numbers (1 to 60)
    winning_numbers = random.sample(range(1, 61), 6)
    winning_numbers.sort()

    # Player input
    print("🎰 Welcome to the 6/60 Lottery Game 🎰")
    player_numbers = []

    while len(player_numbers) < 6:
        try:
            num = int(input(f"Enter number {len(player_numbers)+1} (1-60): "))
            if num < 1 or num > 60:
                print("⚠️ Number must be between 1 and 60.")
            elif num in player_numbers:
                print("⚠️ You already picked that number.")
            else:
                player_numbers.append(num)
        except ValueError:
            print("⚠️ Invalid input, enter a number.")

    player_numbers.sort()

    # Check matches
    matches = set(player_numbers) & set(winning_numbers)
    match_count = len(matches)

    # Prize calculation
    if match_count == 6:
        prize = 1_000_000
    else:
        prize = match_count * 1000

    # Results
    print("\n===== LOTTERY RESULTS =====")
    print("Winning Numbers :", winning_numbers)
    print("Your Numbers    :", player_numbers)
    print("Matched Numbers :", sorted(matches))
    print(f"Total Matches   : {match_count}")
    print(f"🎉 Your Prize    : ₱{prize:,}")

# Run the game
if __name__ == "__main__":
    lottery_game()
