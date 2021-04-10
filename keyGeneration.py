import numpy as np

def generate_key(n, msg):
    msg_list = msg.split(" ")
    user_key=[]
    for ele in msg_list: 
        user_key.extend(ord(num) for num in ele)
    
    size_user_key=len(user_key)
    
    key = np.zeros(n, dtype=np.uint8)
    index=0
    for index in range(n):
        index_user_key=index%size_user_key
        key[index]=(((((index^user_key[index_user_key])%256)**2)%256)^index)%256
    
    return key