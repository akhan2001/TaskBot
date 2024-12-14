import React, { useState, useEffect } from 'react';
import api from '../services/api'; // 后端 API 文件

function HomePage() {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchTasks() {
      try {
        const response = await api.getTasks(); // 调用后端 /tasks API
        setTasks(response); // 保存任务数据
      } catch (error) {
        console.error("Failed to fetch tasks:", error);
      } finally {
        setLoading(false); // 设置加载完成状态
      }
    }
    fetchTasks();
  }, []);

  if (loading) return <p>Loading tasks...</p>;

  return (
    <div>
      <h1>Your Tasks</h1>
      <ul>
        {tasks.map((task, index) => (
          <li key={index}>
            <h3>{task.title}</h3>
            <p>{task.notes}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default HomePage;
