#!/bin/bash
dropdb helios_dev
createdb helios_dev
python manage.py syncdb
python manage.py migrate
echo "from helios_auth.models import User; User.objects.create(user_type='google',user_id='kaio.karam@gmail.com', info={'name':'Kaio Karam'})" | python manage.py shell
