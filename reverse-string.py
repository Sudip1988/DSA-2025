def reverse(input) :
    if is_valid_string(input) :
        output = []
        char_list = list(input)
        for i in range(len(char_list) -1, -1, -1) :
            print(char_list[i])
            output.append(char_list[i])
        print(''.join(output))
        
        


def is_valid_string(input):
    if input is None:
        return False
    return isinstance(input, str)


reverse('Mouma Banerjee')
