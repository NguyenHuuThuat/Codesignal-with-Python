def solution(picture):
    h_0 = len(picture)   
    w_0 = len(picture[0]) 

    for i in range(0, h_0):
        picture[i] = '*' + picture[i] + '*'

    h_1 = len(picture)   
    w_1 = len(picture[0]) 

    add_str = '*' * w_1

    picture.insert(0, add_str)
    picture.insert(h_1+1, add_str)

    return picture

        



picture = ["abc",
           "ded"]

# p = '*' + picture[0] + '*'
# h_0 = len(picture)   
# w_0 = len(picture[0]) 

# print(h_0, w_0)

p = solution(picture)
print(p)