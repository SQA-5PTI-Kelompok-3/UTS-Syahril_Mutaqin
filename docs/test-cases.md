# Test Case White-Box

Semua test menargetkan `Owner.getPet(String name, boolean ignoreNew)` pada
commit `4cd8e1b0cd42578e882247d8801f6be5d402f118`.

| ID | Fixture dan input | Path | Expected |
|---|---|---|---|
| TC-01 | Set pet kosong, `name="Max"`, `ignoreNew=false` | P1 | `null` |
| TC-02 | Pet baru bernama `Max`, `ignoreNew=true` | P2 | `null`, pet baru dilewati |
| TC-03 | Pet lama bernama `Rex`, cari `Max`, `ignoreNew=false` | P3 | `null` |
| TC-04 | Pet lama bernama `Max`, `ignoreNew=false` | P4 | object pet tersebut |
| TC-05 | Pet baru bernama `Max`, `ignoreNew=false` | P4 | object pet baru |
| TC-06 | Pet baru `Max` dan pet lama `Max`, `ignoreNew=true` | P2 lalu P4 | pet lama |
| TC-07 | Pet bernama `mAx`, cari `MAX`, `ignoreNew=false` | P4 | object pet; case-insensitive |
| TC-08 | Dua pet lama bernama `Max`, `ignoreNew=false` | P4 | pet pertama yang diiterasi |
| TC-09 | `name=null` | precondition invalid | `NullPointerException` aktual |

TC-09 bukan expected business success; test ini mendokumentasikan bahwa source
tidak memiliki null guard. Karena `getPetsInternal()` berbasis `HashSet`, urutan
“pet pertama” pada TC-08 tidak boleh diasumsikan stabil kecuali fixture memakai
koleksi/konfigurasi yang mengendalikan iterasi.

## Coverage rationale

TC-01 sampai TC-04 menutup empat basis path. TC-05 dan TC-06 memisahkan kedua
hasil short-circuit pada `!ignoreNew || !pet.isNew()`. TC-07 memverifikasi
normalisasi nama, sedangkan TC-09 menjaga agar dokumentasi tidak mengklaim
perilaku null yang tidak ada di implementasi.
