DROP TABLE User_info;

CREATE TABLE User_info(
	user_id int PRIMARY KEY, -- Student ID
	username nvarchar(255),
	user_password nvarchar(255), -- > 8 character
	email nvarchar(255), -- check validation
	user_type int -- admin(1) or participant(0)
);

INSERT INTO User_info
VALUES 
(20210272, 'Nguyen Dang Duy', 'aothatday123', 'dontunderstandyou12345@gmail.com', 1),
(20215254, 'Bui Duc Viet', 'vietdepzai123', 'viet.bd215254@sis.hust.edu.vn', 1),
(20215182, 'Tran Thuy Chau', 'chauxinggai123', 'chau.tt215182@sis.hust.edu.vn', 1),
(20215207, 'Pham Quang Huy', 'huydepzai123', 'huy.pq215207@sis.hust.edu.vn', 1);

SELECT * FROM User_info;

SELECT * FROM User_info
WHERE User_info.user_id = 20210272
OR User_info.username = 'khabanh';