#!/usr/bin/python3
# function that divides element by element 2 lists.
def list_division(my_list_1, my_list_2, list_length):
    divisionList = []

    for i in range(list_length):
        try:
            list_elem = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            list_elem = 0
        except ZeroDivisionError:
            print("division by 0")
            list_elem = 0
        except IndexError:
            print("out of range")
            list_elem = 0
        finally:
            divisionList.append(list_elem)
    return divisionList
