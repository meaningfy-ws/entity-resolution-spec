# OWL Generation Report: DCAT-AP 3.0.0 LinkML Schema

**Date:** 2026-04-01
**Schema analysed:** `resources/dcat_ap/dcat_ap_linkml.yaml`
**Generator:** `linkml generate owl` (default options)
**Output:** `resources/dcat_ap/dcat_ap_linkml.owl.ttl` (1769 lines)
**Origin:** Auto-generated from DCAT-AP 3.0.0 SHACL shapes via
[dcat-ap_shacl_2_linkml.py](https://github.com/StroemPhi/dcat-4C-ap/tree/main/src/dcat-ap_shacl_2_linkml.py)

---

## 1. Executive Summary

This DCAT-AP LinkML schema is significantly more mature in its use of LinkML
features than the ERS/ERE schemas analysed in the companion report. It makes
good use of `class_uri`, `slot_uri`, schema-level `slots` with `slot_usage`,
`enum_uri`, and `meaning` on permissible values. However, as a machine-generated
schema (SHACL-to-LinkML conversion), it carries systematic issues: all
properties are minted under a local `dcatap_linkml:` namespace and only *mapped*
to their canonical DCAT/Dublin Core URIs via `skos:exactMatch`, rather than
*being* those URIs. The generated OWL is therefore **a parallel ontology that
describes DCAT-AP from a distance**, not a faithful OWL rendering of DCAT-AP
itself.

The OWL output also suffers from the same verbosity issues as the ERS report
(vacuous `minCardinality 0` axioms, un-consolidated cardinality), and reveals
several deeper problems: `slot_uri` is declared in LinkML but **ignored by the
OWL generator** in favour of auto-generated URIs, enum values with `meaning`
URIs are modelled as classes instead of individuals, and the `any_of` union
ranges produce convoluted OWL restrictions.

---

## 2. Current State Assessment

### 2.1 What the schema does well (compared to ERS)

| Feature | LinkML usage | OWL result |
|---------|-------------|------------|
| **`class_uri`** on all major classes | `Catalogue` -> `dcat:Catalog`, `Dataset` -> `dcat:Dataset`, etc. | `skos:exactMatch` annotations generated (e.g., `skos:exactMatch dcat:Catalog`) |
| **`slot_uri`** on all slots | `title` -> `dcterms:title`, `publisher` -> `dcterms:publisher`, etc. | **Not used in OWL property IRIs** — see issue 3.1 |
| **Schema-level `slots`** with `slot_usage` | ~60 slots defined at schema level, specialised per class | No ambiguous attribute warnings; clean property definitions |
| **`enum_uri`** on enums | `DatasetThemes` -> `http://publications.europa.eu/resource/authority/data-theme` | Used as parent class IRI for enum values in OWL |
| **`meaning`** on enum values | `AGRI` -> `http://publications.europa.eu/resource/authority/data-theme/AGRI` | Values get their canonical EU authority URIs in OWL |
| **Custom types** (`duration`, `hexBinary`, `nonNegativeInteger`) | Defined with `uri`, `pattern`, `conforms_to` | OWL datatype restrictions with `xsd:pattern` generated |
| **`any_of` for union ranges** | `primary_topic` range is union of Catalogue, Dataset, DatasetSeries, DataService | `owl:intersectionOf` + `owl:unionOf` generated (see issue 3.3) |
| **`is_a` hierarchy** | `SupportiveEntity` as base for ~15 supportive classes | `rdfs:subClassOf` chain |
| **`recommended`** flag on slots | Used throughout (e.g., `theme`, `contact_point`) | Not reflected in OWL (no OWL equivalent) |
| **License and source metadata** | `license: CC-BY 4.0`, `source:` URL | `dcterms:license` and `dcterms:source` on ontology IRI |

### 2.2 What the generator produces

| Feature | Status |
|---------|--------|
| Class hierarchy | `rdfs:subClassOf` for `is_a` relationships |
| Cardinality | Verbose: separate `minCardinality` / `maxCardinality` including vacuous `min 0` |
| Range constraints | `owl:allValuesFrom` restrictions on each class |
| External class mapping | `skos:exactMatch` from `class_uri` (e.g., `dcatap_linkml:Catalogue skos:exactMatch dcat:Catalog`) |
| Enum values with `meaning` | Enum values use their `meaning` URI as their OWL IRI (good!) |
| Enum values without `meaning` | Local IRI under `enum_uri#name` pattern (e.g., `iana:top-level-media-types#application`) |
| Custom datatypes | `owl:equivalentClass` with `xsd:pattern` facet restrictions |
| Property IRIs | **All under `dcatap_linkml:` namespace** — `slot_uri` is ignored |
| Slot descriptions | Generic "described in more detail within the class" for global slots |
| Ontology IRI | `https://w3id.org/nfdi-de/dcat-ap-linkml.owl.ttl` (with file extension) |

### 2.3 No generator warnings

Unlike the ERS schemas, this schema produces **zero warnings** from the OWL
generator. This is because all properties are defined as schema-level `slots`
(not per-class `attributes`), so there are no ambiguity conflicts.

---

## 3. Critical Issues

### 3.1 `slot_uri` is declared but NOT used as the OWL property IRI

This is the most significant finding and arguably a **generator limitation or
bug**.

**In the LinkML schema:**
```yaml
slots:
  title:
    slot_uri: dcterms:title
  publisher:
    slot_uri: dcterms:publisher
```

**Expected OWL output:**
```turtle
dcterms:title a owl:DatatypeProperty .
dcterms:publisher a owl:ObjectProperty .
```

**Actual OWL output:**
```turtle
dcatap_linkml:title a owl:DatatypeProperty ;
    skos:definition "This slot is described in more detail..." .

dcatap_linkml:publisher a owl:DatatypeProperty ;
    skos:definition "This slot is described in more detail..." .
```

The generator mints **all properties under the `dcatap_linkml:` namespace**,
completely ignoring `slot_uri`. There is no `skos:exactMatch` or any other
mapping to the canonical property URIs. This means:

- `dcatap_linkml:title` exists as a property, but `dcterms:title` does not
  appear in the OWL at all (except indirectly via `dcterms:license` on the
  ontology itself).
- Any SPARQL query or reasoner expecting standard DCAT/Dublin Core property
  URIs will find nothing.
- The OWL is **not interoperable** with existing DCAT-AP data.

**Contrast with `class_uri`:** Classes *do* get a `skos:exactMatch` to their
`class_uri` (e.g., `dcatap_linkml:Catalogue skos:exactMatch dcat:Catalog`).
Properties do not get this treatment.

**Impact:** This is the single biggest reason the generated OWL is not a
faithful representation of DCAT-AP. It may be a generator limitation (the
`--use-native-uris` flag exists but defaults to `True`, which should use the
`slot_uri` — this needs investigation).

### 3.2 All global properties are `owl:DatatypeProperty`

**In the LinkML schema:** Many slots have class ranges in their `slot_usage`
(e.g., `publisher` -> `Agent`, `theme` -> `Concept`, `contact_point` -> `Kind`).

**In the OWL output:** The global property declarations are all
`owl:DatatypeProperty`:

```turtle
dcatap_linkml:publisher a owl:DatatypeProperty .
dcatap_linkml:theme a owl:DatatypeProperty .
dcatap_linkml:contact_point a owl:DatatypeProperty .
```

But within class restrictions, these same properties are used with
`owl:allValuesFrom` pointing to OWL classes:

```turtle
# Inside dcatap_linkml:Dataset:
[ owl:allValuesFrom dcatap_linkml:Agent ;
  owl:onProperty dcatap_linkml:publisher ]
```

**Problem:** In OWL-DL, a `DatatypeProperty` cannot have a class as its range —
that is the job of `ObjectProperty`. This is a **DL profile violation**. The
slots are declared without a `range` at the schema level (range is only set in
`slot_usage`), so the generator defaults to `DatatypeProperty` based on the
schema-level `default_range: string`.

This means the OWL output is technically in **OWL Full**, not OWL-DL, and most
reasoners will either reject it or behave unpredictably.

### 3.3 `any_of` union ranges produce convoluted OWL

**In the LinkML schema (`CatalogueRecord.primary_topic`):**
```yaml
primary_topic:
    range: Any
    any_of:
    - range: Catalogue
    - range: Dataset
    - range: DatasetSeries
    - range: DataService
```

**In the OWL output:**
```turtle
[ owl:allValuesFrom [ owl:intersectionOf (
    [ owl:unionOf ( dcatap_linkml:Catalogue dcatap_linkml:Dataset
                     dcatap_linkml:DatasetSeries dcatap_linkml:DataService ) ]
    dcatap_linkml:Any ) ] ;
  owl:onProperty dcatap_linkml:primary_topic ]
```

**Problem:** The `owl:intersectionOf` wraps the `owl:unionOf` with
`dcatap_linkml:Any`. Since `Any` maps to `linkml:Any` (effectively
`owl:Thing`), the intersection with `owl:Thing` is semantically a no-op, but
it adds unnecessary complexity to the OWL. The `any_of` union itself is
correctly expressed, but the `Any` wrapper is noise.

This is a known limitation noted in the schema's own `todos` — the `any_of`
union is "not fully implemented in LinkML yet" (referencing issue #1813).

### 3.4 Enum values are modelled as classes, not individuals

**In the OWL output:**
```turtle
<http://publications.europa.eu/resource/authority/data-theme/AGRI> a owl:Class ;
    rdfs:subClassOf <http://publications.europa.eu/resource/authority/data-theme> ;
    skos:definition "Agriculture, fisheries, forestry and food" .
```

**Problem:** `AGRI` is a specific data theme — a *value*, not a *type*. The EU
authority table publishes these as `skos:Concept` instances (individuals), not
as classes. Modelling them as `owl:Class` means they cannot be used as instance
data without OWL punning.

**Fix:** Add `implements: [owl:NamedIndividual]` to the `DatasetThemes` and
`TopLevelMediaTypes` enums so that values become `owl:NamedIndividual` with
`owl:oneOf`.

### 3.5 `SupportiveEntity` is a LinkML-only construct with no OWL counterpart

**In the schema:** `SupportiveEntity` is a base class for ~15 supportive types
(Document, Frequency, LegalResource, etc.) with no `class_uri`.

**In the OWL:** It becomes `dcatap_linkml:SupportiveEntity` — a class that does
not exist in DCAT-AP or any standard vocabulary. All supportive classes are
`rdfs:subClassOf dcatap_linkml:SupportiveEntity`, creating a hierarchy that has
no basis in the original DCAT-AP specification.

This is a modelling convenience from the SHACL-to-LinkML conversion, not a
DCAT-AP design decision.

---

## 4. Verbosity and Generator Flag Issues

These are the same issues identified in the ERS report but amplified by the
larger schema:

### 4.1 Vacuous `minCardinality 0` axioms

The `Distribution` class alone has **~20 restrictions** of the form
`owl:minCardinality 0`, each of which is tautologically true. The entire OWL
file would shrink substantially with `--skip-vacuous-min-zero-cardinality-axioms`.

### 4.2 Un-consolidated cardinality

Required single-valued slots generate separate `minCardinality 1` +
`maxCardinality 1` instead of a single `owl:cardinality 1`. Use
`--consolidate-cardinality-axioms`.

### 4.3 Ontology IRI has file extension

`<https://w3id.org/nfdi-de/dcat-ap-linkml.owl.ttl>` — use
`--ontology-iri-suffix ""`.

### 4.4 Slot descriptions are placeholder text

All schema-level slots have the description "This slot is described in more
detail within the class in which it is used." This produces 60+ identical
`skos:definition` annotations in the OWL — pure noise. The `slot_usage`
descriptions per class are richer but are not reflected in the OWL property
declarations.

---

## 5. Limitations of the LinkML OWL Generator (DCAT-AP specific)

Beyond the general limitations documented in the ERS report, the DCAT-AP schema
reveals additional generator limitations:

| Limitation | Impact on DCAT-AP |
|-----------|-------------------|
| **`slot_uri` not used for OWL property IRIs** | All ~60 properties use `dcatap_linkml:` instead of `dcterms:`, `dcat:`, `foaf:`, etc. The OWL is not interoperable with DCAT-AP data. |
| **No `skos:exactMatch` generated for `slot_uri`** | Unlike `class_uri` (which generates `skos:exactMatch`), `slot_uri` produces nothing in the OWL output. |
| **Default range determines property type** | Slots without explicit range at schema level become `DatatypeProperty` even when `slot_usage` gives them a class range — OWL-DL violation. |
| **`recommended` flag has no OWL mapping** | DCAT-AP's mandatory/recommended/optional distinction is lost. SHACL (`sh:severity`) would be the natural target, not OWL. |
| **`any_of` with `Any` produces intersectionOf noise** | Union ranges wrapped with `linkml:Any` add semantically empty `owl:intersectionOf` wrappers. |
| **`inlined_as_list` has no OWL meaning** | Serialisation hints are ignored (correctly), but they add noise to the LinkML schema. |
| **`see_also` on enums not in OWL** | `DatasetThemes.see_also` pointing to the EU authority table is not emitted as `rdfs:seeAlso`. |

---

## 6. Comparison with ERS Schemas

| Aspect | ERS/ERE schemas | DCAT-AP schema |
|--------|----------------|----------------|
| **Schema origin** | Hand-authored | Machine-generated (SHACL -> LinkML) |
| **`class_uri`** | Not used | Used on all major classes |
| **`slot_uri`** | Not used | Used on all slots (but ignored by OWL gen) |
| **Schema-level `slots`** | Not used (attributes only) | Used throughout with `slot_usage` |
| **Enum `meaning`** | Not used | Used on `DatasetThemes` values |
| **`enum_uri`** | Not used | Used on both enums |
| **External vocabulary alignment** | None | `class_uri` generates `skos:exactMatch` |
| **Generator warnings** | 10 ambiguous attribute warnings | Zero warnings |
| **OWL-DL compliance** | Likely compliant | Violated (DatatypeProperty with class ranges) |
| **Interoperability** | Self-contained (by design) | Claims DCAT-AP alignment but properties are local |
| **Verbosity** | High | Very high (~1769 lines for 30 classes) |

**Key insight:** The DCAT-AP schema uses more LinkML features correctly
(slots, slot_usage, class_uri, slot_uri, enum_uri, meaning), but the OWL
generator does not fully honour them — especially `slot_uri`. The ERS schemas
are simpler and use fewer features, but the OWL output is arguably *more
self-consistent* because it does not claim external alignment it cannot deliver.

---

## 7. Recommended Action Plan

### 7.1 Phase 1: Generator flags (immediate)

Update the Makefile target:

```makefile
$(DCAT_AP_OWL_PATH): $(DCAT_AP_SCHEMA)
	@poetry run linkml generate owl \
		--ontology-iri-suffix "" \
		--consolidate-cardinality-axioms \
		--skip-vacuous-min-zero-cardinality-axioms \
		$(DCAT_AP_SCHEMA) 2>/dev/null > $(DCAT_AP_OWL_PATH)
```

### 7.2 Phase 2: Investigate `--use-native-uris`

The `--use-native-uris` flag (defaults to `True`) should cause the generator
to use `slot_uri` as the OWL property IRI. Test with:

```bash
poetry run linkml generate owl --use-native-uris $(DCAT_AP_SCHEMA) > test.ttl
```

If this produces `dcterms:title` instead of `dcatap_linkml:title`, the issue
is that the current Makefile is not passing this flag (or the default is not
working as documented). If it does not help, this is a generator bug that
should be reported.

### 7.3 Phase 3: Schema improvements (if maintaining a fork)

If this schema is maintained locally (not just consumed as-is):

1. **Add `implements: [owl:NamedIndividual]`** to `DatasetThemes` and
   `TopLevelMediaTypes` enums.
2. **Add a `range` to schema-level slots** where the range is always the same
   across all usages (e.g., `publisher` always has range `Agent`). This will
   fix the `DatatypeProperty` vs `ObjectProperty` misclassification.
3. **Replace placeholder descriptions** on schema-level slots with meaningful
   text, or remove them entirely (an absent description is better than a
   misleading one).
4. **Consider removing `SupportiveEntity`** or adding `class_uri: owl:Thing`
   to it, since it has no DCAT-AP equivalent.
5. **Add `see_also`** at the schema level pointing to the DCAT-AP 3.0.0 spec.

### 7.4 Phase 4: Upstream engagement

The most impactful improvements require upstream changes:

1. **Report the `slot_uri` -> OWL property IRI issue** to
   [linkml/linkml](https://github.com/linkml/linkml). This is either a bug
   or an undocumented interaction with `--use-native-uris`.
2. **Report the `DatatypeProperty` misclassification** when `slot_usage`
   provides a class range but the schema-level slot has no range.
3. **Track issue #1813** (union ranges) for `any_of` clean-up.

---

## 8. Conclusion

The DCAT-AP LinkML schema demonstrates that with proper use of `class_uri`,
`slot_uri`, schema-level `slots`, and `slot_usage`, the LinkML model can be
considerably richer than a naive attribute-only approach. It uses roughly
**8-10 out of 20+** OWL-relevant LinkML features (compared to ~4 in the ERS
schemas).

However, the OWL generator does not fully honour this richness. The most
critical gap — `slot_uri` being ignored for OWL property IRIs — means the
generated OWL **duplicates** DCAT-AP under a parallel namespace rather than
**representing** it. Until this is fixed (either via generator flags or upstream
patches), the generated OWL should be treated as an **inspection artefact**,
not as a publishable ontology.

For comparison, the official DCAT-AP OWL ontology published by SEMIC uses the
canonical `dcat:`, `dcterms:`, `foaf:` property URIs directly. Any serious
OWL publication from this LinkML schema would need to either fix the generator
behaviour or post-process the output to replace `dcatap_linkml:` property URIs
with their `slot_uri` equivalents.
