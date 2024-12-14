import React, { useState, useEffect } from 'react';
import api from '../services/api'; // 调用后端 API

function SuggestionModal({ task, onClose }) {
  const [suggestion, setSuggestion] = useState('正在加载建议...');

  useEffect(() => {
    async function fetchSuggestion() {
      try {
        const response = await api.getSuggestion(task.title, task.notes);
        setSuggestion(response.suggestion);
      } catch (error) {
        console.error("获取建议时出错:", error);
        setSuggestion("无法加载建议，请稍后重试。");
      }
    }
    fetchSuggestion();
  }, [task]);

  return (
    <div className="modal">
      <div className="modal-content">
        <h2>Task: Suggestions of {task.title}</h2>
        <p>{suggestion}</p>
        <button onClick={onClose}>Close</button>
      </div>
    </div>
  );
}

export default SuggestionModal;
