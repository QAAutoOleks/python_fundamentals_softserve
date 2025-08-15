initial_list = (
                ["red","green", "black", "red", "brown", 
                 "red", "blue", "red", "red", "yellow"]
            )

filtered_obj = filter(lambda x: x == 'red', initial_list)
print(list(filtered_obj))
