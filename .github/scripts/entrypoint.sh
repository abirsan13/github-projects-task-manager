
#!/bin/bash

set -e

echo "Starting Python Task Manager..."

echo "Running unit tests..."
python3 .github/scripts/todo-test.py

echo "Generating HTML report..."
./.github/scripts/update_index.sh

echo "Task Manager completed successfully."
