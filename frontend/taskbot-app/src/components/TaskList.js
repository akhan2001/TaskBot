import React from 'react';
import TaskItem from './TaskItem';

function TaskList({ tasks, onTaskClick }) {
  return (
    <div>
      {tasks.map((task) => (
        <TaskItem
          key={task.title}
          task={task}
          onClick={() => onTaskClick(task)}
        />
      ))}
    </div>
  );
}

export default TaskList;
