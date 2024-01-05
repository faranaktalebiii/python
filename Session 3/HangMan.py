import random

word_list = ["Benz", "Yellow", "Rice", "Zidan", "Ronaldo", "Messi", "AmirHossein"]
selected_word = random.choice(word_list).lower()
selected_len = len(selected_word)
print(selected_word)

correct_word = []
wrong_word = []
user_mistake = 0

while user_mistake < 6:
    for letter in selected_word:
        if letter in correct_word:
            print(letter, end=" ")
        else:
            print("_ ", end="")

    user_guess = input("Please Enter Your Character: ").lower()
    if len(user_guess) == 1 and user_guess.isalpha():
        if user_guess in selected_word:
            correct_word.append(user_guess)
            print("Yes")
            if len(correct_word) == selected_len:
                print("You Win! 👌")
                print(f"The correct word is: {selected_word.capitalize()}")
                break
        else:
            wrong_word.append(user_guess)
            print("No")
            user_mistake += 1
    else:
        print("Please Enter 1 Valid Character")

if user_mistake == 6:
    print("You Lose! 🫤")
