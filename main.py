def create_cats_dic(number):
    result = {}
    for i in range(1, number+1):
        result[i] = False
    return result

def go_round(num_circles, number_of_cats):
    cats_dic = create_cats_dic(number_of_cats)
    for i in range(1, num_circles+1):
        for j in range(1, number_of_cats+1, i):
            if cats_dic[j] == False:
                cats_dic[j] = True
            else:
                cats_dic[j] = False
    return cats_dic

result = go_round(100,100)
for cat,value in result.items():
    if value == True:
        print(f'Cat # {cat} is in hat')

