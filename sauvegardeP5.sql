SET NAMES 'utf8mb4' COLLATE 'utf8mb4_unicode_ci';

CREATE DATABASE IF NOT EXISTS `P5`CHARACTER SET `utf8mb4`;

CREATE TABLE IF NOT EXISTS `P5`.`Categories` (
  `id_cat` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `category` VARCHAR(45) CHARACTER SET `utf8mb4` NOT NULL,
  PRIMARY KEY (`id_cat`),
  UNIQUE INDEX `category_UNIQUE` (`category` ASC) VISIBLE)
ENGINE = InnoDB DEFAULT CHARSET=`utf8mb4`;

INSERT IGNORE INTO `P5`.`Categories` (`id_cat`, `category`) VALUES (1, 'Boissons');
INSERT IGNORE INTO `P5`.`Categories` (`id_cat`, `category`) VALUES (2, 'Petit déjeuner');
INSERT IGNORE INTO `P5`.`Categories` (`id_cat`, `category`) VALUES (3, 'Produits laitiers');

CREATE TABLE IF NOT EXISTS `P5`.`Products` (
  `id_prod` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `cat_id` INT UNSIGNED NOT NULL,
  `prod_name` VARCHAR(30) CHARACTER SET `utf8mb4` NOT NULL,
  `prod_nb` VARCHAR(15) NOT NULL,
  `prod_stores` VARCHAR(45) CHARACTER SET `utf8mb4` NULL,
  `prod_url` VARCHAR(100) NOT NULL,
  `is_sub` SMALLINT(1) UNSIGNED NOT NULL,
  `sub_to` VARCHAR(45) CHARACTER SET `utf8mb4` NULL,
  `user` VARCHAR(20) CHARACTER SET `utf8mb4` NULL,
  `true_cat` VARCHAR(45) NOT NULL,
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
ENGINE = InnoDB DEFAULT CHARSET=`utf8mb4`;

INSERT IGNORE INTO `P5`.`Products` (`id_prod`, `cat_id`, `prod_name`, `prod_nb`, `prod_stores`, `prod_url`, `is_sub`, `sub_to`, `user`, `true_cat`) VALUES (1, 1, 'Coca cola', '5449000000996', NULL, 'https://fr.openfoodfacts.org/produit/5449000000996', 0, NULL, NULL, 'sodas-au-cola');
INSERT IGNORE INTO `P5`.`Products` (`id_prod`, `cat_id`, `prod_name`, `prod_nb`, `prod_stores`, `prod_url`, `is_sub`, `sub_to`, `user`, `true_cat`) VALUES (2, 1, 'Oasis', '3124480183828', NULL, 'https://fr.openfoodfacts.org/produit/3124480183828', 0, NULL, NULL, 'boissons-aux-fruits');
INSERT IGNORE INTO `P5`.`Products` (`id_prod`, `cat_id`, `prod_name`, `prod_nb`, `prod_stores`, `prod_url`, `is_sub`, `sub_to`, `user`, `true_cat`) VALUES (3, 1, 'Ricard', '3163937010003', NULL, 'https://fr.openfoodfacts.org/produit/3163937010003', 0, NULL, NULL, 'pastis');
INSERT IGNORE INTO `P5`.`Products` (`id_prod`, `cat_id`, `prod_name`, `prod_nb`, `prod_stores`, `prod_url`, `is_sub`, `sub_to`, `user`, `true_cat`) VALUES (4, 2, 'Nutella', '3017620422003', NULL, 'https://fr.openfoodfacts.org/produit/3017620422003', 0, NULL, NULL, 'pates-a-tartiner-aux-noisettes-et-au-cacao');
INSERT IGNORE INTO `P5`.`Products` (`id_prod`, `cat_id`, `prod_name`, `prod_nb`, `prod_stores`, `prod_url`, `is_sub`, `sub_to`, `user`, `true_cat`) VALUES (5, 2, 'Biscottes Heudebert', '3017760363990', NULL, 'https://fr.openfoodfacts.org/produit/3017760363990', 0, NULL, NULL, 'biscottes-aux-cereales');
INSERT IGNORE INTO `P5`.`Products` (`id_prod`, `cat_id`, `prod_name`, `prod_nb`, `prod_stores`, `prod_url`, `is_sub`, `sub_to`, `user`, `true_cat`) VALUES (6, 3, 'Camembert Président', '3228021170039', NULL, 'https://fr.openfoodfacts.org/produit/3228021170039', 0, NULL, NULL, 'camemberts');
INSERT IGNORE INTO `P5`.`Products` (`id_prod`, `cat_id`, `prod_name`, `prod_nb`, `prod_stores`, `prod_url`, `is_sub`, `sub_to`, `user`, `true_cat`) VALUES (7, 3, 'Crème fraîche entière Yoplait', '3329770062771', NULL, 'https://fr.openfoodfacts.org/produit/3329770062771', 0, NULL, NULL, 'cremes-entieres');

CREATE USER IF NOT EXISTS 'testeur' IDENTIFIED BY 'openclassrooms';

GRANT ALL ON `P5`.* TO 'testeur';
