def flames_game(name1, name2):
    # Convert names to lowercase and remove spaces
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()

    # Remove common letters
    for char in name1[:]:
        if char in name2:
            name1 = name1.replace(char, "", 1)
            name2 = name2.replace(char, "", 1)

    total_count = len(name1) + len(name2)

    if total_count == 0:
        return "Not compatible! Single forever </3"

    flames = ["Friendship", "Love", "Affection", "Marriage", "Enemy", "Sibling"]
    idx = 0
    while len(flames) > 1:
        idx = (idx + total_count - 1) % len(flames)
        flames.pop(idx)

    return flames[0]


# Main Program
if __name__ == "__main__":
    name1 = input("Enter your name: ")
    name2 = input("Enter partner's name: ")
    result = flames_game(name1, name2)
    print("Relationship Result:", result)
