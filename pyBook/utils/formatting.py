

# TODO implement this properly
# can probably be more robust
def title(title_string):
    print(title_string)

    # to lower all chars
    lower_case_title = title_string.lower()
    print(lower_case_title)

    # capatolize first word in string
    lower_case_title = lower_case_title[0].upper() + lower_case_title[1:]
    print(lower_case_title)

    # split title into a list of its words
    words = lower_case_title.split()

    formatted_title_string = ""
    for word in words:
        if (word != "the") or (word != "a"):
            formatted_title_string += word[0].upper() + word[1:] + " "

    return formatted_title_string[0:-1]


# formats the title into a sort title
# TODO could probably be more robust
def sort_title(title_string):
    if str(title_string[:4]).lower() == str('the ').lower():
        return str(title_string[4:]).lower()
    if str(title_string[:2]).lower() == str('a ').lower():
        return str(title_string[2:]).lower()
    return str(title_string).lower()

