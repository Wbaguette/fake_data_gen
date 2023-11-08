
CREATE TABLE `Team` (
  `idTeam` INT NOT NULL,
  `name`VARCHAR(45) NULL,
  `wins` INT NULL,
  `losses` INT NULL,
  `ties` INT NULL,
  `rank` INT NULL,
  `value` DECIMAL NULL,
  PRIMARY KEY (`idTeam`))
ENGINE = InnoDB;

CREATE TABLE `Player` (
  `idPlayer` INT NOT NULL,
  `Name` VARCHAR(45) NULL,
  `age` INT NULL,
  `position` VARCHAR(45) NULL,
  `jersey` INT NULL,
  `team` INT NOT NULL,
  PRIMARY KEY (`idPlayer`, `team`),
  INDEX `team_idx` (`team` ASC) VISIBLE,
  CONSTRAINT `team`
    FOREIGN KEY (`team`)
    REFERENCES `Team` (`idTeam`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE `Stadium` (
  `idStadium` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `capacity` INT NULL,
  `location` VARCHAR(45) NULL,
  PRIMARY KEY (`idStadium`))
ENGINE = InnoDB;

CREATE TABLE `Match` (
  `idMatch` INT NOT NULL,
  `idStadium` INT NOT NULL,
  `home` INT NOT NULL,
  `away` INT NOT NULL,
  `datetime` DATETIME NULL,
  PRIMARY KEY (`idMatch`, `home`, `away`, `idStadium`),
  INDEX `home_idx` (`home` ASC) VISIBLE,
  INDEX `away_idx` (`away` ASC) VISIBLE,
  INDEX `stadium_idx` (`idStadium` ASC) VISIBLE,
  CONSTRAINT `home`
    FOREIGN KEY (`home`)
    REFERENCES `Team` (`idTeam`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `away`
    FOREIGN KEY (`away`)
    REFERENCES `Team` (`idTeam`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `stadium`
    FOREIGN KEY (`idStadium`)
    REFERENCES `Stadium` (`idStadium`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE `Sponsor` (
  `idSponsor` INT NOT NULL,
  `idTeam` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `value` DECIMAL NULL,
  PRIMARY KEY (`idSponsor`, `idTeam`),
  INDEX `team_idx` (`idTeam` ASC) VISIBLE,
  CONSTRAINT `fk_team`
    FOREIGN KEY (`idTeam`)
    REFERENCES `Team` (`idTeam`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE `Contract` (
  `idPlayer` INT NOT NULL,
  `salary` DECIMAL NULL,
  `start` DATE NULL,
  `end` DATE NULL,
  CONSTRAINT `player`
    FOREIGN KEY (`idPlayer`)
    REFERENCES `Player` (`idPlayer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE `Staff` (
  `idStaff` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `salary` DECIMAL NULL,
  `role` VARCHAR(45) NULL,
  `stadium` INT NOT NULL,
  PRIMARY KEY (`idStaff`, `stadium`),
  INDEX `works_idx` (`stadium` ASC) VISIBLE,
  CONSTRAINT `works`
    FOREIGN KEY (`stadium`)
    REFERENCES `Stadium` (`idStadium`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE `Statistics` (
  `idPlayer` INT NOT NULL,
  `goals` INT NULL,
  `blocks` INT NULL,
  `yellow_cards` INT NULL,
  `red_cards` INT NULL,
  CONSTRAINT `fk_player`
    FOREIGN KEY (`idPlayer`)
    REFERENCES `Player` (`idPlayer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE `Result` (
  `home_score` INT NULL,
  `away_score` INT NULL,
  `outcome` VARCHAR(45) NULL,
  `match` INT NOT NULL,
  CONSTRAINT `match`
    FOREIGN KEY (`match`)
    REFERENCES `Match` (`idMatch`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
