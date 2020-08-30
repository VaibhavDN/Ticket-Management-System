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
    
#### View endpoint
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
        
    Query result 1
    
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
