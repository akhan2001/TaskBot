import React, { useState, useEffect } from 'react';
import api from '../services/api'; // 后端 API 服务

function HomePage() {
  const [tasks, setTasks] = useState([]); // 保存任务列表
  const [loading, setLoading] = useState(true); // 加载状态
  const [selectedTask, setSelectedTask] = useState(null); // 当前选中的任务
  const [advice, setAdvice] = useState(''); // 保存生成的建议

  useEffect(() => {
    async function fetchTasks() {
      try {
        const response = await api.getTasks();
        setTasks(Array.isArray(response) ? response : []); // 确保 tasks 是数组
      } catch (error) {
        console.error("Failed to fetch tasks:", error);
      } finally {
        setLoading(false);
      }
    }
    fetchTasks();
  }, []);

  const handleGenerateAdvice = async (task) => {
    setSelectedTask(task); // 设置当前选中的任务
    setAdvice('Loading advice...'); // 显示加载提示

    try {
      const response = await api.getSuggestion(task.title, task.notes); // 调用后端 /suggestions API
      setAdvice(response.suggestion); // 设置生成的建议
    } catch (error) {
      console.error("Failed to generate advice:", error);
      setAdvice('Failed to generate advice. Please try again.');
    }
  };

  const handleCloseAdvice = () => {
    setSelectedTask(null); // 关闭建议窗口
    setAdvice(''); // 清空建议
  };

  if (loading) return <p>Loading tasks...</p>;

  return (
    <div>
      <h1>Your Tasks</h1>
      <ul>
        {tasks.map((task, index) => (
          <li key={index}>
            <h3>{task.title}</h3>
            <p>{task.notes}</p>
            <button onClick={() => handleGenerateAdvice(task)}>Generate Advice</button> {/* 添加按钮 */}
          </li>
        ))}
      </ul>

      {selectedTask && (
        <div className="advice-modal">
          <div className="advice-content">
            <h2>Advice for: {selectedTask.title}</h2>
            <p>{advice}</p>
            <button onClick={handleCloseAdvice}>Close</button>
          </div>
        </div>
      )}
    </div>
  );
}

export default HomePage;
