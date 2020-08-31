### Ticket-Management-System
Django REST API to handle booking, updating, viewing and deleting ticket information

- [x] Book a ticket using a user’s name, phone number, and timings
- [x] Update a ticket timing
- [x] View all the tickets for a particular time
- [x] Delete a particular ticket
- [x] View the user’s details based on the ticket id
- [x] Mark a ticket as expired if there is a diff of 8 hours between the ticket timing and current time
- [x] For a particular timing, a maximum of 20 tickets can be booked
- [x] Create a proper readme for your project
- [x] Delete all the tickets which are expired automatically
- [x] Write the tests for all the endpoints

Note: Attach a screenshot of your postman while testing your application

#### Server is hosted on Heroku: https://tmsvaibhav.herokuapp.com/

#### Endpoints: (POST requests only)
- Book: https://tmsvaibhav.herokuapp.com/book/
- View: https://tmsvaibhav.herokuapp.com/view/
- Update: https://tmsvaibhav.herokuapp.com/update/edit/
- Delete: https://tmsvaibhav.herokuapp.com/update/delete/
- Demo site: https://tmsvaibhav.herokuapp.com/panel/book/

#### Some useful information
- Server: Django
- Database: SQLite
- REST API: Django-rest-framework
- API testing: Postman
- Scheduler: Advanced Python Scheduler


#### Project structure
    Ticket Booking System -|
                           |- TMS -|
                                   |- settings.py
                           |- book
                           |- panel
                           |- update
                           |- view
                           |- templates -|
                                         |- panel
                           |- Postman Test
                           |- manage.py
                           |- scheduledTask.py
                           

#### API Endpoints available
View ticket information

    /view/
    
Book ticket

    /book/
   
Update information

    /update/edit/
    
Delete ticket

    /update/delete/
    
### View endpoint
Fields
* query (Required field)
* id (Required if query is set to "id")
* date  (Optional)
* time  (Optional)

Currently, there are 3 types of supported queries
1. "query": "id"

    * Requires an id to be specified
    
    Query example

        {
            "query": "id",
            "id": "86817bc1-1b27-4aa7-884d-7781cf0de5ac"
        }
        
    Query result (Success: Ticket Id found)
    
        [
            {
                "ticketId": "86817bc1-1b27-4aa7-884d-7781cf0de5ac",
                "firstname": "Vaibhav",
                "lastname": "Dwivedi",
                "phone_number": 1234567890,
                "date": "1-09-2020",
                "time_hours": 18,
                "time_minutes": 0,
                "time_seconds": 0,
                "expired": false
            }
        ]

    Query result (Failure: Ticket Id NOT found)
    
        {
            "status": false,
            "message": "Record not found"
        }

    Query result (Failure: Invalid UUID)
    
        {
            "status": false,
            "message": "['“86817bc1-1b27-4aa7-884-7781dc0de5ac” is not a valid UUID.']"
        }
        
    <details><summary>Click here to view the screenshot</summary>
        <p align="center">
            <img width="100%" src="https://github.com/VaibhavDN/Ticket-Booking-System/blob/master/Screenshots/view/viewID.jpg">
        </p>
    </details>
        
****

