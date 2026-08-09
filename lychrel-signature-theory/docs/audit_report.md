# Referee-style audit of the preprint drafts

**Documents reviewed**

- `VF_EnglishPreprint_NLM_Lychrel_Signatures_Canonical_Nodes_citation_name.docx`
- `VF_Francais_Preprint_NLM_FR_Lychrel_Signatures_Noeuds_Canoniques_citation_name.docx`

**Verdict in one line.** The algebraic core (\(\Sigma_m \mapsto K_\Sigma\)) is sound and the 3D/4D experimental claims are publishable as *finite* classifications once definitions of purity, protocol, and \(R_0\) are tightened; the 5D “≈86 components” and the recursive grammar must remain explicitly exploratory/conjectural.

EN and FR drafts are essentially parallel. Issues below apply to both unless noted.

---

## 1. Result status reclassification

| Label in draft | Statement | Recommended status | Reason |
|----------------|-----------|--------------------|--------|
| Def 2.1–2.4 | \(T\), candidates, \(\Sigma_m\), \(K_\Sigma\) | **Definition** (keep) | OK; tighten 2.2/2.4 wording |
| Table 2.5 | \(O,G,F,B,C,M\) | Mixed: some **Definition**, some **informal** | \(G,B,C,M\) are not sharp |
| Prop 3.1 | \(T(N)\) depends only on \(\Sigma_m(N)\) | **Proposition** / **Lemma** (keep or upgrade proof clarity) | Correct; this is the main theorem-quality fact |
| Formulas 3.2 | closed forms | **Corollary** of 3.1 | Algebraic specializations |
| Thm 4.1 | 3D candidates = three signatures | **Experimental Theorem** or **Proposition (finite protocol)** | Exhaustive computation at \(B=500\), not an infinite theorem |
| Prop 4.2 | 4D: 12 pure signatures, 5 families | **Experimental Proposition** | Needs definition of “pure” and of family joining |
| Obs 4.3 | 5D compression / ~86 | **Observation** (keep); mark 86 as **exploratory** | Window-dependent |
| Conj 5.1 | recursive grammar | **Conjecture** (keep) | Not operationally defined |

---

## 2. Critical issues

### C1. Protocol for experimental candidates is ambiguous (Definition 2.2)

Draft: “generated iterates under \(T\) do not reach a palindrome before the bound \(B\).”

Unspecified:

1. Is the seed \(n\) itself tested?
2. Does the count of iterations include the first application of \(T\)?
3. How are already-palindromic seeds treated?

**Why critical.** The four-digit table includes family seed **9999**, which is a palindrome. Under a naïve reading of Def 2.2, 9999 is immediately rejected. The tables are coherent only under a **test-after-first-step** convention.

**Rewrite (recommended).**

> **Definition 2.2 (experimental candidate, bound \(B\)).** Fix \(B\in\mathbb{N}\). Set \(x_0=n\). For \(k=1,\ldots,B\) compute \(x_k=T(x_{k-1})\). The integer \(n\) is an *experimental candidate at bound \(B\)* if none of \(x_1,\ldots,x_B\) is a palindrome. (Equivalently: the seed itself is never tested.) In this manuscript \(B=500\) unless stated otherwise.

### C2. “Pure signature” is used but never defined

Proposition 4.2 asserts “12 pure signatures.” The table columns `Total` and `Candidates` being equal suggest the intended meaning, but it is never stated.

**Rewrite.**

> A signature \(\Sigma\) of width \(m\) is *pure at bound \(B\)* if every \(m\)-digit integer with \(\Sigma_m(N)=\Sigma\) is an experimental candidate at bound \(B\).

### C3. \(R_0\) (and carry vectors) appear in every classification table but are undefined in §2

The abstract and pipeline `Sigma -> K -> R_0 -> family` advertise carry structure; §2.5 never defines \(R_0\), \(R_k\), or the bit-string encoding (`010`, `111`, `1001`, …).

**Required addition (§2.6).** Define digit-wise carries of one step \(n+\mathrm{rev}(n)\), order, and the string encoding used in tables. Empirically, the published 5D strings match **LSD-first** encoding (units carry-out first): e.g. signature \((9,10,8)\) appears as `01111`, not the MSD-first reverse `11110`. State that table values are first-step profiles of a representative (and note independence or dependence on representative if any — for fixed signature, digit pairs vary, so **\(R_0\) need not be signature-invariant**).

**Mathematical warning.** Unlike \(K_\Sigma\), the carry profile is **not** a function of \(\Sigma\) alone: different pairs \((d_i,d_{m+1-i})\) with the same sum can produce different carries. The 3D table happens to show one \(R_0\) per signature because those signatures are sparse / representatives share a profile — this must be checked and stated. Presenting \(R_0\) as a column attached to a signature without comment is a credibility risk.

### C4. Seed / family / basin / component / meta-family are too soft for numbered structure

