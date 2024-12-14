const API_BASE_URL = 'http://localhost:5000'; // 后端地址

async function getTasks() {
  const response = await fetch(`${API_BASE_URL}/tasks`);
  if (!response.ok) {
    console.error("Failed to fetch tasks:", response.statusText);
    return [];
  }
  return response.json();
}

async function getSuggestion(title, notes) {
  const response = await fetch(`${API_BASE_URL}/suggestions`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title, notes }),
  });
  if (!response.ok) {
    console.error("Failed to fetch suggestion:", response.statusText);
    throw new Error('Failed to fetch suggestion');
  }
  return response.json();
}

export default { getTasks, getSuggestion };
