# Restaurant Menu Application

### Introduction:

Restaurant Menu Application is a Flask powered application which gives below information:
   1. Restaurants
   2. Menu's of the specific restaurant

Also, this application provides the ability to add, delete, and modify **restaurants** and **restaurants** **menu**.

### Installation

1. Install Vagrant and VirtualBox:
    - Install [Vagrant](https://www.vagrantup.com/downloads.html) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
    - Please fork the repository [VM Configuration](https://github.com/SatishDivvi/fullstack-nanodegree-vm) or download **Vagrantfile** from the repository.
    - Open terminal in *Mac* or *Linux* or GitBash in *Windows*. 

    **Note (Windows User only):** _please install [GitBash](https://git-scm.com/downloads) if not installed._

2. Configure Vagrant:
    - Open *GitBash* and `cd` to the directory where you have installed Vagrant.
    - Run command `vagrant up`. **Note:** _This step will take some time if executed for the first time._
    - Run command `vagrant ssh`
    - `cd` to folder _vagrant_ with command `cd vagrant`.
3. How to setup Restaurant Menu Application:
    - Download folders `static`, `templates` and files `add_restaurant_data.py`, `database_setup.py`, `lotsofmenu.py`, `project.py`.
    - Place the downloaded folders and files into vagrant folder. 

    **Note:** _The folders and files structure should be same as seen in this repository._

### OAuth Setup - Google

This section is mandatory for Google+ Signin in order to restrict unauthorized users from adding, deleting or modifying restaurants and their menus. This also provides authentication making users mandatory to sign in for admin privileges:

1. Create Client ID and Client Secret:
    - Go to [Google Console](https://console.developers.google.com/apis)
    - Choose **Credentials** from the menu on the left.
    - Create an **OAuth Client ID**.
    - Click on **Configure Consent Screen**.
    - Give a valid name to the application.
    - Add appropriate javascript origins. For this project it should be `http://localhost:5000` or `http://127.0.0.1:5000`.
    - Add appropriate javascript redirects. For this project it should be `http://localhost:5000/login` and `http://localhost:5000/gconnect`.
    - After the consent screen please select **Web application** as the Application Type.
    - Click on the name of the app and **Client ID**, **Client Secret** can be viewed.
    - Download JSON file by clicking on **DOWNLOAD JSON** button and name the file as **client_secrets.json**.
    - Move **client_secrets.json** file to `/vagrant` folder.

    **Note:** *`client_secrets.json` file in this repository is only for you to check on how your json file should look. Please do not use this file as i have removed my `CLIENT_ID` and `CLIENT_SECRET`.*

4. Setup Database and feed data into the database:
    - Execute below commands in the same order and wait for each command to complete execution:

        ```python
        python database_setup.py
        python lotsofmenu.py
        ```
    
    **Note:** _You can create your own data by using `add_restaurant_data.py` file or you can also add more restaurants and menus in `lotsofmenu.py` file._
    
### Project Execution:

- Execute command `python project.py` and with this server is now running at **localhost 5000**.
- Open your favorite browser and enter `http://localhost:5000` or `http://localhost:127.0.0.1:5000`
- **Restaurant Menu Application** is now live.

    **Note:** _Currently host has been configured as `0.0.0.0` in `project.py` which means the server will be able to reach to all ipv4 addresses in your local machine._

### Video Walkthrough:

<img src='https://i.imgur.com/dZjahlY.gif' title='Restaurant Menu Application' width='80%' alt = 'Restaurant Menu Application'/>


### Author

Divvi Naga Venkata Satish - [Portfolio](https://satishdivvi.github.io)

