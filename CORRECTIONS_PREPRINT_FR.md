# Corrections à apporter au préprint (version française)

**Document cible :** `VF_Francais_Preprint_NLM_FR_Lychrel_Signatures_Noeuds_Canoniques_citation_name.docx`  
**Usage :** copier-coller manuellement les blocs « Texte corrigé » dans Word, ou vérifier les remplacements automatiques s’ils ont été appliqués.

---

## Réponses rapides (avant les zones)

### Borne \(B = 500\) : trop petite ?

**Non, pas trop petite** pour une *théorie expérimentale de structure des candidats*, **à condition** de l’afficher partout comme protocole fini.

- \(B=500\) suffit pour soutenir : classification exacte 3D, compression 4D, comptages 5D, formalisme \(\Sigma_m\to K_\Sigma\).
- \(B=500\) est **insuffisant** pour parler de « vrais » nombres de Lychrel ou d’une théorie infinie.
- Recommandation : garder \(B=500\) comme protocole principal, et mentionner en limites qu’une étude de sensibilité (\(B=1000\), \(B=5000\)) est un travail futur utile, non bloquant pour le préprint.

### Que voulais-je dire par « partition exploratoire 5D » ?

Deux choses distinctes existent déjà / restent à faire :

| Déjà fait (dans le dépôt) | Encore exploratoire |
|---------------------------|---------------------|
| Énumération 5D : **5842** candidats, **248** signatures, nœuds, top signatures (`summary_5d.json`) | **Partition en composantes** (~86) : fusion d’orbites de nœuds dans une fenêtre de suivi — dépend de l’algorithme et de la fenêtre |

Les « ~86 composantes » du manuscrit ne sont **pas** le même objet que « 248 signatures ». Les 248 sont solides (énumération). Les ~86 sont une compression dynamique supplémentaire, à étiqueter clairement *exploratoire*.

---

## Légende des zones

- **CRITIQUE** — à corriger avant diffusion
- **IMPORTANT** — fortement recommandé
- **MINEUR** — polish éditorial

Pour chaque zone : *emplacement* → *texte actuel (résumé)* → *texte corrigé (à coller)*.

---

## ZONE 1 — CRITIQUE — Définition 2.2 (candidats expérimentaux)

**Emplacement :** §2.2

**Problème :** le protocole ne dit pas si la graine est testée ; nécessaire pour justifier 9999.

### Texte actuel (à remplacer)

> Définition 2.2. Pour une borne d’itération B fixée, un candidat expérimental est un entier dont les itérés générés sous T ne rejoignent pas de palindrome avant la borne B. Dans ce manuscrit, B=500 sauf mention contraire.

### Texte corrigé

> **Définition 2.2 (candidat expérimental, borne \(B\)).**  
> Soit \(B\in\mathbb{N}\). Posons \(x_0=n\). Pour \(k=1,\ldots,B\), on calcule \(x_k=T(x_{k-1})\). L’entier \(n\) est un *candidat expérimental à la borne \(B\)* si aucun des termes \(x_1,\ldots,x_B\) n’est un palindrome.  
> En particulier, la graine \(n\) elle-même n’est jamais testée : un palindrome tel que \(9999\) peut donc être retenu si son orbite après la première application de \(T\) évite les palindromes pendant \(B\) pas.  
> Dans ce manuscrit, \(B=500\) sauf mention contraire.

---

## ZONE 2 — CRITIQUE — Nouvelle définition : signature pure

**Emplacement :** insérer juste après la Définition 2.2 (nouveau § ou Définition 2.2 bis), et rappeler avant la Prop. 4.2.

### Texte à ajouter

> **Définition 2.2 bis (signature pure).**  
> Une signature \(\Sigma\) de largeur \(m\) est dite *pure à la borne \(B\)* si tout entier à \(m\) chiffres satisfaisant \(\Sigma_m(N)=\Sigma\) est un candidat expérimental à la borne \(B\).

---

## ZONE 3 — CRITIQUE — Nouvelle définition : profil de retenues \(R_0\)

