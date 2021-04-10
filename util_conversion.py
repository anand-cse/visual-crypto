def decimal_to_binary(n, cols=8):
    """
    Gives a vector of binary numbers
    return vector is of size 8 by default and of cols if provided
    """
    res = [int(i) for i in bin(n)[2:]]
    if len(res)==cols:
        return res 
    elif len(res)<cols:
        l=cols-len(res)
        for i in range(l):
            res.insert(0,0)
        return res

def binary_to_decimal(bin_list):
    """
    Given a binary list
    returns an integert corresponding to it
    """
    res = int("".join(str(x) for x in bin_list), 2)
    return res

if __name__ == "__main__":
    print(decimal_to_binary(234,8))
    print(binary_to_decimal([0, 1, 1, 1]))