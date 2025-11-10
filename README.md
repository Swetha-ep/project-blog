# 📝 Inked — Blog Platform

**Inked** is a full-featured **Blog Application** built with **Django**, allowing users to create, edit, and manage their own posts with rich-text formatting.  
It offers a clean, user-friendly interface with secure authentication and engaging features like likes, follows, and bookmarks.

🌐 **Live Demo:** [https://project-blog-5ua8.onrender.com/](https://project-blog-5ua8.onrender.com/)  
💻 **Tech Stack:** HTML, CSS, JavaScript, Django, SQLite, CKEditor, Git

---

## 🚀 Features

### ✍️ User Features
- Create, edit, update, and delete blog posts  
- Format content using **CKEditor** (rich-text support)  
- Like (upvote) and bookmark posts  
- View and follow other authors  
- Manage user profiles with display picture and bio  
- Personalized dashboard to manage own posts  
- Secure login, logout, and signup system  
- Responsive design for all screen sizes   

---

## 🧱 Tech Stack

| Layer | Technologies Used |
|-------|-------------------|
| **Frontend** | HTML, CSS, JavaScript, Bootstrap |
| **Backend** | Django, Django ORM |
| **Database** | SQLite |
| **Rich Text Editor** | CKEditor |
| **Deployment** | Render |
| **Version Control** | Git & GitHub |

---

## ⚡ Installation & Setup

```bash
# 1️⃣ Clone the repository
git clone https://github.com/Swetha-ep/project-blog
cd project-blog

# 2️⃣ Create and activate virtual environment
python -m venv venv
venv\Scripts\activate   # for Windows
# source venv/bin/activate  # for Mac/Linux

# 3️⃣ Install required dependencies
pip install -r requirements.txt

# 4️⃣ Apply migrations
python manage.py makemigrations
python manage.py migrate

# 5️⃣ Create a superuser (for admin access)
python manage.py createsuperuser

# 6️⃣ Run the server
python manage.py runserver
