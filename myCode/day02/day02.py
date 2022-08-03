# a=int(input("a= "))
# b=int(input("b="))
# print(a+b)
#
# f=float(input("输入摄氏度："))
# print("华氏度是："+str(f*1.8+32))


year=int(input("输入年份判断闰年："))
is_leap=year%4==0 and year%100!=0 or year%400==0
print(is_leap)