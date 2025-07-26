# 👨‍💼 Employee Management System

A responsive web application to manage employees using **CRUD operations** (Create, Read, Update, Delete) built with **Django** and **Python**.

This project helps organizations or teams keep track of employee details in a user-friendly, web-based interface.

---

## 🚀 Features

- Add new employees
- View a list of all employees
- Edit/update employee details
- Delete employee records
- Responsive design (works on desktop & mobile)
- Built with Django's powerful admin & template system

---

## 🧰 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS (Bootstrap for responsiveness), JavaScript
- **Database:** SQLite (default for Django, can be replaced)
- **Tools:** VS Code, Git

---

## 📥 Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/employee-management-system.git
cd employee-management-system
```
### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv env
source env/bin/activate      # Linux/macOS
env\Scripts\activate         # Windows
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Start the development server
```bash
python manage.py runserver
```
Then open your browser and go to: http://localhost:8000

## 🛠️ Example Features

- Add Employee: Fill a form to add name, role, department, etc.
- Update Employee: Edit details through a simple UI
- Delete Employee: Remove a record with confirmation
- List Employees: View all records with a responsive table

## 📜 License
This project is open source and available under the MIT License.
