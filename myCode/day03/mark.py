marks = float(input("请输入成绩："))
mark = -1
if 0 <= marks <= 100:
    mark = marks
else:
    print("error")
    mark=-1

if mark >= 90:
    print("优")
if 80 <= mark < 90:
    print("良")
if 60 <= mark < 80:
    print("中")
if 0<=mark<60:
    print("不及格")
if mark==-1:
    print("error")