CREATE TABLE IF NOT EXISTS ami (
             prenom  VARCHAR(20) NOT NULL,
             nom  VARCHAR(20),
             age INT,
             sex CHAR(1));


CREATE TABLE IF NOT EXISTS Utilisateurs (
id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT, nom VARCHAR(20), prenom VARCHAR(20), courriel VARCHAR(50),
mot_de_passe VARCHAR(192), date_naissance DATE, date_creation DATE, sex CHAR(1), derinere_ip_connexion INTEGER UNSIGNED,
couleur_yeux ENUM('brun', 'vert', 'bleu', 'gris'),
couleur_cheveux ENUM('noir', 'brun', 'roux', 'blond', 'gris', 'blanc', 'rouge', 'vert', 'bleu', 'rose', 'coco'),
couleur_peau ENUM('blanche', 'bazanee', 'noire'),
PRIMARY KEY (id),
UNIQUE (courriel)
);


CREATE TABLE IF NOT EXISTS Communautes (
id INTEGER UNSIGNED, nom VARCHAR(50), date_creation DATE,
PRIMARY KEY (id),
UNIQUE (nom)
);


CREATE TABLE IF NOT EXISTS Utilisateurs_roles (
id_utilisateur INTEGER UNSIGNED, id_communaute INTEGER UNSIGNED,
role_utilisateur ENUM('administrateur', 'moderateur'),
FOREIGN KEY (id_utilisateur) REFERENCES Utilisateurs(id),
FOREIGN KEY (id_communaute) REFERENCES Communautes(id)
);


CREATE TABLE IF NOT EXISTS Publications (
id INTEGER UNSIGNED, id_utilisateur INTEGER UNSIGNED, id_communaute INTEGER UNSIGNED,
texte CHAR(150), date_creation DATE,
PRIMARY KEY (id),
FOREIGN KEY (id_utilisateur) REFERENCES Utilisateurs(id),
FOREIGN KEY (id_communaute) REFERENCES Communautes(id)
);


CREATE TABLE IF NOT EXISTS Publications_recherches (
id_publication INTEGER UNSIGNED, age INTEGER, prenom VARCHAR(20),
couleur_yeux ENUM('brun', 'vert', 'bleu', 'gris'),
couleur_cheveux ENUM('noir', 'brun', 'roux', 'blond', 'blanc', 'rouge', 'vert', 'bleu'), 
couleur_peau ENUM('blanche', 'bazanee', 'noire'),
FOREIGN KEY (id_publication) REFERENCES Publications(id)
);


CREATE TABLE IF NOT EXISTS Commentaires (
id INTEGER UNSIGNED, id_utilisateur INTEGER UNSIGNED, date_creation DATE, texte CHAR(150),
id_publication INTEGER UNSIGNED, id_commentaire INTEGER UNSIGNED,
PRIMARY KEY (id),
FOREIGN KEY (id_utilisateur) REFERENCES Utilisateurs(id),
FOREIGN KEY (id_publication) REFERENCES Publications(id),
FOREIGN KEY (id_commentaire) REFERENCES Commentaires(id)
);


CREATE TABLE IF NOT EXISTS Aimer (
id_utilisateur INTEGER UNSIGNED, id_publication INTEGER UNSIGNED,
id_commentaire INTEGER UNSIGNED,
FOREIGN KEY (id_utilisateur) REFERENCES Utilisateurs(id),
FOREIGN KEY (id_publication) REFERENCES Publications(id),
FOREIGN KEY (id_commentaire) REFERENCES Commentaires(id)
);


CREATE TABLE IF NOT EXISTS NePasAimer (
id_utilisateur INTEGER UNSIGNED, id_publication INTEGER UNSIGNED,
id_commentaire INTEGER UNSIGNED,
FOREIGN KEY (id_utilisateur) REFERENCES Utilisateurs(id),
FOREIGN KEY (id_publication) REFERENCES Publications(id),
FOREIGN KEY (id_commentaire) REFERENCES Commentaires(id)
);


CREATE TABLE IF NOT EXISTS Suivre (
id_utilisateur INTEGER UNSIGNED, id_communaute INTEGER UNSIGNED,
FOREIGN KEY (id_utilisateur) REFERENCES Utilisateurs(id),
FOREIGN KEY (id_communaute) REFERENCES Communautes(id)
);


CREATE TABLE IF NOT EXISTS Signaler (
id INTEGER UNSIGNED, id_publication INTEGER UNSIGNED, id_commentaire INTEGER UNSIGNED,
date_creation DATE, fait BIT(1),
PRIMARY KEY (id),
FOREIGN KEY (id_publication) REFERENCES Publications(id),
FOREIGN KEY (id_commentaire) REFERENCES Commentaires(id)
);


CREATE TABLE IF NOT EXISTS Notifications (
id INTEGER UNSIGNED, id_utilisateur INTEGER UNSIGNED, id_publication INTEGER UNSIGNED,
id_commentaire INTEGER UNSIGNED, vu BIT(1), date_creation DATE,
type ENUM('bienvenu', 'estcevous', 'supprime'),
PRIMARY KEY (id),
FOREIGN KEY (id_utilisateur) REFERENCES Utilisateurs(id),
FOREIGN KEY (id_publication) REFERENCES Publications(id),
FOREIGN KEY (id_commentaire) REFERENCES Commentaires(id)
);


CREATE TABLE IF NOT EXISTS Notifications_EstCeVous (
id_notification INTEGER UNSIGNED, reponse_estcevous BIT(1), reponse_contact BIT(1),
FOREIGN KEY (id_notification) REFERENCES Notifications(id)
);
