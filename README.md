# 🚀 FastAPI Kanban Task Manager

A lightweight Task Management API built with **FastAPI** and **Pydantic**.  
It manages tasks across board columns (ToDo, In Progress, Done) using a clean and efficient data architecture.

---

## ✨ Features

- Create tasks with descriptions and priority levels (1–3)  
- Filter tasks using query parameters  
- View tasks by column (`/tasks/ToDo`, `/tasks/InProgress`, etc.)  
- Move tasks between columns with validation  
- Clear all completed tasks from the "Done" column  

---

## 🧠 Key Concepts

### Single Source of Truth (SSOT)
All tasks are stored in a single dictionary, with each task carrying its own state (column).  
This avoids data duplication and keeps the system consistent.

### API Design
- **Path Parameters** → Identify specific resources (e.g., task ID)  
- **Query Parameters** → Enable filtering (e.g., priority)  
- **Request Bodies** → Validated using Pydantic models  

### Efficient Data Handling
Used dictionary iteration (`.items()`) to work with task IDs and data safely and efficiently.

---

## 🛠️ Challenges & Lessons

- **Return inside loops:** Learned to collect results first and return after processing  
- **Data type mismatches:** Fixed using FastAPI type hints (e.g., `task_id: int`)  
- **HTTP 204 responses:** Understood that "No Content" must return an empty response  

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/fastapi-kanban.git
cd fastapi-kanban
```

### 2. Install dependencies
```bash
pip install fastapi uvicorn
```

### 3. Run the server
```bash
uvicorn main:app --reload
```

### 4. Open API Docs
Visit: http://127.0.0.1:8000/docs

---

## 📌 Notes
- Main application file: `main.py`  
- Built as part of backend learning focused on API design and data handling  
