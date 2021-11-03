import re

def extract_contacts(text_data):
    """
    Extracts phone numbers and email addresses from a text file, reformats them, and removes duplicates.
    If the phone number is missing the area code, default one is added instead.
    The function a file for extracted phone numbers and another for emails.

    Arguments:
    text_data: text file path

    Return: None
    """
    # Reading Data File

    with open(text_data, "r") as f:
        raw_data = f.read()

    phone_directory = []
    default_area_code = "206-"

    # Extracting Phone Numbers

    phone_match_nac_format_1 = re.findall('\d{10}', raw_data)
    phone_match_nac_format_2 = re.findall('\(\d{3}\)\d{3}[-.]\d{4}', raw_data)
    phone_match_nac_format_3 = re.findall('\d{3}[-.]\d{3}[-.]\d{4}', raw_data)
    # phone_match_nac_format_4 = re.findall('\d{3}[-.]\d{2}[-.]\d{4}', raw_data)

    phone_match_area_code_format_1 = re.findall('\d{3}[-.]\d{3}[-.]\d{3}[-.]\d{4}', raw_data)
    phone_match_area_code_format_2 = re.findall('[+]\d{1}[-.]\d{3}[-.]\d{3}[-.]\d{4}', raw_data)

    # Reformatting Phone Numbers
    
    for number in phone_match_nac_format_1:
        number = default_area_code + number[:3] + "-" + number[3:6] + "-" + number[6:]
        phone_directory.append(number)

    for number in phone_match_nac_format_2:
        number = default_area_code + number[1:4] + "-" + number[5:8] + "-" + number[9:]
        phone_directory.append(number)  

    for number in phone_match_nac_format_3:
        number = default_area_code + number
        phone_directory.append(number)

    # NOTE: THIS FORMAT DOES NOT MATCH THE REST OF THE PHONE NUMBERS FORMATS (ONE DIGIT LESS)

    # for number in phone_match_nac_format_4:
    #     number = default_area_code + number[4:6] + "-" + number[:3] + "-" + number[7:]
    #     phone_directory.append(number)    


    for number in phone_match_area_code_format_1:
        number = number
        phone_directory.append(number)

    for number in phone_match_area_code_format_2:
        number = "00" + number[1:]
        phone_directory.append(number)

    # Removing Duplicates and Sorting

    phone_directory = list(set(phone_directory))
    phone_directory.sort()

    # Writing New Phones Text File

    with open("phone_numbers.txt", "w+") as f:
        for number in phone_directory:
            number = number + '\n'
            f.write(number)


    # Extracting e-mails

    email_directory =re.findall('[\w\-\.]+@+[\w\-\.]+\w', raw_data)

    # Removing Duplicates and Sorting

    email_directory = list(set(email_directory))
    email_directory.sort()

    # Writing e-mails Text File

    with open("emails.txt", "w+") as f:
        for email in email_directory:
            email = email + '\n'
            f.write(email)


# Running the module and invoking ihe function

# if __name__ == "__main__":


#     extract_contacts("assets/potential-contacts.txt")