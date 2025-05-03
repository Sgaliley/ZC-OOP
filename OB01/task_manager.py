class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"[{status}] {self.description} (До: {self.deadline})"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
        else:
            print("Неверный номер задачи.")

    def show_current_tasks(self):
        print("\nТекущие задачи:")
        current_tasks = [task for task in self.tasks if not task.completed]
        if not current_tasks:
            print("Нет невыполненных задач.")
        else:
            for i, task in enumerate(current_tasks):
                print(f"{i+1}. {task}")
