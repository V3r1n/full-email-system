# Email Ticketing System

This is a web-based email ticketing system, similar to OTRS, designed to manage customer support requests that come in via email. It allows teams to handle high volumes of inbound emails by converting them into tickets and organizing them in a shared system.

## Features

Currently, the project has the following features implemented:

*   **User Authentication:** Users can log in, log out, and change their password.
*   **Custom User Model:** The system collects the user's name, email, and phone number.
*   **Database Models:** Core models for `User`, `Queue`, and `Ticket` are defined.
*   **Admin Interface:** A ready-to-use admin panel to manage users, queues, and tickets.
*   **Basic Structure:** A solid foundation based on the Django web framework.

### Planned Features

The following features are planned for future development:
*   Email fetching to automatically create tickets from emails.
*   Dashboard with statistics for admins and authorized users.
*   Advanced search functionality for tickets.
*   Ticket filtering by status and assigned user.
*   Dark/Light mode toggle.

## Technology Stack

*   **Backend:** Python with the Django Framework
*   **Database:** SQLite (for development)

## Setup and Installation

To get the project up and running on your local machine, follow these steps:

1.  **Clone the repository:**
    ```sh
    git clone <repository-url>
    cd full-email-system
    ```

2.  **Create a virtual environment:**
    It's recommended to use a virtual environment to manage project-specific dependencies.
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    Install all the required packages from the `requirements.txt` file.
    ```sh
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    This will create the necessary tables in your database.
    ```sh
    python manage.py migrate
    ```

5.  **Create a superuser:**
    To access the admin panel, you need to create a superuser account.
    ```sh
    python manage.py createsuperuser
    ```
    Follow the prompts to create your admin user.

6.  **Run the development server:**
    ```sh
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000`. You can access the admin panel at `http://127.0.0.1:8000/admin`.