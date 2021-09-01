# bookstore

git clone https://github.com/hyeinjeon/bookstore.git

git clone 한 뒤에 순서대로 입력하기

git init

python -m venv myvenv

source myvenv/Scripts/activate

cd bookstore

pip install django

pip install pillow

pip install pilkit

pip install django-imagekit

pip install dj-database-url

pip install django-allauth

pip install whitenoise

python manage.py makemigrations

python manage.py migrate

python manage.py runserver