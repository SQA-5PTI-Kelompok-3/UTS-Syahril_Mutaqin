# Test Case White-Box

Semua test berikut menargetkan `Owner.getPet(Integer)` pada source aktual.
Fixture dapat dibuat dengan `Owner owner = new Owner()` dan `Pet pet = new
Pet()`, kemudian mengatur ID melalui `setId` dan menambahkan pet melalui
`owner.addPet(pet)`.

| ID | Kondisi/fixture | Path | Expected |
|---|---|---|---|
| TC-01 | `owner.getPets()` kosong, `id=1` | P1 | `null` |
| TC-02 | Satu pet baru (`id=1` menurut fixture), cari `1` | P2 | `null`, karena pet baru dilewati |
| TC-03 | Pet lama `id=2`, cari `1` | P3 | `null` |
| TC-04 | Pet lama `id=1`, cari `1` | P4 | object pet yang sama |
| TC-05 | Pet lama `id=null`, cari `null` | P4 (match) | object pet yang sama; `Objects.equals` aman |
| TC-06 | Pet lama `id=1`, cari `null` | P3 | `null` |
| TC-07 | Pet baru `id=1`, diikuti pet lama `id=1`, cari `1` | P2 lalu P4 | pet lama, bukan pet baru |
| TC-08 | Pet lama `id=1`, lalu pet lama `id=1`, cari `1` | P4 | pet lama pertama (early return) |

## Trace ringkas

Untuk TC-07, iterasi pertama mengambil cabang `pet.isNew() == true` dan kembali
ke kondisi loop. Iterasi kedua mengambil cabang pet lama, ID cocok, lalu
mengembalikan objek pada iterasi kedua. Ini menguji interaksi loop dan cabang
skip, bukan hanya masing-masing kondisi secara terisolasi.

## Relasi dengan test upstream

Repository upstream memiliki `OwnerTests`, tetapi daftar test tersebut tidak
boleh dianggap otomatis memetakan semua basis path laporan ini. TC-01 sampai
TC-08 adalah rancangan white-box eksplisit yang diturunkan langsung dari
CFG; implementasi test JUnit dapat ditambahkan tanpa mengubah source aplikasi.
