import React, { useState, useEffect } from 'react';
import api from '../services/api';

function HomePage() {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedTask, setSelectedTask] = useState(null);
  const [advice, setAdvice] = useState('');

  useEffect(() => {
    async function fetchTasks() {
      try {
        const response = await api.getTasks();
        setTasks(Array.isArray(response) ? response : []);
      } catch (error) {
        console.error("Failed to fetch tasks:", error);
      } finally {
        setLoading(false);
      }
    }
    fetchTasks();
  }, []);

  const handleGenerateAdvice = async (task) => {
    setSelectedTask(task);
    setAdvice('Loading advice...');

    try {
      const response = await api.getSuggestion(task.title, task.notes);
      setAdvice(response.suggestion);
    } catch (error) {
      console.error("Failed to generate advice:", error);
      setAdvice('Failed to generate advice. Please try again.');
    }
  };

  const handleCloseAdvice = () => {
    setSelectedTask(null);
    setAdvice('');
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
            <button onClick={() => handleGenerateAdvice(task)}>Generate Advice</button> {/* add button */}
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
