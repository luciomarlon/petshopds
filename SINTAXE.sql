use petshop;
desc funcionario;
desc cliente;
select * from Loginfuncionario;
select * from login;
select * from pet;
select * from funcionario;
select * from cliente;
select * from categoriagato;
select * from categoriacachorro;
select * from servicos;
select * from agendamento;
select nome, nomepet, idade, porte, peso from funcionario, pet;
desc agendamento;
alter table servicos add column lixo varchar(1);

select nomepet, idade, especie, porte, raca, peso from pet;
#BUSCA POR ID E CHAVE ESTRANGEIRA
#CRUZAR PET E CLIENTE

SELECT * from cliente inner join pet on cliente.id_cliente = pet.pet_cliente order by nome;
#CRUZAR PET E CLINTE POR NOME CLIENTE
SELECT nome, nomepet,idade, especie, porte, raca, peso, pet_cliente from cliente inner join pet on cliente.id_cliente = pet.pet_cliente order by nome;
SELECT nome, nomepet,idade, especie, porte, raca, peso from cliente inner join pet on cliente.id_cliente = pet.pet_cliente;
SELECT nome, rg, cpf, celular, telefone, logradouro, cep, nomepet, raca, Especie, Peso from cliente inner join pet on cliente.id_cliente = pet.pet_cliente;
select * from pet where nomepet like "%a%";
SELECT * from cliente inner join pet on cliente.id_cliente = pet.pet_cliente where nome = "lucio" order by nome desc;
SELECT * from cliente inner join pet on cliente.id_cliente = pet.pet_cliente WHERE NOME like "%lu%";
SELECT nome, nomepet,idade, especie, porte, raca, peso  from pet inner join cliente on cliente.id_cliente = pet.pet_cliente WHERE nomepet like "%ki%";
SELECT nome, nomepet,idade, especie, porte, raca, peso  from pet inner join cliente on cliente.id_cliente = pet.pet_cliente WHERE  nomepet like '%%' and nome like '%%' order by nome;
SELECT * FROM pet where nomepet = "KIARA";
SELECT * FROM pet where nomepet like "%ca%";
select * from agendamento; 

create table agendamento(
    id_agendamento int primary key auto_increment not null, 
    nomepet varchar(25),
	especie varchar(10),    
	porte varchar(1),
	peso float(6),
	datas date, 
    horario time,
    valorservico float(8),
    nomeprofissional varchar(25),
    procedimento varchar(25),
	realizado varchar(3),
	fk_pet_agendamento int,
    fk_funcionario_pet int,
    constraint fk_pet_agendamento foreign key(fk_pet_agendamento) references pet(id_pet),
    constraint fk_funcionario_pet foreign key(fk_funcionario_pet) references funcionario(id_funcionario) 
    );
   

create table cliente(
id_cliente int primary key auto_increment NOT NULL,
nome varchar(45) not null,
rg varchar(12),
cpf varchar(13),
celular varchar(13),
telefone varchar(12),
logradouro varchar(45),
cep varchar(9),
bairro varchar(30),
cidade varchar(25) 
);

create table pet(
id_pet int primary key auto_increment not null,
nomepet varchar(45) not null,
idade float(5)not null,
especie varchar(10),
porte varchar(1),
raca varchar(20),
peso float(6),
cliente varchar(25),
pet_cliente int,
constraint fk_id_pet foreign key(pet_cliente) references cliente(id_cliente)
ON DELETE SET NULL
ON UPDATE CASCADE
);

CREATE TABLE funcionario (
    id_funcionario INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    nome VARCHAR(45),
    sobrenome VARCHAR(45),
    cargo VARCHAR(25),
    rg VARCHAR(12),
    cpf varchar(13),
    datadeNascimento VARCHAR(10),
    telefone VARCHAR(12),
    celular VARCHAR(13),
    logradouro VARCHAR(45),
    cidade VARCHAR(25),
    cep VARCHAR(9),
    salario FLOAT(8),
    horaentrar time,
    horasaida time
); 

create table login (
id_login int primary key auto_increment not null, 
usuario varchar(25),
senha varchar(12),
datalogin datetime
);

alter table login add datalogin datetime;
create table Loginfuncionario(
id_logintabelafuncionario int primary key auto_increment not null, 
usuario varchar(25),
senha varchar(12),
datalogar datetime
);
create table servicos(
id_servicos int primary key auto_increment not null,
nomeservico varchar(25),
valorservico float(8)
#categoria_servicos int,
#constraint fk_id_servicos foreign key(categoria_servicos) references agendamento(id_agendamento)
);

create table categoriacachorro(
id_cachorro int primary key auto_increment not null,
racacachorro varchar(25),
valorunitario float(8)
);

create table categoriagato(
id_gato int primary key auto_increment not null,
racagato varchar(25),
valorunitario float(8)
);
select * from cliente;
ALTER TABLE funcionario modify column cpf varchar(13);
ALTER table agendamento modify column datas date;
ALTER table agendamento modify column horario time;
alter table pet add constraint fk_id_pet foreign key(pet_cliente) references cliente(id_cliente) ON UPDATE CASCADE ON DELETE SET NULL;
alter table pet modify column idade float(5);
alter table pet change column cpfcliente cliente varchar(25);
ALTER TABLE pet modify cpfcliente int(12);
ALTER TABLE funcionario modify cpf int(12);
ALTER TABLE cliente modify cpf int(12);
ALTER TABLE funcionario modify column sobrenome varchar(45);
alter table funcionario modify column salario float(8);
ALTER TABLE pet modify peso float(6);
ALTER TABLE funcionario modify salario VARCHAR(7);
alter table categoriapet change racas raca varchar(25);
alter table agendamento modify especie varchar(10);
alter table agendamento add column realizado varchar(1);
alter table pet modify column idade int(2) not null; 
ALTER TABLE cliente CHANGE rua logradouro VARCHAR(45);
alter table pet modify column porte varchar(2);
alter table pet add constraint fk_id_pet foreign key(pet_cliente) references cliente(id_cliente) ON UPDATE CASCADE ON DELETE SET NULL;
alter table tabela drop foreign key fk_id_pet;
alter table funcionario modify column rg varchar(12);
alter table pet modify column porte varchar(1);
alter table agendamento modify column peso varchar(5);

desc pet;
