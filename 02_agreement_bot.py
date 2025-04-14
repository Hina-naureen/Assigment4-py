def main():
    print("\033[1;34m🐾 Welcome to the Animal Picker! 🐾\033[0m\n")

    animal = input("\033[1;3m✨ What's your favorite animal? ✨\033[0m ")

    # Trim input and check for empty input
    animal = animal.strip()
    if not animal:
        print("\033[1;31m⚠️ You didn't enter anything. Please try again!\033[0m")
        return

    print(f"\n\033[1;32mAwesome! My favorite animal is also \033[1;4m{animal}\033[0m\033[1;32m! 🐶🐱🦁\033[0m")


if __name__ == '__main__':
    main()
