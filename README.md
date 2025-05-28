


# Clone the project
git clone ....
cd ....
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements/development.txt

# Install Django and ASGI server
pip install django uvicorn

# Run the Project

# Export dev settings
export DJANGO_SETTINGS_MODULE=config.settings.dev
python manage.py migrate
python manage.py runserver
Or run with Uvicorn:
uvicorn config.asgi:application --reload