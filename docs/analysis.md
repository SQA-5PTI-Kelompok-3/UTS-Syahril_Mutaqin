# Analisis White-Box `Owner.getPet(String, boolean)`

## Source dan ref yang diverifikasi

Target tugas diverifikasi dari repository `spring-petclinic/spring-petclinic-rest`:

```text
URL: https://github.com/spring-petclinic/spring-petclinic-rest.git
ref: master
commit: 4cd8e1b0cd42578e882247d8801f6be5d402f118
file: src/main/java/org/springframework/samples/petclinic/model/Owner.java
```

Method yang benar-benar tersedia pada ref tersebut adalah:

```java
public Pet getPet(String name, boolean ignoreNew) {
    name = name.toLowerCase();
    for (Pet pet : getPetsInternal()) {
        if (!ignoreNew || !pet.isNew()) {
            String compName = pet.getName();
            compName = compName.toLowerCase();
            if (compName.equals(name)) {
                return pet;
            }
        }
    }
    return null;
}
```

POM pada ref yang sama menyatakan artifact `spring-petclinic-rest`, versi
`4.0.2`, dengan parent Spring Boot `4.1.1`.

## Perilaku aktual

1. `name` langsung dinormalisasi dengan `toLowerCase()`, jadi pencarian
   case-insensitive menurut default locale JVM.
2. Bila `ignoreNew == false`, semua pet dipertimbangkan.
3. Bila `ignoreNew == true`, pet baru dilewati; pet lama saja yang diperiksa.
4. Nama pet juga di-lowercase sebelum dibandingkan.
5. Method mengembalikan pet pertama yang cocok, atau `null` setelah iterasi
   selesai.
6. Tidak ada guard eksplisit untuk `name == null` atau `pet.getName() == null`;
   keduanya dapat menyebabkan `NullPointerException`. Kondisi ini dicatat
   sebagai perilaku source, bukan dihilangkan dari analisis.

## Kompleksitas siklomatik

Dengan keputusan loop, keputusan filter `!ignoreNew || !pet.isNew()`, dan
keputusan `compName.equals(name)`, terdapat tiga predicate:

`V(G) = predicate + 1 = 3 + 1 = 4`

Short-circuit `||` menambah dua kondisi operasional (`ignoreNew` dan
`!pet.isNew()`), tetapi tidak menambah predicate utama pada CFG statement-level.
Test case karena itu harus tetap menguji kombinasi `ignoreNew` dan status pet.

## Cakupan

Basis path dan test case eksplisit tersedia pada [`test-cases.md`](test-cases.md),
sedangkan node/edge CFG tersedia pada [`cfg.md`](cfg.md). Diagram sumbernya
adalah [`../diagrams/owner-get-pet-flow.mmd`](../diagrams/owner-get-pet-flow.mmd).