- \(G\): “minimal or fundamental representative in the studied data” — not a mathematical definition.
- \(B(G)\): mixes numbers, signatures, and nodes in one “set.”
- \(C_i\): “merge within the computational window” — window and merge predicate undefined.
- \(M_j\): descriptive only.

For a preprint, keep them as **informal computational vocabulary** in §2.5, or give sharp finite-window definitions (as in the accompanying code). Do not let Conjecture 5.1 depend on undefined \(M_j\).

### C5. Overclaim risk in the conclusion

> “search for invariants linking candidate structure to true Lychrel existence”

Acceptable as future work, but the sentence can be read as suggesting the present structure already points to a proof route. Safer:

> “A proof of true Lychrel existence would still require an invariant forbidding all future palindromes; the present finite classification does not provide such an invariant.”

The limitations table already says this; the conclusion should not undercut it.

### C6. Five-digit “approximately 86” treated on equal footing with 13 and 236

Contributions item (5) writes `5842 → 248 → 86` without “approximately,” while the abstract and Observation 4.3 hedge. Component count depends on the merge algorithm and follow window. **Demote** the third arrow to “exploratory component count (protocol-dependent).”

---

## 3. Moderate issues

### M1. Theorem 4.1 statement omits the bound in the sentence

It relies on Def 2.2, but the theorem sentence should say “at bound \(B=500\)” explicitly. Label as **Experimental Theorem** or **Proposition**.

### M2. Canonical node vs node signature confusion in 4D table

Columns: `Node`, `Node signature`. When the node has 5 digits, its signature is \(\Sigma_5\). This is fine but never explained. Add one sentence: “Node signatures are computed at the digit length of \(K_\Sigma\), which may exceed \(m\).”

### M3. Definition 2.4 slightly overstates uniqueness language

“the common value \(K_\Sigma=T(N)\) for all numbers \(N\) sharing the signature” presupposes Prop 3.1. Either forward-reference 3.1 or define \(K_\Sigma\) as \(T(N)\) for a representative and prove independence afterward.

### M4. Basin vs family

\(F(G)\) is defined via orbit intersection; \(B(G)\) is then almost the same object plus signatures/nodes. Either define basin strictly as the set of \(m\)-digit seeds whose orbits enter \(O(G)\), or drop basin from the core vocabulary.

### M5. Section numbering vs preferred structure

Introduction subsections are unnumbered (`Background`, `Previous Work`, `Contributions`). Prefer `1.1–1.3`. Missing explicit `2.2` cross-link to protocol in every experimental statement is a presentation issue.

### M6. Contributions (5) vs abstract inconsistency

Abstract: “approximately 86.” Contributions: “86.” Harmonize.

### M7. 3D comparison row “2 main families” vs 3 signatures

Never stated which signatures merge into which families (presumably 196 vs 879). Add one sentence or a tiny table.

### M8. FR draft punctuation

Missing period at the end of the OEIS paragraph in Travaux antérieurs.

### M9. Citation placement

Generally compliant (intro / previous work / limitations). Good. Do not add citations inside §3–§5.

### M10. NLM reference style

Mostly fine. Minor: OEIS entry could include “OEIS Foundation Inc.” as author (already done). Dates use `[cited 2026 Aug 7]` — keep consistent. p196.org author attribution “VanLandingham W.” should be verified against the site credit line.

---

## 4. Minor issues

- Notation mixes `Sigma_m`, `Σm`, `K_Sigma`, `K_3(x,b)` — pick one typographic standard.
- Pipeline line in Introduction is useful but unexplained; expand or move after definitions.
- “Strongly compressed” / “controlled branching” in the conclusion — mild rhetoric; prefer “substantial compression under the protocol.”
- Author line formatting glitch in extracted text (`KOFFIPreprint`) — check Word styles / missing line break.
- Conjecture 5.1 uses an undefined operator \(F(\ldots)\); say “there exist finitely described rewriting rules” or give a schematic example from 3D→4D.

---

## 5. Missing definitions (checklist)

| Item | Present? | Action |
|------|----------|--------|
| \(T\), rev | Yes | — |
| Experimental candidate | Partial | Fix protocol |
| \(\Sigma_m\) | Yes | Specify digit indexing and leading-digit constraint |
| \(K_\Sigma\) | Yes | Order vs Prop 3.1 |
| \(R_0\) | **No** | Add |
| Pure signature | **No** | Add |
| Family join predicate | **No** | Add finite-window definition |
| \(S_m\) | Implicit only | Define before Conjecture 5.1 |
| Meta-family | Vague | Mark informal or define |

---

## 6. Notation inconsistencies

1. \(K_\Sigma\) vs \(K_3(x,b)\): acceptable if stated that \(K_m\) is the closed form evaluating \(K_\Sigma\).
2. User-facing ambiguity “\(K_k(n)\)” does **not** appear in the drafts; do not introduce it without definition.
3. Carry strings vs integer carry vectors: tables use strings; prose never says so.
4. “Node signature” for a 5-digit image of a 4-digit seed uses \(\Sigma_5\) without saying so.

