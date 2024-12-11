class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def print_info(self):
        print(f"员工名字：{self.name}, 工号：{self.id}")
class FullTimeEmployee(Employee):
    def __init__(self, name, id, monthly_salry):
        super().__init__(name, id)
        self.monthly_salry = monthly_salry
    def calulate_monthly_pay(self):
        return self.monthly_salry
class PartTimeEmployee(Employee):
    def __init__(self, name, id, daily_salary, work_days):
        super().__init__(name, id)
        self.daily_salary = daily_salary
        self.work_days = work_days
    def calulate_daily_pay(self):
        return self.daily_salary * self.work_days

zhangsan = FullTimeEmployee("张三", "1001",6000)
zhangsan.print_info()
print(f"工资：{zhangsan.calulate_monthly_pay()}")
lisi = PartTimeEmployee("李四", "1002",230,15)
lisi.print_info()
print(f"工资：{lisi.calulate_daily_pay()}")