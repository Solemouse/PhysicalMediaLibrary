DROP DATABASE IF EXISTS PhysicalMedia;
CREATE DATABASE PhysicalMedia;
USE PhysicalMedia;

CREATE TABLE Locations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(75) NOT NULL,
    address VARCHAR(75) NOT NULL,
    UNIQUE (name, address)
);

CREATE TABLE Media_Types (
    id INT AUTO_INCREMENT PRIMARY KEY,
    type VARCHAR(50) NOT NULL,
    category VARCHAR(50) NOT NULL,
    UNIQUE (type)
);

CREATE TABLE Renters (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    num_loans INT NOT NULL,
    CHECK (num_loans >= 0)
);

CREATE TABLE Media_Names (
    id INT AUTO_INCREMENT PRIMARY KEY,
    location_id INT,
    name VARCHAR(75),
    acquiry_date DATE,
    quantity INT,
    type_id INT,
    CHECK (quantity >= 0),
    FOREIGN KEY (location_id) REFERENCES Locations(id) ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (type_id) REFERENCES Media_Types(id) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE Media (
    id INT AUTO_INCREMENT PRIMARY KEY,
    media_type_id INT,
    media_name_id INT,
    UNIQUE (media_type_id, media_name_id),
    FOREIGN KEY (media_type_id) REFERENCES Media_Types(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (media_name_id) REFERENCES Media_Names(id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Active_Loans (
    id INT AUTO_INCREMENT PRIMARY KEY,
    renter_id INT,
    media_id INT,
    home_id INT,
    check_out_date DATE DEFAULT (CURRENT_DATE),
    loan_expiration DATE NOT NULL,
    CHECK (loan_expiration > check_out_date),
    FOREIGN KEY (renter_id) REFERENCES Renters(id) ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (media_id) REFERENCES Media_Names(id) ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (home_id) REFERENCES Locations(id) ON DELETE SET NULL ON UPDATE CASCADE
);