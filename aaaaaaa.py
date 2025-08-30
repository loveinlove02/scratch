create table member (
	user_id 	INT PRIMARY KEY,
    user_name	VARCHAR(20) NOT NULL, 
    join_date	DATE NOT NULL,
    agree		BIT
);
