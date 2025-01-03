# E-Commerce Project

## Backend Repository

### Overview
This repository contains the backend code for the e-commerce application. Built with Django, it manages the application logic, API endpoints, and server-side processing.

### Technologies Used
- **Framework**: Django
- **Purpose**: Manages the server-side logic and communication between the frontend and database.
- **Database**: MySQL
- **Purpose**: Stores user data, product details, orders, and other e-commerce-related information.

### Features (Current)
- API endpoints for secure communication with the frontend.
- Database integration for e-commerce data management.

### Installation and Setup
#### Prerequisites
- Python (v3.8 or later)
- MySQL (v8 or later)

#### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/MegaBeing/ecom-backend.git
    ```
2. Navigate to the backend directory:
    ```bash
    cd ecom-backend
    ```
3. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Apply migrations:
    ```bash
    python manage.py migrate
    ```
6. Start the development server:
    ```bash
    python manage.py runserver
    ```

### Database Setup
1. Ensure MySQL is installed and running.
2. Create a new database:
    ```sql
    CREATE DATABASE Ecom;
    ```
---