---

## 7. Overclaims

| Phrase / implication | Risk | Safer form |
|----------------------|------|------------|
| “Theorem 4.1” without bound in-sentence | Readers may think infinite | State \(B=500\) in the theorem |
| Contributions `→ 86` | False precision | `→ ~86` exploratory components |
| 9999 as Lychrel-related family | Looks like a contradiction | Explain post-\(T\) protocol |
| Conjecture grammar “generated by” | Sounds structural-complete | “appear compatible with a recursive description” |
| Conclusion linking structure to true existence | Proof-adjacent | Keep only in limitations |

Scope sentence and limitations table are appropriately cautious — preserve them.

---

## 8. Algebraic checks performed

- \(K_3(x,b)=101x+20b\): identity for 3-digit \(N\).
- \(K_4(x,y)=1001x+110y\): identity for 4-digit \(N\); examples \((6,13)\mapsto 7436\), \((8,13)\mapsto 9438\), \((18,18)\mapsto 19998\) hold.
- \(K_5(x,y,z)=10001x+1010y+200z\): identity; example \((9,8,7)\mapsto 99489\) holds.
- Prop 3.1 proof idea is correct (mirrored coefficients).
- 4D family counts \(102+70+30+33+1=236\): arithmetic OK.

---

## 9. Suggested replacement text (weak sections)

### Definition 2.2

See Critical issue C1.

### New Definition (purity)

See Critical issue C2.

### New Definition / Remark (\(R_0\))

> **Definition 2.6.** Write the base-10 digits of an \(m\)-digit \(n\) as \(d_1,\ldots,d_m\). Adding \(n\) and \(\mathrm{rev}(n)\) from the right produces carry-outs \(c_m,\ldots,c_1\in\{0,1\}\) (and possibly a leading overflow). The *first-step carry profile* is the string \(R_0(n)=c_1\cdots c_m\) (most-significant position first). **Remark.** \(R_0(n)\) is not in general a function of \(\Sigma_m(n)\) alone.

### Theorem 4.1

> **Experimental Theorem 4.1.** Under Definition 2.2 with \(B=500\), the three-digit experimental candidates are exactly the 13 integers whose signatures lie in \(S_3=\{(7,9),(15,8),(17,7)\}\). Moreover each of these signatures is pure.

### Contributions item (5)

> (5) Five-digit compression under the same protocol: \(5842\) candidates → \(248\) signatures → an exploratory component count of order \(10^2\) (reported as approximately 86 under one merge window).

### Conclusion (last sentence)

> The next step is to formalize a recursive description of candidate signatures across digit lengths. Separately, any link to true Lychrel existence would require an independent invariant preventing all future palindromes; no such invariant is claimed here.

---

## 10. Corrected manuscript outline

1. Abstract  
2. Introduction — 1.1 Background; 1.2 Previous Work; 1.3 Contributions  
3. Preliminaries — \(T\); experimental candidates (**explicit protocol**); \(\Sigma_m\); \(K_\Sigma\); **\(R_0\)**; orbits/seeds/families (**finite-window**); purity  
4. Algebraic structure — Prop 3.1; corollaries \(K_3,K_4,K_5\)  
5. Experimental classification — 3D experimental theorem; 4D compression; 5D exploratory  
6. Recursive signature grammar — Conjecture only  
7. Limitations and reproducibility — bound, no existence proof, GitHub, 5D caveat, need for invariant  
8. Conclusion  
9. References (NLM; cite only in 1.x and 7)  
10. Appendices — reproducibility package; full 4D/5D tables  

---

## 11. Previous Work / Contributions / Limitations checklist

| Requirement | Status |
|-------------|--------|
| reverse-and-add / 196-algorithm / suspected Lychrel / OEIS A023108 / p196 / MathWorld | **Met** |
| Contrast: trajectories vs signatures+nodes | **Met** |
| Contributions (1)–(6) present | **Met**, fix (5) hedging |
| Limitations: no existence proof; finite protocol; bound; 5D exploratory; nD conjectural; need repo; need invariant | **Mostly met**; make bound and repo mandatory prose, not only table |

---

## 12. Readiness scores (0–100)

| Axis | Score | Comment |
|------|------:|---------|
| Mathematical clarity | **72** | Core Prop 3.1 clear; protocol/purity/\(R_0\)/families soft |
| Publication readiness | **68** | Publishable as experimental preprint after C1–C4 fixes |
| Reproducibility (manuscript alone) | **45** | Needs public code + explicit protocol; addressed by companion repo |
| Originality | **80** | Signature→node framing is a genuine organizational contribution |
| Risk of overclaiming | **58** | Scope sentence helps; 9999 + “86” + Thm label elevate risk |

**Composite editorial recommendation:** major revision of definitions and hedging; algebraic section can stay; attach reproducible code with \(B=500\) before circulation.
