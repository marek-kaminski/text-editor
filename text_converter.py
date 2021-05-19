
def backend():
    user_input = (str.lower(input("podaj słowa ")))
    # user_input = ("marek, gun,sen  alicja\nania, konik\nwa'ga")
    user_input_modify = user_input.replace(", ", "|").replace(",", "|").replace('\n', '|').replace("  ", "|").replace(" ", "|")
    # print(user_input_modify)
    user_input_dec = int(input("podaj tryb "))

    attribute_string = "AttributesContain["
    item_name_string = "item_name"
    bullet_point_string = "bullet_point"
    product_description_string = "product_description"

    end_syntax = 1
    if user_input_dec == 1:
        end_syntax = attribute_string + item_name_string + ":" + user_input_modify + "]"
    elif user_input_dec == 2:
        end_syntax = attribute_string + item_name_string + "|" + bullet_point_string + ":" + user_input_modify + "]"
    elif user_input_dec == 3:
        end_syntax = attribute_string + item_name_string + "|" + bullet_point_string + "|" + product_description_string + ":" + user_input_modify + "]"

    # end_syntax = attribute_string + item_name_string + "|" + bullet_point_string + product_description_string + ":" + user_input_modify + "]"

    print(end_syntax)


