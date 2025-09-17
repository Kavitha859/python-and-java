import random
import json
import os

# List of words
WORDS = [
    "python", "computer", "library", "programming", "challenge",
    "science", "internet", "keyboard", "screen", "college",
    "student", "teacher", "notebook", "project", "learning"
]

# File to save high scores
SCORE_FILE = "highscores.json"

def load_scores():
    """Load high score from file"""
    if os.path.exists(SCORE_FILE):
        try:
            with open(SCORE_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            # If file is corrupted, reset it
            return {"high_score": 0}
    return {"high_score": 0}

def save_scores(scores):
    """Save high score to file"""
    with open(SCORE_FILE, "w") as f:
        json.dump(scores, f)

def scramble(word):
    """Scramble the letters of a word"""
    letters = list(word)
    random.shuffle(letters)
    return ''.join(letters)

def play_round():
    """Play one round of the game"""
    word = random.choice(WORDS)
    scrambled = scramble(word)
    print(f"\nUnscramble this word: {scrambled}")
    guess = input("Your guess: ").lower().strip()
    if guess == word:
        print("Correct!")
        return 1
    else:
        print(f"Wrong! The correct word was: {word}")
        return 0

def play_game():
    """Play the full game"""
    print("\n--- Welcome to Word Scramble ---")
    scores = load_scores()
    high_score = scores.get("high_score", 0)

    print(f"Current High Score: {high_score}")
    rounds = 5
    score = 0

    for r in range(1, rounds + 1):
        print(f"\nRound {r}/{rounds}")
        score += play_round()

    print(f"\nGame Over! Your score: {score}/{rounds}")

    if score > high_score:
        print("New High Score!")
        scores["high_score"] = score
        save_scores(scores)
    else:
        print("Try again to beat the high score!")

def main():
    """Main game loop"""
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != "y":
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
