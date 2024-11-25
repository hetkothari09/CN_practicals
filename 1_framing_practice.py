def character_count():
    str_count = int(input("Enter the number of strings: "))
    final_str = ''

    for i in range(str_count):
        str_data = input(f"Enter string {i+1}: ")
        char_count = str(len(str_data)+1) + str_data
        final_str += char_count
    return final_str


def byte_stuffing():
    message = input("Enter the message to be transmitted: ")
    start_flag = input("Enter the start flag: ")
    end_flag = input("Enter the end flag: ")
    esc_character = input("Enter the escape character: ")
    final_message = ''
 
    # if start_flag in message:
    #     split_msg = message.split(sep=start_flag)
    #     new_msg = start_flag + split_msg[0] + esc_character + start_flag + split_msg[1] + end_flag
    #     print(new_msg)
    # elif end_flag in message:
    #     split_msg = message.split(sep=end_flag)
    #     new_msg = start_flag + split_msg[0] + esc_character + end_flag + split_msg[1] + end_flag
    #     print(new_msg)
    # else:
    #     final_message = start_flag + message + end_flag

    for i in range(0, len(message)):
        if(message[i] == start_flag or message[i] == end_flag):
            final_message += esc_character + message[i]
        else:
            final_message += message[i]
    
    new_msg = start_flag + final_message + end_flag
    
    return new_msg


def bit_stuffing():
    sequence = input("Enter the number sequence to be transmitted: ")
    count_ones = 0
    final = ''

    for i in sequence:
        if(i == 1):
            c+=1
        else:
            c=0
        final+=i
        if(c==5):
            final+='0'
            c=0
    return final 


if __name__ == "__main__":
    # print(character_count())
    # print(byte_stuffing())
    print(bit_stuffing())