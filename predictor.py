import random


def generating_randomness(num=100):
    number_list = []
    while len(number_list) < num:
        user_input = input("Print a random string containing 0 or 1:\n\n")
        number_list.extend(list(user_input))
        number_list = [i for i in number_list if i == "0" or i == "1"]
        if len(number_list) < num:
            print(f"Current data length is {len(number_list)}, {num - len(number_list)} symbols left")
        else:
            print("Final data string:")
            print("".join(number_list))
            print()
            print("You have $1000. Every time the system successfully predicts your next press, you lose $1.")
            print('Otherwise, you earn $1. Print "enough" to leave the game. Let\'s go!\n')
    money = 1000
    checking = ["000", "001", "010", "011", "100", "101", "110", "111"]
    temp_dict = {i: [0, 0] for i in checking}
    checking = ["".join(number_list)[i:i+4] for i in range(len("".join(number_list)))]
    checking = [i for i in checking if len(i) == 4]
    for i in checking:
        for j in temp_dict.keys():
            if i[:3] == j:
                if i[-1] == "0":
                    temp_dict[j][0] += 1
                else:
                    temp_dict[j][-1] += 1

    string_for_guess = input("Print a random string containing 0 or 1:\n")
    while string_for_guess != "enough":
        if len(string_for_guess) == len([i for i in string_for_guess if i == "1" or i == "0"]):
            print("prediction:")
            prediction = list("x" * len(string_for_guess))
            for i in range(3):
                prediction[i] = str(random.choice([0, 1]))
            for i in range(3, len(prediction)):
                reference = string_for_guess[(i-3):i]
                if temp_dict[reference][0] > temp_dict[reference][-1]:
                    prediction[i] = "0"
                elif temp_dict[reference][0] < temp_dict[reference][-1]:
                    prediction[i] = "1"
                else:
                    prediction[i] = str(random.choice([0, 1]))
            print("".join(prediction))
            print()
            correct = 0
            for i in range(3, len(prediction)):
                if prediction[i] == string_for_guess[i]:
                    correct += 1
                    money -= 1
                else:
                    money += 1
            correct_rate = round((correct / (len(prediction) - 3)) * 100, 2)
            print(f"Computer guessed right {correct} out of {len(prediction) - 3} symbols ({correct_rate} %)")
            print(f"Your capital is now ${money}")
            print()
            string_for_guess = input("Print a random string containing 0 or 1:\n")
        else:
            print()
            string_for_guess = input("Print a random string containing 0 or 1:\n")
    print("Game over!")


generating_randomness()
