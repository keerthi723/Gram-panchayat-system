# Gram Panchayat E-Services System

A web application built using Python and Flask to digitize and manage the core services of a Gram Panchayat. The system allows villagers to interact with the Panchayat office digitally—register complaints, apply for schemes, pay fines, and receive updates. It also enables the PDO (Panchayat Development Officer) to manage all citizen-related activities online.

# Features

-  **Complaint Registration** – Users can file complaints and check their status.
-  **Scheme Application** – Citizens can apply for eligible government schemes.
-  **Fine Payments** – View and pay pending fines online.
-  **Notice Board** – View public announcements and circulars.
-  **PDO Dashboard** – Panchayat Development Officer can manage all requests.
-  **Authentication System** – Secure login for users, PDOs, and admins.
-  **Admin Panel** – Admin can monitor user activities and oversee the system.

---

# Tech Stack

| Layer        | Technology                 |
|--------------|----------------------------|
| Frontend     | HTML, CSS, JavaScript      |
| Backend      | Python with Flask Framework|
| Database     | MySQL (via XAMPP)          |
| Server       | Localhost (XAMPP Apache)   |
| Dev Tools    | VS Code, Git, GitHub       |

---

# Project Structure
Gram-panchayat-system/
│
├── static/ # Static assets (CSS, JS, images)
├── templates/ # HTML templates (Flask Jinja2)
├── .gitignore # Git ignored files/folders
├── home.py # Main application logic
├── ar_master.py # Sub module logic
├── test.py # For testing purposes
├── Pipfile # Python dependencies
├── python_digital_gram_panchayat.sql # Database structure
├── python_digital_gram_panchayat.doc # Project documentation
└── README.md # Project info


---

# Installation Guide

## Step 1: Clone the Repository

```bash
git clone https://github.com/keerthi723/Gram-panchayat-system.git
cd Gram-panchayat-system
```
## Step 2: Set Up Python Environment
```
pip install flask mysql-connector-python
```
## Step 3: Set Up MySQL Database

- Launch XAMPP and start Apache and MySQL.
- Open http://localhost/phpmyadmin.
- Create a database named:
  ```
  gram_panchayat
  ```
-Import the SQL file:

   - python_digital_gram_panchayat.sql

# Step 4: Run the Application
 ```
 python home.py
```
Developer
Keerthiga P
🎓 B.E. CSE - J.P.R. Institute of Technology
📧 Email: keerthiga342@gmail.com
🌐 GitHub: keerthi723




