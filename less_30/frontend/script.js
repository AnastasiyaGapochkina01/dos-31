const API_BASE = "http://backend:8080/api";

async function fetchNotes() {
  const res = await fetch(`${API_BASE}/notes`);
  const data = await res.json();
  renderNotes(data);
}

function toLocalInputValue(isoString) {
  if (!isoString) return "";
  const d = new Date(isoString);
  const off = d.getTimezoneOffset();
  const local = new Date(d.getTime() - off * 60 * 1000);
  return local.toISOString().slice(0, 16);
}

function fromLocalInputValue(val) {
  if (!val) return "";
  const d = new Date(val);
  return d.toISOString();
}

function renderNotes(notes) {
  const container = document.getElementById("notes");
  container.innerHTML = "";
  notes.forEach((n) => {
    const div = document.createElement("div");
    div.className = "note";

    const header = document.createElement("div");
    header.className = "note-header";

    const title = document.createElement("div");
    title.className = "note-title";
    title.textContent = n.title;

    if (n.is_completed) {
      title.style.textDecoration = "line-through";
      title.style.opacity = "0.7";
    }

    const actions = document.createElement("div");
    actions.className = "note-actions";

    const toggleBtn = document.createElement("button");
    toggleBtn.className = "complete";
    toggleBtn.textContent = n.is_completed ? "Снять" : "Готово";
    toggleBtn.onclick = () => toggleComplete(n);

    const deleteBtn = document.createElement("button");
    deleteBtn.className = "delete";
    deleteBtn.textContent = "Удалить";
    deleteBtn.onclick = () => deleteNote(n.id);

    actions.appendChild(toggleBtn);
    actions.appendChild(deleteBtn);

    header.appendChild(title);
    header.appendChild(actions);

    const content = document.createElement("div");
    content.textContent = n.content;

    const meta = document.createElement("div");
    meta.style.fontSize = "12px";
    meta.style.opacity = "0.8";
    let metaText = `Создано: ${new Date(n.created_at).toLocaleString()}`;
    if (n.reminder_at) {
      metaText += ` | Напоминание: ${new Date(n.reminder_at).toLocaleString()}`;
    }
    meta.textContent = metaText;

    div.appendChild(header);
    div.appendChild(content);
    div.appendChild(meta);

    container.appendChild(div);
  });
}

async function createNote(e) {
  e.preventDefault();
  const title = document.getElementById("title").value.trim();
  const content = document.getElementById("content").value.trim();
  const reminderInput = document.getElementById("reminder").value;

  if (!title) return;

  await fetch(`${API_BASE}/notes`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      title,
      content,
      reminder_at: fromLocalInputValue(reminderInput),
    }),
  });

  document.getElementById("note-form").reset();
  fetchNotes();
}

async function toggleComplete(note) {
  await fetch(`${API_BASE}/notes/${note.id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      is_completed: !note.is_completed,
    }),
  });
  fetchNotes();
}

async function deleteNote(id) {
  await fetch(`${API_BASE}/notes/${id}`, {
    method: "DELETE",
  });
  fetchNotes();
}

document.getElementById("note-form").addEventListener("submit", createNote);

fetchNotes();

