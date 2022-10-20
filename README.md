## Development 👨‍💻

Note : Make sure you have Python version 3.8+

## Environment Setup 🚀

<pre><code>$ git clone https://github.com/GauravSighariya/skininks.git</code></pre>

<pre><code>$ cd django_project/</code></pre>

If virtualenv is not installed (What is virtualenv?):

<pre><code>$ pip install virtualenv</code></pre>

Create a virtual environment

<pre><code>$ virtualenv venv</code></pre>

Activate the environment everytime you open the project

<pre><code>$ source venv/Scripts/activate</code></pre>

Install requirements 🛠

<pre><code>$ pip install -r requirements.txt</code></pre>

Run migrations for Database

<pre><code>$ python manage.py makemigrations</code></pre>

<pre><code>$ python manage.py migrate</code></pre>

Create superuser for Admin Login 🔐

<pre><code>$ python manage.py createsuperuser</code></pre>

Enter your desired username, email and password. Make sure you remember them as you'll need them in future.

eg.

Username: admin

Email: admin@admin.com

Password: HighlyConfidentialPassword

All Set! 🤩

Now you can run the server to see your application up & running 🚀

<pre><code>$ python manage.py runserver</code></pre>

To exit the environment ❎

<pre><code>$ deactivate</code></pre>

Every time you want to open the application in browser, make sure you run:

<pre><code>$ source venv/Scripts/activate</code></pre>

<pre><code>$ python manage.py runserver</code></pre>
