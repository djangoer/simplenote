# simplenote
simplenote webpage

## installation

    # create and activate virtual env
    python3 -m venv env
    source env/bin/activate 
    # install requirements
    pip install -r requirements.txt
    ./manage.migrate
    # create an admin user
    ./manage.py createsuperuser
    ./manage.runserver
    
