name = input("What is your name?")
while True:
    language = input("What is your favourite language? (Type exit to stop): ")

    if language.lower() == "exit":
        print("Goodbye!")
        break

    language_lower = language.lower()
    if language_lower == "python":
        choice = "Great choice!"
    elif language_lower == "java":
        choice = "Very enterprise of you."
    else:
        choice = "Nice!"

    print(f"Hi {name}, I see that you like {language}. {choice}")
