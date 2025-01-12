# Prime.Picks

**Prime.Picks** is a Django-based e-commerce platform designed to deliver a seamless online shopping experience. Users can browse products, make purchases, and track their orders, while admins can manage the backend with ease.

## Features

### User Features:
- **Product Listing and Categorization:** Displays products organized by categories for easy browsing.
- **User Registration and Authentication:** Secure registration, login, and logout functionality.
- **Contact Form:** Allows users to send inquiries and messages directly to the admin.
- **Checkout Process:** Simple and secure order placement with PayTM payment gateway integration.
- **Order Tracking:** Users can view and track their orders through their profile.

### Admin Features:
- **Admin Panel:** Manage products, categories, and orders effortlessly.
- **View User Inquiries:** Admin can view and respond to messages sent via the contact form.

## Installation and Setup

### Prerequisites:
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step 1: Clone the Repository
```bash
git clone https://github.com/OmBedre/Prime.Picks.git
cd Prime.Picks
```

Step 2: Create a Virtual Environment
```bash
python -m venv venv
```
Activate the virtual environment:

On Windows:
```bash
venv\Scripts\activate
```

On macOS/Linux:
```bash
source venv/bin/activate
```

Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

Step 4: Configure the Database
Run the following commands to apply database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

Step 5: Create a Superuser
To access the Django admin panel, create a superuser:
```bash
python manage.py createsuperuser
```
Follow the prompts to set a username, email, and password.

Step 6: Run the Development Server
Start the server with:
```bash
python manage.py runserver
```
Visit the project in your browser at http://127.0.0.1:8000/

Usage
Accessing the Admin Panel:
URL: http://127.0.0.1:8000/admin/

Log in using the superuser credentials created earlier.
Viewing the Website:
URL: http://127.0.0.1:8000/

Testing Contact Form:
Navigate to the contact page and send a test inquiry.


Static Files: Ensure static files are collected for production using:
```bash
python manage.py collectstatic
```

Environment Variables: Store sensitive data like database credentials and API keys in an .env file for security.

License
This project is open-source and available under the MIT License.





