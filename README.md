<img width="405" alt="login_chat" src="https://github.com/user-attachments/assets/f6217880-06a8-4a2c-ac2d-aa96b61849e1">
<img width="405" alt="chat_pic" src="https://github.com/user-attachments/assets/7524e303-2249-4a25-b5be-39b483c0aaf0">

# Live Chat Application

Welcome to the **Live Chat Application** built using Django! This project provides real-time messaging functionality, allowing users to engage in live conversations.

## Features

- Real-time messaging with multiple users
- Authentication and user registration
- Chat room creation and management
- Persistent chat history
- Notifications for new messages
- Responsive design, optimized for mobile and desktop
- Secure and scalable backend

## Technologies Used

- **Django 4.2.16** – Backend framework
- **Django Channels** – Enables real-time communication via WebSockets
- **Redis** – Used as the message broker for WebSocket handling
- **HTML5/CSS3/JavaScript** – Frontend technologies
- **SQLite** (or other database options) – Data storage
- **Docker** (Optional) – For containerization and easy deployment

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.9+
- Django 4.2.16+
- Redis (for WebSocket handling)
- Docker (Optional)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/live-chat-django.git
   cd live-chat-django
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**

   Run the migrations to set up the initial database schema.

   ```bash
   python manage.py migrate
   ```

5. **Start the Redis server:**

   Ensure Redis is running for WebSocket handling.

   ```bash
   redis-server
   ```

6. **Run the development server:**

   Start the Django development server to view the app in your browser.

   ```bash
   python manage.py runserver
   ```

### Access the Application

After running the server, open your web browser and navigate to:

```
http://127.0.0.1:8000/
```

## Usage

1. **Register or log in** to create an account.
2. **Join an existing chat room** or create a new one.
3. Start chatting in real-time with other users!
4. Messages are stored and can be viewed even after logging out.

## Docker Setup (Optional)

You can also run this application using Docker for easy deployment.

1. Build and run the application with Docker:

   ```bash
   docker-compose up --build
   ```

2. Visit the app at `http://localhost:8000/` in your browser.

## Contributing

Contributions to the project are welcome! Feel free to:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and submit a pull request.

If you encounter any issues or have suggestions, please open an issue.

## Acknowledgements

- Django framework
- Django Channels for WebSocket handling
- Redis for real-time messaging
- All contributors to this project
