num_1 = [int(input())]
num_2 = [int(input())]
num_3 = [int(input())]
def srav():
 if num_1[0]>num_2[0] and num_1[0]>num_3[0]:
    print(num_1[0], 'самое большое')
 elif num_2[0]>num_1[0] and num_2[0]>num_3[0]:
    print(num_2[0], 'самое большое')
 elif num_3[0]>num_1[0] and num_3[0]>num_2[0]:
    print(num_3[0], 'самое большое')
srav()