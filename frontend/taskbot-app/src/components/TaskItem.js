import React from 'react';

function TaskItem({ task, onClick }) {
  return (
    <div className="task-item" onClick={onClick}>
      <h3>{task.title}</h3>
      <p>{task.notes || '没有备注信息'}</p>
    </div>
  );
}

export default TaskItem;
