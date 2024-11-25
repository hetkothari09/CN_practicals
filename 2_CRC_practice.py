def division(divisor, dividend):

    divisor = divisor[:]
    dividend = dividend[:]

    n = len(divisor)
    quotient = []

    for i in range(len(dividend) - n + 1):
        if(dividend[i]==1):
            quotient.append('1')
            for j in range(n):
                dividend[i+j] = str(int(dividend[i+j]) ^ int(divisor(j)))
        else:
            quotient.append('0')

    remainder = dividend[-(n-1):]

    return quotient, remainder

def encode_data(data, divisor):
    n = len(divisor) - 1
    new_data = data + n*[0]

    quotient, remainder = division(divisor, new_data)

    transmitted_data = data + remainder[-n:]

    return transmitted_data

def decode_data(data, divisor):
    n = len(divisor)

    quotient, remainder = division(divisor, data)

    remainder_data = int(''.join(remainder))

    if(remainder_data == 0):
        print("The transmitted data is perfectly fine.")
    else:
        print("The transmitted data was manipulated!")
        print(f"The quotient is : {quotient} and the remainder is : {remainder}")

def crc():
    data = list(input("Enter the data to be transmitted: "))
    divisor_sender = list(input("Enter the divisor: ").lstrip('0'))

    received_data = encode_data(data, divisor_sender)
    print(f"The received data is : {received_data}")

    data_received = list(input("Enter the received data: "))
    divisor_receiver = list(input("Enter the divisor: ").lstrip('0'))

    decode_data(data_received, divisor_receiver)


if __name__ == "__main__":
    crc()