const API_BASE_URL = 'http://localhost:5000'; // 后端地址

async function getTasks() {
  const response = await fetch(`${API_BASE_URL}/tasks`);
  return response.json();
}

async function sendEmail(taskSuggestions) {
  const response = await fetch(`${API_BASE_URL}/email`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ task_suggestions: taskSuggestions }),
  });
  return response.json();
}

export default { getTasks, sendEmail };
