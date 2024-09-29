CREATE TABLE User (
    id INT PRIMARY KEY,
    username VARCHAR(255),
    password VARCHAR(255),
    name VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE Telephone (
    telephone VARCHAR(255),
    id INT PRIMARY KEY,
    fk_User_id INT
);

ALTER TABLE Telephone ADD COLUMN fk_User_id CONSTRAINT FK_Telephone_2
    REFERENCES User (id)
    ON DELETE CASCADE;