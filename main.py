from checker import get_phone_number_info

def main():
    # Get phone number input from user
    phone_number_input = input("Enter a phone number: ")

    # Remove spaces from the phone number input
    phone_number_input = phone_number_input.replace(" ", "")

    # Use the checker module to retrieve information
    get_phone_number_info(phone_number_input)

if __name__ == "__main__":
    main()
