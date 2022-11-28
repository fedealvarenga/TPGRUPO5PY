-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Usuarios` (
  `id_Usuario` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NULL,
  `Apellido` VARCHAR(45) NULL,
  `Email` VARCHAR(45) NULL,
  `Password` VARCHAR(45) NULL,
  `Usuario` TINYINT(1) NULL,
  PRIMARY KEY (`id_Usuario`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Parques`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Parques` (
  `id_Parque` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NULL,
  `Ubicacion` VARCHAR(45) NULL,
  `Capacidad_fastpass` INT NULL,
  `Capacidad_normal` INT NULL,
  PRIMARY KEY (`id_Parque`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Tipo_Entrada`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Tipo_Entrada` (
  `id_Tipo_Entrada` INT NOT NULL AUTO_INCREMENT,
  `Tipo` VARCHAR(45) NULL,
  `Descripcion` VARCHAR(45) NULL,
  PRIMARY KEY (`id_Tipo_Entrada`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Factura`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Factura` (
  `id_Factura` INT NOT NULL AUTO_INCREMENT,
  `FK_Usuario` INT NOT NULL,
  `Facturacol` VARCHAR(45) NULL,
  `Total` FLOAT NULL,
  PRIMARY KEY (`id_Factura`),
  INDEX `fk_Factura_Usuarios1_idx` (`FK_Usuario` ASC) VISIBLE,
  CONSTRAINT `fk_Factura_Usuarios1`
    FOREIGN KEY (`FK_Usuario`)
    REFERENCES `mydb`.`Usuarios` (`id_Usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Entradas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Entradas` (
  `id_Entrada` INT NOT NULL AUTO_INCREMENT,
  `FK_Tipo_Entrada` INT NOT NULL,
  `FK_Parque` INT NOT NULL,
  `FK_Factura` INT NOT NULL,
  `FK_Usuario` INT NOT NULL,
  `Fecha` DATE NULL,
  `Precio` FLOAT NULL,
  PRIMARY KEY (`id_Entrada`),
  INDEX `fk_Entradas_Tipo_Entrada1_idx` (`FK_Tipo_Entrada` ASC) VISIBLE,
  INDEX `fk_Entradas_Parques1_idx` (`FK_Parque` ASC) VISIBLE,
  INDEX `fk_Entradas_Factura1_idx` (`FK_Factura` ASC) VISIBLE,
  INDEX `fk_Entradas_Usuarios1_idx` (`FK_Usuario` ASC) VISIBLE,
  CONSTRAINT `fk_Entradas_Tipo_Entrada1`
    FOREIGN KEY (`FK_Tipo_Entrada`)
    REFERENCES `mydb`.`Tipo_Entrada` (`id_Tipo_Entrada`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Entradas_Parques1`
    FOREIGN KEY (`FK_Parque`)
    REFERENCES `mydb`.`Parques` (`id_Parque`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Entradas_Factura1`
    FOREIGN KEY (`FK_Factura`)
    REFERENCES `mydb`.`Factura` (`id_Factura`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Entradas_Usuarios1`
    FOREIGN KEY (`FK_Usuario`)
    REFERENCES `mydb`.`Usuarios` (`id_Usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
