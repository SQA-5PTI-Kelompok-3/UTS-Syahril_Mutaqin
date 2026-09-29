# CFG `Owner.getPet(String name, boolean ignoreNew)`

## Node

| Node | Statement/decision |
|---|---|
| N1 | Entry |
| N2 | `name = name.toLowerCase()` |
| N3 | Evaluasi kondisi loop pada `getPetsInternal()` |
| N4 | Evaluasi `!ignoreNew || !pet.isNew()` |
| N5 | Ambil dan lowercase `compName` |
| N6 | Evaluasi `compName.equals(name)` |
| N7 | `return pet` |
| N8 | Loop selesai |
| N9 | `return null` |

## Edge

`N1→N2→N3`; dari N3, item tersedia menuju N4 dan iterator habis menuju
N8→N9. Dari N4, kondisi false kembali ke N3. Kondisi true menuju N5→N6.
Dari N6, match menuju N7 (exit), sedangkan tidak match kembali ke N3.

Ada tiga predicate utama: loop, filter, dan equality. Karena itu
`V(G)=3+1=4`.

## Basis path

- **P1**: koleksi kosong → normalisasi nama → loop habis → `null`.
- **P2**: pet ditemukan tetapi filter false → pet dilewati → loop habis → `null`.
- **P3**: filter true tetapi nama tidak sama → lanjut iterasi → `null`.
- **P4**: filter true dan nama sama → early return pet.

Short-circuit filter harus dipasangkan dengan test `ignoreNew=false` dan
`ignoreNew=true`; CFG ringkas tetap merepresentasikan hasil boolean filter.
