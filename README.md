# to_do_tracker

git clone https://github.com/alisher1989/to_do_tracker.git

cd to_do_tracker/

virtualenv -p python3.7 venv

source venv/bin/activate

pip install --upgrade pip

pip install -r req.txt

./manage.py migrate

./manage.py runserver
