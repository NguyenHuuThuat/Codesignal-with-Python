
def solution(s1, s2):
    
    common_char = ""
    for i in s1:
        if i not in common_char:
        
            i_in_s1 = s1.count(i)
            i_in_s2 = s2.count(i)
        
            comm_num = []
            comm_num.append(i_in_s1)
            comm_num.append(i_in_s2)
        
            comm_i = min(comm_num)
            new_char = i * comm_i
            common_char += new_char
    
  
    return len(common_char)

s1 = "aabcc"
s2 = "adcaa"
sol = solution(s1, s2)
print(sol)