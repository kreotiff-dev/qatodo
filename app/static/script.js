const form = document.querySelector('#add_task_form');
const taskList = document.getElementById('taskList');
const editButtons = document.querySelectorAll('.editButton');
const deleteButtons = document.querySelectorAll('.deleteButton');

// Динамическое добавление новой задачи
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
        window.location.reload(); // обновление страницы
      } else {
        console.error('There was an error adding the task:', response);
      }
    })
    .catch((error) => {
      console.error('There was an error adding the task:', error);
    });
});

//   // Модальное окно редактирования задачи
// editButtons.forEach(button => {
//     // Добавляем обработчик события для нажатия кнопки
//     button.addEventListener('click', () => {
//         // Получаем id задачи из атрибута data-task-id кнопки
//         const taskId = button.getAttribute('data-task-id');
//
//         // Отправляем GET-запрос на сервер для получения данных задачи по её id
//         fetch(`/get_task/${taskId}`)
//             .then(response => response.json())
//             .then(data => {
//                 // Заполняем форму редактирования данными задачи
//                 document.getElementById('editTaskInput').value = data.title;
//                 document.getElementById('editTaskDescription').value = data.description;
//
//                 // Открываем модальное окно с формой редактирования
//                 document.getElementById('editTaskForm').style.display = 'block';
//             })
//             .catch(error => console.error('Error:', error));
//     });
// });
// Обработчик события для кнопки "Сохранить" в модальном окне редактирования задачи
document.getElementById('editForm').addEventListener('submit', (event) => {
    event.preventDefault();

    // Получаем данные из формы
    const title = document.getElementById('editTaskInput').value;
    const description = document.getElementById('editTaskDescription').value;

    // Отправляем POST-запрос на сервер для обновления задачи
    fetch(`/edit_task/${taskId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `title=${encodeURIComponent(title)}&description=${encodeURIComponent(description)}`
    })
        .then(response => {
            if (response.status === 200) {
                console.log('Task updated successfully!');
                window.location.reload(); // обновление страницы
            } else {
                console.error('There was an error updating the task:', response);
            }
        })
        .catch(error => console.error('There was an error updating the task:', error));
});
// Обработчик события для кнопки "Редактировать" в модальном окне редактирования задачи
document.getElementById('editTaskForm').addEventListener('click', (event) => {
    if (event.target === document.getElementById('cancelEditButton')) {
        // Закрываем модальное окно
        document.getElementById('editTaskForm').style.display = 'none';
    }
});