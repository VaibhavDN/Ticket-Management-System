### Ticket-Booking-System
Django server to handle booking, updating and viewing ticket information

- [x] Book a ticket using a user’s name, phone number, and timings
- [x] Update a ticket timing
- [x] View all the tickets for a particular time
- [x] Delete a particular ticket
- [x] View the user’s details based on the ticket id
- [x] Mark a ticket as expired if there is a diff of 8 hours between the ticket timing and current time
- [x] For a particular timing, a maximum of 20 tickets can be booked
- [ ] Create a proper readme for your project
- [x] Delete all the tickets which are expired automatically
- [x] Write the tests for all the endpoints

Note: Attach a screenshot of your postman while testing your application

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

Currently there are 3 types of supported queries
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

#### Note: If "id" is specified with "query": "datetime" then it will be ignored. To query by "id" use "query": "id" instead.
****

3. "query": "all"
    * Returns all the entries in the database
    
    Query example
    
        {
            "query": "all"
        }
        
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
    
    Some queries return error, common ones are:
    
    Query result (Failure: 20 entries already exist for this time)
    
        {
            "status": false,
            "message": "20 entries already exist for this time"
        }
        
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
3. Specify any optional field to replace the old field data with new one

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
        
    Query result (Failure: Id not present in the database)
    
        {
            "status": false,
            "message": "Id not found"
        }
        
****

