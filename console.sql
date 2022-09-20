CREATE DATABASE landlysthotelDB;
USE landlysthotelDB;

CREATE TABLE emails (
    emailID int NOT NULL AUTO_INCREMENT,
    email varchar(255),
    PRIMARY KEY (emailID));
CREATE TABLE expansions (
    expansionID int NOT NULL AUTO_INCREMENT,
    kitchen bool,
    jacuzzi bool,
    double_bed bool,
    balcony bool,
    bath bool,
    PRIMARY KEY (expansionID));
CREATE TABLE contact_info (
    contacttID int NOT NULL AUTO_INCREMENT,
    phonenumber int,
    emailID int,
    FOREIGN KEY (emailID) REFERENCES emails(emailID),
    PRIMARY KEY (contactID));
CREATE TABLE rooms (
    roomID int NOT NULL AUTO_INCREMENT,
    price int,
    expansionID int,
    booked bool,
    room_number int,
    FOREIGN KEY (expansionID) REFERENCES expansions(expansionID),
    PRIMARY KEY (roomID));
CREATE TABLE guest (
    guestID int NOT NULL AUTO_INCREMENT,
    zipcode int,
    address varchar(255),
    fname varchar(255),
    lname varchar(255),
    contactID int,
    FOREIGN KEY (contactID) REFERENCES contact_info(contactID) ,
    PRIMARY KEY (guestID));
CREATE TABLE bookings (
    bookingID int NOT NULL AUTO_INCREMENT,
    roomID int,
    start_date VARCHAR(10),
    end_date VARCHAR(10),
    guestID int,
    PRIMARY KEY (bookingID),
    FOREIGN KEY (roomID) REFERENCES rooms(roomID),
    FOREIGN KEY (guestID) REFERENCES guest(guestID));



INSERT INTO expansions (kitchen, jacuzzi, double_bed, balcony, bath) VALUES (0, 0, 1, 0, 1), (0, 0, 1, 0, 0), (0, 1, 1, 1, 0),
                                                                            (1, 1, 1, 1, 0), (0, 1, 1, 0, 1), (0, 0, 0, 0, 1),
                                                                            (0, 0, 0, 1, 1), (0, 0, 0, 1, 0), (0, 0, 1, 1, 0);


INSERT INTO rooms (room_number) VALUES (100), (101), (102), (103), (104), (105), (106), (107), (108), (109), (110),
                                       (200), (201), (202), (203), (204), (205), (206), (207), (208), (209),
                                       (300), (301), (302), (303), (304), (305), (306), (307), (308), (309),
                                       (400), (401), (402), (403), (404), (405), (406), (407), (408), (409),
                                       (500), (501), (502), (503), (504), (505), (506), (507), (508), (509), (510);
UPDATE rooms SET booked = 0 WHERE booked IS NULL;
