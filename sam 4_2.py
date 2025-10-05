import random


def dice_game():
    dice_value = random.randint(1, 6)

    print(f"Выпало: {dice_value}")

    if dice_value == 5 or dice_value == 6:
        print("Вы победили")
    elif dice_value == 3 or dice_value == 4:
        dice_game()
    elif dice_value == 1 or dice_value == 2:
        print("Вы проиграли")


if __name__ == "__main__":
    dice_game()
