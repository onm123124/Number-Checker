import phonenumbers
from phonenumbers import carrier

def get_phone_number_info(phone_number_str):
    try:
        # Parse the phone number
        phone_number = phonenumbers.parse(phone_number_str)

        # Check if the phone number is valid
        if phonenumbers.is_valid_number(phone_number):
            # Format the phone number in international format
            formatted_number = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

            # Get carrier information
            carrier_name = carrier.name_for_number(phone_number, "en")

            # Get region information
            region_code = phonenumbers.region_code_for_number(phone_number)

            # Print the information
            print("Phone Number:", formatted_number)
            print("Is Valid:", "Yes")
            print("Carrier:", carrier_name)
            print("Region Code:", region_code)

        else:
            print("Invalid phone number")

    except phonenumbers.NumberParseException as e:
        print(f"Error parsing phone number: {e}")


