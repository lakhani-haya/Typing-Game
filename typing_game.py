import time
import random
import textwrap

sentences = {
    "easy": [
        "The cat sat on the mat and took a nap.",
        "I love pizza and ice cream on sunny days.",
        "Dogs are fun pets to have at home.",
        "Books help us learn new things every day.",
        "Music makes me happy when I feel sad.",
        "The sun is bright and warm today."
    ],
    "medium": [
        "The quick brown fox jumps over the lazy dog while wearing sunglasses.",
        "Pizza is the answer to all of life's problems, especially on Monday morning.",
        "Cats secretly rule the world from their cardboard box headquarters.",
        "I tried to catch some fog earlier, but I mist completely!",
        "Coffee is just bean soup that makes you vibrate with productivity.",
        "My keyboard is fluent in typos and autocorrect disasters."
    ],
    "hard": [
        "Why do programmers prefer dark mode? Because light attracts bugs & debugging sessions!",
        "The wifi password is 'P@ssw0rd123!' - hidden in the most obvious place, naturally.",
        "Unicorns use Python because it's the most magical programming language (definitely not C++).",
        "Time flies like an arrow; fruit flies like a banana smoothie at 3:14 AM.",
        "My computer has a sense of humor - it laughs at my code errors & syntax mistakes.",
        "Dancing penguins make the best debugging partners, obviously (trust me on this one)."
    ]
}

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
