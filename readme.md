# 🚀 Installation & Running Guide

Follow these steps to set up and run the project locally on your machine.

---

### Prerequisites
Make sure you have:
- **Python 3.10+** installed
- **Git** installed
- A **Gemini API Key** from [Google AI Studio](https://aistudio.google.com/)

---

### Step 1: Clone the Repository
Open your terminal or command prompt and clone the repository:
```bash
git clone [https://github.com/](https://github.com/)<your-username>/<your-repo-name>.git
cd <your-repo-name>
Step 2: Create & Activate Virtual Environment
On Windows:

Bash
python -m venv venv
venv\Scripts\activate
On macOS / Linux:

Bash
python3 -m venv venv
source venv/bin/activate
Step 3: Install Required Packages
Bash
pip install -r requirements.txt
Step 4: Configure the API Key
Create a .env file in the main folder (where manage.py is located) and paste your API key:

Code snippet
GEMINI_API_KEY=your_actual_gemini_api_key_here
Step 5: Run Database Migrations
Bash
python manage.py migrate
(Optional) Create an admin login:

Bash
python manage.py createsuperuser
Step 6: Start the Server
Bash
python manage.py runserver