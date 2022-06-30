python manage.py makemigrations
python manage.py migrate

heroku config:set API_KEY=2187627981sds19646
heroku config:set API_SECRET=OqsHrsdswFb-l8xmD_9eUcYBj_tVN8
heroku config:set CLOUDINARY_URL=cloudinary://1233349796sdfsd96849:Jvd78nFKUziejHAW-b5Qn0gLuHk@da7srpwm6
heroku config:set CLOUD_NAME=sdsd

heroku config:set DEBUG=False
heroku config:set DISABLE_COLLECTSTATIC=1
heroku config:set MODE=prod
heroku config:set SECRET_KEY='django-insecure-h-4_vq % @6x462t8ly = k = +8os_54n7_lziad!i4 *$_rey9b@1mb'
heroku config:set ALLOWED_HOSTS=demo-angular-django.herokuapp.com


git switch -c main
git switch main
git merge develop

python manage.py collectstatic

pip freeze > requirements.txt

git add .
git commit -m "heroku deployment"
git push heroku main



# heroku run python manage.py makemigrations
# heroku run python manage.py migrate
# heroku pg:reset
# heroku pg:push eloan DATABASE_URL --app eloan-ke

git switch develop
heroku open