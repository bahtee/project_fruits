def get_cheapest_fruit_id(data:str)->id:
    """
    This function returns the index of the cheapest fruit in the list

    args:
        data: CSV file with the fruits data
    returns:
        name of the cheapest fruit
    """
    # your code here
    return data

data = open("fruits.csv","r", encoding='utf8' ).read()
print(get_cheapest_fruit_id(data))
