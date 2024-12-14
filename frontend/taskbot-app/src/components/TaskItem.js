import React from 'react';

function TaskItem({ task, onClick }) {
  return (
    <div className="task-item" onClick={onClick}>
      <h3>{task.title}</h3>
      <p>{task.notes || 'No notes'}</p>
    </div>
  );
}

export default TaskItem;
