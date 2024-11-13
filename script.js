function addTask() {
    const taskInput = document.getElementById("taskInput");
    const taskText = taskInput.value.trim();
    
    if (taskText === "") {
        alert("Please enter a task.");
        return;
    }

    const taskList = document.getElementById("taskList");
    const li = document.createElement("li");
    li.appendChild(document.createTextNode(taskText));
    const editButton = document.createElement("button");
    editButton.textContent = "Done"
    editButton.className = "done-btn"
    editButton.onclick = function() {
        taskList.textContent('li');
    };
    const deleteButton = document.createElement("button");
    deleteButton.textContent = "Delete";
    deleteButton.className = "delete-btn";
    deleteButton.onclick = function() {
        taskList.removeChild(li);
    };
    li.appendChild(editButton)
    li.appendChild(deleteButton);
    editButton.onclick = function() {
        li.classList.toggle("completed");
    };

    taskList.appendChild(li);
    taskInput.value = "";
}
