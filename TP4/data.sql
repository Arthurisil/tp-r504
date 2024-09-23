CREATE DATABASE demosql;
USE demosql;
CREATE TABLE myTable (id int AUTO_INCREMENT, name varchar(45) NOT NULL
	, PRIMARY KEY(id));
INSERT INTO myTable (id, name) VALUES (NULL, 'arthur');
INSERT INTO myTable (id, name) VALUES (NULL, 'clement');
INSERT INTO myTable (id, name) VALUES (NULL, 'matheo');
