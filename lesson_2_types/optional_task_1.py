number = 5271

number_to_str = str(number)
product = (int(number_to_str[0])  
        *  int(number_to_str[1]) 
        *  int(number_to_str[2]) 
        *  int(number_to_str[3]))

reversed_string = number_to_str[::-1]
reversed_number = int(reversed_string)

sorted_list = sorted(number_to_str)
sorted_str = (sorted_list[0]
            + sorted_list[1]
            + sorted_list[2]
            + sorted_list[3]) 
sorted_number = int(sorted_str)