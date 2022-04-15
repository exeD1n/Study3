def thesaurus(*names):

    names_dict_list = dict()

    for name in names:
        first_letter = name[0].upper()
        names_dict_list[first_letter] = names_dict_list.setdefault(first_letter, []) + [name.capitalize()]
        
    return names_dict_list


if __name__ == "__main__":
    print(thesaurus("Майа", "Дарси", 'Макс', "Никита", "женя"))