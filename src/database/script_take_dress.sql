
CREATE DATABASE take_dress; 
USE take_dress;

CREATE TABLE trajes(
id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(200), 
valor FLOAT,
quantidade INT
);

CREATE TABLE usuarios(
id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
usuario VARCHAR(200),
senha VARCHAR(200)
);

CREATE TABLE alugueis(
id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
id_usuario INT NOT NULL,
id_traje INT NOT NULL,
data_aluguel DATE,
data_devolucao DATE,
valor FLOAT,
FOREIGN KEY(id_traje) REFERENCES trajes(id),
FOREIGN KEY(id_usuario) REFERENCES usuarios(id)
);

CREATE TABLE imagens(
id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
imagem LONGBLOB,
nome VARCHAR(200)
)

SELECT * FROM trajes;
SELECT * FROM usuarios; 
SELECT * FROM alugueis;
SELECT * FROM imagens;

DELETE FROM imagens WHERE ID >= 1 ;

DROP TABLE trajes;
DROP TABLE usuarios;
DROP TABLE alugueis;
DROP table imagens;