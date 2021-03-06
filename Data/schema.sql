-- MySQL Script generated by Anders Van Winkle
-- 4/3/15 13:13:13
-- Model: New Model    Version: 1.0
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema bookswap
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `bookswap` ;
CREATE SCHEMA IF NOT EXISTS `bookswap` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `bookswap` ;

-- -----------------------------------------------------
-- Table `bookswap`.`user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `bookswap`.`user` ;

CREATE TABLE IF NOT EXISTS `bookswap`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(20) NOT NULL,
  `password` VARCHAR(128) NOT NULL,
  `salt` VARCHAR(16) NOT NULL,
  `role` VARCHAR(20),
  `created` DATETIME DEFAULT NULL,
  `last_login` DATETIME DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `bookswap`.`college`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `bookswap`.`college` ;

CREATE TABLE IF NOT EXISTS `bookswap`.`college` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100),

  PRIMARY KEY (`id`),

  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `bookswap`.`user_info`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `bookswap`.`user_info` ;

CREATE TABLE IF NOT EXISTS `bookswap`.`user_info` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `college_id` INT NOT NULL,
  `first_name` VARCHAR(50),
  `last_name` VARCHAR(50),
  `email` VARCHAR(50),
  `address` VARCHAR(150),
  `phone_number` VARCHAR(10),

  PRIMARY KEY (`id`),
  INDEX (`user_id`),

  FOREIGN KEY (`user_id`)
    REFERENCES user(`id`),

  FOREIGN KEY (`college_id`)
    REFERENCES college(`id`),

  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `bookswap`.`author`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `bookswap`.`author` ;

CREATE TABLE IF NOT EXISTS `bookswap`.`author` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,

  PRIMARY KEY (`id`),

  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `bookswap`.`book`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `bookswap`.`book` ;

CREATE TABLE IF NOT EXISTS `bookswap`.`book` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `isbn` VARCHAR(13) NOT NULL,
  `title` VARCHAR(100) NOT NULL,
  `edition` INT NOT NULL,

  PRIMARY KEY (`id`),

  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `bookswap`.`author_book`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `bookswap`.`author_book` ;

CREATE TABLE IF NOT EXISTS `bookswap`.`author_book` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `author_id` INT NOT NULL,
  `book_id` INT NOT NULL,

  INDEX (`author_id`),
  INDEX (`book_id`),

  PRIMARY KEY (`author_id`, `book_id`),

  FOREIGN KEY (`author_id`)
    REFERENCES author(`id`),

  FOREIGN KEY (`book_id`)
    REFERENCES book(`id`),

  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `bookswap`.`listing`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `bookswap`.`listing` ;

CREATE TABLE IF NOT EXISTS `bookswap`.`listing` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `book_id` INT NOT NULL,
  `price` DECIMAL(10, 2) NOT NULL,
  `book_condition` VARCHAR(100),
  `description` VARCHAR(100),
  `image_path` VARCHAR(100),

  PRIMARY KEY (`id`),
  INDEX (`user_id`),

  FOREIGN KEY (`user_id`)
    REFERENCES user(`id`),

  FOREIGN KEY (`book_id`)
    REFERENCES book(`id`),

  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `bookswap`.`course`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `bookswap`.`course` ;

CREATE TABLE IF NOT EXISTS `bookswap`.`course` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `college_id` INT NOT NULL,
  `title` VARCHAR(100) NOT NULL,
  `abbreviation` VARCHAR(4) NOT NULL,
  `number` VARCHAR(6) NOT NULL,

  PRIMARY KEY (`id`),

  FOREIGN KEY (`college_id`)
    REFERENCES college(`id`),

  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `bookswap`.`course_book`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `bookswap`.`course_book` ;

CREATE TABLE IF NOT EXISTS `bookswap`.`course_book` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `course_id` INT NOT NULL,
  `book_id` INT NOT NULL,

  INDEX (`course_id`),
  INDEX (`book_id`),

  PRIMARY KEY (`course_id`, `book_id`),

  FOREIGN KEY (`course_id`)
    REFERENCES course(`id`),

  FOREIGN KEY (`book_id`)
    REFERENCES book(`id`),

    UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
