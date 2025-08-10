# 💬 Flask Chat App
## 📌 Overview

This is a **real-time chat application** built with **Flask**, **Flask-SocketIO**, and **SQLAlchemy**.
It supports **user registration**, **login**, and **live chat** with custom avatars.
Messages are stored in a database, and all connected users can see them instantly.

## ✨ Features
- 📝 **User Registration & Login** – Secure account creation and authentication.

- 💬 **Real-Time Chat** – Messages appear instantly for all connected users.

- 🖼 **Automatic Avatars** – Each user gets a random avatar on joining.

- 📜 **Message History** – Past chat messages are stored and can be viewed.

- 🔐 **Secure Passwords** – Passwords are hashed for security.

## 🏗 How It Works
### 1. User Accounts
- Users register with a username and password.

- Passwords are securely stored using hashing.

- Authentication is handled via Flask-Login.

### 2. Real-Time Messaging
- Flask-SocketIO handles live updates.

- When a user sends a message:

- It’s saved to the database.

- It’s broadcast to all connected clients instantly.

### 3. Avatars
- Each user gets a random avatar generated from:

    `https://avatar.iran.liara.run/public/{gender}?username={username}`

- Gender is randomly assigned as "boy" or "girl".

### 4. Message History
- Stored in the `ChatMessage` table.

- Accessible via `/chat_history` in JSON format.

## 🚀 Getting Started
### 1. Clone the Repository

`git clone https://github.com/yourusername/chat-app.git`

`cd chat-app`

### 2. Install Dependencies

`pip install -r requirements.txt`

### 3. Set Up Environment Variables

Create a .env file:

`SECRET_KEY=your_secret_key`

`DATABASE_URL=sqlite:///chat.db1`

### 4. Initialize the Database

`flask db upgrade`

### 5. Run the Application

`flask run`

Visit: http://localhost:5000

### 📌 Usage
- Register or log in with your username & password.

- Start chatting — messages appear instantly for everyone.

- Avatars and usernames are visible next to each message.

- Open multiple browser tabs to simulate multiple users.

### 🛠 Tech Stack
- Backend: Flask, Flask-SocketIO, Flask-Login, SQLAlchemy

- Frontend: HTML, CSS, JavaScript

- Database: SQLite (default) or PostgreSQL/MySQL

- Avatars: Iran Liara avatar API