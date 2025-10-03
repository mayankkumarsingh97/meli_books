# 🛒 Django eCommerce Project

A full-featured eCommerce web application built with Django. This project includes user authentication, product listings, shopping cart functionality, order management, and payment integration.

## 🚀 Features

- User registration and login
- Product catalog with categories and search
- Shopping cart and checkout flow
- Order history and tracking
- Admin dashboard for managing products, orders, and users
- Payment gateway integration (e.g., Stripe or Razorpay)
- Responsive design using Bootstrap
- A new commit added on readme file

## 🧰 Tech Stack

- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite (default), PostgreSQL (recommended for production)
- **Payment**: Stripe or Razorpay
- **Deployment**: Heroku / Render / AWS

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/django-ecommerce.git
   cd django-ecommerce

- Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

##
##
- Install dependencies

pip install -r requirements.txt

- Set up environment variables Create a .env file and add your secret keys
SECRET_KEY=your_secret_key
DEBUG=True
STRIPE_API_KEY=your_stripe_key

- Run migrations
python manage.py migrate
###
###
- Create a superuser
python manage.py createsuperuser
##
##
- Start the development server
python manage.py runserver

