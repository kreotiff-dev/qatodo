const form = document.querySelector('#add_task_form');
const titleInput = document.querySelector('#taskInput');
const descriptionInput = document.querySelector('#descriptionInput');
const taskList = document.getElementById('taskList');


form.addEventListener('submit', (event) => {
  event.preventDefault();

  fetch('/add_task', {
    method: 'POST',
    body: new FormData(form),
  })
    .then((response) => {
      if (response.status === 200) {
        console.log('Task added successfully!');
        form.reset();
        taskList.appendChild(li);
        // window.location.reload(); // Динамическое обновление страницы
      } else {
        console.error('There was an error adding the task:', response);
      }
    })
    .catch((error) => {
      console.error('There was an error adding the task:', error);
    });

     // Функция для добавления новой задачи в список
   function addTask(taskText) {
       const li = document.createElement('li');
       li.innerHTML = `
           ${taskText}
           <button class="delete-button">Delete</button>
       `;
       taskList.appendChild(li);
   }
});


//document.addEventListener('DOMContentLoaded', async function() {
//  const addTaskForm = document.getElementById('add_task_form');
//  const taskList = document.getElementById('taskList');
//  const taskInput = document.getElementById('taskInput');
//  const descriptionInput = document.getElementById('descriptionInput');
//
//  // Функция для добавления задачи
//  addTaskForm.addEventListener('submit', async function(event) {
//    event.preventDefault();
//    const taskInputValue = taskInput.value;
//    const descriptionInputValue = descriptionInput.value;
//    if (taskInputValue.trim() !== '' && descriptionInputValue.trim() !== '') {
//      await addTask(taskInputValue, descriptionInputValue);
//      addTaskForm.reset();
//
//      // Отправляем данные на сервер
//      const response = await fetch('/add_task', {
//        method: 'POST',
//        headers: {
//          'Content-Type': 'application/json'
//        },
//        body: JSON.stringify({
//          title: taskInputValue,
//          description: descriptionInputValue
//        })
//      });
//      if (!response.ok) {
//        console.error('Error:', response.status);
//      }
//    }
//  });
//
//    // Функция для удаления задачи
//    taskList.addEventListener('click', function(event) {
//        if (event.target.tagName === 'BUTTON') {
//            const taskItem = event.target.parentElement;
//            if (event.target.classList.contains('delete-button')) {
//                taskItem.remove();
//            }
//        }
//    });
//

//});