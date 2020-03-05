CREATE TABLE IF NOT EXISTS `P5`.`Categories` (
  `id_cat` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `category` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_cat`),
  UNIQUE INDEX `category_UNIQUE` (`category` ASC) VISIBLE)
ENGINE = InnoDB;

INSERT INTO `P5`.`Categories` (`id_cat`, `category`) VALUES (1, 'Boissons');
INSERT INTO `P5`.`Categories` (`id_cat`, `category`) VALUES (2, 'Petit déjeuner');
INSERT INTO `P5`.`Categories` (`id_cat`, `category`) VALUES (3, 'Produits laitiers');

CREATE TABLE IF NOT EXISTS `P5`.`Products` (
  `id_prod` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `cat_id` INT UNSIGNED NOT NULL,
  `prod_nb` VARCHAR(15) NOT NULL,
  `true_cat` VARCHAR(45) NOT NULL,
  `prod_name` VARCHAR(30) NOT NULL,
  UNIQUE INDEX `id_prod_UNIQUE` (`id_prod` ASC) VISIBLE,
  PRIMARY KEY (`id_prod`),
  UNIQUE INDEX `prod_nb_UNIQUE` (`prod_nb` ASC) VISIBLE,
  UNIQUE INDEX `prod_name_UNIQUE` (`prod_name` ASC) VISIBLE,
  INDEX `fk_cat_id_idx` (`cat_id` ASC) VISIBLE,
  CONSTRAINT `fk_cat_id`
    FOREIGN KEY (`cat_id`)
    REFERENCES `P5`.`Categories` (`id_cat`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

INSERT INTO `P5`.`Products` (`id_prod`, `cat_id`, `prod_nb`, `true_cat`, `prod_name`) VALUES (1, 1, '5449000000996', 'sodas-au-cola', 'Coca cola');
INSERT INTO `P5`.`Products` (`id_prod`, `cat_id`, `prod_nb`, `true_cat`, `prod_name`) VALUES (2, 1, '3124480183828', 'boissons-aux-fruits', 'Oasis');
INSERT INTO `P5`.`Products` (`id_prod`, `cat_id`, `prod_nb`, `true_cat`, `prod_name`) VALUES (3, 1, '3163937010003', 'pastis', 'Ricard');
INSERT INTO `P5`.`Products` (`id_prod`, `cat_id`, `prod_nb`, `true_cat`, `prod_name`) VALUES (4, 2, '3017620422003', 'pates-a-tartiner-aux-noisettes-et-au-cacao', 'Nutella');
INSERT INTO `P5`.`Products` (`id_prod`, `cat_id`, `prod_nb`, `true_cat`, `prod_name`) VALUES (5, 2, '3017760363990', 'biscottes-aux-cereales', 'Biscottes Heudebert');
INSERT INTO `P5`.`Products` (`id_prod`, `cat_id`, `prod_nb`, `true_cat`, `prod_name`) VALUES (6, 3, '3228021170039', 'camemberts', 'Camembert Président');
INSERT INTO `P5`.`Products` (`id_prod`, `cat_id`, `prod_nb`, `true_cat`, `prod_name`) VALUES (7, 3, '3329770062771', 'cremes-entieres', 'Crème fraîche entière Yoplait');

CREATE TABLE IF NOT EXISTS `P5`.`Saved_data` (
  `id_saved` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `saved_name` VARCHAR(30) NOT NULL,
  `saved_store` VARCHAR(80) NULL DEFAULT 'Pas de magasin référencé',
  `saved_url` VARCHAR(100) NOT NULL,
  `sub_to` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`id_saved`),
  UNIQUE INDEX `id_save_UNIQUE` (`id_saved` ASC) VISIBLE,
  UNIQUE INDEX `saved_name_UNIQUE` (`saved_name` ASC) VISIBLE,
  INDEX `fk_sub_to_idx` (`sub_to` ASC) VISIBLE,
  CONSTRAINT `fk_sub_to`
    FOREIGN KEY (`sub_to`)
    REFERENCES `P5`.`Products` (`prod_name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE USER 'testeur' IDENTIFIED BY 'openclassrooms';

GRANT ALL ON `P5`.* TO 'testeur';
