dx = input("请输入你的基本工资（底薪）：")
dx = float(dx)
cq = input("请输入出勤天数（法定为21.75天）:")
cq = float(cq)
s = dx/21.75/8
p = input("请输入平时加班数（1.5倍）:")
p = float(p)
z = input("请输入周末加班数（2.0倍）:")
z = float(z)
r = input("请输入节日加班数（3.0倍）:")
r = float(r)
j = input("请输入其他加项（奖金）：")
j = float(j)
f = input("请输入其他减项（罚款）:")
f = float(f)

if dx != "" and cq != "":
    xz = (s * cq * 8) + (s * p * 1.5) + (s * z *2.0) + (s * r * 3.0) + j - f
print("你本月的工资为：",'%.2f' % xz)
