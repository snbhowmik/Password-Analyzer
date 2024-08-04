def analyze_password(password):
    length_ok = len(password) >= 8
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special_char = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_special_char = True

    score = sum([length_ok, has_uppercase, has_lowercase, has_digit, has_special_char])
    strength = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]

    print(f"Password: {password}")
    print("Analysis:")
    print(f" - Length >= 8: {'✔️' if length_ok else '❌'}")
    print(f" - Contains uppercase letter: {'✔️' if has_uppercase else '❌'}")
    print(f" - Contains lowercase letter: {'✔️' if has_lowercase else '❌'}")
    print(f" - Contains digit: {'✔️' if has_digit else '❌'}")
    print(f" - Contains special character: {'✔️' if has_special_char else '❌'}")
    print(f"Overall Strength: {strength[score-1]}")

if __name__ == "__main__":
    while True:
        print("\nPassword Analyzer Tool")
        print("1. Analyze a password")
        print("2. Exit")

        choice = input("Choose an option (1/2): ")

        if choice == '1':
            password = input("Enter the password to analyze: ")
            analyze_password(password)

        elif choice == '2':
            print("Exiting the tool.")
            break

        else:
            print("Invalid option, please try again.")