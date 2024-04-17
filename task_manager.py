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
