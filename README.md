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

### Oauth Setup - Facebook

This section is mandatory for Facebook Signin in order to restrict unauthorized users from adding, deleting or modifying restaurants and their menus. This also provides authentication making users mandatory to sign in for admin privileges:

1. Create App ID and App Secret:
    - Go to [Facebook Developers](https://developers.facebook.com/)
    - Sign in using your facebook account. **Note:** _If you don't have facebook account, you can create one at [Facebook Signup](https://www.facebook.com/)_
    - Click on **Add New App**.
    - Give App a name and click on **Create App ID**.
    - Go to `Settings\Basic`.
    - Go to **Add Platform** Section and select the app type as **website**.
    - Enter the site URL as `http://localhost:5000` and click on **Save Changes**.
    - Click on the `App Name` Dropdown on the top left pane.
    - Create Test App by clicking on **Creat Test App**. **Note:** _This step is mandatory as Facebook stopped supporting http protocol and only test apps support http protocol_
    - Your **App ID** and **App Secret** are created and can be viewed now. Create `fb_client_secrets.json` file or use the file available for reference in this repository and replace with your **App ID** and **App Secret**.
    
    Below are couple of resources i am sharing for your references:
    1. [loginbutton](https://developers.facebook.com/docs/facebook-login/web/#loginbutton)
    2. [redirecturl](https://developers.facebook.com/docs/facebook-login/web/#redirecturl)
    3. [loginsettings](https://developers.facebook.com/apps/408172529765462/fb-login/settings/)
    4. [accesstokens](https://developers.facebook.com/docs/facebook-login/web/accesstokens)
    5. [permissions](https://developers.facebook.com/docs/facebook-login/web/permissions)

### Project Execution:

 - Setup Database and feed data into the database:
    - Execute below commands in the same order and wait for each command to complete execution:

        ```python
        python database_setup.py
        python lotsofmenu.py
        ```
    
    **Note:** _You can create your own data by using `add_restaurant_data.py` file or you can also add more restaurants and menus in `lotsofmenu.py` file._

- Execute command `python project.py` and with this server is now running at **localhost 5000**.
- Open your favorite browser and enter `http://localhost:5000` or `http://localhost:127.0.0.1:5000`
- **Restaurant Menu Application** is now live.

    **Note:** _Currently host has been configured as `0.0.0.0` in `project.py` which means the server will be able to reach to all ipv4 addresses in your local machine._

### Video Walkthrough:

<img src='https://i.imgur.com/dZjahlY.gif' title='Restaurant Menu Application' width='80%' alt = 'Restaurant Menu Application'/>


### Author

Divvi Naga Venkata Satish - [Portfolio](https://satishdivvi.github.io)

