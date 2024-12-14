import React from 'react';
import TaskItem from './TaskItem';

function TaskList({ tasks, onTaskClick }) {
  return (
    <div>
      {tasks.map((task) => (
        <TaskItem
          key={task.title} // 使用任务标题作为唯一标识（需要确保标题唯一）
          task={task}
          onClick={() => onTaskClick(task)} // 点击任务时触发回调
        />
      ))}
    </div>
  );
}

export default TaskList;
