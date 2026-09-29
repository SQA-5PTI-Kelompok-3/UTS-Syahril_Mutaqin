# Control Flow Graph `Owner.getPet(Integer)`

## Node dan edge

| Node | Statement/decision |
|---|---|
| N1 | Entry |
| N2 | Ambil iterator `getPets()` dan evaluasi kondisi `for` |
| N3 | Evaluasi `!pet.isNew()` |
| N4 | Ambil `compId = pet.getId()` |
| N5 | Evaluasi `Objects.equals(compId, id)` |
| N6 | `return pet` |
| N7 | Iterator habis |
| N8 | `return null` / exit |

Edge utama: `N1→N2`, `N2→N3` (ada item), `N2→N7` (kosong/habis),
`N3→N4` (pet lama), `N3→N2` (pet baru), `N4→N5`, `N5→N6` (match),
`N5→N2` (tidak match), `N6→N8`, `N7→N8`.

## Diagram

Diagram yang sama tersedia sebagai file Mermaid:
`diagrams/owner-get-pet-flow.mmd`.

```mermaid
flowchart TD
    N1([Entry]) --> N2{Masih ada pet?}
    N2 -- tidak --> N7[return null]
    N2 -- ya --> N3{pet.isNew()?}
    N3 -- ya --> N2
    N3 -- tidak --> N4[compId = pet.getId()]
    N4 --> N5{Objects.equals(compId, id)?}
    N5 -- ya --> N6[return pet]
    N5 -- tidak --> N2
    N6 --> N8([Exit])
    N7 --> N8
```

## Basis path

`V(G) = 4`, sehingga contoh basis path independen:

- **P1**: koleksi kosong → `N1-N2-N7-N8`.
- **P2**: ada pet baru lalu koleksi habis → `N1-N2-N3-N2-N7-N8`.
- **P3**: pet lama, ID tidak cocok, lalu habis → `N1-N2-N3-N4-N5-N2-N7-N8`.
- **P4**: pet lama dengan ID cocok → `N1-N2-N3-N4-N5-N6-N8`.

P4 juga membuktikan early return. P2 membuktikan cabang skip untuk pet baru,
yang sering hilang bila CFG hanya dibuat dari contoh abstrak.
