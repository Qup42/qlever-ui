# What is QLeverUI?
QLeverUI is an easy to use interactive user interface for the very fast SPARQL search engine QLever that helps you to discover the scopes and information in very large knowledge bases by providing context sensitive suggestions and auto-completions and adding helpful information an views to the various outputs.

QLever UI supports different types of results (e.g. geographical data, named instances, images and more) and is highly customizable to the needs of its users and the structure of the underlying dataset.

### Authors, Contributors & Copyright
© 2016 - 2021 University of Freiburg, [Chair for Algorithms and Data Structures](https://ad.cs.uni-freiburg.de/)

- @jbuerklin <jb@software-design.de>   
- @dKemen <dk@software-design.de>
- @hannahbast <bast@informatik.uni-freiburg.de>

## What is QLever?
QLever (pronounced "clever") is an efficient SPARQL engine that can handle very large datasets. For example, QLever can index the complete Wikidata (~ 18 billion triples) in less than 24 hours on a standard Linux machine using around 40 GB of RAM, with subsequent query times below 1 second even for relatively complex queries with large result sets. On top of the standard SPARQL functionality, QLever also supports SPARQL+Text search and SPARQL autocompletion.

For more information on QLever, visit the corresponding [GitHub Repo](https://github.com/ad-freiburg/QLever).

# Overview
* [Building the QLeverUI Docker Image](#building-the-qleverui-docker-container)
    * [Setting up the database](#setting-up-the-database)
    * [Running a QLeverUI Docker container](#running-a-qleverui-docker-container)
* [Installing QLever UI without docker](#building-the-qleverui-docker-container)
    * [Setting up the database manually](#setting-up-the-database-manually)
    * [Running QLever UI without docker](#running-a-qleverui-docker-container)
* [Configure QLeverUI]()
* [Extending QLeverUI / Contributions]()
    * [Extending SPARQL syntax]()
    * [Extending Langauge Parser]()
    * [Extending the user interface]()


# Building the QLeverUI Docker image
Clone the QLeverUI repo
```
git clone https://github.com/jbuerklin/qleverUI.git qleverui
cd qleverui
```
Before building the Docker Image, move `settings_secret_template.py` to `settings_secret.py` and edit it to fit your needs.
```
mv qlever/settings_secret_template.py qlever/settings_secret.py
```
Then build the Docker Image
```
docker build -t qleverui .
```
You have now created a Docker Image that contains everything you need to run QLeverUI.

## Setting up the database
__You can skip this step if you already have a database file.__  
To setup the database, first run a bash inside the QLeverUI container as follows.
```
docker run -it --rm \
           -v "$(pwd)/db:/app/db" \
           --entrypoint "bash" qleverui
```
Where `$(pwd)/db` is the path where QLeverUI will store it's database. If you want to use a separate path, make sure to  change this part in all subsequent `docker` commands.

Create the empty database file with the following command.
```
python manage.py migrate
```
Then create a superuser for your database by entering
```
python manage.py createsuperuser
```
and following the instructions in your terminal.  
You can now exit the container as QLeverUI is finally ready to run.

## Running a QLeverUI Docker container
To run a QLeverUI container use the following command.
```
docker run -it -p 8000:8000 \
           -v "$(pwd)/db:/app/db" \
           --name qleverui \
           qleverui
``` 
__Note:__ If you already have a QLeverUI database file `qleverui.sqlite3` you want to use, make sure it is located in the specified path or provide the correct path to it.  
If you want the container to run in the background and restart automatically replace `-it` with `-d --restart=unless-stopped`  
You should now be able to connect to QLeverUI via <http://localhost:8000>.  
# Installing QLever without docker
When not using docker there are some additional steps to do. QLever UI is build upon a [Python 3](https://www.python.org/downloads/) / [Django 3](https://www.djangoproject.com/) backend so you will need to have Python 3 installed in order to run QLever UI. It's strongly recommended to use [virtual environments](https://docs.python.org/3/library/venv.html) to manage the project's dependencies when not using the docker build. In order to manage the dependencies we use pip - if "[pip](https://pypi.org/project/pip/)" is installed on your system / in your virtual environment you can simply use 
```
	pip install -r requirements.txt
```
inside the projects root folder to automatically install all dependencies. Otherwise you can find the list of dependencies in the requirements.txt file to install dem manually.

Next, you will need to adjust your individual settings in `qlever/settings_secret_template.py` and rename it to `qlever/settings_secret.py` to let QLever UI automatically detect your settings file.
```
mv qlever/settings_secret_template.py qlever/settings_secret.py
```

## Setting up the database manually
The last step required is creating an SQLite database for the backend. Simply run
```
	python manage.py make migrations —-merge && python manage.py migrate
```
inside the project root folder in order to do so. You will only need to do this once. If you prefer you can also overwrite the database settings to use some other database management system in your settings_secret.py.

For configuring you QLever backend you will need an administrative user for the QLever UI administration panel. You can create an admin account by simply running the following command in your project root: 
```
	./manage.py createsuperuser
```
## Running QLever UI without docker
You can either start a development server by simply running
```
	./manage.py runserver localhost:8042
```
or prepare a productive environment.

You can start the development instance at any time with this single command and access your instance by opening http://localhost:8042. Feel free to change the port or hostname if needed.

# Configure QLeverUI

Assuming that you already have a QLever Instance running and super user created you can now configure your existing QLever backend in you new QLever UI instance. 

You may access the admin panel by adding `/admin` to the URL you are using for your QLever UI instance and login with the credentials you just created.

If you don't have a QLever instance readily available to key in or just want to get up and running as fast as possible, you can use our [example settings](resources/) that use a QLever instance with Wikidata KB hosted at the Chair of Algorithms and Data Structures at the University of Freiburg.  

Click "Backends" and "Add backend" in order to start configuring your first QLever backend. There are many help texts below each configuration box that guide you through the process. If you are done save the settings and reload the QLever UI interface.

You can also import the respective `*-sample.csv` file for the example backend.

If everything worked correctly you should see backend details displayed on top right of the regular QLever UI. If not you can enable details error logging in the user interface (in top right dropdown menu) and open your browsers developer console to see the outputs.

# Extending QLever UI