2. "query": "datetime"

    * Specify date (Optional)
    * Specify time (Optional)
    
    Based on the fields provided API will return the results with best match
    
    Query example 1
    
        {
            "query": "datetime",
            "date": "1-09-2020",
            "time": "9:00:00"
        }
        
    Query result 1 (All the tickets having date 1-09-2020 and time 9:00:00 are returned)
    
        [
            {
                "ticketId": "cf5b7944-e4cc-4dd3-aab4-55e84fc03616",
                "firstname": "Saksham",
                "lastname": "Modi",
                "phone_number": 1128789022,
                "date": "1-09-2020",
                "time_hours": 9,
                "time_minutes": 0,
                "time_seconds": 0,
                "expired": false
            },
            {
                "ticketId": "0f42d9c8-5eb9-4a80-8a8f-112bb5c572a7",
                "firstname": "Varun",
                "lastname": "Mittal",
                "phone_number": 5558789022,
                "date": "1-09-2020",
                "time_hours": 9,
                "time_minutes": 0,
                "time_seconds": 0,
                "expired": false
            }
        ]
        
    <details><summary>Click here to view the screenshot</summary>
        <p align="center">
            <img width="100%" src="https://github.com/VaibhavDN/Ticket-Booking-System/blob/master/Screenshots/view/viewDateTime.jpg">
        </p>
    </details>
        
    Query example 2
    
        {
            "query": "datetime",
            "date": "1-09-2020"
        }
    
    Query result 2 (All the tickets having date 1-09-2020 and any time are returned)
        
        [
            {
                "ticketId": "86817bc1-1b27-4aa7-884d-7781cf0de5ac",
                "firstname": "Vaibhav",
                "lastname": "Dwivedi",
                "phone_number": 1234567890,
                "date": "1-09-2020",
                "time_hours": 18,
                "time_minutes": 0,
                "time_seconds": 0,
                "expired": false
            },
            {
                "ticketId": "cf5b7944-e4cc-4dd3-aab4-55e84fc03616",
                "firstname": "Saksham",
                "lastname": "Modi",
                "phone_number": 1128789022,
                "date": "1-09-2020",
                "time_hours": 9,
                "time_minutes": 0,
                "time_seconds": 0,
                "expired": false
            },
            {
                "ticketId": "0f42d9c8-5eb9-4a80-8a8f-112bb5c572a7",
                "firstname": "Varun",
                "lastname": "Mittal",
                "phone_number": 5558789022,
                "date": "1-09-2020",
                "time_hours": 9,
                "time_minutes": 0,
                "time_seconds": 0,
                "expired": false
            }
        ]
        
    <details><summary>Click here to view the screenshot</summary>
        <p align="center">
            <img width="100%" src="https://github.com/VaibhavDN/Ticket-Booking-System/blob/master/Screenshots/view/viewDate.jpg">
        </p>
    </details>
        
    Query example 3
    
        {
            "query": "datetime",
            "time": "9:00:00"
        }
        
    Query result 3 Query result 2 (All the tickets having any date and time 9:00:00 are returned)
    
        [
            {
                "ticketId": "cf5b7944-e4cc-4dd3-aab4-55e84fc03616",
                "firstname": "Saksham",
                "lastname": "Modi",
                "phone_number": 1128789022,
                "date": "1-09-2020",
                "time_hours": 9,
                "time_minutes": 0,
                "time_seconds": 0,
                "expired": false
            },
            {
                "ticketId": "0f42d9c8-5eb9-4a80-8a8f-112bb5c572a7",
                "firstname": "Varun",
                "lastname": "Mittal",
                "phone_number": 5558789022,
                "date": "1-09-2020",
                "time_hours": 9,
                "time_minutes": 0,
                "time_seconds": 0,
                "expired": false
            },
            {
                "ticketId": "b7e52464-96ca-4b87-a2fb-55ff216a7dcf",
                "firstname": "Desh",
                "lastname": "Bandha",
                "phone_number": 8789022777,
                "date": "2-09-2020",
                "time_hours": 9,
                "time_minutes": 0,
                "time_seconds": 0,
                "expired": false
            }
        ]
        
    <details><summary>Click here to view the screenshot</summary>
        <p align="center">
            <img width="100%" src="https://github.com/VaibhavDN/Ticket-Booking-System/blob/master/Screenshots/view/viewTime.jpg">
        </p>
    </details>

#### Note: If "id" is specified with "query": "datetime" then it will be ignored. To query by "id" use "query": "id" instead.
****

3. "query": "all"
    * Returns all the entries in the database
    
    Query example
    
        {
            "query": "all"
        }
        
    <details><summary>Click here to view the screenshot</summary>
        <p align="center">
            <img width="100%" src="https://github.com/VaibhavDN/Ticket-Booking-System/blob/master/Screenshots/queryAll.jpg">
        </p>
    </details>
        
#### Note: When using "query": "all" all other fields are ignored.

****

### Book endpoint
#### Note: There can NOT be more than 20 entries at a given time
Fields:
- firstname (Required)
- lastname (Required)
- phone_number (Required)
- date (Required)
- time (Required)

    Query example
    
        {
            "firstname": "Ishan",
            "lastname": "Dixit",
            "phone_number": 9927898022,
            "date": "12-09-2020",
            "time": "21:00:0"
        }
        
    Query result (Success: Returns ticket id of the newly created ticket)
    
        {
            "status": true,
            "message": "Success",
            "id": "70a67513-51cd-4487-87eb-817aa9a07a53"
        }
        
    <details><summary>Click here to view the screenshot</summary>
        <p align="center">
            <img width="100%" src="https://github.com/VaibhavDN/Ticket-Booking-System/blob/master/Screenshots/book/bookSuccess.jpg">
        </p>
    </details>
    
    Some queries return error, common ones are:
    
    Query result (Failure: 20 entries already exist for this time)
    
        {
            "status": false,
            "message": "20 entries already exist for this time"
        }
        
    <details><summary>Click here to view the screenshot</summary>
        <p align="center">
            <img width="100%" src="https://github.com/VaibhavDN/Ticket-Booking-System/blob/master/Screenshots/morethantwenty.jpg">
        </p>
    </details>
        
    Query result (Failure: If one or more parameters are missing)
    
        {
            "status": false,
            "message": "Missing required parameters"
        }

