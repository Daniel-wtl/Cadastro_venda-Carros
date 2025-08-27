# Cadastro e Venda - Carros
Interface com cadastro de carros com marcas, modelos e proprietários. Usando Python e MySql.
Neste projeto é necessario que seja criado um Banco de Dados de acordo com as instruções.

## Bibliotecas
- CustomTKinter
- TKinter
- MySQLdb
  
Se necessário, no **cmd** rode o comando de download:

Para baixar o TKinter: `pip install tkinter`

Para baixar o CustomTKinter: `pip install customtkinter`

Para baixar o MySQLdb: `pip install mysqlclient`

## Como Baixar o  código
Clique em **code --> download ZIP** e abra a pasta. Depois selecione o arquivo **loja de carros (cadastro)**

## Como criar o Banco de Dados
Baixe o MySql Workbench: `https://www.mysql.com/products/workbench/`

Abra o arquivo e siga os passos.

No MySqlWorkbench abra um projeto e rode o codigo:
``` SQL
CREATE SCHEMA `carros` ;

CREATE TABLE `carros`.`ano` (
  `id_ano` INT NOT NULL AUTO_INCREMENT,
  `ano_fabricaco` VARCHAR(15) NOT NULL,
  `ano_modelo` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`id_ano`));

CREATE TABLE `carros`.`marca` (
  `id_marca` INT NOT NULL AUTO_INCREMENT,
  `marca_nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_marca`));

CREATE TABLE `carros`.`modelo` (
  `id_modelo` INT NOT NULL AUTO_INCREMENT,
  `nome_modelo` VARCHAR(45) NOT NULL,
  `origem` VARCHAR(45) NOT NULL,
  `id_marca` INT NOT NULL,
  PRIMARY KEY (`id_modelo`),
  INDEX `fk_id_marca_idx` (`id_marca` ASC) VISIBLE,
  CONSTRAINT `fk_id_marca`
    FOREIGN KEY (`id_marca`)
    REFERENCES `carros`.`marca` (`id_marca`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE `carros`.`proprietario` (
  `id_proprietario` INT NOT NULL AUTO_INCREMENT,
  `nome_proprietario` VARCHAR(60) NOT NULL,
  `cpf` VARCHAR(11) NOT NULL,
  `celular` VARCHAR(11) NOT NULL,
  PRIMARY KEY (`id_proprietario`));

CREATE TABLE `carros`.`veiculo` (
  `id_veiculo` INT NOT NULL AUTO_INCREMENT,
  `id_marca` INT NOT NULL,
  `id_modelo` INT NOT NULL,
  `id_ano` INT NOT NULL,
  `id_proprietario` INT NOT NULL,
  `cor` VARCHAR(15) NULL,
  `placa` VARCHAR(7) NULL,
  `valor` INT NOT NULL,
  `valor_fipe` INT NULL,
  `km` INT NULL,
  PRIMARY KEY (`id_veiculo`),
  INDEX `fk_id_ano_idx` (`id_ano` ASC) VISIBLE,
  INDEX `fk_id_marca2_idx` (`id_marca` ASC) VISIBLE,
  INDEX `fk_id_modelo_idx` (`id_modelo` ASC) VISIBLE,
  INDEX `fk_id_proprietario_idx` (`id_proprietario` ASC) VISIBLE,
  CONSTRAINT `fk_id_ano`
    FOREIGN KEY (`id_ano`)
    REFERENCES `carros`.`ano` (`id_ano`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_id_marca2`
    FOREIGN KEY (`id_marca`)
    REFERENCES `carros`.`marca` (`id_marca`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_id_modelo`
    FOREIGN KEY (`id_modelo`)
    REFERENCES `carros`.`modelo` (`id_modelo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_id_proprietario`
    FOREIGN KEY (`id_proprietario`)
    REFERENCES `carros`.`proprietario` (`id_proprietario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
```

Depois procure um botão chamado **Administration** e clique, logo após, em **Users and Privileges**, e adicione uma conta, crie um nome e uma senha. Depois vá em **Schema Privileges**, **Add Entry**, selecione todas as opções da aba **Object Rights**.

No menu, clique em **+**, coloque um nome na conecxão logo, insira o nome de usuario que foi criado e então em **Default Schema** coloque o nome **carros**.

No código Python, na variável **user** coloque seu nome de usuário e na variável **password** coloque sua senha (o nome de usuario e senha entre aspas).

Agora pode rodar o código.
