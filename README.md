## PhysicalMediaLibrary
A database that manages a physical media rental system 

## What each table does
* Locations: Stores all the locations where the media is stored and loans managed
* Media_Types: Stores all the types of physical media available (Such as DVD, Vinyl, Cassette)
* Media_Names: Stores all the actual titles available (Movies, Music, etc)
* Media: The table that links Media_Types and Media_Names
* Renters: Stores the people who are currently renting media
* Active_Loans: Tracks every rental and links a renter to what media they currently have checked out, with checkout and expiration dates

#### USAGE

#### MORE STUFF
* First download the fishserver.py file and a client file of your chosing
* Find the ip of the server
* Launch the client of your chosing
* If using fishclient it will automatically ask for a port
* If using fishchatsharp you need to go to file and then connect to server
* Then you enter the ip, port, and username
* Then it will connect and you can start chatting

#### Video Demonstration
```mermaid
erDiagram
    Locations }|--o{ Media_Names : hold
    Locations ||--o{ Active_Loans : provide
    Active_Loans }| -- || Media_Names : contains
    Renters ||--o{ Active_Loans : create
    Media_Types ||--|{ Media : categorize
    Media }|--|| Media_Names : identify
    Locations {
        int id PK
        string name
        string address
    }
    Media_Types {
        int id PK
        string type
        string category
    }
    Renters {
        int id PK
        string name
        int num_loans
    }
    Active_Loans {
        int id PK
        int renter_id FK
        int media_id FK
        date check_out_Date
        date loan_expiration
        int home_id FK
    }
    Media_Names {
        int id PK
        int location_id FK
        string name
        date acquiry_Date
        int quantity
        int type_id FK
    }
    Media {
        int id PK
        int media_type_id FK
        int media_name_id FK
    }
```
