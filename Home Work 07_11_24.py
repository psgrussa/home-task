print('сколько пар вы хотите ввести?')
mass = list(map(int, input().split(" ")))
para1 = [mass[0], mass[1]]
para2 = [mass[2], mass[3]]
para3 = [mass[4], mass[5]]
para4 = [mass[6], mass[7]]
para5 = [mass[8], mass[9]]
para1.sort()
para2.sort()
para3.sort()
para4.sort()
para5.sort()
para1_max = para1[1]
para2_max = para2[1]
para3_max = para3[1]
para4_max = para4[1]
para5_max = para5[1]
max = para1_max + para2_max + para3_max + para4_max + para5_max
max_2 = [para1_max, para2_max, para3_max, para4_max, para5_max]
if max%3 == 0:
   print(max)
elif max%3 != 0:
    max_2.sort()
    print(max-max_2[0])