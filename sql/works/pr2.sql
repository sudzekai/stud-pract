-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Market
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Market
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Market` DEFAULT CHARACTER SET utf8 ;
SHOW WARNINGS;
USE `Market` ;

-- -----------------------------------------------------
-- Table `Market`.`Author`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Market`.`Author` (
  `AuthorId` INT NOT NULL AUTO_INCREMENT,
  `FirstName` NVARCHAR(50) NOT NULL,
  `LastName` NVARCHAR(50) NOT NULL,
  `Country` NVARCHAR(30) NOT NULL DEFAULT 'Россия',
  PRIMARY KEY (`AuthorId`),
  INDEX `UniqueNS` (`FirstName` ASC, `LastName` ASC) INVISIBLE)
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `Market`.`Book`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Market`.`Book` (
  `BookId` INT NOT NULL AUTO_INCREMENT,
  `Title` NVARCHAR(50) NOT NULL,
  `Genre` ENUM('проза', 'поэзия', 'другое') NOT NULL DEFAULT 'Проза',
  `Price` DECIMAL(6,2) UNSIGNED NOT NULL DEFAULT 0,
  `Weight` DECIMAL(4,3) UNSIGNED NOT NULL DEFAULT 0,
  `Pages` SMALLINT UNSIGNED NOT NULL DEFAULT 0,
  `ReleaseYear` YEAR NULL,
  `AuthorId` INT NOT NULL,
  PRIMARY KEY (`BookId`),
  INDEX `fk_Book_Author1_idx` (`AuthorId` ASC) VISIBLE,
  UNIQUE INDEX `Title_UNIQUE` (`Title` ASC) VISIBLE,
  CONSTRAINT `fk_Book_Author1`
    FOREIGN KEY (`AuthorId`)
    REFERENCES `Market`.`Author` (`AuthorId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `Market`.`Customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Market`.`Customer` (
  `CustomerId` INT NOT NULL AUTO_INCREMENT,
  `Login` NVARCHAR(20) NOT NULL,
  `FirstName` NVARCHAR(50) NOT NULL,
  `LastName` NVARCHAR(50) NOT NULL,
  `Address` NVARCHAR(100) NOT NULL,
  `Phone` NVARCHAR(20) NULL,
  PRIMARY KEY (`CustomerId`),
  UNIQUE INDEX `Login_UNIQUE` (`Login` ASC) VISIBLE)
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `Market`.`Order`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Market`.`Order` (
  `OrderId` INT NOT NULL AUTO_INCREMENT,
  `OrderDateTime` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `CustomerId` INT NOT NULL,
  PRIMARY KEY (`OrderId`),
  INDEX `fk_Order_Customer1_idx` (`CustomerId` ASC) VISIBLE,
  CONSTRAINT `fk_Order_Customer1`
    FOREIGN KEY (`CustomerId`)
    REFERENCES `Market`.`Customer` (`CustomerId`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE)
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `Market`.`OrderBooks`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Market`.`OrderBooks` (
  `OrderId` INT NOT NULL,
  `BookId` INT NOT NULL,
  `Quantity` INT UNSIGNED NOT NULL DEFAULT 1,
  PRIMARY KEY (`OrderId`, `BookId`),
CONSTRAINT CheckQuantity CHECK (Quantity > 0 AND Quantity <= 100),
  INDEX `fk_Order_has_Book_Book1_idx` (`BookId` ASC) VISIBLE,
  INDEX `fk_Order_has_Book_Order1_idx` (`OrderId` ASC) VISIBLE,
  CONSTRAINT `fk_Order_has_Book_Order1`
    FOREIGN KEY (`OrderId`)
    REFERENCES `Market`.`Order` (`OrderId`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Order_has_Book_Book1`
    FOREIGN KEY (`BookId`)
    REFERENCES `Market`.`Book` (`BookId`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE)
ENGINE = InnoDB;

SHOW WARNINGS;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
