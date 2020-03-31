CREATE DATABASE IF NOT EXISTS `P5` DEFAULT CHARACTER SET utf8mb4;

CREATE TABLE IF NOT EXISTS `P5`.`Category` (
  `idCategory` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nameCat` VARCHAR(50) CHARACTER SET 'utf8mb4' NOT NULL,
  PRIMARY KEY (`idCategory`),
  UNIQUE INDEX `idCategory_UNIQUE` (`idCategory` ASC) VISIBLE,
  UNIQUE INDEX `nameCat_UNIQUE` (`nameCat` ASC) VISIBLE)
ENGINE = InnoDB;

INSERT INTO `P5`.`Category` (`idCategory`, `nameCat`) VALUES (1, 'Sodas au cola');
INSERT INTO `P5`.`Category` (`idCategory`, `nameCat`) VALUES (2, 'Pâtes à tartiner aux noisettes');
INSERT INTO `P5`.`Category` (`idCategory`, `nameCat`) VALUES (3, 'Camemberts');
INSERT INTO `P5`.`Category` (`idCategory`, `nameCat`) VALUES (4, 'Biscottes aux céréales');
INSERT INTO `P5`.`Category` (`idCategory`, `nameCat`) VALUES (5, 'Bouillons cubes');

CREATE TABLE IF NOT EXISTS `P5`.`Product` (
  `idProduct` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nameProd` VARCHAR(45) CHARACTER SET 'utf8mb4' NULL,
  `CatId` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`idProduct`),
  UNIQUE INDEX `idProduct_UNIQUE` (`idProduct` ASC) INVISIBLE,
  UNIQUE INDEX `nameProd_UNIQUE` (`nameProd` ASC) VISIBLE,
  INDEX `fk_CatID_idx` (`CatId` ASC) VISIBLE,
  CONSTRAINT `fk_CatID`
    FOREIGN KEY (`CatId`)
    REFERENCES `P5`.`Category` (`idCategory`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `P5`.`User` (
  `idUser` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `Username` VARCHAR(45) CHARACTER SET 'utf8mb4' NOT NULL,
  PRIMARY KEY (`idUser`),
  UNIQUE INDEX `Username_UNIQUE` (`Username` ASC) VISIBLE)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `P5`.`ProdDatas` (
  `idProdDatas` INT NOT NULL AUTO_INCREMENT,
  `ProdID` INT UNSIGNED NOT NULL,
  `ProdStore` VARCHAR(45) CHARACTER SET 'utf8mb4' NULL,
  `ProdUrl` VARCHAR(200) NOT NULL,
  `ProdScore` FLOAT NOT NULL,
  `UserID` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`idProdDatas`),
  UNIQUE INDEX `idProdDatas_UNIQUE` (`idProdDatas` ASC) VISIBLE,
  UNIQUE INDEX `ProdId_UNIQUE` (`ProdID` ASC) VISIBLE,
  UNIQUE INDEX `ProdUrl_UNIQUE` (`ProdUrl` ASC) VISIBLE,
  INDEX `fk_UserID_idx` (`UserID` ASC) VISIBLE,
  CONSTRAINT `fk_ProdID`
    FOREIGN KEY (`ProdID`)
    REFERENCES `P5`.`Product` (`idProduct`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_UserID`
    FOREIGN KEY (`UserID`)
    REFERENCES `P5`.`User` (`idUser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE USER IF NOT EXISTS 'testeur' IDENTIFIED BY 'openclassrooms';

GRANT ALL ON `P5`.* TO 'testeur';
