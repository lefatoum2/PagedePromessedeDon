# PagedePromessedeDon

Grâce à Python, vous allez mettre en place une page de promesse de dons pour une association.

## Contexte du projet


Votre client est une association caritative qui veut récolter des dons sur le web. Pour ça, il a besoin d'une page qui présente la cause défendue et d'un formulaire de promesse de don. Ces promesses doivent évidement être sauvegardées (pour relancer les donnateurs et gérer la partie juridique des dons) et consultables en un clique sur une page web. Votre travail est de mettre en place le site, le client a déjà contacté un web designer pour l'UI/UX.

## Modalités pédagogiques


Vous devez créer un site web dynamique en utilisant PYTHON, HTML/CSS (BOOTSTRAP est autorisé). Ce site doit contenir :

Une page d'accueil qui présente l'association et la bonne cause à financer,
Un formulaire qui permet de faire une promesse de don (avec saisie du nom, prénom, adresse, mail, somme promise, une coche 'vous avez pris connaissance..',...),
Un page qui affiche toutes les informations sur les promesses de don (Liste des donnateurs, sommes promises, emails à contacter), ainsi que le total récolté.
Les informations du formulaire sont à stocker dans une base MONGODB. Le format des documents est à votre appréciation.

Vous devez mettre en place un site fonctionnel, le design n'est pas une priorité. Il n'est à faire que lorsque toutes les pages fonctionnent.

Pour le contenu, vous êtes libre de choisir l'association que vous souhaitez et de vous inspirez de son site officiel pour vos travaux. Vous pouvez faire un peu de veille concurentielle pour personnaliser vos pages.

Une option peut être ajoutée : un formulaire de login sur la page récapitulative des dons. Demandez un login/mot de passe et si la personne est identifiée, en base, comment étant un responsable de l'association alors elle accède à la page récapitulative.

C'est un travail individuel.

## Critères de performance

Le site doit contenir les 3 pages demandées. Les pages doivent être lisibles et la base doit bien contenir toutes les informations saisies sur le formulaire. l'UI/UX n'est pas obligatoire, votre travaille est d'apprendre à restituer des données sur le web, pas à faire du design.

## Modalités d'évaluation

Présentation de 5 minutes du site devant l'ensemble de la promo. Évaluation par les paires.

## Livrables

Un lien vers un projet GITHUB qui contient le code Python et HTML/CSS du site et un readme qui explique la base mise en place. La base de données doit être créée sur MONGODB ATLAS.

## Documentation 
https://flask.palletsprojects.com/en/1.1.x/patterns/wtforms/
https://stackoverflow.com/questions/38402850/validate-that-a-wtforms-booleanfield-is-checked
https://www.programcreek.com/python/example/82254/wtforms.IntegerField
https://wtforms.readthedocs.io/en/2.3.x/fields/

## Base de données

Pour ce projet, il a été créé une base de donnée et une collection dons où j'ai pu stocker les noms et prénoms , les emails et les dons promis. 
Pour créer une session, il aurait fallu créer une deuxième collection qui aurait pour nom , utilisateur. 
