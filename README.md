# Team Project: Final Web Application

### Team members:
* Baxi, Priyesha
* Ramani, Karan

#### Project Description:
* This project is for the purpose of the Final Web Application submission, which goes over complete and working web
application integration. By using; Flask framework this application runs on Docker, combined with MySQL Database 
service.
* In this project we have used the csv table "Grades.csv" from previously provided 
[list of CSV files](https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html).
* Below are the complete set of features added to this project.

    * Application running on web server (Using Docker)
    * View Database content on webserver's webpage
    * Edit Database content from browser side interface.
    * Delete Database entries from browser side interface.
    * Add entries to Database from browser side.
    * Flask App is enabled for testing GET, POST, PUT, DELETE methods on Postman services.
    
* In addition to above features, below are the final features added as part of the Final Project Submission 
**(By individual team members)**:

    * Login and registration process that includes email verification. - **Ramani, Karan**
        * This process is done by database entries, website forms are directly connected to the backend database 
        verifying the user inputs with the database, site is logged in if the user input is correct or new user is made
        based on user's choice.
        * This process also has email feature for each attempt of user login or signup.
        
        * Functionalities: 
            * Login = ✅
            * Logout = ✅
            * New User registration form = ✅
            * New User Email authorization with Code = ✅
            * New User Email Auth code check with database = ✅
            * On success check =✅
            * On failed auth code entry removal = ✅
            
        * [Click here to view project Screenshots](Final_Project.pdf)
        * This function covers the above listed functionalities of ensuring that the user of the site is logged in with a session. It also then has function to securely log out of the session. 
        ## Please see Canvas submission comment for mail app testing purpose. Email password is included to attach on downloaded code (Paste on Line 78 of app.py file) 

### Feature: Calendar API **By Priyesha Baxi**
       * Successfully included Events DB(which goes with calendar feature)
       * Successfully installed client_secret json file
       * Grades Data sucessfully running on both end
        
        
      