class FlamesGame:
    def __init__(self, name1, name2):
        self.name1 = name1.replace(" ", "").lower()
        self.name2 = name2.replace(" ", "").lower()
        self.flames = ["Friendship", "Love", "Affection", "Marriage", "Enemy", "Sibling"]
    
    def remove_common_letters(self):
        for char in self.name1[:]:
            if char in self.name2:
                self.name1 = self.name1.replace(char, "", 1)
                self.name2 = self.name2.replace(char, "", 1)
    
    def calculate_result(self):
        total_count = len(self.name1) + len(self.name2)
        
        if total_count == 0:
            return "Not compatible! Single forever </3"
        
        idx = 0
        while len(self.flames) > 1:
            idx = (idx + total_count - 1) % len(self.flames)
            self.flames.pop(idx)
        
        return self.flames[0]
    
    def get_relationship_result(self):
        self.remove_common_letters()
        return self.calculate_result()


# Main Program
if __name__ == "__main__":
    name1 = input("Enter your name: ")
    name2 = input("Enter partner's name: ")
    
    flames_game = FlamesGame(name1, name2)
    result = flames_game.get_relationship_result()
    
    print("Relationship Result:", result)
