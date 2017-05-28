--insertion dans table Matiere 
insert into Matiere (identifiantMat ,nomMat) values (1,'Bouteille');
insert into Matiere (identifiantMat ,nomMat) values (2,'Plastique (PET)');
insert into Matiere (identifiantMat ,nomMat) values (3,'Flacon');
insert into Matiere (identifiantMat ,nomMat) values (4,'Bidon');
insert into Matiere (identifiantMat ,nomMat) values (5,'Conserve');
insert into Matiere (identifiantMat ,nomMat) values (6,'Métal');
insert into Matiere (identifiantMat ,nomMat) values (7,'Carton');
insert into Matiere (identifiantMat ,nomMat) values (8,'Brique');
insert into Matiere (identifiantMat ,nomMat) values (9,'Papier');
insert into Matiere (identifiantMat ,nomMat) values (10,'Canette');
insert into Matiere (identifiantMat ,nomMat) values (11,'Verre');
insert into Matiere (identifiantMat ,nomMat) values (12,'Dosette');
insert into Matiere (identifiantMat ,nomMat) values (13,'Plastique');
insert into Matiere (identifiantMat ,nomMat) values (14,'Sachet');
insert into Matiere (identifiantMat ,nomMat) values (15,'Sac');
insert into Matiere (identifiantMat ,nomMat) values (16,'Barquette');
insert into Matiere (identifiantMat ,nomMat) values (17,'Beutel');
insert into Matiere (identifiantMat ,nomMat) values (18,'Emballage');
insert into Matiere (identifiantMat ,nomMat) values (19,'Film');
insert into Matiere (identifiantMat ,nomMat) values (20,'Pot');
insert into Matiere (identifiantMat ,nomMat) values (21,'Tube');
insert into Matiere (identifiantMat ,nomMat) values (22,'Filet');
insert into Matiere (identifiantMat ,nomMat) values (23,'Bois');
insert into Matiere (identifiantMat ,nomMat) values (24,'Gourde');
insert into Matiere (identifiantMat ,nomMat) values (25,'Aluminium');
insert into Matiere (identifiantMat ,nomMat) values (26,'Polystyrène');

-- insertion Poubelle 
insert into Poubelle (idPoub ,couleurPoub) values (1, 'Bac bleu');
insert into Poubelle (idPoub ,couleurPoub) values (2, 'Poubelle grise avec un couvercle vert');
insert into Poubelle (idPoub ,couleurPoub) values (3, 'Poubelle bleu');
insert into Poubelle (idPoub ,couleurPoub) values (4, 'Poubelle grise avec un couvercle jaune');
insert into Poubelle (idPoub ,couleurPoub) values (5, 'Poubelle pour le verre uniquement');
insert into Poubelle (idPoub ,couleurPoub) values (6, 'Magasin Nespresso ou autre point de collecte');
insert into Poubelle (idPoub ,couleurPoub) values (7, 'Poubelle grise à couvercle rouge.');

--insertion dans Région
insert into Region (numeroR ,nomR) values (1,'Occitanie');


-- insertion Municipalite
insert into Municipalite (idMun ,nomMun,ville,codePostal,idRegion) values (1,'' ,'Saint-Sulpice',81370,1);
insert into Municipalite (idMun ,nomMun,ville,codePostal,idRegion) values (2,'' ,'Toulouse',31000,1);
insert into Municipalite (idMun ,nomMun,ville,codePostal,idRegion) values (3,'' ,'Villeneuve-Tolosane',31270,1);

-- insertion Trie
insert into Trie (idPoub, idMun, identifiantMat, consigneTri) values (4,3, 1,'');
insert into Trie (idPoub, idMun, identifiantMat, consigneTri) values (4,3, 2,'');
insert into Trie (idPoub, idMun, identifiantMat, consigneTri) values (4,3, 3,'');
insert into Trie (idPoub, idMun, identifiantMat, consigneTri) values (4,3, 4,'');
insert into Trie (idPoub, idMun, identifiantMat, consigneTri) values (4,3, 5,'Bien rincer');
insert into Trie (idPoub, idMun, identifiantMat, consigneTri) values (4,3, 6,''); 
insert into Trie (idPoub, idMun, identifiantMat, consigneTri) values (4,3, 7,' sauf cartons gras');
insert into Trie (idPoub, idMun, identifiantMat, consigneTri) values (4,3, 8,'');
insert into Trie (idPoub, idMun, identifiantMat, consigneTri) values (4,3, 9,'');
insert into Trie (idPoub, idMun, identifiantMat, consigneTri) values (4,3, 10,'');
insert into Trie (idPoub, idMun, identifiantMat, consigneTri) values (5,3, 11,'');
insert into Trie (idPoub, idMun, identifiantMat, consigneTri) values (6,3, 12,'');
insert into Trie (idPoub, idMun, identifiantMat, consigneTri) values (7,3, 13,'');
insert into Trie (idPoub, idMun, identifiantMat, consigneTri) values (7,3, 14,'');
insert into Trie (idPoub, idMun, identifiantMat, consigneTri) values (7,3, 15,'');
insert into Trie (idPoub, idMun, identifiantMat, consigneTri) values (7,3, 16,'');
insert into Trie (idPoub, idMun, identifiantMat, consigneTri) values (7,3, 17,'');
insert into Trie (idPoub, idMun, identifiantMat, consigneTri) values (7,3, 18,'');
insert into Trie (idPoub, idMun, identifiantMat, consigneTri) values (7,3, 19,'');
insert into Trie (idPoub, idMun, identifiantMat, consigneTri) values (7,3, 20,'');
insert into Trie (idPoub, idMun, identifiantMat, consigneTri) values (7,3, 21,'');
insert into Trie (idPoub, idMun, identifiantMat, consigneTri) values (7,3, 22,'');
insert into Trie (idPoub, idMun, identifiantMat, consigneTri) values (7,3, 23,'');
insert into Trie (idPoub, idMun, identifiantMat, consigneTri) values (7,3, 24,'');
insert into Trie (idPoub, idMun, identifiantMat, consigneTri) values (7,3, 25,'');
insert into Trie (idPoub, idMun, identifiantMat, consigneTri) values (7,3, 26,'');

--insertion Région
insert into Region (numeroR,nomR) values (1, 'Occitanie');  
insert into Produit (EAN, nomP) values (3037920132006, 'Mélange d''épices pour guacamole'); 
insert into EstFait (EAN,identifiantMat) values (3037920132006, 14);
insert into EstFait (EAN,identifiantMat) values (3037920132006, 15);