****

### Update endpoint [/update/edit/]
Fields:
- id (Required)
- firstname (Optional)
- lastname (Optional)
- phone_number (Optional)
- date (Optional)
- time (Optional)

Note:
1. "id" is the only required field field
2. Id can not be changed
3. Specify any optional field to replace the old field data with the new one

    Query example
    
        {
            "id": "86817bc1-1b27-4aa7-884d-7781cf0de5ac",
            "time": "18:30",
            "date": "1-09-2020"
        }
        
    Query result (Success: date and time values are updated)
    
        {
            "status": true,
            "message": "Success"
        }
        
    <details><summary>Click here to view the screenshot</summary>
        <p align="center">
            <img width="100%" src="https://github.com/VaibhavDN/Ticket-Booking-System/blob/master/Screenshots/edit/updateEditSuccess.jpg">
            <img width="100%" src="https://github.com/VaibhavDN/Ticket-Booking-System/blob/master/Screenshots/edit/updateEdit.jpg">
        </p>
    </details>
        
    Query result (Failure: Id specified is not present in the database)
    
        {
            "status": false,
            "message": "Id not found"
        }
        
****

### Delete endpoint [/update/delete/]
Fields:
- id (Required)

Note:
1. All the details of the ticket whose "id" is specified are permanently deleted
2. All other fields will be ignored 

    Query example
    
        {
            "id": "f20a98ba-e833-4108-b196-a2153406395b"
        }
        
    Query result (Success: Ticket details are deleted)
    
        {
            "status": true,
            "message": "Success"
        }
        
    <details><summary>Click here to view the screenshot</summary>
        <p align="center">
            <img width="100%" src="https://github.com/VaibhavDN/Ticket-Booking-System/blob/master/Screenshots/delete/deleteTicket.jpg">
        </p>
    </details>
        
    Query result (Failure: Id not present in the database)
    
        {
            "status": false,
            "message": "Id not found"
        }
        
****

### Scheduler [Advanced Python Scheduler]
The APScheduler is used to mark and delete the tickets older than 8 hours (scheduledTask.py).

Why APScheduler?

As highlighted in the official documentation, "APScheduler can be used as a cross-platform, application specific replacement to platform specific schedulers, such as the cron daemon or the Windows task scheduler."

It is cross-platform, light-weight python scheduler which is exactly what we needed.

The scheduler is currently scheduled to run every 1 minute. It calculates the difference between the "time of the ticket" and the "current time" for each entry in the database. If the difference is less than -8 the ticket is marked as expired and deleted. Scheduler needs to be started only once.

To start the scheduler run:

    python scheduledTask.py
    
<details><summary>Click here to view the screenshot</summary>
    <p align="center">
        <img width="100%" src="https://github.com/VaibhavDN/Ticket-Booking-System/blob/master/Screenshots/scheduledDelete.jpg">
    </p>
</details>
    
****

### Postman Tests
Postman tests are exported in Postman Task directory. Below are some screenshots.

- Book collection

<details><summary>Click here to view the screenshot</summary>
    <p align="center">
        <img width="100%" src="https://github.com/VaibhavDN/Ticket-Booking-System/blob/master/Screenshots/PM%20collections/postman_book_collection.jpg">
    </p>
</details>

- Update collection

<details><summary>Click here to view the screenshot</summary>
    <p align="center">
        <img width="100%" src="https://github.com/VaibhavDN/Ticket-Booking-System/blob/master/Screenshots/PM%20collections/postman_edit_collection.jpg">
    </p>
</details>

- View collection

<details><summary>Click here to view the screenshot</summary>
    <p align="center">
        <img width="100%" src="https://github.com/VaibhavDN/Ticket-Booking-System/blob/master/Screenshots/PM%20collections/postman_view_collection.jpg">
    </p>
