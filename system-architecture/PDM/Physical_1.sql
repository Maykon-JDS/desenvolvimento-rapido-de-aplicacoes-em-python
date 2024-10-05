-- #TODO: id deve ser auto increment
-- #TODO: username deve ser unico e not null
-- #TODO: email deve ser unico e not null



CREATE TABLE User (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

-- #TODO: telephone deve ser unico e not null

CREATE TABLE Telephone (
    telephone VARCHAR(255),
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    fk_User_id INTEGER CONSTRAINT FK_Telephone_2
    REFERENCES User (id)
    ON DELETE CASCADE
);