**Emplacement :** nouveau §2.6 (après 2.5), car \(R_0\) apparaît dans toutes les tables sans définition.

### Texte à ajouter

> **Définition 2.6 (profil de retenues au premier pas).**  
> Soient \(d_1,\ldots,d_m\) les chiffres décimaux d’un entier à \(m\) chiffres \(n\) (chiffre de poids fort \(d_1\)). L’addition chiffre à chiffre de \(n\) et de \(\mathrm{rev}(n)\), de la droite vers la gauche, produit des retenues sortantes \(c_0,c_1,\ldots,c_{m-1}\) où \(c_0\) est la retenue issue de la position des unités, \(c_1\) celle des dizaines, etc.  
> On note \(R_0(n)\) la chaîne \(c_0c_1\ldots c_{m-1}\) (ordre **LSD-first** : unités d’abord).  
>  
> **Remarque.** Contrairement au nœud canonique \(K_\Sigma\), le profil \(R_0(n)\) **ne dépend pas uniquement** de \(\Sigma_m(n)\) en général : des réalisations distinctes d’une même signature peuvent produire des retenues différentes. Dans les tables, la colonne \(R_0\) est celle d’un représentant explicite (en pratique le plus petit candidat de la signature), sauf mention contraire.

---

## ZONE 4 — IMPORTANT — Table 2.5 (orbites, graines, familles, bassins)

**Emplacement :** §2.5

**Problème :** \(G\), \(B(G)\), \(C_i\), \(M_j\) trop flous.

### Texte corrigé (remplacer le tableau / les définitions souples)

> **Définition 2.5 (vocabulaire dynamique, fenêtre finie).**  
> Soit \(W\in\mathbb{N}\) une fenêtre de suivi (dans les expériences 4D, \(W=B=500\) sauf mention contraire).  
>  
> - \(O_W(n)=\{n,T(n),\ldots,T^W(n)\}\) : orbite tronquée.  
> - Une *graine* \(G\) est un représentant désigné d’une famille dans les données (ex. \(196\), \(879\), \(1997\), \(7059\), \(9999\)).  
> - La *famille dynamique* \(F_W(G)\) est l’ensemble des entiers \(n\) tels que \(O_W(n)\cap O_W(G)\neq\emptyset\).  
> - Le *bassin* \(B_W(G)\) est l’ensemble des seeds / signatures / nœuds dont l’orbite tronquée rencontre \(O_W(G)\) (vocabulaire descriptif dérivé de \(F_W(G)\)).  
> - Une *composante dynamique* est une classe de nœuds canoniques dont les orbites tronquées s’intersectent deux à deux (fermeture transitive) dans la fenêtre \(W\).  
> - Une *méta-famille* est un regroupement descriptif de composantes (projections, centres, retenues) ; ce n’est pas un objet axiomatisé dans ce préprint.

---

## ZONE 5 — IMPORTANT — Définition 2.4 (nœud canonique)

**Emplacement :** §2.4

**Problème :** suppose déjà la Prop. 3.1.

### Texte corrigé

> **Définition 2.4.** Soit \(\Sigma\) une signature de largeur \(m\). On appelle *nœud canonique* associé à \(\Sigma\) la valeur \(K_\Sigma:=T(N)\) pour un entier \(N\) à \(m\) chiffres de signature \(\Sigma\).  
> L’indépendance du représentant est établie par la Proposition 3.1 : \(T(N)\) ne dépend que de \(\Sigma_m(N)\).  
> En particulier, \(K_\Sigma\) peut avoir \(m\) ou \(m+1\) chiffres.

---

## ZONE 6 — IMPORTANT — Théorème 4.1 (3 chiffres)

**Emplacement :** §4.1

### Texte actuel (à remplacer)

> Théorème 4.1. Dans l’ensemble des entiers à trois chiffres, les candidats expérimentaux sont exactement les entiers dont la signature symétrique est (7,9), (15,8) ou (17,7).

### Texte corrigé

