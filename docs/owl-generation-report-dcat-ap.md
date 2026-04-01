# OWL Generation Report: DCAT-AP 3.0.0 LinkML Schema

**Date:** 2026-04-01
**Schema analysed:** `resources/dcat_ap/dcat_ap_linkml.yaml`
**Generator:** `linkml generate owl` (default options)
**Output:** `resources/dcat_ap/dcat_ap_linkml.owl.ttl` (1769 lines)
**Origin:** Auto-generated from DCAT-AP 3.0.0 SHACL shapes via
[dcat-ap_shacl_2_linkml.py](https://github.com/StroemPhi/dcat-4C-ap/tree/main/src/dcat-ap_shacl_2_linkml.py)

---

## 1. Executive Summary

This report analyses a LinkML representation of DCAT-AP 3.0.0 and the OWL
ontology generated from it. The goal is to assess how well LinkML's OWL
generation capabilities are exercised, what is lost or distorted in
translation, and where the model or the generator fall short.

The schema uses a wider range of LinkML features than many hand-authored
schemas — notably `class_uri`, `slot_uri`, schema-level `slots` with
`slot_usage`, `enum_uri`, and `meaning` on permissible values. However, the
generated OWL reveals that several of these features are **not honoured by the
OWL generator**: `slot_uri` is ignored for property IRIs, slots without an
explicit range are misclassified as `owl:DatatypeProperty`, and enum values are
modelled as classes rather than individuals.

The result is a **parallel ontology** under the `dcatap_linkml:` namespace that
*describes* DCAT-AP from a distance, rather than a faithful OWL rendering of
DCAT-AP itself.

---

## 2. LinkML Feature Usage Inventory

### 2.1 Features used in this schema

The following table catalogues every OWL-relevant LinkML feature that this
schema exercises, along with how it translates (or fails to translate) into OWL:

| LinkML feature | How this schema uses it | OWL result | Assessment |
|----------------|------------------------|------------|------------|
| **`class_uri`** | Declared on all major classes (e.g., `Catalogue` -> `dcat:Catalog`, `Dataset` -> `dcat:Dataset`, `Agent` -> `foaf:Agent`) | `skos:exactMatch` annotation generated (e.g., `dcatap_linkml:Catalogue skos:exactMatch dcat:Catalog`) | Partially effective. The class IRI remains `dcatap_linkml:Catalogue`, not `dcat:Catalog`. The mapping is present but the identity is not reused. |
| **`slot_uri`** | Declared on all ~60 slots (e.g., `title` -> `dcterms:title`, `publisher` -> `dcterms:publisher`) | **Ignored.** Properties are minted under `dcatap_linkml:` namespace. No `skos:exactMatch` or any mapping emitted. | Broken. This is the single biggest fidelity issue — see section 3.1. |
| **Schema-level `slots`** | ~60 slots defined at schema level | Clean global property declarations; no ambiguous attribute warnings | Correct. This is the right approach and avoids the problems seen in attribute-only schemas. |
| **`slot_usage`** | Every class specialises slot descriptions, ranges, cardinality, and `required` per class | Class-level `owl:Restriction` axioms with correct ranges and cardinalities | Correct. Slot usage drives the local restrictions as expected. |
| **`is_a`** | `SupportiveEntity` as base for ~15 supportive classes; no deeper hierarchies | `rdfs:subClassOf` chain | Correct, but `SupportiveEntity` itself has no standard counterpart (see section 3.5). |
| **`enum_uri`** | `DatasetThemes` -> `http://publications.europa.eu/resource/authority/data-theme`; `TopLevelMediaTypes` -> `iana:top-level-media-types` | Used as the parent class IRI for enum values | Correct. Values are minted under the authority table namespace. |
| **`meaning`** on enum values | All 14 `DatasetThemes` values have `meaning` URIs from the EU Publications Office authority table | Enum values use their `meaning` URI as their OWL IRI (e.g., `.../data-theme/AGRI`) | Partially correct. The IRIs are right, but values are modelled as `owl:Class` instead of `owl:NamedIndividual` — see section 3.4. |
| **Custom types** | `duration` (xsd:duration), `hexBinary` (xsd:hexBinary), `nonNegativeInteger` (xsd:nonNegativeInteger) — each with `uri`, `pattern`, `conforms_to` | `owl:equivalentClass` with `xsd:pattern` facet restrictions | Correct. Pattern-based datatype restrictions are faithfully rendered. |
| **`any_of`** for union ranges | `CatalogueRecord.primary_topic` range is union of Catalogue, Dataset, DatasetSeries, DataService | `owl:intersectionOf` wrapping `owl:unionOf` with `linkml:Any` | Semantically noisy — the intersection with `Any` (= `owl:Thing`) is a no-op. See section 3.3. |
| **`required`** | Used throughout on mandatory slots | `owl:minCardinality 1` | Correct. |
| **`multivalued`** | Used on most slots to indicate repeatable properties | Absence of `owl:maxCardinality` on multivalued slots | Correct (no upper bound emitted). |
| **`recommended`** | Used on many slots (e.g., `theme`, `contact_point`, `modification_date`) | **Not reflected in OWL.** No OWL equivalent exists. | Expected limitation. OWL cannot express "recommended". SHACL (`sh:severity`) would be the natural target. |
| **`inlined_as_list`** | Used pervasively on object-range slots | **No OWL effect.** This is a serialisation hint. | Correct (no OWL translation expected). |
| **`description`** on classes | Present on all classes, pointing to DCAT-AP spec sections | `skos:definition` annotations | Correct. |
| **`description`** on schema-level slots | All slots have placeholder text: "described in more detail within the class in which it is used" | 60+ identical `skos:definition` annotations — pure noise | Misleading. Placeholder descriptions pollute the OWL. |
| **`description`** on slot_usage | Rich, per-class descriptions | **Not emitted** in OWL property declarations. Only the schema-level slot description appears. | Lost information. The per-class descriptions (which are the real documentation) do not make it into OWL. |
| **`license`** and **`source`** | Schema-level metadata | `dcterms:license` and `dcterms:source` on ontology IRI | Correct. |
| **`title`** | Schema-level metadata | `dcterms:title` on ontology IRI | Correct. |
| **`see_also`** on enums | `DatasetThemes` has `see_also` pointing to EU authority table URL | **Not emitted** in OWL. No `rdfs:seeAlso`. | Lost information. |
| **`todos`** | Schema-level notes on known limitations | Not emitted (expected — these are development notes) | Correct. |

### 2.2 Features NOT used in this schema

The following OWL-relevant LinkML features are available but not exercised:

| LinkML feature | What it would produce in OWL | Why it matters for DCAT-AP |
|----------------|------------------------------|---------------------------|
| **`defining_slots`** | `owl:equivalentClass` (intersection of superclass + slot restrictions) | Could define `Catalogue` as "a thing with `has_dataset` and `publisher`" — enabling OWL automated classification |
| **`disjoint_with`** | `owl:disjointWith` axioms | `Dataset`, `DataService`, `Catalogue`, and `DatasetSeries` are clearly disjoint in DCAT-AP; nothing prevents a reasoner from merging them |
| **`abstract`** | Covering axioms (`owl:equivalentClass [ owl:unionOf ... ]`) | `SupportiveEntity` is essentially abstract but is not declared as such |
| **`mixin`** | GCI axioms or additional `rdfs:subClassOf` (depending on CLI flags) | Several DCAT-AP classes share patterns (e.g., Dataset and DatasetSeries share many slots) that could be captured as mixins |
| **`identifier: true`** | `owl:hasKey` axioms (OWL 2) | No slot is marked as the identity key, even though `dcterms:identifier` is semantically a key |
| **`exact_mappings`** / **`close_mappings`** / etc. | `skos:exactMatch`, `skos:closeMatch`, etc. on properties | Could compensate for `slot_uri` not being used: at minimum, properties would get `skos:exactMatch dcterms:title`, etc. |
| **`implements: [owl:NamedIndividual]`** on enums | `owl:oneOf` over `owl:NamedIndividual` instances | Enum values (AGRI, ECON, etc.) should be individuals, not classes — see section 3.4 |
| **`comments`** / **`notes`** | `rdfs:comment` or `skos:note` | Several classes have important caveats (e.g., temporal literal restrictions) that could be annotations |
| **`deprecated`** / **`status`** | `owl:deprecated true` | Useful if any elements are being phased out |
| **`structured_aliases`** | `skos:prefLabel` with language tags | DCAT-AP is an EU standard — multilingual labels in EN, FR, DE, etc. would be valuable |
| **`classification_rules`** | `owl:equivalentClass` from conditional slot constraints | More expressive than `defining_slots` for complex type discrimination |
| **`rules`** (preconditions/postconditions) | Limited OWL translation (SWRL planned) | Could formalise DCAT-AP validation rules (e.g., "if Dataset has no Distribution, it must have a landing_page") |
| **`broad_mappings`** / **`narrow_mappings`** / **`related_mappings`** | `skos:broadMatch`, `skos:narrowMatch`, `skos:relatedMatch` | DCAT-AP sits in a family of profiles (GeoDCAT-AP, StatDCAT-AP) — cross-profile mappings would be useful |
| **`union_of`** on classes | `owl:equivalentClass [ owl:unionOf ... ]` | Could formally declare that `dcat:Resource = Dataset ∪ DataService ∪ Catalogue ∪ DatasetSeries` |
| **`tree_root`** | Serialisation entry point | `Dataset` or `Catalogue` would be natural roots |

In total, this schema uses roughly **10 out of 25+** OWL-relevant LinkML
features. Of those 10, two are broken or partially broken in the OWL output
(`slot_uri`, `meaning` with default enum strategy). The remaining ~15 features
are available and would meaningfully improve the generated OWL.

### 2.3 No generator warnings

Unlike attribute-only schemas, this schema produces **zero warnings** from the
OWL generator. This is because all properties are defined as schema-level
`slots` (not per-class `attributes`), so there are no ambiguity conflicts.

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
Properties do not get this treatment — an asymmetry that appears unintentional.

**Impact:** This is the single biggest reason the generated OWL is not a
faithful representation of DCAT-AP. The `--use-native-uris` flag (defaults to
`True`) should theoretically cause the generator to use `slot_uri` as the OWL
property IRI — this needs investigation.

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

**Fix:** Add an explicit `range` to schema-level slots where the range is
consistently a class across all usages (e.g., `publisher` always has range
`Agent`).

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
union is "not fully implemented in LinkML yet" (referencing
[linkml/linkml#1813](https://github.com/linkml/linkml/issues/1813)).

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

The `meaning` URIs are correctly resolved (the OWL IRIs match the authority
table), but the ontological status is wrong.

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
`skos:definition` annotations in the OWL — pure noise. The richer `slot_usage`
descriptions per class are not reflected in the OWL property declarations.

---

## 5. Limitations of the LinkML OWL Generator (DCAT-AP specific)

Beyond the general limitations of the OWL generator (open-world vs.
closed-world mismatch, no SWRL rules, no native abstract classes — documented
in the companion ERS report), the DCAT-AP schema reveals additional generator
limitations:

| Limitation | Impact on DCAT-AP |
|-----------|-------------------|
| **`slot_uri` not used for OWL property IRIs** | All ~60 properties use `dcatap_linkml:` instead of `dcterms:`, `dcat:`, `foaf:`, etc. The OWL is not interoperable with DCAT-AP data. |
| **No `skos:exactMatch` generated for `slot_uri`** | Unlike `class_uri` (which generates `skos:exactMatch`), `slot_uri` produces nothing in the OWL output. Asymmetric treatment. |
| **Default range determines property type** | Slots without explicit range at schema level become `DatatypeProperty` even when `slot_usage` gives them a class range — OWL-DL violation. |
| **`recommended` flag has no OWL mapping** | DCAT-AP's mandatory/recommended/optional distinction is lost. SHACL (`sh:severity`) would be the natural target, not OWL. |
| **`any_of` with `Any` produces intersectionOf noise** | Union ranges wrapped with `linkml:Any` add semantically empty `owl:intersectionOf` wrappers. |
| **`see_also` on enums not emitted** | `DatasetThemes.see_also` pointing to the EU authority table is not emitted as `rdfs:seeAlso`. |
| **`slot_usage` descriptions not in OWL** | Only the schema-level slot description appears on the OWL property. The per-class descriptions (which contain the real documentation) are lost. |

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
| **Features used** | ~4 of 25+ | ~10 of 25+ |
| **Verbosity** | High | Very high (~1769 lines for ~30 classes) |

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
5. **Add `disjoint_with`** between the main DCAT-AP classes (Dataset,
   DataService, Catalogue, DatasetSeries).
6. **Add `exact_mappings`** on schema-level slots as a fallback mapping
   mechanism until `slot_uri` is honoured by the generator.

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
`slot_uri`, schema-level `slots`, and `slot_usage`, a LinkML model can be
considerably richer than a naive attribute-only approach. It uses roughly
**10 out of 25+** OWL-relevant LinkML features. Of the ~15 unused features,
several would be directly valuable: `disjoint_with`, `defining_slots`,
`exact_mappings`, `implements` on enums, `abstract`, `identifier`, and
`structured_aliases` for multilingual labels.

However, the OWL generator does not fully honour even the features that *are*
used. The most critical gap — `slot_uri` being ignored for OWL property IRIs —
means the generated OWL **duplicates** DCAT-AP under a parallel namespace
rather than **representing** it. Combined with the `DatatypeProperty`
misclassification (an OWL-DL violation), the generated output should be treated
as an **inspection artefact**, not as a publishable ontology.

For reference, the official DCAT-AP OWL ontology published by SEMIC uses the
canonical `dcat:`, `dcterms:`, `foaf:` property URIs directly. Any serious OWL
publication from this LinkML schema would need to either fix the generator
behaviour or post-process the output to replace `dcatap_linkml:` property URIs
with their `slot_uri` equivalents.
