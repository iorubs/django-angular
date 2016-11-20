# Keeperoo
Password keeper  

### Description:  
A tool that allows individuals/teams to manage their passwords.  

### Instructions:  
1 - Install Docker, https://www.docker.com/products/docker.  
2 - `git clone https://github.com/vasconr2/keeperoo.git`  
3 - `cd keeperoo`  
4 - `docker build -t keeperoo .`  
5 - `docker run -it -v "$PWD"/application:/src/keeperoo -p 8000:8000 keeperoo sh`  
6 - `bower install`  
7 - `python manage.py runserver 0.0.0.0:8000`  
8 - Open http://localhost:8000/ on your browser.  

### Tech Stack:   
![alt tag](https://github.com/vasconr2/keeperoo/blob/master/Stack.png)  

### Todo list:  
1 - Password Manager Back/Front end.  
2 - Create prod Dockerfile.  
3 - Organization Back/Front end.  
3 - Everything else...  