> **Théorème expérimental 4.1.** Sous la Définition 2.2 avec \(B=500\), les candidats expérimentaux à trois chiffres sont exactement les 13 entiers dont la signature appartient à  
> \(S_3=\{(7,9),(15,8),(17,7)\}\).  
> De plus, chacune de ces trois signatures est pure au sens de la Définition 2.2 bis.

*(Option plus prudente : remplacer « Théorème expérimental » par « Proposition 4.1 ».)*

---

## ZONE 7 — IMPORTANT — Proposition 4.2 (4 chiffres)

**Emplacement :** §4.2

### Texte corrigé

> **Proposition expérimentale 4.2.** Sous le même protocole fini (\(B=500\), Définition 2.2), les 236 candidats expérimentaux à quatre chiffres réalisent exactement 12 signatures, toutes pures. Chaque signature possède un nœud canonique unique \(K_\Sigma\), et ce nœud rejoint, dans la fenêtre \(W=500\), l’une des cinq familles dynamiques de graines  
> \(\{196,879,1997,7059,9999\}\).

**Phrase à ajouter sous le tableau des familles :**

> La graine \(9999\) est un palindrome ; elle est retenue uniquement grâce à la convention de la Définition 2.2 (test après le premier pas \(T\)).

**Phrase à ajouter sous la colonne « Signature du nœud » :**

> Lorsque \(K_\Sigma\) a cinq chiffres, la « signature du nœud » est calculée avec \(\Sigma_5\).

---

## ZONE 8 — CRITIQUE / IMPORTANT — Contributions (5) et cohérence « 86 »

**Emplacement :** Contributions, item (5) ; aussi Résumé / Observation 4.3

### Texte actuel problématique

> (5) Compression à cinq chiffres  
> 5842 → 248 → 86

### Texte corrigé

> (5) Compression à cinq chiffres sous le même protocole :  
> 5842 candidats → 248 signatures → un nombre *exploratoire* de composantes dynamiques de l’ordre de \(10^2\) (environ 86 pour une fenêtre de fusion donnée ; ce troisième cran dépend du protocole de fusion et n’a pas le même statut que 5842 et 248).

**Dans le Résumé**, conserver « environ 86 composantes observées » et ajouter :

> (comptage exploratoire, fenêtre-dépendant)

---

## ZONE 9 — IMPORTANT — Observation 4.3 (5 chiffres)

**Emplacement :** §4.3

### Texte corrigé (paragraphe d’ouverture)

> **Observation 4.3.** Le cas à cinq chiffres conserve le principe signature → nœud, mais présente une ramification plus importante. Sous le protocole \(B=500\), on obtient 5842 candidats et 248 signatures candidates.  
> Une compression supplémentaire en *composantes dynamiques* (fusion d’orbites de nœuds dans une fenêtre finie) est **exploratoire** : selon la fenêtre et le critère de fusion, on observe de l’ordre de \(10^2\) composantes (environ 86 dans l’expérience rapportée ici). Ce chiffre ne doit pas être lu au même niveau de solidité que 5842 et 248.

**Phrase « 5D = 4D + centre + bifurcation » :** la garder, mais la qualifier :

> Cette description est heuristique ; elle motive la Conjecture 5.1, elle ne la démontre pas.

---

## ZONE 10 — IMPORTANT — Conjecture 5.1

**Emplacement :** §5

### Texte corrigé

> **Conjecture 5.1.** Il existe une description récursive, encore à formaliser, permettant de produire l’ensemble \(S_{m+1}\) des signatures candidates à \(m+1\) chiffres à partir de \(S_m\), des régimes de retenues, des chiffres centraux (cas impair) et de règles de bifurcation.  
> On résume schématiquement cette idée par  
> \(S_{m+1}=F(S_m,\text{retenues},\text{centres},\text{bifurcations})\),  
> où \(F\) désigne un système de règles à spécifier, et non une fonction déjà construite.  
> Cette conjecture n’est pas démontrée ici ; elle résume la transition observée entre le cas 3D fermé, la compression 4D et la ramification 5D.

---

## ZONE 11 — IMPORTANT — Conclusion (dernière phrase)

