DROP DATABASE IF EXISTS PhysicalMedia;
CREATE DATABASE PhysicalMedia;
USE PhysicalMedia;

CREATE TABLE Locations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(75) NOT NULL,
    address VARCHAR(75) NOT NULL
);

CREATE TABLE Media_Types (
    id INT AUTO_INCREMENT PRIMARY KEY,
    type VARCHAR(50) NOT NULL,
    category VARCHAR(50) NOT NULL
);

CREATE TABLE Renters (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    num_loans INT NOT NULL
);

CREATE TABLE Media_Names (
    id INT AUTO_INCREMENT PRIMARY KEY,
    location_id INT,
    name VARCHAR(75),
    acquiry_date DATE,
    quantity INT,
    type_id INT,
    FOREIGN KEY (location_id) REFERENCES Locations(id),
    FOREIGN KEY (type_id) REFERENCES Media_Types(id)
);

CREATE TABLE Media (
    id INT AUTO_INCREMENT PRIMARY KEY,
    media_type_id INT,
    media_name_id INT,
    FOREIGN KEY (media_type_id) REFERENCES Media_Types(id),
    FOREIGN KEY (media_name_id) REFERENCES Media_Names(id)
);

CREATE TABLE Active_Loans (
    id INT AUTO_INCREMENT PRIMARY KEY,
    renter_id INT,
    media_id INT,
    home_id INT,
    check_out_date DATE,
    loan_expiration DATE,
    FOREIGN KEY (renter_id) REFERENCES Renters(id),
    FOREIGN KEY (media_id) REFERENCES Media_Names(id),
    FOREIGN KEY (home_id) REFERENCES Locations(id)
);