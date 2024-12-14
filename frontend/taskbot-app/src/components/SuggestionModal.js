import React, { useState, useEffect } from 'react';
import api from '../services/api'; // 调用后端 API

function SuggestionModal({ task, onClose }) {
  const [suggestion, setSuggestion] = useState('正在加载建议...');

  useEffect(() => {
    async function fetchSuggestion() {
      try {
        const response = await api.getSuggestion(task.title, task.notes); // 调用后端建议 API
        setSuggestion(response.suggestion);
      } catch (error) {
        console.error("获取建议时出错:", error);
        setSuggestion("无法加载建议，请稍后重试。");
      }
    }
    fetchSuggestion();
  }, [task]); // 当 task 更新时重新获取建议

  return (
    <div className="modal">
      <div className="modal-content">
        <h2>任务: {task.title} 的建议</h2>
        <p>{suggestion}</p>
        <button onClick={onClose}>关闭</button>
      </div>
    </div>
  );
}

export default SuggestionModal;
