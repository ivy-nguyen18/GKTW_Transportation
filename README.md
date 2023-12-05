# GKTW Dispatcher (Non Reservation Ver)
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
     <img width="327" alt="image" src="https://github.com/ivy-nguyen18/GKTW_Transportation/assets/73045170/809a9df9-60ab-4120-aa47-f46c179779a6">
  5. Click on the database you just connected to and at the top, there is a button with an image of a scroll and says "SQL"
     <img width="332" alt="image" src="https://github.com/ivy-nguyen18/GKTW_Transportation/assets/73045170/cfe202d9-92b7-4e8a-8655-c1b4e41c025b">
  6. Clicking this button will generate a SQL script specific to your database where you are able to write your queries
     <img width="1095" alt="image" src="https://github.com/ivy-nguyen18/GKTW_Transportation/assets/73045170/12601c6d-0be9-46be-8e94-5f1f94052a56">
     
# Running the Application
1. In the command prompt or terminal, go to the GKTW_Transportation directory using 'cd /path to directory/GKTW_Transportation'
2. Install required libraries using **pip install -r requirements.txt**
3. Run the program by compiling the program with **python app.py** (make sure you are in the same directory as the application to run this line, otherwise you need to the entire file path)
4. Launch the application by calling **streamlit run app.py**
![image](https://github.com/ivy-nguyen18/GKTW_Transportation/assets/73045170/8ba479fe-0f56-41de-99ff-b49f2ee6dc32)

## Attributes of the Application
The application is divided into three sections: Input, Standard Shuttle View, and ADA Shuttle View

### Input
The dispatcher gets this information from the guest as the guest calls in to make a reservation and adds them to their respective queue and into the database:

![image](https://github.com/ivy-nguyen18/GKTW_Transportation/assets/73045170/d9e517d6-948c-4a94-8169-737401b356d2)

### Standard Shuttle View and ADA Shuttle View
Depending on whether the ADA checkbox was checked, the guest will populate into the respective shuttle after clicking the "ADD" button.
The functionality of the tables displayed:
* Deleteable rows by either clicking the check box at the top of the table to select all and pressing the  *Backspace*  button on the keyboard:

  ![image](https://github.com/ivy-nguyen18/GKTW_Transportation/assets/73045170/1837381f-b8f1-4c75-83c3-15fe13ec926d)

  or clicking the row for particular guests and pressing the *Backspace* button on the keyboard:

  ![image](https://github.com/ivy-nguyen18/GKTW_Transportation/assets/73045170/0a5b608f-80d8-471a-aee5-2ae29c8e5de3)


* Status is a drop-down that has the options: Picking Up or Dropping Off

  ![image](https://github.com/ivy-nguyen18/GKTW_Transportation/assets/73045170/72f040f7-d8be-49b7-92ee-cf2307c713f9)

* Readjusting the column widths for a better visual experience by hovering on the line between the column headers

* **WARNING**: you are able to add guests to the table by hovering over the bottom of the table until a plus icon appears in the cell. HOWEVER, adding guests via this method does not save to the database. Thus, PLEASE ADD GUESTS VIA THE INPUT FORM.

   ![image](https://github.com/ivy-nguyen18/GKTW_Transportation/assets/73045170/1e508a49-6f32-4320-a201-73a5c05250c2)

## Functionality and Caveats
This application is able to:
* Run offline
* Does not save current state, so if the application is closed and reopened, everyone in the queue is lost. **DO NOT CLOSE THE APPLICATION**
* Even if the application closes prematurely, the guest data still persists in the databases. The only thing that is deleted is the current queue in the interface.

## Dispatcher Steps:
1. Guest calls in to request a shuttle, the dispatcher inputs the guest data into the form
2. Before adding the guest to the queue, the dispatcher must communicate with the driver to get their current status in the queue. They must delete guests and update the status column as necessary. 
3. After adding the guest to the queue, a wait time will be displayed at the bottom and the dispatcher relays this information back to the guest
  ![image](https://github.com/ivy-nguyen18/GKTW_Transportation/assets/73045170/e1b4ff88-dc0b-411a-91f8-18c2053550c9)
4. The dispatcher relays the guest pickup and dropoff location to the appropriate shuttle driver (ADA or Standard)
