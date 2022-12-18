# flask_REST_api

![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white)
![](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white)
![](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)

A small project to create Flask REST-API. 

> Install Python (if it's not installed), preferably starting with version 3.8<br>
> [Download Python3](https://www.python.org/downloads/release/python-3910/)

Clone the repository:
```
git clone https://github.com/AlexanderZug/flask_REST_api.git
```

Go to folder:
```
cd flask_REST_api
```

Install requirements:
```
pip3 install -r requirements.txt
```

If you wish, you can also use Docker:
```
docker build -t <your-image-name> .
```
```
docker run -dp 5000:5000 <your-image-name>
```

if you want to make changes to the code without restarting the container, then build the image and then run the command:
```
docker run -dp 5000:5000 -w /app -v "$(pwd):/app" <your-image-name>
```

> The project was completed as part of a Flask course on Udemy (REST APIs with Flask and Python in 2022).
