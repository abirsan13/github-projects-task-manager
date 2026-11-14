
#!/bin/bash

set -e

# Run the Python task manager and save its output
python3 .github/scripts/todo.py > /tmp/task_manager_output.txt

# Update the HTML report using the task manager output
python3 - <<'PY'
from pathlib import Path
from html import escape

output = Path("/tmp/task_manager_output.txt").read_text()

todo_tasks = []
done_tasks = []
current_section = None

for line in output.splitlines():
    line = line.strip()

    if line == "ToDo Tasks:":
        current_section = todo_tasks
    elif line == "Done Tasks:":
        current_section = done_tasks
    elif line.startswith("- ") and current_section is not None:
        current_section.append(line[2:])

def create_list(tasks):
    if not tasks:
        return "<li>No tasks found.</li>"

    return "\n".join(
        f"<li>{escape(task)}</li>" for task in tasks
    )

index_path = Path("index.html")
html = index_path.read_text()

todo_html = create_list(todo_tasks)
done_html = create_list(done_tasks)

html = html.replace(
    '<ul id="todo-tasks">\n            <li>Tasks will appear here after the report is generated.</li>\n        </ul>',
    f'<ul id="todo-tasks">\n{todo_html}\n        </ul>'
)

html = html.replace(
    '<ul id="done-tasks">\n            <li>Completed tasks will appear here after the report is generated.</li>\n        </ul>',
    f'<ul id="done-tasks">\n{done_html}\n        </ul>'
)

index_path.write_text(html)
print("HTML report updated successfully.")
print(f"ToDo tasks: {len(todo_tasks)}")
print(f"Done tasks: {len(done_tasks)}")
PY
