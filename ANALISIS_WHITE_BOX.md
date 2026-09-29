# Analisis White-Box Testing Spring PetClinic REST

Dokumen utama analisis telah dikoreksi ke target yang diminta:
`spring-petclinic/spring-petclinic-rest`, branch `master`, commit
`4cd8e1b0cd42578e882247d8801f6be5d402f118`, file
`src/main/java/org/springframework/samples/petclinic/model/Owner.java`.

Method yang dianalisis adalah `getPet(String name, boolean ignoreNew)`, bukan
`Owner.getPet(Integer)` dari repository MVC yang berbeda.

## Implementasi aktual

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

Kompleksitas siklomatik statement-level adalah `V(G)=4`: loop, filter
`!ignoreNew || !pet.isNew()`, dan equality `compName.equals(name)`, ditambah
satu. Basis path P1-P4, test case TC-01 sampai TC-11, serta perilaku null yang
memang dapat melempar `NullPointerException` didokumentasikan di `docs/`.

Berdasarkan definisi CFG yang dicantumkan, suite tersebut mencapai branch
predicate `6/6`, outcome short-circuit `4/4`, statement/control node `8/8`,
dan loop `3/3` (semuanya 100%). Ini adalah coverage analitis dari pemetaan
test case, bukan klaim hasil instrumentasi seluruh repository.

Lihat:

- [`docs/analysis.md`](docs/analysis.md)
- [`docs/cfg.md`](docs/cfg.md)
- [`docs/test-cases.md`](docs/test-cases.md)
- [`diagrams/owner-get-pet-flow.mmd`](diagrams/owner-get-pet-flow.mmd)
