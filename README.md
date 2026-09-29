  # 💙 A Circle Of Care

### 🤝 AI-Powered Family Communication & Support Platform

**A Circle Of Care** is an AI-powered web application built with **Django** to strengthen family communication and create a supportive environment for family members.

The platform combines **structured feedback, AI-powered chatbot assistance, and supportive suggestions** to encourage better communication and understanding within families.

---

## ✨ Key Features

* 🤖 **AI Chatbot** — AI-powered chatbot assistance for users.
* 💬 **Family Feedback** — Share feedback and thoughts to improve communication.
* 💡 **Supportive Suggestions** — Receive helpful suggestions based on user interactions.
* 👨‍👩‍👧‍👦 **Family-Centered Platform** — Designed to encourage healthy communication among family members.
* 🔐 **User Authentication** — Secure user registration and login functionality.
* 🗄️ **Database Integration** — Efficient storage and management of application data.
* 📱 **Responsive Interface** — User-friendly interface across different screen sizes.

---

## 🛠️ Tech Stack

| Technology                | Purpose                         |
| ------------------------- | ------------------------------- |
| 🐍 **Python**             | Core programming language       |
| 🌐 **Django**             | Backend web framework           |
| 🎨 **HTML / CSS**         | Frontend development            |
| ⚡ **JavaScript**          | Interactive functionality       |
| 🤖 **Google Gemini API**  | AI chatbot and AI assistance    |
| 🗄️ **SQLite / Database** | Data storage                    |
| 🔐 **Python dotenv**      | Environment variable management |

---

## 📂 Project Structure

```text
A_Circle_Of_Care/
│
├── manage.py
├── requirements.txt
├── .env
│
├── project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── ...
│
├── templates/
│   └── ...
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── README.md
```

> **Note:** The exact folder structure may vary depending on your Django project configuration.

---

# 🚀 Installation & Setup

Follow the steps below to run **A Circle Of Care** locally.

## 📋 Prerequisites

Make sure you have the following installed:

* 🐍 **Python 3.10+**
* 📦 **pip**
* 🔧 **Git**
* 🤖 **Google Gemini API Key**

---

## 1️⃣ Clone the Repository

Open your terminal or command prompt:

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
```

Navigate to the project directory:

```bash
cd <your-repo-name>
```

---

## 2️⃣ Create a Virtual Environment

### 🪟 Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### 🐧 macOS / Linux

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure the Gemini API Key

Create a `.env` file in the main project directory, where `manage.py` is located.

Add your Gemini API key:

```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

### 🔒 Security

Never upload your `.env` file or expose your API key publicly.

Add the following to `.gitignore`:

```gitignore
.env
venv/
__pycache__/
*.pyc
db.sqlite3
```

---

## 5️⃣ Run Database Migrations

```bash
python manage.py migrate
```

---

## 6️⃣ Create an Admin Account

To access the Django admin panel:

```bash
python manage.py createsuperuser
```

Follow the instructions displayed in the terminal.

> This step is optional.

---

## 7️⃣ Start the Development Server

Run:

```bash
python manage.py runserver
```

The application will be available at:

```text
http://127.0.0.1:8000/
```

Open the URL in your browser to access **A Circle Of Care**. 🎉

---

# 🔑 Environment Variables

The project uses environment variables to protect sensitive configuration.

| Variable         | Description                                     |
| ---------------- | ----------------------------------------------- |
| `GEMINI_API_KEY` | Google Gemini API key used for AI functionality |

Example:

```env
GEMINI_API_KEY=your_api_key_here
```

---

# 🎯 Project Objectives

The main objectives of **A Circle Of Care** are:

* ❤️ Encourage better family communication.
* 💬 Provide a platform for sharing feedback.
* 🤖 Provide AI-powered chatbot assistance.
* 💡 Offer supportive suggestions to users.
* 🌐 Demonstrate the integration of AI with Django.
* 🔐 Provide a secure and user-friendly web application.

---

# 🔮 Future Improvements

* 📱 Mobile application version
* 🧠 Advanced AI personalization
* 📊 Communication analytics
* 🔔 Notifications and reminders
* 👥 Multiple family member profiles
* 🌍 Multi-language support
* 🔐 Enhanced security and privacy
* ☁️ Cloud deployment

---

# 👨‍💻 Developer

### **Harshal Sonar**

**Computer Engineering Student | Full-Stack & Application Developer**

### 💻 Interests

`Python` • `Django` • `React Native` • `JavaScript` • `AI` • `Cloud Computing` • `UI/UX`

---

# ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ **Star**.

Your support is appreciated! ❤️

---

## 📄 License

This project is created for **educational and development purposes**.

---

<p align="center">
  Made with ❤️ using Python & Django
</p>
