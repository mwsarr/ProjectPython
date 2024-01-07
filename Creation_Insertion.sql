/*Creation des tables*/

CREATE TABLE CLIENTS(
clientID INT IDENTITY(10,5)PRIMARY KEY,
Nom NVARCHAR(50),
Prenom NVARCHAR(50),
Solde Decimal (18,2))

CREATE TABLE TRANSACTIONS (
    TransactionID INT IDENTITY(10,5) PRIMARY KEY,
    clientID INT,
    Montant DECIMAL(18, 2),
    TypeTransaction NVARCHAR(10),
    DateTransaction DATE,
    FOREIGN KEY (ClientID) REFERENCES CLIENTS(clientID)
)

/*Insertion des données */

INSERT INTO CLIENTS (Nom,Prenom,Solde) VALUES ('SARR','MICHEL WALY',5000000.95),
INSERT INTO CLIENTS (Nom,Prenom,Solde) VALUES ('THIMBO','MOUSTAPHA',2000000.50),
INSERT INTO CLIENTS (Nom,Prenom,Solde) VALUES ('DUPONT','ALEX',1000.52)

--SELECT * FROM CLIENTS