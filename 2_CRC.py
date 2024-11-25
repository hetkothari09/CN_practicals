def division(divisor, dividend):
    # Copy divisor and dividend to avoid modifying the original
    dividend = dividend[:]
    divisor = divisor[:]
    
    # Length of divisor
    n = len(divisor)
    
    # Initialize quotient
    quotient = []
    
    # Perform division
    for i in range(len(dividend) - n + 1):
        # If the current bit is 1, perform XOR
        if dividend[i] == '1':
            quotient.append('1')
            for j in range(n):
                dividend[i + j] = str(int(dividend[i + j]) ^ int(divisor[j]))
        else:
            quotient.append('0')
    
    # Remainder is the last `n-1` bits of the dividend
    remainder = dividend[-(n - 1):]
    return quotient, remainder


def encode_message(data,divisor):
    n=len(divisor)-1

    temp_processed_data=data+n*[0]
    quotient,remainder=division(divisor,temp_processed_data)

    transmitted_message=data+remainder[-n:]
    return transmitted_message


def decode_message(received_data,divisor):
    n=len(divisor)
    quotient,remainder=division(divisor,received_data)
    decoding_result=int(''.join(remainder))
    if(decoding_result==0):
        print("You got the correct message 🥳!!!!")
    else:
        print("message has been manipulated 💀👽!!!!!")
        print(f"quotient:{quotient},remainder:{remainder}")


def crc():
    data=list(input("Enter data:"))
    divisor_sender=list(input("Enter divisor:").lstrip('0'))

    
    transmitted_message=encode_message(data,divisor_sender)
    print(f'transmitted message: {transmitted_message}')

    received_message=list(input("Enter the received message:"))
    divisor_receiver=list(input("Enter divisor:").lstrip('0'))
    decode_message(received_message,divisor_receiver)


crc()   