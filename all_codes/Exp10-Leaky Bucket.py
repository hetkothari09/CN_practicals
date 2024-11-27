
storage = 0


no_of_queries = 4


bucket_size = 10


input_pkt_size = 4


output_pkt_size = 1
for i in range(0, no_of_queries): 

    size_left = bucket_size - storage
    if input_pkt_size <= size_left:
      
        storage += input_pkt_size
    else:
        print("Packet loss = ", input_pkt_size)

    print(f"Buffer size= {storage} out of bucket size = {bucket_size}")

    
    storage -= output_pkt_size


