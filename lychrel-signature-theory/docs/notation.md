# Notation

| Symbol | Name | Formal meaning in this repository |
|--------|------|-------------------------------------|
| \(T(n)\) | reverse-and-add | \(n + \mathrm{rev}(n)\) |
| \(\mathrm{rev}(n)\) | digit reverse | integer reverse; leading zeros dropped |
| \(\Sigma_m(N)\) | symmetric signature | paired digit sums; center kept if \(m\) odd |
| \(K_\Sigma\) | canonical node | common value \(T(N)\) for all \(N\) with signature \(\Sigma\) |
| \(K_3(x,b)\) | 3D closed form | \(101x + 20b\) |
| \(K_4(x,y)\) | 4D closed form | \(1001x + 110y\) |
| \(K_5(x,y,z)\) | 5D closed form | \(10001x + 1010y + 200z\) |
| \(R_0\) | first-step carry profile | LSD-first carry-outs of one digit-wise addition \(n+\mathrm{rev}(n)\) (units first) |
| \(O(n)\) | orbit | \(\{n, T(n), T^2(n), \ldots\}\) |
| \(G\) | seed | designated family representative |
| \(F(G)\) | dynamic family | numbers whose orbits meet \(O(G)\) in a finite window |
| \(B(G)\) | basin | (preprint) numbers/signatures/nodes leading to \(F(G)\); not fully formalized in code |
| \(C_i\) | dynamic component | nodes whose orbits intersect within a follow window |
| \(M_j\) | meta-family | coarser grouping of components (conjectural / descriptive) |
| \(S_m\) | candidate signature set | set of \(\Sigma_m\) realized by \(m\)-digit experimental candidates |

## Ambiguity to avoid

Do not confuse:

- **experimental candidate** (finite bound) with **true Lychrel number** (infinite avoidance);
- **canonical node** \(K_\Sigma\) (a single integer \(T(N)\)) with a **carry regime** \(R_0\);
- **family seed** \(G\) with **canonical node** (a seed need not equal the node of its signature).
