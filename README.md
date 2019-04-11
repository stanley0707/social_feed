# Project Title

One Paragraph of project description goes here

## Getting Started

requirements:
python3.6


### use)
 - sudo apt-get update
 - 
 - sudo apt-get install postrgresql postgresql-contrib
 - 
 - sudo su - postgres
 - 
 - psql
 - 
 - CREATE DATABASE user_db;
 - 
 - CREATE USER user WITH PASSWORD '123'
 - 
 - ALTER ROLE user SET client_encoding TO 'utf8';
 - 
 - ALTER ROLE user SET default_transaction_isolation TO 'read committed';
 - 
 - ALTER ROLE user SET timezone TO 'UTC'
 - 
 - GRANT ALL PRIVILEGES ON DATABASE user_db TO user;
 - 
 - /q
 - 
 - exit
 - 
 - create and activare your virtualenv
 -  
 - pip install -r requirements.txt
 - 
 - python manage.py makemigrations 
 - 
 - python manage.py migrate
 - 
 - python manage.py createsuperuser
 - 
 - python manage.py runserver 0.0.0.0:8080
 - 
 - Для отображения своей стены необходимо авторизовать сеюя в админке VkUser
 - 
 

```
    // пример обращения к api axios
    
    axios.get(this.baseUrl, { params: {
          "part": this.part,
          "page": this.page++,
    }})
    .then(response => {
        this.info = response.data;
         console.log(response.data)
    })
    .catch(error => {
        console.log(error);
        this.errored = true;
    })
    .finally(() => (this.loading = false));
    
```
####  url и параметры серверной пагинации

```
https://social-feed-back-stanleyws.c9users.io:8080/api/?page=<page number>&part=<number of required posts in one request>
```