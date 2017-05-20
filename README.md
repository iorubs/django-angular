# django-angular

### Description:  
Quick start django-angular app template plus authentication.

### Instructions:  
1 - Install Docker, https://www.docker.com/products/docker.  
2 - `git clone https://github.com/vasconr2/django-angular.git`  
3 - `cd django-angular`  
4 - `docker build -t django-angular .`  
5 - `docker run -it -v "$PWD"/application:/src/django-angular -p 8000:8000 django-angular sh`  
6 - `bower install`  
7 - `python manage.py makemigrations`  
8 - `python manage.py migrate`  
9 - `python manage.py runserver 0.0.0.0:8000`  
10 - Open http://localhost:8000/ on your browser.  

### Tech Stack:   
![alt tag](https://github.com/iorubs/django-angular/blob/master/Stack.png)  
