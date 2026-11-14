import unittest
from todo import Task, TaskPool


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.task = Task("Test task", "This is a test task")
        self.task_pool = TaskPool()

    def test_task_initial_status(self):
        self.assertEqual(self.task.status, "ToDo")

    def test_mark_task_done(self):
        self.task.mark_done()
        self.assertEqual(self.task.status, "Done")

    def test_add_task(self):
        self.task_pool.add_task(self.task)
        self.assertEqual(len(self.task_pool.tasks), 1)

    def test_complete_task(self):
        self.task_pool.add_task(self.task)
        result = self.task_pool.complete_task("Test task")

        self.assertTrue(result)
        self.assertEqual(self.task.status, "Done")

    def test_complete_nonexistent_task(self):
        result = self.task_pool.complete_task("Unknown task")
        self.assertFalse(result)

    def test_get_tasks_by_status(self):
        self.task_pool.add_task(self.task)
        self.task.mark_done()

        completed_tasks = self.task_pool.get_tasks_by_status("Done")
        self.assertEqual(len(completed_tasks), 1)


if __name__ == "__main__":
    unittest.main()