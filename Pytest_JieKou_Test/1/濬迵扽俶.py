class People:
    # 类属性
    # 初始化方法
    def __init__(self, name, age, sex, monthly_salary):
        self.name = name
        self.age = age
        self.sex = sex
        # 月工资
        self.monthly_salary = monthly_salary

    # 年薪
    # 自定义方法
    def get_income(self):
        year_income = int(self.monthly_salary * 12)
        return year_income


# 实例化类
# p 对象具体
p = People("张女士", 26, "女", 1000)

# print(p.monthly_salary)


# 实例化对象p.属性名称的形式去获取
print(p.get_income())


