FROM python:3.11
COPY . Ecom/
WORKDIR /Ecom
RUN pip install django
RUN pip install djangorestframework
RUN pip install mysqlclient
RUN python -m pip install Pillow
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
EXPOSE 8000
CMD [ "python3" ,"manage.py" ,"runserver" ,"8000" ]