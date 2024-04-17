#First program
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: division by zero"

# Пример использования:
print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

choice = input("Введите номер операции (1/2/3/4): ")

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

if choice == '1':
    print("Результат:", add(num1, num2))
elif choice == '2':
    print("Результат:", subtract(num1, num2))
elif choice == '3':
    print("Результат:", multiply(num1, num2))
elif choice == '4':
    print("Результат:", divide(num1, num2))
else:
    print("Неверный ввод")

#Second program
class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
        else:
            print("Invalid task index")

    def display_tasks(self):
        print("Current tasks:")
        for i, task in enumerate(self.tasks):
            status = "✔️" if task.completed else "❌"
            print(f"{i + 1}. [{status}] {task.description}")

# Пример использования:
task_manager = TaskManager()
task_manager.add_task("Подготовить презентацию")
task_manager.add_task("Сделать покупки")
task_manager.display_tasks()
task_manager.mark_task_completed(0)
task_manager.display_tasks()