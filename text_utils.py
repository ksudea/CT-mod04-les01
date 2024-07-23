def reverse_string(s):
    # function to reverse a string
    s_list = list(s)
    reverse_s = []
    for i in range(len(s_list)-1, -1, -1):
        reverse_s.append(s_list[i])
    return "".join(reverse_s)

def capitalize_string(s):
    # function to capitalize a string
    if s.isupper() or s.isnumeric():
        return s
    return s.capitalize()