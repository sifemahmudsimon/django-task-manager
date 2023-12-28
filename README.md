# Task Manager App (Django)

The Task Manager App is a Django-based application designed to facilitate task organization and management. It provides a user-friendly interface to create, track, and manage tasks efficiently. Users can organize their tasks, set priorities, deadlines, and categorize them for better management.

## Features
- **User Registration,Login,Password Reset:** User can register, login & password reset with a confirmation link in email.
- **Task Creation:** Users can create tasks specifying details such as title, description, deadline, and priority.
- **Task Organization:** Tasks can be categorized, edited, and deleted for better organization.
- **Prioritization:** Ability to set task priorities to manage time effectively.
- **Deadline Tracking:** Keep track of deadlines to ensure timely task completion.
- **Date Created & Modified Time:** See the date of the task created & modified last time.
- **Task Filtere:** Task can be filtered by Title & Dropdown menu.
- **User-Friendly Interface:** Intuitive design for seamless task management.

## Getting Started

### Installation
1. Clone the repository using the terminal:
    ```
    git clone https://github.com/sifemahmudsimon/django-task-manager.git
    ```

### Usage
1. **Activate Virtual Environment:**
   - No need to navigate anywhere after clone
   - Activate the virtual environment:
     ```
     call "django-task-manager\task_manager(venv)\Scripts\activate.bat"
     ```

2. **Run the Project:**
   - Change directory to the project folder:
     ```
     cd django-task-manager\task_manager(venv)\task_manager
     ```
   - Start the Django development server:
     ```
     py manage.py runserver
     ```
   - Access the development server link displayed in the terminal
     ```
     Starting development server at http://127.0.0.1:8000/
     ```
     click on the link  http://127.0.0.1:8000/ from terminal or enter via a web browser.

## Username & Passwords
**Admin Pannel:**

- go to http://127.0.0.1:8000/admin page:
    
     ```
     Username : admin
     password : 123
     ```
**Other Users:**

| User | Username        | Password |
|------|-----------------|----------|
| 01   | sifemahmudsimon | 1111     |
| 02   | wazedali        | 1234     |
| 03   | tasnumpromi     | 0000     |

### Note
All the dependencies are already installed. if theres any problem occures during project run, Ensure that all dependencies are installed as per the project's requirements before executing the above steps.
