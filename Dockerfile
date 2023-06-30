FROM python:3.5.7


ENV PYTHONUNBUFFERED 1


# Set the working directory to /api

WORKDIR /api

RUN ls .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

VOLUME /api

EXPOSE 8080

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
