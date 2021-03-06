CREATE DATABASE gradesDataFinal;
use gradesDataFinal;

CREATE TABLE IF NOT EXISTS grades (
    `id` int auto_increment,
    `Last_name` VARCHAR(9) CHARACTER SET utf8,
    `First_name` VARCHAR(16) CHARACTER SET utf8,
    `SSN` VARCHAR(21) CHARACTER SET utf8,
    `Test1` VARCHAR(14) CHARACTER SET utf8,
    `Test2` NUMERIC(3, 1),
    `Test3` NUMERIC(4, 1),
    `Test4` NUMERIC(3, 1),
    `Final` VARCHAR(8) CHARACTER SET utf8,
    `Grade` VARCHAR(7) CHARACTER SET utf8,
    primary key (id)
);
INSERT INTO grades (Last_name, First_name, SSN, Test1, Test2, Test3, Test4, Final, Grade) VALUES
('Alfalfa','Aloysius','123-45-6789',40.0,90.0,100.0,83.0,49.0,'D-'),
('Alfred','University','123-12-1234',41.0,97.0,96.0,97.0,48.0,'D+'),
('Gerty','Gramma','567-89-0123',41.0,80.0,60.0,40.0,44.0,'C'),
('Android','Electric','087-65-4321',42.0,23.0,36.0,45.0,47.0,'B-'),
('Bumpkin','Fred','456-78-9012',43.0,78.0,88.0,77.0,45.0,'A-'),
('Rubble','Betty','234-56-7890',44.0,90.0,80.0,90.0,46.0,'C-'),
('Noshow','Cecil','345-67-8901',45.0,11.0,-1.0,4.0,43.0,'F'),
('Buff','Bif','632-79-9939',46.0,20.0,30.0,40.0,50.0,'B+'),
('Airpump','Andrew','223-45-6789',49.0,90.0,100.0,83.0,50.0,'A'),
('Backus','Jim','143-12-1234',48.0,1.0,97.0,96.0,97.0,'A+'),
('Carnivore','Art','565-89-0123',44.0,1.0,80.0,60.0,40.0,'D+'),
('Dandy','Jim','087-75-4321',47.0,1.0,23.0,36.0,45.0,'C+'),
('Elephant','Ima','456-71-9012',45.0,1.0,78.0,88.0,77.0,'B-'),
('Franklin','Benny','234-56-2890',50.0,1.0,90.0,80.0,90.0,'B-'),
('George','Boy','345-67-3901',40.0,1.0,11.0,-1.0,4.0,'B'),
('Heffalump','Harvey','632-79-9439',30.0,1.0,20.0,30.0,40.0,'C');

CREATE TABLE IF NOT EXISTS login (
    `id` int auto_increment,
    `firstname` VARCHAR(50),
    `lastname` VARCHAR(50),
    `email` VARCHAR(50) UNIQUE,
    `username` VARCHAR(50) UNIQUE,
    `password` VARCHAR(50),
    `verification_code` int,
    primary key (`id`)
);

INSERT INTO login (firstname, lastname, email, username, password, verification_code) VALUES ('Super', 'User','ramanikaran@gmail.com', 'admin','password', 123456),
                                                                   ('Karan','Ramani','kjr27@njit.edu','karanramani', 'password', 565188);


# CREATE TABLE IF NOT EXISTS events (
#     `id` int auto_increment,
#     `name` varchar(255) NOT NULL,
#     `event` varchar(255) NOT NULL,
#     `dayweek` VARCHAR(50) NOT NULL,
#     `start_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
#     `end_date` timestamp NOT NULL,
#     primary key (id)
# );
# INSERT INTO events (name, event, dayweek, start_date, end_date) VALUES
# ('sam','HappyHour','Wed','2020-12-16 12:00:00','2020-12-16 13:00:00');