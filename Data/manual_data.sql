USE `bookswap`;

# Users
INSERT INTO user(username, password, salt) VALUES('andersvw', 'WcDYdWCOinWESwuAANDbAl8baMT0Cr18CLq7EiXAd74=', 'testtesttesttest');
INSERT INTO user(username, password, salt) VALUES('bcollins', 'WcDYdWCOinWESwuAANDbAl8baMT0Cr18CLq7EiXAd74=', 'testtesttesttest');
INSERT INTO user(username, password, salt) VALUES('bworatyla', 'WcDYdWCOinWESwuAANDbAl8baMT0Cr18CLq7EiXAd74=', 'testtesttesttest');

# Colleges
INSERT INTO college(`name`) VALUES('University of Delaware');
INSERT INTO college(`name`) VALUES('Delaware State University');

# User Information
INSERT INTO user_info(`user_id`, `college_id`, `first_name`, `last_name`, `email`, `address`, `phone_number`) VALUES(1, 1, 'Anders', 'Van Winkle', 'andersvw@udel.edu', '32 Prospect Avenue Newark, DE', '3028934380');
INSERT INTO user_info(`user_id`, `college_id`, `first_name`, `last_name`, `email`, `address`, `phone_number`) VALUES(2, 1, 'Brad', 'Collins', 'icon@udel.edu', '21 Haines Street Newark, DE', '3028535989');
INSERT INTO user_info(`user_id`, `college_id`, `first_name`, `last_name`, `email`, `address`, `phone_number`) VALUES(3, 1, 'Ben', 'Woratyla', 'woratyla@udel.edu', '21 Haines Street Newark, DE', '3026026506');

# Authors
INSERT INTO author(`name`) VALUES('Roger C. Park');
INSERT INTO author(`name`) VALUES('Richard D. Friedman');
INSERT INTO author(`name`) VALUES('Bill Nelson');
INSERT INTO author(`name`) VALUES('Amelia Phillips');
INSERT INTO author(`name`) VALUES('Christopher Steuart');

# Books
INSERT INTO book(`isbn`, `title`, `edition`) VALUES('9781609301385', 'Evidence, Case and Materials', 12);
INSERT INTO book(`isbn`, `title`, `edition`) VALUES('9781285060033', 'Guide to Computer Forensics and Investigations', 5);

# Author to Book pairings
INSERT INTO author_book(`author_id`, `book_id`) VALUES(1, 1);
INSERT INTO author_book(`author_id`, `book_id`) VALUES(2, 1);
INSERT INTO author_book(`author_id`, `book_id`) VALUES(3, 2);
INSERT INTO author_book(`author_id`, `book_id`) VALUES(4, 2);
INSERT INTO author_book(`author_id`, `book_id`) VALUES(5, 2);

# Listings
INSERT INTO listing(`user_id`, `book_id`, `price`, `book_condition`, `description`) VALUES(1, 1, 50.00, 'Good', 'This text is required for CRJU457');
INSERT INTO listing(`user_id`, `book_id`, `price`, `book_condition`, `description`) VALUES(1, 2, 50.00, 'Very Good', 'This text is required for CPEG495');

# Courses
INSERT INTO course(`college_id`, `title`, `abbreviation`, `number`) VALUES(1, 'Criminal Evidence', 'CRJU', '457010');
INSERT INTO course(`college_id`, `title`, `abbreviation`, `number`) VALUES(1, 'Digital Forensics', 'CPEG', '495010');

# Course to Book pairings
INSERT INTO course_book(`course_id`, `book_id`) VALUES(1, 1);
INSERT INTO course_book(`course_id`, `book_id`) VALUES(2, 2);
