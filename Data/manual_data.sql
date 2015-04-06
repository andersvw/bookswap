USE `bookswap`;

# Users
INSERT INTO user(`username`, `password`, `salt`, `created`, `last_login`) VALUES('andersvw', '31e71beb61d5f0a2055c07a2911191ae7534a91fe937cc0679e6e4ff11ffce1b99ab476c09b6b58c2ebf363771083fea8a9b88472c526970bf5f208f38c74d4f', 'test', NOW(), NOW());
INSERT INTO user(`username`, `password`, `salt`, `created`, `last_login`) VALUES('bcollins', '39d21a9a443703c0cfb7a82d93ca88c27a0bf91c13835a1aa660ef45d3eba0b17be1ae814fa74a7b07f07ab167a5869af753b880eea795418f0c84f9fb4f7d37', 'test', NOW(), NOW());
INSERT INTO user(`username`, `password`, `salt`, `created`, `last_login`) VALUES('bworatyla', '4558b3cb1c9d8f50bd659a1260c3395534e099a99de7cecc85effbe215fc41833b35d097aa416c7abc98616d1620269ddc4101d9d0bb5a3d9d29b3418d7a4d28', 'test', NOW(), NOW());

# Colleges
INSERT INTO college(`name`) VALUES('University of Delaware');
INSERT INTO college(`name`) VALUES('Delaware State University');

# User Information
INSERT INTO user_info(`user_id`, `college_id`, `first_name`, `last_name`, `email`, `address`, `phone_number`) VALUES(1, 1, 'Anders', 'Van Winkle', 'andersvw@udel.edu', '32 Prospect Avenue Newark, DE', '3028934380');
INSERT INTO user_info(`user_id`, `college_id`, `first_name`, `last_name`, `email`, `address`, `phone_number`) VALUES(2, 1, 'Brad', 'Collins', 'bcollinz@udel.edu', '21 Haines Street Newark, DE', '3028535989');
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
