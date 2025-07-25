import time
import random
import textwrap

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an easy to learn, powerful programming language.",
    "Practice makes perfect.",
    "Typing speed is a useful skill.",
    "Stay focused and keep improving."
]

def start_game():
    print("\nWelcome to the Typing Speed Game!")
    input("Press Enter to begin...")

    sentence = random.choice(sentences)
    print("\nType the following:\n")
    print(textwrap.fill(sentence, width=60))
    print()

    input("Press Enter when you're ready to start...")
    start_time = time.time()
    typed = input("\nStart typing: \n")
    end_time = time.time()

    time_taken = end_time - start_time
    words = len(sentence.split())
    wpm = round(words / (time_taken / 60), 2)

    correct_chars = sum(1 for a, b in zip(typed, sentence) if a == b)
    accuracy = round((correct_chars / len(sentence)) * 100, 2)

    print(f"\n⏱️ Time Taken: {round(time_taken, 2)} seconds")
    print(f"💨 Words per Minute (WPM): {wpm}")
    print(f"🎯 Accuracy: {accuracy}%")

    if input("\nPlay again? (y/n): ").lower() == 'y':
        start_game()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    start_game()
