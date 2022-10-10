def get_formatted_name(first, last, middle=''):
    """This function will return the formatted name."""
    if middle:
        formatted_name = first +" "+ middle +" "+ last
    else:
        formatted_name = first +" "+ last
    return (formatted_name.title())