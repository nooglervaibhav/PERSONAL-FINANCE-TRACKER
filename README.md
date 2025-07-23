# PERSONAL-FINANCE-TRACKER


A Django-based web application to help users manage their personal finances efficiently. Users can track their income, expenses, and savings goals in a modern, visually appealing dashboard.

## 🚀 Features

- 📥 Add income and expense entries with categories
- 📈 Real-time graph visualization of finances
- 🎯 Set and manage savings goals
- 🔄 Reset/clear fields instantly
- 📊 Animated dashboard using JavaScript
- ✅ Clean, card-style responsive UI (Tailwind CSS)

## 🛠️ Tech Stack

| Layer      | Technology              |
|------------|--------------------------|
| Frontend   | HTML, Tailwind CSS, JavaScript |
| Backend    | Django (Python)          |
| Database   | SQLite (local dev)       |
| Charting   | Chart.js                 |

## 📂 Project Structure

```bash
PersonalFinanceTracker/
├── finance_tracker/        # Django project settings
├── tracker/                # Main app (models, views, templates)
│   ├── static/             # CSS, JS, chart config
│   └── templates/          # HTML templates
├── db.sqlite3              # Local database
└── manage.py               # Django manager