**Emplacement :** §7

### Texte actuel risqué

> … et à rechercher des invariants reliant la structure des candidats à l’existence véritable de nombres de Lychrel.

### Texte corrigé

> La prochaine étape consiste à formaliser une description récursive des signatures candidates selon la longueur.  
> Séparément, toute preuve d’existence d’un vrai nombre de Lychrel en base 10 exigerait un invariant interdisant *tous* les palindromes futurs ; aucun tel invariant n’est établi dans ce travail, et la classification finie présentée ici n’en fournit pas.

---

## ZONE 12 — IMPORTANT — Limites (§6) : renforcer trois phrases

**Emplacement :** §6, avant ou dans le tableau

### Texte à ajouter (paragraphe)

> Tous les résultats numériques de ce manuscrit sont relatifs à la borne \(B=500\) et à la Définition 2.2. Modifier \(B\) peut modifier l’ensemble des candidats.  
> Le dépôt logiciel associé fournit le code d’énumération 3D/4D/5D, les formules de nœuds canoniques, les profils de retenues et les tables CSV nécessaires à la reproduction.  
> Le comptage « environ 86 » composantes en 5D est exploratoire et fenêtre-dépendant.

---

## ZONE 13 — MINEUR — Contributions (2) notation

### Texte corrigé

> (2) Introduction du formalisme des nœuds canoniques \(\Sigma_m \mapsto K_\Sigma\).

---

## ZONE 14 — MINEUR — Travaux antérieurs (ponctuation FR)

**Emplacement :** paragraphe OEIS

### Corriger

Ajouter le point final après A023108 :

> … sous l’itération répétée de l’opérateur reverse-and-add [1].

---

## ZONE 15 — MINEUR — Introduction / familles 3D

**Emplacement :** tableau comparatif 3D/4D/5D ou §4.1

### Texte à ajouter

> En trois chiffres, les trois signatures se regroupent en deux familles principales observées : la famille de \(196\) pour \((7,9)\), et la famille de \(879\) pour \((15,8)\) et \((17,7)\), sous la fenêtre \(W=500\).

---

## ZONE 16 — MINEUR — Ton de la conclusion

### Remplacer

- « fortement comprimé » → « substantiellement comprimé sous le protocole fini »
- « ramification contrôlée » → « ramification structurée mais encore exploratoire »

---

## ZONE 17 — MINEUR — Numérotation souhaitée

Transformer :

- Background → **1.1 Contexte**
- Travaux antérieurs → **1.2 Travaux antérieurs**
- Contributions → **1.3 Contributions**

(Introduction = section 1)

---

## Checklist finale avant soumission / arXiv

- [ ] Déf. 2.2 avec test après le premier \(T\)
- [ ] Déf. signature pure
- [ ] Déf. \(R_0\) (LSD-first) + remarque de non-invariance
- [ ] Vocabulaire dynamique à fenêtre \(W\)
- [ ] Thm/Prop 4.1 avec \(B=500\) explicite
- [ ] Prop 4.2 + note sur 9999
- [ ] Contributions (5) avec « ~86 exploratoire »
- [ ] Observation 4.3 hedgee
- [ ] Conjecture 5.1 sans \(F\) magique
- [ ] Conclusion sans surclaim d’existence
- [ ] Limites : borne, dépôt, 5D exploratoire
- [ ] Lien GitHub / dépôt `lychrel-signature-theory`

---

## Statut logique des résultats (à garder en tête)

| Résultat | Statut correct |
|----------|----------------|
| \(\Sigma_m\mapsto K_\Sigma\), formules 3/4/5 | Proposition / corollaires algébriques |
| 13 / 3 en 3D à \(B=500\) | Théorème ou proposition **expérimentale** |
| 236 / 12 / 5 en 4D à \(B=500\) | Proposition **expérimentale** |
| 5842 / 248 en 5D à \(B=500\) | Observation / résultat expérimental solide |
| ~86 composantes | Observation **exploratoire** |
| Grammaire récursive | **Conjecture** |