</details>

- View tests

<details><summary>Click here to view the screenshot</summary>
    <p align="center">
        <img width="100%" src="https://github.com/VaibhavDN/Ticket-Booking-System/blob/master/Screenshots/view/viewTest.jpg">
        <img width="100%" src="https://github.com/VaibhavDN/Ticket-Booking-System/blob/master/Screenshots/view/viewTest2.jpg">
        <img width="100%" src="https://github.com/VaibhavDN/Ticket-Booking-System/blob/master/Screenshots/view/viewTest3.jpg">
        <img width="100%" src="https://github.com/VaibhavDN/Ticket-Booking-System/blob/master/Screenshots/view/viewTest4.jpg">
    </p>
</details>

- Book tests

<details><summary>Click here to view the screenshot</summary>
    <p align="center">
        <img width="100%" src="https://github.com/VaibhavDN/Ticket-Booking-System/blob/master/Screenshots/book/bookFailedTestDate.jpg">
        <img width="100%" src="https://github.com/VaibhavDN/Ticket-Booking-System/blob/master/Screenshots/book/bookSuccessTest.jpg">
    </p>
</details>

- Update tests

<details><summary>Click here to view the screenshot</summary>
    <p align="center">
        <img width="100%" src="https://github.com/VaibhavDN/Ticket-Booking-System/blob/master/Screenshots/edit/updateEditTest1.jpg">
        <img width="100%" src="https://github.com/VaibhavDN/Ticket-Booking-System/blob/master/Screenshots/edit/updateEditTest2.jpg">
    </p>
</details>


### Some common error messages

#### Incorrect time format

Time must be specified in one of these 3 formats
1. 12:30:50 (HH:MM:SS)
2. 12:30 (HH:MM)
3. 12 (HH)

Note: HH, MM and SS all must be integers

Else an error message like the following will be returned

Error:

    {
        "status": false,
        "message": "Incorrect time format"
    }
    
<details><summary>Click here to view the screenshot</summary>
    <p align="center">
        <img width="100%" src="https://github.com/VaibhavDN/Ticket-Booking-System/blob/master/Screenshots/edit/updateEditFailedTime.jpg">
        <img width="100%" src="https://github.com/VaibhavDN/Ticket-Booking-System/blob/master/Screenshots/book/bookFailedTime.jpg">
    </p>
</details>

#### Incorrect date format

Date must be specified strictly in the following format
1. 31-08-2020 (dd-mm-yyyy)

Note: dd, mm and yyyy all must be integers

Else an error message like the following will be returned

Error:

    {
        "status": false,
        "message": "Incorrect date format. Should be dd-mm-yyyy"
    }
    
<details><summary>Click here to view the screenshot</summary>
    <p align="center">
        <img width="100%" src="https://github.com/VaibhavDN/Ticket-Booking-System/blob/master/Screenshots/edit/updateEditFailedDate.jpg">
        <img width="100%" src="https://github.com/VaibhavDN/Ticket-Booking-System/blob/master/Screenshots/book/bookFailedDate.jpg">
    </p>
</details>

#### Invalid phone number
Phone number must be of 10 digits

Else an error message like the following will be returned

Error:

    {
        "status": false,
        "message": "Phone number must be of 10 digits"
    }
    
<details><summary>Click here to view the screenshot</summary>
    <p align="center">
        <img width="100%" src="https://github.com/VaibhavDN/Ticket-Booking-System/blob/master/Screenshots/book/bookFailedPhone.jpg">
    </p>
</details>
    
#### Id not found
If id specified is not present in the database following error message will be returned

Error:

    {
        "status": false,
        "message": "Record not found"
    }
    
<details><summary>Click here to view the screenshot</summary>
    <p align="center">
        <img width="100%" src="https://github.com/VaibhavDN/Ticket-Booking-System/blob/master/Screenshots/view/viewFailID.jpg">
    </p>
</details>
    
****

### Booking site demo [/panel/book/]
Visit /panel/book/ to run the demo site.

Site demonstrates how to take input from the user using a HTML form and POST the form details after converting them to JSON format.

Site takes name, date and time from the user as input and returns ticket ID of the newly created ticket.

<details><summary>Click here to view the screenshot</summary>
    <p align="center">
        <img width="100%" src="https://github.com/VaibhavDN/Ticket-Booking-System/blob/master/Screenshots/demosite.jpg">
    </p>
</details>

****
