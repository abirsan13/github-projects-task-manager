class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.status = "ToDo"

    def mark_done(self):
        self.status = "Done"


class TaskPool:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_done()
                return True
        return False

    def get_tasks_by_status(self, status):
        return [task for task in self.tasks if task.status == status]

    def display_tasks(self):
        print("ToDo Tasks:")
        for task in self.get_tasks_by_status("ToDo"):
            print(f"- {task.title}: {task.description}")

        print("\nDone Tasks:")
        for task in self.get_tasks_by_status("Done"):
            print(f"- {task.title}: {task.description}")


if __name__ == "__main__":
    task_pool = TaskPool()

    task_pool.add_task(Task("Set up repository", "Create the GitHub repository"))
    task_pool.add_task(Task("Develop task manager", "Create the Python task manager"))
    task_pool.add_task(Task("Write unit tests", "Test the task manager functions"))
    task_pool.add_task(Task("Create HTML report", "Display tasks in a web page"))
    task_pool.add_task(Task("Build Docker image", "Package the application in Docker"))
    task_pool.add_task(Task("Configure GitHub Actions", "Automate the project workflow"))

    task_pool.complete_task("Set up repository")
    task_pool.complete_task("Develop task manager")
    task_pool.complete_task("Write unit tests")

    task_pool.display_tasks()