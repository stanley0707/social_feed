# Social Feed (VK API)


## Getting Started

- After running go to admin panel and save your "vk" login and password in Vkuser model.
Don't worry, your confidential data don't go to any people and save
in database, which you create



lang:
python3.6.3


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


## project models
![models](api_models.png?raw=true)


## project UMl
![UMl](apidiagram.png?raw=true)


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
####  url with params example

```
https://domain:8080/api/?page=<page number>&part=<number of required posts in one request>
```

####  json example
```
{
    "data":[
      { 
        "date": "1555074301",
        "index": "2",
        "id": "387997",
        "vk_id": "34827356835",
        "text": "some text",
        "type": "photo",
        "media"{"url": [
            "https://domain.com/media/image.jpg",
            "https://domain.com/media/image.jpg",
            "https://domain.com/media/image.jpg",
        ]
      },
      { 
        "date": "1555073421",
        "index": "3",
        "id": "387123",
        "vk_id": "34827332425",
        "text": "some text",
        "type": "photo",
        "media"{"url": [
            "https://domain.com/media/image.jpg",
            "https://domain.com/media/image.jpg",
            "https://domain.com/media/image.jpg",
        ]
      },
    ],
    "msg":{
        "ret": 200,
        "status": "true",
        "total": 75,
    },
}
```
######  data – array with articles ( length this array equal to the parameter sent to "part") 
######  msg – contains the status of the response
######      total – sum of all articles, wo you can take from server