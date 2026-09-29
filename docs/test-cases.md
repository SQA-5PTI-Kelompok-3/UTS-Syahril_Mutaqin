# Path Testing dan Coverage

Semua test menargetkan `Owner.getPet(String name, boolean ignoreNew)` pada
commit `4cd8e1b0cd42578e882247d8801f6be5d402f118`.

## Path testing table

| ID | Fixture dan input | Path aktual | Iterasi | Expected |
|---|---|---|---:|---|
| TC-01 | Koleksi kosong, `name="Max"`, `ignoreNew=false` | P1: N3(F) | 0 | `null` |
| TC-02 | Pet baru `Max`, `ignoreNew=true` | P2: N3(T)-N4(F)-N3(F) | 1 | `null`; pet baru dilewati |
| TC-03 | Pet lama `Rex`, cari `Max`, `ignoreNew=false` | P3: N4(T)-N6(F)-N3(F) | 1 | `null`; non-match |
| TC-04 | Pet lama `Max`, `ignoreNew=false` | P4: N4(T)-N6(T)-N7 | 1 | object pet; match |
| TC-05 | Pet baru `Max`, `ignoreNew=false` | P4: N4(T)-N6(T)-N7 | 1 | object pet baru; A short-circuit true |
| TC-06 | Pet baru `Max` lalu pet lama `Max`, `ignoreNew=true` | P2 lalu P4 | 2 | pet lama; skip lalu match |
| TC-07 | Pet `mAx`, cari `MAX`, `ignoreNew=false` | P4 | 1 | object pet; lowercase cocok |
| TC-08 | Pet lama `Rex`, lalu pet lama `Max`, cari `Max`, `ignoreNew=false` | P3 lalu P4 | 2 | pet kedua; non-match lalu match |
| TC-09 | Dua pet lama `Max`, `ignoreNew=false` | P4 pada iterasi pertama | ≥1 | pet pertama yang diiterasi; early return |
| TC-10 | Pet lama `Max`, `ignoreNew=true` | N4: A false, B true, lalu P4 | 1 | object pet; operand kanan `||` dievaluasi |
| TC-11 | `name=null` | sebelum N3 | 0 | `NullPointerException` aktual; bukan jalur valid |

TC-01, TC-02, TC-03, TC-04, TC-06, dan TC-08 secara eksplisit mencakup
0 iterasi, skip pet baru, non-match, match, serta multi-iterasi. TC-10
diperlukan khusus untuk membuktikan operand kanan short-circuit.

## Branch coverage level predicate

Keputusan yang dihitung pada CFG statement-level adalah N3, N4, dan N6:

| Decision | True dieksekusi oleh | False dieksekusi oleh | Covered |
|---|---|---|---|
| N3: elemen loop tersedia? | TC-02, TC-03, TC-04, TC-06, TC-08, TC-10 | TC-01, TC-02, TC-03, TC-06, TC-08 | Ya |
| N4: filter lolos? | TC-03, TC-04, TC-05, TC-06 (pet lama), TC-08, TC-10 | TC-02, TC-06 (pet baru) | Ya |
| N6: nama cocok? | TC-04, TC-05, TC-06, TC-07, TC-08, TC-10 | TC-03, TC-08 | Ya |

Rumus branch coverage:

```text
branch coverage = branch yang dieksekusi / seluruh branch
                = 6 / 6
                = 100%
```

### Coverage operand short-circuit

Untuk N4, `A = !ignoreNew` dan `B = !pet.isNew()`:

| Operand | True | False | Catatan |
|---|---|---|---|
| A | TC-03, TC-04, TC-05, TC-07, TC-08 | TC-02, TC-06, TC-10 | A true men-short-circuit B |
| B | TC-10 | TC-02, TC-06 | B hanya dievaluasi saat A false |

Dengan suite TC-01–TC-11, outcome operand yang benar-benar dievaluasi adalah
`A=True/False` dan `B=True/False`, masing-masing `2/2 = 100%`. Ini dilaporkan
terpisah dari branch coverage N4.

## Statement coverage

Statement yang dihitung adalah node statement N2, N5, N7, N8, N9 serta
evaluasi keputusan N3, N4, dan N6 sebagai statement kontrol:

| Statement/node | Test yang mengeksekusi |
|---|---|
| N2 normalisasi nama | TC-01 sampai TC-10 |
| N3 kondisi loop | TC-01 sampai TC-10 |
| N4 filter | TC-02 sampai TC-10 |
| N5 ambil/lowercase nama pet | TC-03 sampai TC-10, untuk setiap pet yang lolos filter |
| N6 equality | TC-03 sampai TC-10 kecuali TC-02; pada TC-06 juga untuk pet lama |
| N7 `return pet` | TC-04, TC-05, TC-06, TC-07, TC-08, TC-09, TC-10 |
| N8 loop selesai | TC-01, TC-02, TC-03, TC-06, TC-08 |
| N9 `return null` | TC-01, TC-02, TC-03, TC-08 |

Semua node statement N2, N5, N7, N8, dan N9 memiliki setidaknya satu
eksekusi; N3, N4, dan N6 juga memiliki true dan false pada suite. Dengan
perhitungan node statement kontrol yang konsisten:

```text
statement coverage = statement yang dieksekusi / seluruh statement
                    = 8 / 8
                    = 100%
```

Angka ini adalah coverage yang diharapkan dari desain suite test case, bukan
hasil laporan tool instrumentasi runtime. TC-11 sengaja tidak menambah coverage
karena berhenti sebelum N3 akibat null dereference pada N2.

## Loop coverage

| Kategori | Test | Hasil |
|---|---|---|
| 0 iterasi | TC-01 | loop langsung N3(F) |
| 1 iterasi | TC-02, TC-03, TC-04, TC-05, TC-07, TC-10 | satu pet diproses/di-skip |
| >1 iterasi | TC-06, TC-08, TC-09 | iterasi berulang; dapat berhenti saat match |

Loop coverage kategori: `3/3 = 100%`.

## Ringkasan coverage gabungan

| Metrik | Numerator/denominator | Hasil |
|---|---:|---:|
| Branch level predicate | 6/6 | 100% |
| Operand short-circuit (`A`, `B`) | 4 outcome/4 outcome | 100% |
| Statement/control node | 8/8 | 100% |
| Loop 0, 1, >1 | 3/3 kategori | 100% |

Kesimpulan: berdasarkan suite desain TC-01 sampai TC-11 dan pemetaan path di
atas, 100% tercapai untuk metrik yang didefinisikan dalam dokumen ini. Ini
bukan klaim coverage seluruh repository atau bukti pengukuran JaCoCo; klaimnya
terbatas pada method target dan definisi CFG/statement yang dicantumkan.
