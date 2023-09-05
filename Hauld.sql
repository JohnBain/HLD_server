CREATE DATABASE Hauld;

use Hauld;

CREATE TABLE Hauld.Users (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    username varchar(255) NOT NULL,
    pword varchar(255) NOT NULL, 
    oauthProvider varchar(255),
    oauthUID varchar(255),
    createdOn DATETIME
);

#email, real name?

CREATE TABLE Hauld.Items (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    UserID INT NOT NULL,
    FOREIGN KEY (UserId) REFERENCES Users(ID),
    imageUrl varchar(255),
    createdOn DATETIME,
    updatedOn DATETIME
);

CREATE TABLE Hauld.Collages (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    imageUrl varchar(255),
    itemsContained JSON, 
    createdOn DATETIME,
    updatedOn DATETIME
);


INSERT INTO Users (username,pword) VALUES ('test2','test2');
INSERT INTO Items (UserID,imageUrl) VALUES (1, 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Random_Turtle.jpg/2560px-Random_Turtle.jpg');
-- UPDATE Items SET imageUrl="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Random_Turtle.jpg/2560px-Random_Turtle.jpg" WHERE ID = 1;
    
#itemsContained is a temporary solution that may prove more trouble than it's worth
