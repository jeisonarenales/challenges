def solution(n)->int:
    n_bin = to_bin(n)
    if n_bin.count('1') == len(n_bin):
        return 0
    else:
        zero_max = 0
        count = 0
        for i in n_bin:
            if i == '1':
                if zero_max < count:
                    zero_max = count
                count = 0
            else:
                count +=1 
        
        return zero_max

def to_bin(n)->str:
    return bin(n).replace("0b","")
