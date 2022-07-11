# PROJET MICRO LANGUAGE en python

## Commande FIND:
> ex : FIND langue-des-signes CP 78300 LIMIT 1
recherche un élement 

### OPTION DE LA COMMANDE FIND

#### CP
> obligatoire
code postal de la ville de la recherche
 
#### Limit
>pas obligatoire
limite le nombre de résultat

#### WHERE
a définir 

### RETOUR DE LA COMMANDE : 

Number result : XX

===============
Name : ...
Desc : ...
URL LOGO : ...
PLACE : ...
ID : ...
==============

## Commande SELECT : 
> ex : SELECT * FROM id
recupère les infos de bases d'une element 

### OPTION DE LA COMMANDE 

#### FROM 
> obligatoire 
from est toujours suivi d'un id recupé via la commande FIND 

#### * ou ex [title] , [Name]
* -> tout
sinon selection des élement a afficher 

### RESULTAT DE LA RECHERCHE

===============
Title : ...
Name : ...
Price?: ...
Price with gouverment help?: ...
Quotation_url : ... 
AVIS : ...
LOGO_URL : ...
LAST_CONNEXION : ...
NUM? : ...
CONTACT_FROM_URL : ... 
===============
