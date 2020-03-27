SET NAMES 'utf8mb4' COLLATE 'utf8mb4_unicode_ci';

CREATE DATABASE IF NOT EXISTS `P5`CHARACTER SET `utf8mb4`;

CREATE TABLE IF NOT EXISTS `P5`.`Categories` (
  `id_cat` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `category` VARCHAR(45) CHARACTER SET 'utf8' NOT NULL,
  PRIMARY KEY (`id_cat`),
  UNIQUE INDEX `id_cat_UNIQUE` (`id_cat` ASC) VISIBLE)
ENGINE = InnoDB;

INSERT IGNORE INTO `P5`.`Categories` (`id_cat`, `category`) VALUES (1, 'Boissons');
INSERT IGNORE INTO `P5`.`Categories` (`id_cat`, `category`) VALUES (2, 'Petit déjeuner');
INSERT IGNORE INTO `P5`.`Categories` (`id_cat`, `category`) VALUES (3, 'Produits laitiers');

CREATE TABLE IF NOT EXISTS `P5`.`Products` (
  `id_prod` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `cat_id` INT UNSIGNED NOT NULL,
  `prod_name` VARCHAR(50) CHARACTER SET 'utf8mb4' NOT NULL,
  `prod_nb` VARCHAR(15) NOT NULL,
  `prod_stores` VARCHAR(45) CHARACTER SET 'utf8mb4' NULL,
  `prod_url` VARCHAR(100) NOT NULL,
  `sub_to` VARCHAR(50) NULL,
  `true_cat` VARCHAR(45) NOT NULL,
  `is_sub` SMALLINT(1) UNSIGNED NOT NULL,
  UNIQUE INDEX `id_prod_UNIQUE` (`id_prod` ASC) VISIBLE,
  PRIMARY KEY (`id_prod`),
  UNIQUE INDEX `prod_nb_UNIQUE` (`prod_nb` ASC) VISIBLE,
  UNIQUE INDEX `prod_name_UNIQUE` (`prod_name` ASC) VISIBLE,
  UNIQUE INDEX `prod_url_UNIQUE` (`prod_url` ASC) VISIBLE,
  INDEX `fk_cat_id_idx` (`cat_id` ASC) VISIBLE,
  CONSTRAINT `fk_cat_id`
    FOREIGN KEY (`cat_id`)
    REFERENCES `P5`.`Categories` (`id_cat`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

INSERT INTO `P5`.`Products` (`id_prod`, `cat_id`, `prod_name`, `prod_nb`, `prod_stores`, `prod_url`, `sub_to`, `true_cat`, `is_sub`) VALUES (1, 1, 'Coca cola', '5449000000996', NULL, 'https://fr.openfoodfacts.org/produit/5449000000996', NULL, 'sodas-au-cola', 0);
INSERT INTO `P5`.`Products` (`id_prod`, `cat_id`, `prod_name`, `prod_nb`, `prod_stores`, `prod_url`, `sub_to`, `true_cat`, `is_sub`) VALUES (2, 1, 'Oasis', '3124480183828', NULL, 'https://fr.openfoodfacts.org/produit/3124480183828', NULL, 'boissons-aux-fruits', 0);
INSERT INTO `P5`.`Products` (`id_prod`, `cat_id`, `prod_name`, `prod_nb`, `prod_stores`, `prod_url`, `sub_to`, `true_cat`, `is_sub`) VALUES (3, 1, 'Ricard', '3163937010003', NULL, 'https://fr.openfoodfacts.org/produit/3163937010003', NULL, 'pastis', 0);
INSERT INTO `P5`.`Products` (`id_prod`, `cat_id`, `prod_name`, `prod_nb`, `prod_stores`, `prod_url`, `sub_to`, `true_cat`, `is_sub`) VALUES (4, 2, 'Nutella', '3017620422003', NULL, 'https://fr.openfoodfacts.org/produit/3017620422003', NULL, 'pates-a-tartiner-aux-noisettes-et-au-cacao', 0);
INSERT INTO `P5`.`Products` (`id_prod`, `cat_id`, `prod_name`, `prod_nb`, `prod_stores`, `prod_url`, `sub_to`, `true_cat`, `is_sub`) VALUES (5, 2, 'Biscottes Heudebert', '3017760363990', NULL, 'https://fr.openfoodfacts.org/produit/3017760363990', NULL, 'biscottes-aux-cereales', 0);
INSERT INTO `P5`.`Products` (`id_prod`, `cat_id`, `prod_name`, `prod_nb`, `prod_stores`, `prod_url`, `sub_to`, `true_cat`, `is_sub`) VALUES (6, 3, 'Camembert Président', '3228021170039', NULL, 'https://fr.openfoodfacts.org/produit/3228021170039', NULL, 'camemberts', 0);
INSERT INTO `P5`.`Products` (`id_prod`, `cat_id`, `prod_name`, `prod_nb`, `prod_stores`, `prod_url`, `sub_to`, `true_cat`, `is_sub`) VALUES (7, 3, 'Crème fraîche entière Yoplait', '3329770062771', NULL, 'https://fr.openfoodfacts.org/produit/3329770062771', NULL, 'cremes-entieres', 0);


CREATE TABLE IF NOT EXISTS `P5`.`Users` (
  `id_user` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(45) CHARACTER SET 'utf8mb4' NULL,
  PRIMARY KEY (`id_user`),
  UNIQUE INDEX `user_name_UNIQUE` (`user_name` ASC) VISIBLE,
  UNIQUE INDEX `id_user_UNIQUE` (`id_user` ASC) VISIBLE)
ENGINE = InnoDB;

INSERT INTO `P5`.`Users` (`id_user`, `user_name`) VALUES (1, 'all');

CREATE TABLE IF NOT EXISTS `P5`.`Subs` (
  `id_sub` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `prod_id` INT UNSIGNED NOT NULL,
  `user_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id_sub`),
  UNIQUE INDEX `id_sub_UNIQUE` (`id_sub` ASC) VISIBLE,
  INDEX `fk_user_id_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_prod_id_idx` (`prod_id` ASC) VISIBLE,
  CONSTRAINT `fk_prod_id`
    FOREIGN KEY (`prod_id`)
    REFERENCES `P5`.`Products` (`id_prod`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `P5`.`Users` (`id_user`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE USER IF NOT EXISTS 'testeur' IDENTIFIED BY 'openclassrooms';

GRANT ALL ON `P5`.* TO 'testeur';
