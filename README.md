# GKTW Dispatcher (Reservation Ver)
A second iteration of the initial GKTW Dispatcher that allows for reservations but does not include wait times.

# Environment Setup

## Python
1. Installation of [python](https://www.python.org/downloads/)
2. Add python to PATH. Refer to this [video](https://www.youtube.com/watch?v=YYXdXT2l-Gg) for help
3. Ensure that pip is installed properly by calling 'pip --version' in the command prompt or terminal (which can be found by using the search bar at the top or bottom of your screen)

## Database
* The database used is **SQLite** . The database is located in database/GKTWTransportationDataRes.db 
* There is also an Excel output option in the repo: database/GKTW_Transportation_Data_Res.xlsx
* To view the database, use DBeaver Community Edition [installation guide](https://dbeaver.io/download/)
  1. After launching DBeaver, at the top of the screen go to Database > New Database Connection > SQLite
     <img width="786" alt="image" src="https://github.com/ivy-nguyen18/GKTW_Transportation/assets/73045170/b78dddd4-668d-4af4-aa16-81aab31d2efa">
     <img width="685" alt="image" src="https://github.com/ivy-nguyen18/GKTW_Transportation/assets/73045170/29fc58ed-9e01-43a4-978c-7a71137f8644">
  2. Press Open... and locate database/GKTWTransportationData.db
  3. Press Open to exit the popup and then Finish to exit the initial popup
     <img width="689" alt="image" src="https://github.com/ivy-nguyen18/GKTW_Transportation/assets/73045170/e58d6b72-0221-4512-b296-7743d69aea72">
  4. You should be able to view the connection on the left panel of the screen under Database Navigator
     <img width="329" alt="image" src="https://github.com/ivy-nguyen18/GKTW_Transportation/assets/73045170/fb47cb17-31b2-4bee-8688-b6f88ababecc">
  5. Click on the database you just connected to and at the top, there is a button with an image of a scroll and says "SQL"
     <img width="333" alt="image" src="https://github.com/ivy-nguyen18/GKTW_Transportation/assets/73045170/d4ca2360-1872-4b62-8336-e632892ff904">
  6. Clicking this button will generate a SQL script specific to your database where you are able to write your queries
     <img width="1102" alt="image" src="https://github.com/ivy-nguyen18/GKTW_Transportation/assets/73045170/2f11dfbb-aea8-4494-ae7c-526ce34e3302">
     
# Running the Application
1. In the command prompt or terminal, go to the GKTW_Transportation directory using 'cd /path to directory/GKTW_Transportation'
2. Install required libraries using 'pip install -r requirements.txt'
3. Run the application by calling 'streamlit run app.py'
![image](https://github.com/ivy-nguyen18/GKTW_Transportation/assets/73045170/acac0c8c-c098-48e1-b238-3b903b1ff119)

## Attributes of the Application
The application is divided into three sections: Input, Standard Shuttle View, and ADA Shuttle View

### Input
The dispatcher gets this information from the guest as the guest calls in to make a reservation and adds them to their respective queue and into the database:

![image](https://github.com/ivy-nguyen18/GKTW_Transportation/assets/73045170/d9e517d6-948c-4a94-8169-737401b356d2)

### Standard Shuttle View and ADA Shuttle View
Depending on whether the ADA checkbox was checked, the guest will populate into the respective shuttle after clicking the "ADD" button.
The functionality of the tables displayed:
* Deleteable rows by either clicking the check box at the top of the table to select all and pressing the * *Backspace* * button on the keyboard:
  
  ![image](https://github.com/ivy-nguyen18/GKTW_Transportation/assets/73045170/1592b418-1cfd-4370-a5e3-08c08023065f)
  
  or clicking the row for particular guests and pressing the Backspace button on the keyboard:
  
  ![image](https://github.com/ivy-nguyen18/GKTW_Transportation/assets/73045170/8830774d-dcb9-4b1b-a24b-2e39bdb2ad8b)
  
* **WARNING**: you are able to add guests to the table by hovering over the bottom of the table until a plus icon appears in the cell. HOWEVER, adding guests via this method does not save to the database. Thus, PLEASE ADD GUESTS VIA THE INPUT FORM.

   ![image](https://github.com/ivy-nguyen18/GKTW_Transportation/assets/73045170/1ff0f9f4-f4b4-4648-8bf9-962f51734a3c)

## Functionality and Caveats
This application is able to:
* Repopulate the table based on reservation time: If a guest chooses to reserve for a future date, when the future date comes, the guest will be repopulated in the table.
* Sort based on reservation time
* Run offline
* Due to the repopulation nature of the table, if the operator were to delete some people and then exit from the application, and the run the application again, everyone that had a reservation date of the current date will be repopulated back into the table, regardless of whether or not they were previously deleted. Thus, **IT IS IMPORTANT TO NOT EXIT FROM THE APPLICATION**

## Dispatcher Steps:
1. Guest calls in to request a shuttle, the dispatcher inputs the guest data into the form and adds them to the queue
2. The dispatcher then relays the guest pickup and dropoff location to the appropriate shuttle driver (ADA or Standard)
3. The shuttle driver will update the dispatcher on who has been dropped off/ completed in the queue. 



