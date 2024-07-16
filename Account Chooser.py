import subprocess
import pyperclip

def main():
    title_command = 'title Account Chooser - by elevenxyz'
    subprocess.call(title_command, shell=True)
   
    print("Choose an account:")
    print("- 1: Account 1")
    print("- 2: Account 2")
    print("- 3: Account 3")
    print(" ")
    choice = input("Enter a number (1-3): ")

    if choice == '1':
        pyperclip.copy('username:password')
        print("Copied '1. Account' to clipboard.")

    elif choice == '2':
        pyperclip.copy('username:password')
        print("Copied '2. Account' to clipboard.")

    elif choice == '3':
        pyperclip.copy('username:password')
        print("Copied '3. Account' to clipboard.")
    else:
        print("Invalid choice. Please run the program again and enter a number from 1 to 3.")

if __name__ == "__main__":
    main()

