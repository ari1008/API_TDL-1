from scrapper.Selectscrapper import Cselect
from scrapper.Findscrapper import Cfind, BuildUrl, parse, request

def test_select_aidepersonneshandicapees():
   url = BuildUrl("aide-personnes-handicapees", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_languedessignes():
   url = BuildUrl("langue-des-signes", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_transporthandicape():
   url = BuildUrl("transport-handicape", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_aideauxpersonnesagees():
   url = BuildUrl("aide-aux-personnes-agees", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_cuisinepourpersonnesagees():
   url = BuildUrl("cuisine-pour-personnes-agees", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_familleaccueil():
   url = BuildUrl("famille-accueil", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_auxiliairedevie():
   url = BuildUrl("auxiliaire-de-vie", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_livraisonderepas():
   url = BuildUrl("livraison-de-repas", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_amenagementdomicile():
   url = BuildUrl("amenagement-domicile", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_maisonretraite():
   url = BuildUrl("maison-retraite", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_residenceservicesseniors():
   url = BuildUrl("residence-services-seniors", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_teleassistance():
   url = BuildUrl("teleassistance", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_coiffuredomicile():
   url = BuildUrl("coiffure-domicile", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_estheticienne():
   url = BuildUrl("estheticienne", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_massagedomicile():
   url = BuildUrl("massage-domicile", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_toilettageanimaux():
   url = BuildUrl("toilettage-animaux", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_maquillage():
   url = BuildUrl("maquillage", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_epilation():
   url = BuildUrl("epilation", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_extensiondecheveux():
   url = BuildUrl("extension-de-cheveux", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_lissagebresilien():
   url = BuildUrl("lissage-bresilien", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_prothesisteongulaire():
   url = BuildUrl("prothesiste-ongulaire", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_coursallemand():
   url = BuildUrl("cours-allemand", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_coursanglais():
   url = BuildUrl("cours-anglais", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_coursarabe():
   url = BuildUrl("cours-arabe", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_courschinois():
   url = BuildUrl("cours-chinois", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_coursespagnol():
   url = BuildUrl("cours-espagnol", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_coursfrancais():
   url = BuildUrl("cours-francais", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_coursitalien():
   url = BuildUrl("cours-italien", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_coursjaponais():
   url = BuildUrl("cours-japonais", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_coursportugais():
   url = BuildUrl("cours-portugais", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_coursrusse():
   url = BuildUrl("cours-russe", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_autrescourslangue():
   url = BuildUrl("autres-cours-langue", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_traduction():
   url = BuildUrl("traduction", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_soutienscolaire():
   url = BuildUrl("soutien-scolaire", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_aideauxdevoirs():
   url = BuildUrl("aide-aux-devoirs", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_coursbiologie():
   url = BuildUrl("cours-biologie", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_conseilorientation():
   url = BuildUrl("conseil-orientation", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_coursdessin():
   url = BuildUrl("cours-dessin", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_courseconomie():
   url = BuildUrl("cours-economie", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_coursmaths():
   url = BuildUrl("cours-maths", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_coursphysiquechimie():
   url = BuildUrl("cours-physique-chimie", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_autrescoursparticuliers():
   url = BuildUrl("autres-cours-particuliers", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_coursfrancaislitterature():
   url = BuildUrl("cours-francais-litterature", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_animationenfant():
   url = BuildUrl("animation-enfant", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_assistantematernelle():
   url = BuildUrl("assistante-maternelle", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_babysitting():
   url = BuildUrl("baby-sitting", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_gardeenfants():
   url = BuildUrl("garde-enfants", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_sortieclasse():
   url = BuildUrl("sortie-classe", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_nounou():
   url = BuildUrl("nounou", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_educateurjeunesenfants():
   url = BuildUrl("educateur-jeunes-enfants", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_auxiliairepuericulture():
   url = BuildUrl("auxiliaire-puericulture", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_auxiliairepetiteenfance():
   url = BuildUrl("auxiliaire-petite-enfance", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_informatique():
   url = BuildUrl("informatique", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_formationinformatique():
   url = BuildUrl("formation-informatique", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_depannageinformatique():
   url = BuildUrl("depannage-informatique", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_montagephotovideo():
   url = BuildUrl("montage-photo-video", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_creationsite():
   url = BuildUrl("creation-site", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_photographe():
   url = BuildUrl("photographe", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_coursbatterie():
   url = BuildUrl("cours-batterie", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_courschant():
   url = BuildUrl("cours-chant", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_coursguitare():
   url = BuildUrl("cours-guitare", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_courspiano():
   url = BuildUrl("cours-piano", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_courssolfege():
   url = BuildUrl("cours-solfege", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_coursviolon():
   url = BuildUrl("cours-violon", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_dj():
   url = BuildUrl("dj", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_coursflute():
   url = BuildUrl("cours-flute", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_autrescoursmusique():
   url = BuildUrl("autres-cours-musique", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_coach():
   url = BuildUrl("coach", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_coursrock():
   url = BuildUrl("cours-rock", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_courstango():
   url = BuildUrl("cours-tango", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_courstennis():
   url = BuildUrl("cours-tennis", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_coursyoga():
   url = BuildUrl("cours-yoga", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_autressports():
   url = BuildUrl("autres-sports", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_dansesalon():
   url = BuildUrl("danse-salon", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_autresdanses():
   url = BuildUrl("autres-danses", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_menagedebureaux():
   url = BuildUrl("menage-de-bureaux", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_nettoyageindustriel():
   url = BuildUrl("nettoyage-industriel", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_cuisinier():
   url = BuildUrl("cuisinier", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_bricolage():
   url = BuildUrl("bricolage", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_electricien():
   url = BuildUrl("electricien", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

def test_select_menuiserie():
   url = BuildUrl("menuiserie", 78300)
   res = request(url)
   r = parse(res)
   test = Cselect(r[0]["ID"][2:-1], ["*"])
   assert test == 0

