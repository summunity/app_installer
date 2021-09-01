### tags - pm2, nginx, django, react

# Description
If you are in the business of creating and releasing frontend/backend apps, you understand the frustration that comes along with releasing an application. It's not difficult per se but tedious and any small mistake can take time debugging. The app installer aims to automate the django and react application release process. 

# Caveats
The app installer was written to support the deployment of applications on a Redhat linux server. We have not yet added support for other linux platforms. If needed, please let us know and we will be happy to provide support.



# Linux Installation

 1. clone the git repository into the desired directory
```
cd <path>
git clone https://github.com/summunity/app_installer 
```

 2. Open .bashrc file
```
sudo nano ~/.bashrc
```

 3. Add the directory path to the PATH variable
```
export APP_INSTALL = "<path>"
path = $APP_INSTALL:$PATH
```

 4. Source the .bashrc file
 ```
 source ~/.bashrc
 ```
 
The app_installer is now available and should be executed at the root directory of the application you wish to install 

# Dependencies
Installing a django project requires a requirements.txt file containing all dependencies. This will be used to create a virtual environment that will run the application. Generate the requirements.txt file with :

```
python -m pip freeze > requirements.txt
```  

# Instructions
The application installer must be launched from the root directory of your django/react project. This allows the application to search for and/or create the configurations needed for deployment.


 1. change directory to the project's root directory
```
>>> cd <path>
```

 2. launch the application installer
```
>>> app_install
```

 3. Specify the project type i.e. django or react  
```
product type (django or react)
>>> django
```

 4. Specify the project name 
 ```
product name
>>> django_test
 ```
 
 5. Specify the port to be used as the reverse proxy 
 ```
port
>>> 8000
 ```
 
That's it. 

NGINX will host the the application at the following url: 
> < host >/< project name >

PM2 will host the project using the project name. Check the projects status with:
> pm2 status




