# python tutorial 
Question 1: 
#题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
d=[]
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i != j) and (i != k) and (j != k):
                d.append([i,j,k])
                print(i,j,k)
print('Number :', len(d))

Question 2:
#题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，
超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

def get_bonus(i):
    bonus = 0
 
    if i <= 10:
        bonus = i * 0.1
   
    elif i <= 20 and i > 10:
        bonus = (i - 10) * 0.075 + get_bonus(10)
   
    elif i <= 40 and i > 20:
        bonus = (i - 20) * 0.05 + get_bonus(20)
   
    elif i <= 60 and i > 40:
        bonus = (i - 40) * 0.03 + get_bonus(40)
   
    elif i <= 100 and i > 60:
        bonus = (i - 60) * 0.015 + get_bonus(60)
   
    else:
        bonus = (i - 100) * 0.01 + get_bonus(100)

    return bonus
    #close the loop

print("profits:", i)
print("bonus:", get_bonus(i/10000) * 10000)

Question 3:
