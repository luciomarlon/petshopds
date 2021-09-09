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