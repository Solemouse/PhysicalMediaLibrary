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
* Make sure you have the database with all the entries inputted and created
* Python3 the main.py file to begin utilizing the database
* Select options based on the list
##### When it asks you to select an entity from a list you have to use the ID number

#### Video Demonstration
https://github.com/Solemouse/PhysicalMediaLibrary/blob/main/2026-05-04%2023-35-48.mp4


#### ERD Diagram
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


### Reflection
As it turns out, getting things to work exactly as you want them to in Python with MySQL is rather difficult, and docker likes to be a pain.
