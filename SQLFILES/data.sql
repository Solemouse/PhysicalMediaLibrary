INSERT INTO Locations (name, address) VALUES
	('Belmar', '555 S Allison Pkwy, Lakewood, CO 80226'),
	('Golden', '1019 10th St, Golden, CO 80401'),
	('Denver', '10 W 14th Ave, Denver, CO 80204'),
    ('Evergreen', '5000 County Hwy 73, Evergreen, CO 80439'),
	('Columbine', '7706 W Bowles Ave, Littleton, CO 80123'),
	('Englewood', '1000 Englewood Pkwy, Englewood, CO 80110'),
    ('Pueblo', '1315 E 7th St, Pueblo, CO 81001'),
	('Durango', '1900 E 3rd Ave, Durango, CO 81301'),
	('Cortez', '202 N Park St, Cortez, CO 81321'),
    ('Arvada', '7525 W 57th Ave, Arvada, CO 80002');

INSERT INTO Renters (name, num_loans) VALUES
    ('Jacob Dreier', '5'),
    ('Owen Milota', '3'),
    ('Timoty Siebrecht', '8'),
    ('Aiden Sundermann', '2'),
    ('Pascal Davis', '1'),
    ('Grace Person', '6'),
    ('Evan Santos', '13'),
    ('Carson Rickard', '4'),
    ('Ronan Hubbard', '6'),
    ('Jacob Casey', '1');

INSERT INTO Media_Types (type, category) VALUES
    ('DVD', 'Movie'),
    ('Blu-Ray', 'Movie'),
    ('VHS', 'Movie'),
    ('CD', 'Music'),
    ('Vinyl', 'Music'),
    ('Cassette', 'Music'),
    ('VCD', 'Movie'),
    ('LaserDisk', 'Movie'),
    ('8-TrackTape', 'Music'),
    ('BetaMax', 'Movie');
   
INSERT INTO Media_Names (location_id, name, acquiry_date, quantity, type_id) VALUES
    (3, 'Tomorrowland', '2020-03-15', 3, 1),
    (4, 'Startrek into darkness', '2023-07-20', 4, 2),
    (7, 'Wallace & Grommit: A Grand Day Out', '1995-04-20', 1, 3),
    (5, '90125', '2022-04-08', 5, 4),
    (6, 'Interstellar Album', '2026-01-29', 1, 5),
    (2, 'Top Gun Soundtrack', '2021-02-15', 2, 6),
    (8, 'The Simpsons Greatest Hits', '2019-05-18', 3, 7),
    (9, 'Back to the Future', '1990-07-23', 3, 8),
    (10, 'Elvis Burning Love', '2001-04-07', 3, 9),
    (1, 'A Christmas Carol', '1999-02-27', 3, 10);

INSERT INTO Media (media_type_id, media_name_id) VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10);

INSERT INTO Active_Loans (renter_id, media_id, home_id, check_out_date, loan_expiration) VALUES
    (1, 1, 3, '2024-01-10', '2024-02-10'),
    (2, 2, 4, '2024-02-15', '2024-03-15'),
    (3, 3, 7, '2024-03-01', '2024-04-01'),
    (4, 4, 5, '2024-03-10', '2024-04-10'),
    (5, 5, 6, '2024-04-01', '2024-05-01'),
    (6, 6, 2, '2024-04-10', '2024-05-10'),
    (7, 7, 8, '2024-05-01', '2024-06-01'),
    (8, 8, 9, '2024-05-15', '2024-06-15'),
    (9, 9, 10, '2024-06-01', '2024-07-01'),
    (10, 10, 1, '2024-06-10', '2024-07-10');


