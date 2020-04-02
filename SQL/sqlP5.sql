CREATE DATABASE IF NOT EXISTS `P5` DEFAULT CHARACTER SET utf8mb4;

CREATE TABLE IF NOT EXISTS `P5`.`Categories` (
  `cat_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `cat_name` VARCHAR(50) CHARACTER SET 'utf8mb4' NOT NULL,
  PRIMARY KEY (`cat_id`),
  UNIQUE INDEX `idCategory_UNIQUE` (`cat_id` ASC) VISIBLE,
  UNIQUE INDEX `nameCat_UNIQUE` (`cat_name` ASC) VISIBLE)
ENGINE = InnoDB;

INSERT INTO `P5`.`Categories` (`cat_id`, `cat_name`) VALUES (1, 'Sodas au cola');
INSERT INTO `P5`.`Categories` (`cat_id`, `cat_name`) VALUES (2, 'Pâtes à tartiner aux noisettes');
INSERT INTO `P5`.`Categories` (`cat_id`, `cat_name`) VALUES (3, 'Camemberts');
INSERT INTO `P5`.`Categories` (`cat_id`, `cat_name`) VALUES (4, 'Biscottes aux céréales');
INSERT INTO `P5`.`Categories` (`cat_id`, `cat_name`) VALUES (5, 'Bouillons cubes');

CREATE TABLE IF NOT EXISTS `P5`.`Products` (
  `prod_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `prod_cat_id` INT UNSIGNED NOT NULL,
  `prod_name` VARCHAR(70) CHARACTER SET 'utf8mb4' NULL,
  `prod_store` VARCHAR(70) NULL,
  `prod_url` VARCHAR(150) NOT NULL,
  `prod_score` FLOAT NOT NULL,
  `prod_desc` VARCHAR(150) NULL,
  PRIMARY KEY (`prod_id`),
  UNIQUE INDEX `idProduct_UNIQUE` (`prod_id` ASC) INVISIBLE,
  UNIQUE INDEX `nameProd_UNIQUE` (`prod_name` ASC) VISIBLE,
  INDEX `fk_CatID_idx` (`prod_cat_id` ASC) VISIBLE,
  UNIQUE INDEX `prod_url_UNIQUE` (`prod_url` ASC) VISIBLE,
  CONSTRAINT `fk_cat_id`
    FOREIGN KEY (`prod_cat_id`)
    REFERENCES `P5`.`Categories` (`cat_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `P5`.`Users` (
  `user_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(45) CHARACTER SET 'utf8mb4' NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE INDEX `Username_UNIQUE` (`user_name` ASC) VISIBLE)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `P5`.`Saved_datas` (
  `saved_datas_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `saved_data_user_id` INT UNSIGNED NOT NULL,
  `saved_data_prod_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`saved_datas_id`),
  UNIQUE INDEX `idProdDatas_UNIQUE` (`saved_datas_id` ASC) VISIBLE,
  INDEX `fk_user_id_idx` (`saved_data_user_id` ASC) VISIBLE,
  INDEX `fk_prod_id_idx` (`saved_data_prod_id` ASC) VISIBLE,
  CONSTRAINT `fk_user_id`
    FOREIGN KEY (`saved_data_user_id`)
    REFERENCES `P5`.`Users` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_prod_id`
    FOREIGN KEY (`saved_data_prod_id`)
    REFERENCES `P5`.`Products` (`prod_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE USER IF NOT EXISTS 'testeur' IDENTIFIED BY 'openclassrooms';

GRANT ALL ON `P5`.* TO 'testeur';
