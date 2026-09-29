# Analisis White-Box

## Baseline yang diverifikasi

Repository kosong pada awal pengerjaan, sehingga source tidak diasumsikan
tersedia di `HEAD`. Source diambil dengan clone shallow:

```text
https://github.com/spring-projects/spring-petclinic.git
ref: main (checkout shallow pada 2026-09-29)
```

Versi build pada source yang diverifikasi adalah Spring Boot `4.1.0` dan Java
`17` dari `pom.xml`. Repository `spring-petclinic-rest` juga memiliki model
`Owner`, tetapi method dan struktur yang menjadi target tugas tidak boleh
dianggap sama tanpa verifikasi. Target yang dipakai di laporan ini adalah
`spring-petclinic` MVC karena `Owner.getPet(Integer)` benar-benar ditemukan
pada file:

```text
src/main/java/org/springframework/samples/petclinic/owner/Owner.java
```

## Unit yang dianalisis

```java
public Pet getPet(Integer id) {
    for (Pet pet : getPets()) {
        if (!pet.isNew()) {
            Integer compId = pet.getId();
            if (Objects.equals(compId, id)) {
                return pet;
            }
        }
    }
    return null;
}
```

Method melakukan pencarian linear. Pet baru sengaja dilewati, kemudian ID
dibandingkan dengan `Objects.equals`, sehingga perbandingan aman ketika salah
satu nilai `null`. Method berhenti lebih awal saat menemukan kecocokan dan
mengembalikan `null` setelah seluruh koleksi diperiksa.

## Kompleksitas siklomatik

Dengan CFG berbasis short-circuit dan loop:

- keputusan loop `for`: 1
- keputusan `!pet.isNew()`: 1
- keputusan `Objects.equals(compId, id)`: 1
- sehingga `V(G) = 1 + 3 = 4`

Empat independent path diperlukan untuk basis path coverage. Kompleksitas ini
berlaku pada method aktual, bukan pada CFG generik yang mengasumsikan validasi
atau cabang lain yang tidak ada di source.

## Temuan implementasi

1. `null` pada parameter `id` tidak otomatis menghasilkan exception; pet dengan
   ID `null` tetap dapat cocok jika pet tersebut bukan pet baru.
2. Pet baru selalu dilewati, walaupun ID-nya kebetulan sama dengan parameter.
3. Hasil pertama yang cocok dikembalikan; duplikasi ID pada koleksi tidak
   diekspos oleh method.
4. Koleksi kosong dan tidak adanya kecocokan memiliki output yang sama, yaitu
   `null`.

Rincian node CFG dan test case ada di [`cfg.md`](cfg.md) dan
[`test-cases.md`](test-cases.md).
