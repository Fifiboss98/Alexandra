#!/usr/bin/env python
# pylint: disable=W0613, C0116
# type: ignore[union-attr]
# This program is dedicated to the public domain under the CC0 license.

import os
import sys
import logging
from decouple import config 
from threading import  Thread
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
    MessageHandler
)

TOKEN = config("TOKEN")

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

B1, B2, B3, B4, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34, B35, B36, B37, B38, B39, B40, B41, B42, B43, B44, B45, B46, B47, B48, B49, B50, B51, B52, B53, B54, B55, B56, B57, B58, B59, B60, B61, B62, B63, B64, B65, B66, B67, B68, B69, B70, B71, B72, B73, B74, B75, B76, B77, B78= range(78)


def start(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Hum… pas vraiment',  'Un peu oui' ,  'Pas du tout']]

    update.message.reply_text('Salut, je suis Alexandra Ivanov, un gentil robot créée par Fidèle Dossou, crypto enthousiaste béninois. \n Je suis là pour t’accompagner d’une manière simple et conviviale dans ton aventure dans le monde des cryptos. \n Pour commencer sais-tu ce que veut dire blockchain ?',  
    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )

    return B1
    
def b1(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Système de datage ?']]

    update.message.reply_text('Ok. La blockchain est tout simplement un système de datage sécurisé rapide et efficace.  \n Utilisé principalement dans le domaine des crypto monnaies, son adoption depuis sa création n’a cessé de croitre. ',  
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        )

    return B2
    
    
def b2(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Pour toujours ?']]

    update.message.reply_text("Oui. Tu sais amigo, le nom originel de la blockchain était Tamperproof server ce qui veut dire serveur de datage. \n C’est un système où tout ce qui s’y passe est gravé pour toujours. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
   
    return B3
    
    
def b3(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Ok je vois. \n Mais j’imagine un peu… il doit être énorme ce cahier !']]

    update.message.reply_text('Oui bébé. \n En réalité, la blockchain est née d’un concept. Celui de créer un écosystème sûr sans tiers de confiance. \n La blockchain peut aussi être considérée comme un vaste réseau où toutes les activités sont consignées dans un gros cahier infalsifiable distribué à tous les nœuds du réseau. \n Ne panique pas nous verrons ce terme un peu plus tard. \n Mais déjà sache que ce sont les mineurs qui assurent à 80% la sécurité du réseau. ',
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B4


def b4(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['300 Go !!! \n Santa Maria !']]
    update.message.reply_text( "Oh que oui mon chou ! \n Sa taille dépend de la fréquence d’activité sur le réseau. \n Par exemple,  la blockchain du bitcoin créée par le fameux Satoshi Nakamoto pèse plus de 300 Go a l’heure où je te parle. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B5

def b5(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Hahaha']]
    update.message.reply_text( "Stp laisse dame Marie en dehors de ça.",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B6

def b6(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Wow ! ça devient intéressant.']]
    update.message.reply_text( "Cela veut juste dire que tu peux voyager à travers la blockchain en remontant jusqu’à la toute première transaction jamais effectuée sur le bitcoin, consulter l’historique des transactions de tous les portefeuilles que tu veux, interagir avec la blockchain etc ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B7
    
def b7(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Cool alors. Dis, tu parlais de nœuds tout à l’heure… ']]
    update.message.reply_text( "Le sujet de la blockchain est très passionnant tu peux en être certain petit cœur. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B8
    
def b8(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['500 projets !!! ']]
    update.message.reply_text( "En effet, qu’est ce qu’un nœud ? \n Avant de répondre à cette question laisse moi te mettre l’accent sur ceci. \n La blockchain est un système décentralisé ; c’est à dire dépourvu d’autorité centrale. \n Ce qui implique que personne ne dicte les lois dans une blockchain. \n C’est un programme entièrement créé par la communauté et pour la communauté. Le Bitcoin est la première crypto à avoir utilisé la blockchain. \n Les quelques 500 autres cryptos ayant précédé ont presque tous échoué. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B9

def b9(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Euh… Pourquoi ? ']]
    update.message.reply_text( "Oh que oui trésor. \n Ce n’est pas en 2008 que les gens ont commencé à réfléchir à une sorte de monnaie virtuelle. \n Mais ils sont tous mort ces projets. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B10

def b10(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['DSR ? ']]
    update.message.reply_text( "Tout simplement parce qu’il leur manquait un pilier du DSR. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B11

def b11(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Ah d’accord ! ']]
    update.message.reply_text( "Oui mon chou. \n DSR est un code que j’ai créé pour me rappeler les trois solutions majeures apportées par le Bitcoin qui ont notamment soutenu son adoption en masse. \n DSR veut dire Décentralisation, Sécurité et Rapidité. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B12

def b12(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['C’est triste... ']]
    update.message.reply_text( "Le Bitcoin a su allier robustesse efficacité, sécurité et décentralisation dans un seul plat. \n Notre système financier actuel souffre cruellement d’inégalités inavouées.  ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B13

def b13(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Alors la blockchain résous en quelque sorte ces inégalités ? ']]
    update.message.reply_text( "En effet… ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B14

def b14(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Mais ?  ']]
    update.message.reply_text( "Oui \n Mais… ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B15

def b15(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Toute action ? ']]
    update.message.reply_text( "Malgré toutes ces caractéristiques hautement louables, des individus malhonnêtes obnubilés par l’appât du gain facile tentent de duper le système par un moyen ou par un autre. \n C’est en ce moment qu’intervient le rôle primordial des mineurs. \n Satoshi Nakamoto a employé le mot nœud. \ n C’est avec l’évolution des choses que des expressions comme validateur, mineur, générateur de blocs etc. ont vu le jour. \ n Mais ne t’en fais pas toutes ces expressions veulent pratiquement dire la même chose. \n En gros, un mineur ou un nœud si tu préfères est toute personne qui assure la sécurité du réseau en gardant un œil sur tout ce qui se passe. \n C’est en quelques sortes une porte d’accès au réseau concerné. \n Toute action de quelque nature que ce soit passe obligatoirement par au moins un nœud. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B16

def b16(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Wahoo!!! \n C’est donc ça un nœud. ']]
    update.message.reply_text( " Oui  absolument toute action. \n N’oublie pas que la blockchain est dépourvue d’autorité centrale donc ce sont les nœuds qui gardent une copie de l’état d’avancement des choses. \n La moindre transaction que tu réalises doit passer par un nœud avant d’être validée car n’importe qui doit pouvoir vérifier l’effectivité de la transaction à n’importe quel moment.",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B17

def b17(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Cryptographie… hum… ']]
    update.message.reply_text( "Oui mon cœur. \n La blockchain en elle-même est inébranlable de par son architecture car elle bénéficie des avantages de la cryptographie a clé unique. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B18

def b18(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Vraiment ?']]
    update.message.reply_text( "La cryptographie est en résumé la science permettant de sécuriser les données. \n La blockchain étant une structure décentralisée il faut qu’elle soit robuste en elle-même. \n Pour cela les données sont cryptées, autrement dit elles sont cachées. \n La cryptographie n’est pas difficile à comprendre. \n Même toi tu as déjà utilisé la cryptographie sans le savoir. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B19

def b19(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Hein ? ']]
    update.message.reply_text( "Absolument trésor. \n Tiens dis-moi quand as-tu croisé une meuf pour la dernière fois ?  ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B20

def b20(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Lol. \n Où est le rapport ?  ']]
    update.message.reply_text( "Il n’y a qu’un troglodyte qui ne sait pas que meuf est l’inverse de ‘’femme’’ en verlan. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B21

def b21(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Hahaha. Drôle']]
    update.message.reply_text( "Bonne question. \n En inversant les syllabes de femme pour obtenir meuf tu as justement fait de la cryptographie. \n Le troglodyte n’en saura jamais rien et mieux, tu peux lui piquer sa meuf au passage. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B22

def b22(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Oui j’imagine… ']]
    update.message.reply_text( "En effet hihihi \n Cela paraît facile au premier abord mais avec les ordinateurs c’est beaucoup plus compliqué. \n Et par conséquent beaucoup plus sécurisé. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B23 

def b23(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Je vois… ']]
    update.message.reply_text( "Tu entendras parler de SHA, RIPEMD, X11 etc. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B24

def b24(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Absolument']]
    update.message.reply_text( "J’avoue que ce n’est pas facile quand on débute en blockchain avec tous ces nouveaux termes. \n Mais laisse-moi te dire que si tu veux vraiment être un incontournable en blockchain il te faut beaucoup de lecture. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B25 

def b25(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Très bien. ']]
    update.message.reply_text( "Néanmoins je tâcherai de te faire découvrir les bases histoire de te donner un avant-gout. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B26

def b26(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Ben on n’a qu’à introduire une sorte de récompense destinée aux mineurs. Simple et efficace.  ']]
    update.message.reply_text( "Évoluons un peu jeune soldat. \n Mettons-nous un instant à la place de Satoshi Nakamoto. \n Nous voulons construire un système robuste, décentralisé et rapide où les gens pourront s’envoyer de l’argent sans intermédiaire de confiance. \n Le système devant être à tout prix dénué d’autorité centrale, chacun doit être libre d’intervenir et/ou de se retirer à tout moment s’il le souhaite. \n Une question cruciale se pose : ce truc n’a jamais réussi auparavant. \n  Mais nous, nous croyons en la faisabilité de la chose. \n Dis-moi petit génie t’aurais pas une petite idée de comment nous y prendre pour ne pas essuyer un échec ? ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B27 

def b27(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Sans soucis... ']]
    update.message.reply_text( "Ah ça ! \n Tu es vraiment un génie. \n Rappelle-le-moi je te dois une bière. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B28 

def b28(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Vilain robot']]
    update.message.reply_text( "Euh… une minute chéri. \n Notre ami Satoshi y avait déjà pensé avant toi !!!  \n Donc désolé plus de bière. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B29 

def b29(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Hum… Je vois. \n Que veut dire clé privée ? ']]
    update.message.reply_text( "Hahaha \n Eh oui. La vie est injuste. \n Satoshi a ainsi implémenté un système de génération de revenus par deux activités sur la blockchain. \n La première est la validation des transactions, ici, le mineur collectionne les frais de transaction. \n La deuxième, celle qui retiendra le plus notre attention est le minage des blocs. \n Retenons d’abord ceci : la validation ou minage des blocs est différente de la validation des transactions. \n Lorsque tu effectues une transaction sur la blockchain celle-ci n’est pas automatiquement envoyée vers l’expéditeur mais reste d’abord en file d’attente. \n Si un mineur tombe sur votre transaction il vérifie d’abord si le solde est suffisant pour la transaction et si la clé privée utilisée pour signer la transaction est valable. \n Si tout est ok il la valide¸ avale les frais de transactions...\n  euh non il les encaisse plutôt et la laisse aux mineurs de blocs qui l’incluront dans la blockchain. \n  Il peut toutefois le faire lui-même s’il mine aussi les blocs. \n Il est bon de savoir que la validation des blocs varie d’une blockchain à une autre. \n Chacun l’implémente à sa façon.  ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B30

def b30(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Ouiii…. ']]
    update.message.reply_text( "Oups je suis allée un eu trop vite on dirait… ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B31 

def b31(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Qu’est-ce qu’une crypto monnaie d’abord ? ']]
    update.message.reply_text( "Voilà. Je disais tantôt que la blockchain est beaucoup utilisée dans le domaine des crypto monnaies… ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B32 

def b32(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Raah bon? ']]
    update.message.reply_text( "Cela peut te surprendre mais tu as déjà utilisé les cryptos sans le savoir.. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B33 

def b33(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [[" Ah ! Sorcière!!! \n Comment t'as su ??? "]]
    update.message.reply_text( "Oui chou. \n Je ne connais pas ton compte en banque actuellement mais je sais que c’est un nombre décimal. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B34

def b34(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Ok je vois. \n Alors comment fonctionne elle avec la blockchain ? ']]
    update.message.reply_text( "Hahaha. \n Où je veux en venir est que ton compte ne reflète jamais ce qui est dans les réserves de la banque. \n Aucune pièce ou billet de 0.001 euro n’existe. \n Tout ce que tu vois c’est du virtuel, une sorte de monnaie digitale donc de la crypto monnaie.  ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B35 

def b35(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Au moins deux exemples ']]
    update.message.reply_text( "Bonne question. \n Pour résumer la blockchain sert de couche de sécurité à la crypto monnaie. \n A partir du moment où toutes les transactions sont désormais visibles par tous, horodatées et ineffaçables, le risque de tricherie est éliminé. \n De plus la blockchain a tellement d’autres domaines d’applications qu’il serait difficile de tous les développer ici.  ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B36 

def b36(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Pourquoi ? ']]
    update.message.reply_text( "Bon bon ok. \n Le premier exemple qui me vient à l’esprit est l’enregistrement de documents. \n En effet selon la configuration de la blockchain il peut être possible d’enregistrer telle ou telle taille de fichiers. \n Comme par exemple des actes de naissances, sais pas moi… des conventions de vente pff plein de choses…à condition que lesdits documents ne contiennent pas d’informations confidentielles car ne l’oublie jamais tout ce qui est sur la blockchain est visible par tous. \n Le second exemple que je peux donner est l’enregistrement d’œuvres d’art. \n  Si tu es artiste et que tu te soucies de ton copyright, l’agence nationale est une option mais la blockchain est le meilleur choix que tu puisses faire. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B37 

def b37(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Wow ! ']]
    update.message.reply_text( "Très bien. \n Procédons par comparaison… \n L’agence nationale te prends une somme considérable pour enregistrer ton œuvre, avec la blockchain notamment signature chain qui est un projet à propos développé sur la blockchain Waves, tu n’as même pas à payer le dixième des frais exigés par l’agence nationale avec de biens meilleurs avantages. \n Enregistrement immédiat contrairement aux nombreux jours où tu dois attendre ailleurs, un système plus sécurisé et plus robuste ; tu n’as pas à craindre une éventuelle perte de données ; enfin vient la cerise sur le gâteau : tu peux vendre ton œuvre en toute simplicité sans jamais te déplacer de chez toi. \n Au cas où tu voudrais aller plus loin www.signaturechain.com  ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B38 

def b38(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['A vos ordres capitaine ! ']]
    update.message.reply_text( "On avance soldat! ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B39 

def b39(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Oui robot chou ']]
    update.message.reply_text( "Bien. \n Depuis un moment on parle de transactions mais comment se passe réellement la chose c’est ce que nous allons découvrir maintenant. \n Pour faire des transactions à la banque tu as besoin d’un portefeuille n’est ce pas champion ? ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B40 

def b40(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Enfin on y arrive !  ']]
    update.message.reply_text( "Eh ben c’est pareil avec les cryptos. \n Sauf qu’ici tu as plus de pouvoir qu’à la banque. \n Un compte sur la blockchain n’est rien d’autre qu’une paire de clés. \n Clé publique clé privée. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B41 

def b41(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Oh ok… ']]
    update.message.reply_text( "Je ne t’avais pas oublié mon cœur.\n Une clé publique est ce qui te permet d’envoyer et de recevoir des cryptos sur la blockchain. \n Chaque blockchain avec sa paire de clé associée. \n Tu ne peux pas utiliser l’un sur l’autre. \n Comme son nom l’indique cette clé peut être publique mais pas la clé privée. \n Une clé privée est une sorte de mot de passe associé à ton compte. \n C’est grâce à la clé privée que tu prouves que tu es le détenteur des pièces et l’expéditeur de telle transaction. \n Et c’est ce qui permet aux mineurs de pouvoir valider ta transaction.",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B42

def b42(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['C’est compris. ']]
    update.message.reply_text( "Evidemment nul n’est besoin de te rappeler qu’il ne faut jamais divulguer ta clé privée à qui que ce soit. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B43 

def b43(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['PoW PoS… hum ']]
    update.message.reply_text( "Chaque blockchain avec ses règles et méthodes de fonctionnement. \n Les blocs sont créés certes mais ne sont pas validés de la même manière. \n En parlant de méthode de validation des blocs voyons rapidement les deux formes les plus courantes. \n La méthode par résolution de calculs mathématiques appelée PoW et la validation par présentation de preuve de propriété PoS. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B44 

def b44(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Que veut dire selfish mining ? ']]
    update.message.reply_text( "PoW veut dire Proof of Work. \n Si tu veux valider les blocs sur la blockchain bitcoin par exemple, il te faut d’abord toute l’historique de la blockchain en plus de grosses machines appelées rigs de minage capables d’effectuer des calculs Mathématiques très complexes. \n Le problème avec ce genre de validation est qu’il est gourmand en énergie et pas toujours rentable. \n De plus il cache deux vecteurs d’attaque pouvant nuire à la réputation du système. \n Il s’agit du selfish mining et de l’attaque des 51%. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B45 

def b45(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Cousin lol ']]
    update.message.reply_text( "Le minage égocentrique ou selfish mining est un phénomène découvert pour la première fois par le Prof Emin Gün Sirer, un Old Gangster (pour dire qu’il est un ancien du game) dans le monde de la blockchain et son associé Ittay Eyal mon cousin ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B46 

def b46(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Aargh!! Les fils de… !! ']]
    update.message.reply_text( "Étant donné le fait que selon le PoW c’est celui qui a la plus grande puissance de calcul qui validera le plus de blocs, les mineurs ont réfléchi à ce type d’attaque. \n Le selfish mining consiste à se réunir en groupe de minage pour augmenter la puissance de calcul, ensuite de créer des ramifications de la chaîne principale afin de miner le plus de blocs possible puis de les greffer plus tard à la blockchain mère. \n C’est une attaque qui peut rapporter des millions de dollars. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B47 

def b47(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['En quoi consiste l’attaque des 51% ? ']]
    update.message.reply_text( "Évidemment c’est dommage. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B48 

def b48(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Bien sûr. ']]
    update.message.reply_text( "Tu te souviens que la blockchain est une longue chaine de blocs infalsifiable non? ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B49 

def b49(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Ok ']]
    update.message.reply_text( "En effet elle est infalsifiable mais pas non duplicable. \n Dans une blockchain, il faut que la majorité des mineurs s’accordent pour sécuriser le réseau. \n Mais ce n’est pas toujours le cas. \n Les cupides veulent toujours contourner l’éthique. \n Ce que je m’apprête à t’expliquer est un peu complexe donc à lire posément. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B50 

def b50(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Ok ']]
    update.message.reply_text( "La blockchain a résolu plusieurs problèmes de la finance traditionnelle dont notamment celui de la double dépense. \n Qui dit falsification de billet de banque en finance traditionnelle dit double dépense en crypto. \n Ce sont deux phénomènes assez similaires. \n Sauf qu’ici tu ne peux pas falsifier la crypto mais tu peux réécrire la blockchain et réutiliser tes Bitcoins (ou la monnaie du réseau concerné) dans la nouvelle chaîne alors qu’ils étaient déjà dépensés selon l’historique de l’autre chaîne. \n C’est un scénario assez complexe à mettre en œuvre puisqu’il faut considérer la puissance de hashage du réseau, le coût de location de serveurs, la puissance de hashage disponible etc \n Il est à retenir que ce genre d’attaque n’est possible que si la blockchain fonctionne sur un algorithme PoW. \n Les algorithmes PoS sont résistants à ce genre d’attaque comme nous allons le voir par la suite. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B51 

def b51(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Ah oui ! Donc le PoS est plus sécurisé que le PoW. \n Je comprends ']]
    update.message.reply_text( "PoS veut dire Proof of Stake. \n Contrairement au PoW où il te faut une grosse puissance de calculs avec tous ces vecteurs d’attaques en plus un système PoS ne requiert le plus souvent qu’un matériel modeste. \n Sauf qu’ici il te faut détenir une certaine quantité des pièces de la plateforme. \n Ceci afin de sécuriser davantage le réseau. \n  Avec ton argent impliqué désormais tu réfléchiras par trois fois avant d’attaquer le réseau. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B52 

def b52(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Delegated Proof of Stake !! ']]
    update.message.reply_text( "Absolument. \n Il existe une variété de systèmes PoS. \n Nous avons le Delegated PoS (DPoS), le Leased Proof of Stake etc \n Le problème constaté est que les gens veulent participer à la validation des blocs mais soit n’ont pas assez de moyens soit sont assez limités techniquement. \n Monter un nœud exige des connaissances en informatique bien entendu. \n Commençons par le DPoS ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B53 

def b53(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Interessant ']]
    update.message.reply_text( "Bravo pour la définition ! \n Dans Delegated nous avons le fait de déléguer ses pièces. \n  Par exemple il faut 1000 Waves pour tourner un nœud sur la blockchain Waves. \n Même si tu n’as pas le montant requis, le DPoS te permet de déléguer tes pièces à quelqu’un qui les a pour que vous puissiez partager les récompenses une fois les transactions ou les blocs minés. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B54 

def b54(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Oui je vois. \n Cool ! ']]
    update.message.reply_text( "Pareil pour le LPoS utilisé sur la blockchain Waves. \n Sauf qu’ici les pièces que tu délègues ou que tu loues ne quittent jamais ton portefeuille. \n  Dans un DPoS ils doivent quitter ton portefeuille donc c’est en quelques sortes moins sécurisé que le LPoS. \n Dans l’un tu as le contrôle total de tes fonds, dans l’autre non. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B55 

def b55(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Ah ouais ? \n Je t’écoute… ']]
    update.message.reply_text( "Tu sais mon ami si je t’ai fait faire tout ce chemin c’est pour que tu aies une base solide avant que je ne t’introduise au protocole Waves, actuellement l’une des meilleures blockchains existantes. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B56 

def b56(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Bon à savoir ']]
    update.message.reply_text( "Le plus souvent en crypto les noms des projets n’ont pas véritablement une signification en tant que telle. \n Tu entendras parler de Ethereum, Litecoin, Zcash, Monero, Waves etc ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B57 

def b57(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['D’accord ']]
    update.message.reply_text( "Tu peux aller faire un tour sur www.coinmarketcap.com pour apprécier la multitude de crypto monnaies existantes. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B58 

def b58(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Ah bon ? \n Dis-moi plus stp ']]
    update.message.reply_text( "Waves est une plateforme qui a été créée par un informaticien russo-ukrainien de renom. \n Il s’agit du sieur Alexandr Ivanov également connu sous le pseudonyme Sasha Ivanov. \n Sasha a créé énormément de choses que nous ne saurions finir d’éplucher aujourdh’hui. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B59 

def b59(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['C’est quoi un DEX ? ']]
    update.message.reply_text( "Parmi ses œuvres on peut citer entre autres Coinomat, un échangeur decentralisé automatique ou DEX plus simplement et un stablecoin (crypto monnaie créée dans le but de contrer la volatilité du marché). ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B60 

def b60(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Te rappeler quoi ? ']]
    update.message.reply_text( "Bonne question !! \n Rappelle-le moi stp. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B61

def b61(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Mdrr ']]
    update.message.reply_text( "Que je te dois un yaourt pour la question. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B62 

def b62(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Comment ça ? ']]
    update.message.reply_text( "Hahaha .\n Je disais tout à l’heure qu’un DEX (Decentralised Exchange en anglais) est un échangeur où contrairement aux échangeurs traditionnels qui ne font que coordonner les ordres d’achats et de vente des uns et des autres, un Dex lui, ne répertorie aucun ordre. \n Tu achètes et vends tes cryptos au prix actuel du marché. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B63 

def b63(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Ok mais est-ce rentable ? ']]
    update.message.reply_text( "Voilà je t’explique. \n D’abord le Dex est constitué de ce qu’on appelle une pool. \n Chaque paire de crypto avec sa pool. \n Pool en anglais veut dire équipe. \n En crypto cela veut dire réserve de fonds. \n Le plus souvent ceux qui assurent la liquidité sur les Dex approvisionnent les pools en proportions égales. \n Par exemple si tu veux ajouter de la liquidité sur la paire BTC/ETH tu donnes une certaine quantité de BTC et une portion proportionnelle en ETH également. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B64

def b64(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Intéressant alors ']]
    update.message.reply_text( "Oh que oui trésor. \n Les investisseurs du Dex gagnent des dividendes des frais liés aux transactions effectuées par les utilisateurs. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B65

def b65(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Pourquoi faire ? ']]
    update.message.reply_text( "Ouaip \n Ensuite le Dex utilise ce qu’on appelle en crypto un oracle.  \n Oracle selon le jargon cryptodique veut dire tout simplement source d’informations. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B66

def b66(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Hahaha ']]
    update.message.reply_text( "Une autre bonne question. \n Ça fait deux yaourts ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B67

def b67(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Quoi ? ']]
    update.message.reply_text( "En effet l’oracle est vital pour un Dex. \n Le marché des cryptos étant très volatile (c’est-à-dire que les valeurs des monnaies bougent dans les deux sens) alors les conversions entre-elles varient à chaque seconde. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B68

def b68(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Ok je vois. \n L’Oracle sert à synchroniser les données du marché. ']]
    update.message.reply_text( "Oui mon amour. \n 1 BTC peut équivaloir à 200 ETH à un instant t par exemple et varier à 206 ETH une minute après pour une raison ou pour une autre. \n Imagine un Dex qui te propose 1BTC à 200 ETH à t+ une minute alors qu’il est à 206 normalement !!! ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B69

def b69(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Oulàlà. ']]
    update.message.reply_text( "Là je te dois non un yaourt mais un gros bisou. \n Tu comprends vite les choses c'est bien. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B70

def b70(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['C’est vrai. ']]
    update.message.reply_text( "C’est exact. \n L’oracle permet au Dex d’être continuellement à jour des mouvements du marché. \n Un oracle maladif peut mettre en péril l’argent des investisseurs. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B71

def b71(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Fort bien. ']]
    update.message.reply_text( "Avançons un peu plus. \n Tu sais mon chou à la crème qu’il est très onéreux de faire fonctionner une blockchain qui plus est depuis 2016. \n Cela demande non seulement des moyens financiers mais aussi des ressources humaines. \n Si Waves tient encore debout jusqu’à aujourd’hui c’est surtout grâce à sa communauté. \n Elle est fière d’appartenir à un écosystème dont le souci est de faire adopter la blockchain à la plus grande masse. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B72

def b72(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Quoi ? vraiment ? ']]
    update.message.reply_text( "Depuis sa création Waves ne cesse d’innover malgré les ressources limitées dont ils disposent. \n Eh oui. \n Par exemple, tu n’as besoin d’aucune connaissance en informatique avant de lancer ta propre monnaie. \n Le processus te prend juste 5 minutes et ne te coûtera jamais plus que 1 Waves de frais de transaction. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B73 

def b73(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Incroyable ! ']]
    update.message.reply_text( "Non je rigole. \n Clique sur cette adresse www.waves.exchange et vérifie par toi-même. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B74

def b74(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Troooop cool ! ']]
    update.message.reply_text( "Notre mission à Waves est de rendre la blockchain tellement accessible que même un nouveau-né y trouvera son plaisir. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B75

def b75(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Incroyable ! ']]
    update.message.reply_text( "Autre aspect non négligeable est bien entendu les frais de transaction presqu’insignifiants pour une telle rapidité. \n 5 secondes chrono pour que ta transaction soit validée en temps normal, 60 secondes si le réseau est congestionné. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B76 

def b76(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Génial. !!! ']]
    update.message.reply_text( "Hahaha et dire qu’un transfert bancaire te prends des heures ! \n Sans oublier chou que les frais de transactions sont très bas. 0.01 Waves tu peux t'amuser à calculer ce que ça vaut actuellement. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return B77

def b77(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [["D'accord"]]
    update.message.reply_text( "Ouf ! Ainsi nous arrivons au terme du premier module du cours sur l’introduction en blockchain. \n J’espère que tu as apprécié l’aventure. \n Avant d’entamer le deuxième module dédié à l’exploration en profondeur de la blockchain Waves dis-moi comment tu as trouvé le cours et aussi comment je pourrai l’améliorer en m’envoyant tes impressions, avis et commentaires sur @Fideledossou. ",
reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return ConversationHandler.END




def main() -> None:
    
    # Create the Updater and pass it your bot's token.
    updater = Updater("TOKEN")
    dispatcher = updater.dispatcher
    
    def stop_and_restart():
        updater.stop()
        os.execl(sys.executable, sys.executable, *sys.argv)
            
    def restart(update, context):
        update.message.reply_text('Un instant, je redémarre mon moteur...')
        Thread(target=stop_and_restart).start()
    
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start),
                                CommandHandler('restart', restart) 
        ],
        

        states={
            B1:[MessageHandler(Filters.text, b1)], 
            B2:[MessageHandler(Filters.text, b2)], 
            B3:[MessageHandler(Filters.text, b3)], 
            B4:[MessageHandler(Filters.text, b4)], 
            B5:[MessageHandler(Filters.text, b5)], 
            B6:[MessageHandler(Filters.text, b6)], 
            B7:[MessageHandler(Filters.text, b7)], 
            B8:[MessageHandler(Filters.text, b8)], 
            B9:[MessageHandler(Filters.text, b9)], 
            B10:[MessageHandler(Filters.text, b10)], 
            B11:[MessageHandler(Filters.text, b11)], 
            B12:[MessageHandler(Filters.text, b12)], 
            B13:[MessageHandler(Filters.text, b13)], 
            B14:[MessageHandler(Filters.text, b14)], 
            B15:[MessageHandler(Filters.text, b15)], 
            B16:[MessageHandler(Filters.text, b16)], 
            B17:[MessageHandler(Filters.text, b17)], 
            B18:[MessageHandler(Filters.text, b18)], 
            B19:[MessageHandler(Filters.text, b19)], 
            B20:[MessageHandler(Filters.text, b20)], 
            B21:[MessageHandler(Filters.text, b21)], 
            B22:[MessageHandler(Filters.text, b22)], 
            B23:[MessageHandler(Filters.text, b23)], 
            B24:[MessageHandler(Filters.text, b24)], 
            B25:[MessageHandler(Filters.text, b25)], 
            B26:[MessageHandler(Filters.text, b26)], 
            B27:[MessageHandler(Filters.text, b27)], 
            B28:[MessageHandler(Filters.text, b28)], 
            B29:[MessageHandler(Filters.text, b29)], 
            B30:[MessageHandler(Filters.text, b30)], 
            B31:[MessageHandler(Filters.text, b31)], 
            B32:[MessageHandler(Filters.text, b32)], 
            B33:[MessageHandler(Filters.text, b33)], 
            B34:[MessageHandler(Filters.text, b34)], 
            B35:[MessageHandler(Filters.text, b35)], 
            B36:[MessageHandler(Filters.text, b36)], 
            B37:[MessageHandler(Filters.text, b37)], 
            B38:[MessageHandler(Filters.text, b38)], 
            B39:[MessageHandler(Filters.text, b39)], 
            B40:[MessageHandler(Filters.text, b40)], 
            B41:[MessageHandler(Filters.text, b41)], 
            B42:[MessageHandler(Filters.text, b42)], 
            B43:[MessageHandler(Filters.text, b43)], 
            B44:[MessageHandler(Filters.text, b44)], 
            B45:[MessageHandler(Filters.text, b45)], 
            B46:[MessageHandler(Filters.text, b46)], 
            B47:[MessageHandler(Filters.text, b47)], 
            B48:[MessageHandler(Filters.text, b48)], 
            B49:[MessageHandler(Filters.text, b49)], 
            B50:[MessageHandler(Filters.text, b50)], 
            B51:[MessageHandler(Filters.text, b51)], 
            B52:[MessageHandler(Filters.text, b52)], 
            B53:[MessageHandler(Filters.text, b53)], 
            B54:[MessageHandler(Filters.text, b54)], 
            B55:[MessageHandler(Filters.text, b55)], 
            B56:[MessageHandler(Filters.text, b56)], 
            B57:[MessageHandler(Filters.text, b57)], 
            B58:[MessageHandler(Filters.text, b58)], 
            B59:[MessageHandler(Filters.text, b59)], 
            B60:[MessageHandler(Filters.text, b60)], 
            B61:[MessageHandler(Filters.text, b61)], 
            B62:[MessageHandler(Filters.text, b62)], 
            B63:[MessageHandler(Filters.text, b63)], 
            B64:[MessageHandler(Filters.text, b64)], 
            B65:[MessageHandler(Filters.text, b65)], 
            B66:[MessageHandler(Filters.text, b66)], 
            B67:[MessageHandler(Filters.text, b67)], 
            B68:[MessageHandler(Filters.text, b68)], 
            B69:[MessageHandler(Filters.text, b69)], 
            B70:[MessageHandler(Filters.text, b70)], 
            B71:[MessageHandler(Filters.text, b71)], 
            B72:[MessageHandler(Filters.text, b72)], 
            B73:[MessageHandler(Filters.text, b73)], 
            B74:[MessageHandler(Filters.text, b74)], 
            B75:[MessageHandler(Filters.text, b75)], 
            B76:[MessageHandler(Filters.text, b76)], 
            B77:[MessageHandler(Filters.text, b77)]
        

            },
        fallbacks=[ ],
    )

    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
