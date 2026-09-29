# UTS - Syahril Mutaqin

## UTS White-Box Testing — Spring PetClinic REST

## Identitas Mahasiswa

- **Nama:** Syahril Mutaqin
- **Mata kuliah:** Software Quality Assurance
- **Tugas:** Analisis White-Box Testing

## Tujuan Tugas

Repository ini berisi artefak analisis white-box terhadap satu method pada
project Spring PetClinic REST. Project Spring PetClinic REST **tidak disalin
ke repository tugas**; source hanya dijadikan referensi eksternal agar analisis
berdasarkan implementasi aktual.

## Target Source yang Dianalisis

| Item | Nilai |
|---|---|
| Repository source | [`spring-petclinic/spring-petclinic-rest`](https://github.com/spring-petclinic/spring-petclinic-rest) |
| Ref yang diverifikasi | `master` |
| Commit yang diverifikasi | `4cd8e1b0cd42578e882247d8801f6be5d402f118` |
| File | `src/main/java/org/springframework/samples/petclinic/model/Owner.java` |
| Package | `org.springframework.samples.petclinic.model` |
| Class | `Owner` |
| Method | `getPet(String name, boolean ignoreNew)` |

Source method diverifikasi langsung pada URL:

<https://github.com/spring-petclinic/spring-petclinic-rest/blob/master/src/main/java/org/springframework/samples/petclinic/model/Owner.java>

## Alasan Pemilihan Method

Method `Owner.getPet(String name, boolean ignoreNew)` dipilih karena memiliki
beberapa jalur kontrol yang relevan untuk white-box testing:

1. Normalisasi input nama dengan `toLowerCase()`.
2. Iterasi koleksi pet menggunakan `for`.
3. Filter pet baru/lama melalui `ignoreNew` dan `pet.isNew()`.
4. Perbandingan nama secara case-insensitive.
5. Early return ketika pet ditemukan dan return `null` ketika pencarian selesai.

Method ini cukup kecil untuk ditelusuri secara tepat, tetapi tetap memiliki
loop, keputusan majemuk, jalur skip, jalur sukses, dan jalur gagal. Analisis
juga mendokumentasikan perilaku aktual untuk input `null`, karena source tidak
memiliki null guard eksplisit.

## Artefak Analisis

- [`ANALISIS_WHITE_BOX.md`](ANALISIS_WHITE_BOX.md) — ringkasan analisis dan
  kompleksitas siklomatik.
- [`docs/analysis.md`](docs/analysis.md) — baseline source dan perilaku aktual.
- [`docs/cfg.md`](docs/cfg.md) — node, edge, dan basis path CFG.
- [`docs/test-cases.md`](docs/test-cases.md) — test case white-box dan alasan
  coverage.
- [`diagrams/owner-get-pet-flow.mmd`](diagrams/owner-get-pet-flow.mmd) —
  diagram control flow dalam format Mermaid.

Kompleksitas siklomatik statement-level yang dihitung untuk method target adalah
`V(G) = 4`.
