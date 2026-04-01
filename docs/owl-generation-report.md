# OWL Generation Report: ERS/ERE LinkML Schemas

**Date:** 2026-04-01
**Schemas analysed:** `core-schema-v0.1.0.yaml`, `ere-service-schema-v0.1.0.yaml`
**Generator:** `linkml generate owl` (default options)
**Output:** `resources/schemas/ere-service-schema-v0.1.0.owl.ttl`

---

## 1. Executive Summary

The current LinkML schemas produce a structurally correct OWL ontology, but they
use only a fraction of the OWL generator's capabilities. The output is verbose
(many redundant cardinality axioms), has namespace issues, and misses several
OWL constructs that would make the ontology richer and more useful for reasoning,
validation, and interoperability.

This report catalogues every concrete improvement opportunity, grouped by
severity, and maps each to specific LinkML features documented in the
[OWL generator reference](https://linkml.io/linkml/generators/owl.html).

---

## 2. Current State Assessment

### 2.1 What the generator produces today

| Feature | Status |
|---------|--------|
| Class hierarchy (`is_a`) | Correct: `rdfs:subClassOf` chain |
| Cardinality constraints | Correct but verbose (separate min/max axioms) |
| Range constraints | Correct: `owl:allValuesFrom` restrictions |
| Numeric facets (min/max value) | Correct: `xsd:minInclusive` / `xsd:maxInclusive` via `owl:withRestrictions` |
| Enum translation | Default (`owl:Class`-based `owl:unionOf`) |
| Property classification | Correct: `owl:ObjectProperty` vs `owl:DatatypeProperty` |
| Descriptions | Mapped to `skos:definition` |
| Abstract classes | Rendered as regular `owl:Class` (no covering axiom) |
| Ontology IRI | Auto-generated with `.owl.ttl` suffix |

### 2.2 What the generator COULD produce (unused capabilities)

The OWL generator supports many features that our schemas do not yet exercise.
This table summarises what is available but dormant:

| Generator capability | LinkML feature needed | OWL construct produced | Status in our schemas |
|----------------------|-----------------------|------------------------|-----------------------|
| **Equivalence axioms** | `defining_slots` on classes | `owl:equivalentClass` (intersection of superclass + slot restrictions) | Not used on any class |
| **Covering axioms for abstract classes** | `abstract: true` + subclasses (generator default) | `owl:equivalentClass [ owl:unionOf (...subclasses...) ]` | Generated but may need verification; `--skip-abstract-class-as-unionof-subclasses` flag exists to suppress |
| **Disjointness** | `disjoint_with` on classes | `owl:disjointWith` axioms | Not declared anywhere |
| **Enum as individuals** | `implements: [owl:NamedIndividual]` on enums | `owl:oneOf` over `owl:NamedIndividual` instances | Using default (`owl:Class` + `owl:unionOf`) |
| **Enum as literals** | `implements: [rdfs:Literal]` on enums | `owl:oneOf` over string literals | Not used |
| **Enum value URIs** | `meaning: CURIE` on permissible values | Named individuals/classes with external URIs | No `meaning` declared on any enum value |
| **Mixed enum strategies** | Per-value `implements` override | Mixed individuals/classes/literals in one enum | Not used |
| **SKOS mappings** | `exact_mappings`, `close_mappings`, `broad_mappings`, `narrow_mappings`, `related_mappings` | `skos:exactMatch`, `skos:closeMatch`, etc. annotations | Zero mappings declared |
| **External property URIs** | `slot_uri: dct:created` | Property IRI becomes the external URI directly | No `slot_uri` on any slot |
| **External class URIs** | `class_uri: schema:Person` | Class IRI becomes the external URI directly | No `class_uri` on any class |
| **OWL key axioms** | `identifier: true` on slots | `owl:hasKey` (OWL 2) | No slot marked as identifier |
| **Mixin as expression** | `mixin: true` + `--mixins-as-expressions` CLI flag | GCI axioms with `owl:someValuesFrom` instead of `rdfs:subClassOf` | No mixin classes declared |
| **Consolidated cardinality** | (CLI flag only) `--consolidate-cardinality-axioms` | Single `owl:cardinality N` instead of separate min+max | Not using the flag |
| **Clean ontology IRI** | (CLI flag only) `--ontology-iri-suffix ""` | Ontology IRI without `.owl.ttl` extension | Not using the flag |
| **Suppressed vacuous axioms** | (CLI flag only) `--skip-vacuous-min-zero-cardinality-axioms` | Omits tautological `minCardinality 0` | Not using the flag |
| **OLS metadata profile** | (CLI flag only) `--metadata-profile ols` | Ontology Lookup Service annotations | Using default `linkml` profile |
| **Root metaclasses** | (CLI flag only) `--add-root-classes` | `ClassDefinition`, `SlotDefinition`, etc. parent classes for portal navigation | Not using the flag |
| **Multilingual labels** | `structured_aliases` with `in_language` | `skos:prefLabel` with language tags | Not used |
| **Deprecation markers** | `deprecated: true` or `status: deprecated` | `owl:deprecated true` annotation | Not used |
| **Comments / notes** | `comments`, `notes` on elements | `rdfs:comment` or `skos:note` (profile-dependent) | Only `description` is used |
| **Classification rules** | `classification_rules` on classes | `owl:equivalentClass` from conditional slot constraints | Not used |
| **Conditional rules** | `rules` with preconditions/postconditions | Limited OWL translation (SWRL planned for future) | Not used |

In short, the current schemas use roughly **4 out of 20+** available OWL-relevant
features: class hierarchy, cardinality, range restrictions, and descriptions.
The remaining capabilities — equivalence axioms, disjointness, external
mappings, enum strategies, key axioms, and several CLI optimisations — are all
available but untapped.

### 2.3 Generator warnings

The OWL generator emits "Ambiguous attribute" warnings for: `source_id`, `id`,
`about_entity_mention`, `candidates`, `created_at`. These are attributes that
appear in multiple classes and get merged into a single global OWL property.

---

## 3. Issues and Improvements

### 3.1 CRITICAL: Namespace and URI Issues

#### 3.1.1 Ontology IRI contains file extension

**Current:** `<https://data.europa.eu/ers/schema/ere.owl.ttl>`

**Problem:** The `.owl.ttl` suffix is a serialisation artefact, not a semantic
identifier. It will cause confusion when referencing the ontology from other
systems and violates common practice for persistent ontology IRIs.

**Fix (Makefile):** Pass `--ontology-iri-suffix ""` to the generator.

**Alternative fix (schema):** No schema-level override exists; this is purely a
generator CLI option.

#### 3.1.2 Two namespaces but no `class_uri` / `slot_uri` alignment

**Current:** Core classes use `ers:` prefix, ERE service classes use `ere:` prefix.
Properties from the core schema land under `ers:` (e.g., `ers:source_id`), while
ERE properties land under `ere:` (e.g., `ere:entity_mention`). This is correct,
but none of the classes or slots declare explicit `class_uri` or `slot_uri`.

**Problem:** All URIs are auto-generated from `default_prefix + name`. This means:
- Renaming a class in LinkML silently changes its OWL URI (breaking change).
- There is no mapping to well-known external vocabularies.

**Fix:** Add explicit `class_uri` and `slot_uri` where stability matters or where
external alignments exist. For example:

```yaml
classes:
  EntityMention:
    class_uri: ers:EntityMention   # explicit, stable URI
```

#### 3.1.3 No external ontology mappings

**Current:** Zero `exact_mappings`, `close_mappings`, `broad_mappings`,
`narrow_mappings`, or `related_mappings` are declared.

**Problem:** The OWL output is a self-contained island with no links to the
broader semantic web. For an EU data.europa.eu ontology, this is a significant
gap. Relevant external vocabularies exist:

| ERS concept | Candidate external mapping | Mapping type |
|-------------|---------------------------|--------------|
| `EntityMention` | `nif:String` (NLP Interchange Format) | `related_mappings` |
| `EntityMentionIdentifier` | `adms:Identifier` (ADMS) | `close_mappings` |
| `content_type` | `dct:format` (Dublin Core) | `close_mappings` |
| `content` | `rdf:value` | `broad_mappings` |
| `created_at` | `dct:created` (Dublin Core) | `exact_mappings` |
| `updated_at` | `dct:modified` (Dublin Core) | `exact_mappings` |
| `actor` | `prov:wasAssociatedWith` (PROV-O) | `close_mappings` |
| `confidence_score` | `prov:value` or custom | `related_mappings` |
| `cluster_id` | `skos:Concept` (SKOS) | `broad_mappings` |
| `entity_type` | `rdf:type` | `related_mappings` |

**Fix:** Add mappings in the LinkML schema. These generate `skos:exactMatch`,
`skos:closeMatch`, etc. in the OWL output:

```yaml
prefixes:
  dct: http://purl.org/dc/terms/
  prov: http://www.w3.org/ns/prov#
  adms: http://www.w3.org/ns/adms#

slots:
  created_at:
    exact_mappings:
      - dct:created
  updated_at:
    exact_mappings:
      - dct:modified
```

---

### 3.2 HIGH: Structural and Semantic Improvements

#### 3.2.1 Ambiguous attributes should become schema-level slots

**Current:** All properties are declared as class-level `attributes`.

**Problem:** When the same attribute name (e.g., `id`, `source_id`, `candidates`,
`created_at`) appears in multiple classes, the OWL generator must merge them into
a single global property. This causes:
- "Ambiguous attribute" warnings.
- Loss of class-scoping: in OWL, `ers:id` is one property shared across
  `Decision` and `UserAction`.
- If the ranges ever diverge, the OWL becomes inconsistent.

**Fix (option A — preferred):** Promote shared attributes to schema-level `slots`
and use `slot_usage` to specialise per class. This gives the generator a single
canonical definition:

```yaml
slots:
  id:
    description: Unique identifier
    range: string
    required: true

classes:
  Decision:
    slots:
      - id
    slot_usage:
      id:
        description: Unique decision identifier
  UserAction:
    slots:
      - id
    slot_usage:
      id:
        description: Unique audit trail entry identifier
```

**Fix (option B — if class-scoping is needed):** Use distinct names like
`decision_id`, `user_action_id`, `lookup_source_id`, etc.

#### 3.2.2 Enum values should be `owl:NamedIndividual`, not `owl:Class`

**Current:** `UserActionType` enum values (`ACCEPT_TOP`, `ACCEPT_ALTERNATIVE`,
`REJECT_ALL`) are rendered as OWL classes (`owl:unionOf` over subclasses).

**Problem:** These are discrete values, not types. Modelling `ACCEPT_TOP` as a
class means it represents a category of things, not a single thing. In instance
data, `myAction ere:action_type ere:ACCEPT_TOP` would be asserting that the
action type is a *class*, which is OWL punning and can confuse reasoners.

**Fix:** Use the `implements` annotation on the enum:

```yaml
enums:
  UserActionType:
    description: Types of curator actions on entity mention resolutions
    implements:
      - owl:NamedIndividual
    permissible_values:
      ACCEPT_TOP:
        description: Curator accepted the top candidate from ERE
      ACCEPT_ALTERNATIVE:
        description: Curator selected an alternative candidate
      REJECT_ALL:
        description: Curator rejected all candidates
```

This produces `owl:oneOf` over named individuals instead of `owl:unionOf` over
classes, which is the correct OWL modelling for a closed set of values.

#### 3.2.3 Abstract classes lack covering axioms

**Current:** `EREMessage`, `ERERequest`, and `EREResponse` are marked
`abstract: true` in LinkML but appear as plain `owl:Class` in OWL.

**Problem:** OWL has no `abstract` keyword. However, the OWL generator can
express the intent via a **covering axiom**: the abstract class is equivalent to
the union of its concrete subclasses. This is not generated by default.

**Opportunity:** The generator has a flag `--skip-abstract-class-as-unionof-subclasses`
(which *suppresses* this behaviour), implying that with the right configuration,
covering axioms *can* be generated. Verify whether the current LinkML version
supports this. If it does, the covering axiom would be:

```turtle
ere:EREResponse owl:equivalentClass [
    owl:unionOf ( ere:EntityMentionResolutionResponse ere:EREErrorResponse )
] .
```

This formally states "every EREResponse is either a resolution response or an
error response" — a powerful axiom for reasoning and validation.

#### 3.2.4 `EREMessage` should use `mixin: true` properly

**Current:** `EREMessage` is declared `abstract: true` and uses `is_a` for the
subclass chain. The LinkML description says "This is modelled as a mixin in
LinkML (so that it can't be instantiated directly)" — but the schema actually
uses `abstract: true` on a regular class, not the `mixin: true` metamodel slot.

**Problem:** This is an inconsistency between the documentation comment and the
actual schema. If `EREMessage` is truly a mixin (providing shared attributes to
both requests and responses), it should be:

```yaml
EREMessage:
    mixin: true
    attributes:
      type: ...
      ere_request_id: ...
      timestamp: ...

ERERequest:
    abstract: true
    mixins:
      - EREMessage

EREResponse:
    abstract: true
    mixins:
      - EREMessage
```

**OWL impact:** With `--mixins-as-expressions`, this would generate General
Class Inclusion (GCI) axioms instead of a simple `rdfs:subClassOf`, which better
reflects the "interface-like" nature of `EREMessage`.

**Trade-off:** This is a modelling decision. If `EREMessage` is genuinely an
abstract base class (not an interface), the current `is_a` approach is fine.
Clarify the intent and pick one consistently.

#### 3.2.5 No `defining_slots` for OWL equivalence axioms

**Current:** No class uses `defining_slots`.

**Problem:** `defining_slots` is the LinkML mechanism for generating
`owl:equivalentClass` axioms — the most powerful OWL construct for automated
classification. For example, `EntityMentionResolutionRequest` *is* an ERERequest
*that has* an `entity_mention`. This could be expressed as:

```yaml
EntityMentionResolutionRequest:
    is_a: ERERequest
    defining_slots:
      - entity_mention
    attributes:
      entity_mention:
        range: EntityMention
        required: true
```

This would generate:

```turtle
ere:EntityMentionResolutionRequest owl:equivalentClass [
    owl:intersectionOf (
        ere:ERERequest
        [ a owl:Restriction ;
          owl:onProperty ere:entity_mention ;
          owl:someValuesFrom ers:EntityMention ]
    )
] .
```

An OWL reasoner could then automatically classify any `ERERequest` with an
`entity_mention` as an `EntityMentionResolutionRequest`.

**Candidates for `defining_slots`:**

| Class | Defining slots | Rationale |
|-------|---------------|-----------|
| `EntityMentionResolutionRequest` | `entity_mention` | A request *with* an entity mention |
| `EntityMentionResolutionResponse` | `entity_mention_id`, `candidates` | A response *with* mention ID and candidates |
| `EREErrorResponse` | `error_type` | A response *with* an error type |

#### 3.2.6 `tree_root` is not declared

**Current:** No class is marked `tree_root: true`.

**Problem:** While `tree_root` primarily affects JSON Schema and data validation,
it helps document which class is the intended top-level serialisation entry
point. For this schema, `EREMessage` (or its concrete subclasses) would be
natural roots.

**Fix:**

```yaml
EntityMentionResolutionRequest:
    tree_root: true
    ...
EntityMentionResolutionResponse:
    tree_root: true
    ...
```

---

### 3.3 MEDIUM: Generator CLI Improvements

#### 3.3.1 Consolidate cardinality axioms

**Current:** Each required single-valued slot generates three separate
restrictions: `owl:minCardinality 1`, `owl:maxCardinality 1`, and
`owl:allValuesFrom`. For `Decision` alone, this produces 17 restrictions.

**Fix:** Use `--consolidate-cardinality-axioms` to emit a single
`owl:cardinality 1` when min equals max. This significantly reduces output
verbosity.

#### 3.3.2 Remove vacuous axioms

**Current:** Optional slots generate `owl:minCardinality 0`, which is
tautologically true (every class trivially satisfies "zero or more of X").

**Fix:** Use `--skip-vacuous-min-zero-cardinality-axioms` to suppress these.

#### 3.3.3 Use metadata profile appropriate for the context

**Current:** Default `linkml` profile.

**Options:**
- `--metadata-profile rdfs` — uses `rdfs:comment` instead of `skos:definition`,
  which is more conventional for standalone OWL ontologies.
- `--metadata-profile ols` — adds annotations for the Ontology Lookup Service,
  useful if this ontology will be published on an EU ontology portal.

**Recommendation:** Since this is a `data.europa.eu` ontology, `ols` may be the
most appropriate profile for future portal publication.

#### 3.3.4 Updated Makefile target

Consider updating the `generate-owl` target to:

```makefile
$(OWL_SCHEMA_PATH): $(ALL_SCHEMA_SOURCES)
	@poetry run linkml generate owl \
		--ontology-iri-suffix "" \
		--consolidate-cardinality-axioms \
		--skip-vacuous-min-zero-cardinality-axioms \
		$(ERE_SCHEMA_PATH) 2>/dev/null > $(OWL_SCHEMA_PATH)
```

---

### 3.4 MEDIUM: Missing Schema Features

#### 3.4.1 No `slot_uri` for standard properties

**Current:** No slot declares a `slot_uri`.

**Problem:** Properties like `created_at`, `updated_at`, `content_type` are
generic concepts with well-known IRIs in Dublin Core, PROV-O, etc. Without
`slot_uri`, the OWL properties use auto-generated URIs that are unknown to the
wider semantic web.

**Fix:** Where a direct equivalence exists, declare `slot_uri`:

```yaml
slots:
  # In the core schema, if promoted to slots:
  created_at:
    slot_uri: dct:created
    range: datetime
```

**Caveat:** Using `slot_uri` overrides the default URI entirely. If you want to
keep the `ers:` URI and add a mapping, use `exact_mappings` instead.

#### 3.4.2 No `identifier: true` on key fields

**Current:** Fields like `Decision.id`, `UserAction.id`, and
`CanonicalEntityIdentifier.identifier` are marked `required: true` but not
`identifier: true`.

**Problem:** The `identifier` metamodel slot tells LinkML (and downstream
generators) that this field uniquely identifies instances. In OWL, this can
generate `owl:hasKey` axioms (OWL 2 feature), enabling key-based reasoning.

**Fix:**

```yaml
classes:
  Decision:
    attributes:
      id:
        identifier: true
        description: Unique decision identifier
```

**Note:** `identifier: true` implies `required: true`, so the `required` can be
dropped.

#### 3.4.3 No comments or notes on classes/slots

**Current:** Only `description` is used.

**Problem:** The `comments` metamodel slot maps to `rdfs:comment` in OWL (or
`skos:note` depending on profile), providing a separate annotation channel from
the primary definition. The `notes` slot is available for implementation notes.

**Opportunity:** Use `comments` for non-normative guidance and `notes` for
implementation hints:

```yaml
EntityMentionResolutionResponse:
    description: An entity resolution response returned by the ERE.
    comments:
      - Future versions may support batch responses with entityIndex/totalEntities.
    notes:
      - Implementation should validate that candidates list is non-empty.
```

#### 3.4.4 No `deprecated` or `status` annotations

**Current:** No element uses `deprecated`, `status`, or `rank`.

**Opportunity:** If any classes or slots are experimental or may change, marking
them explicitly generates `owl:deprecated true` in OWL:

```yaml
parsed_representation:
    description: JSON representation of the parsed entity data.
    status: testing
```

---

### 3.5 LOW: Advanced OWL Features

#### 3.5.1 Disjointness axioms

**Current:** No `disjoint_with` declarations.

**Problem:** In the current ontology, it is logically possible for an OWL
reasoner to conclude that `ERERequest` and `EREResponse` are the same class, or
that a `Decision` is also a `UserAction`. Adding disjointness closes this gap.

**Candidates:**

```yaml
ERERequest:
    disjoint_with:
      - EREResponse

Decision:
    disjoint_with:
      - UserAction
      - LookupState
      - EntityMention

EntityMentionResolutionRequest:
    disjoint_with:
      - EntityMentionResolutionResponse
      - EREErrorResponse
```

#### 3.5.2 Classification rules

**Current:** Not used.

**Opportunity:** LinkML `classification_rules` can generate OWL equivalent class
axioms based on slot conditions. For example:

```yaml
EREErrorResponse:
    is_a: EREResponse
    classification_rules:
      - is_a: EREResponse
        slot_conditions:
          error_type:
            required: true
```

This is an alternative to `defining_slots` with more expressive power.

#### 3.5.3 Rules for conditional constraints

**Current:** Not used.

**Opportunity:** The schema has implicit conditional constraints that could be
formalised. For example, in `UserAction`: "if `action_type` is `REJECT_ALL`,
then `selected_cluster` must be null". While OWL rules support is limited (SWRL
may be generated in future LinkML versions), declaring them in LinkML is still
valuable for documentation and for other generators (e.g., JSON Schema, SHACL).

```yaml
UserAction:
    rules:
      - preconditions:
          slot_conditions:
            action_type:
              equals_string: REJECT_ALL
        postconditions:
          slot_conditions:
            selected_cluster:
              required: false
```

#### 3.5.4 Structured aliases for multilingual support

**Current:** Not used.

**Opportunity:** Since this is an EU project (`data.europa.eu`), multilingual
labels could be valuable:

```yaml
EntityMention:
    structured_aliases:
      - literal_form: Mention d'entite
        predicate: skos:prefLabel
        in_language: fr
      - literal_form: Entitaetsnennung
        predicate: skos:prefLabel
        in_language: de
```

---

## 4. Limitations of the LinkML OWL Generator

These are inherent limitations that cannot be worked around by improving the
schemas:

| Limitation | Impact | Workaround |
|-----------|--------|------------|
| **No native `abstract` in OWL.** Abstract classes become plain classes. | Instances can be created for abstract types in OWL. | Covering axioms (`owl:equivalentClass` + `owl:unionOf`) partially compensate. |
| **Open-world vs. closed-world mismatch.** LinkML validates closed-world; OWL reasons open-world. | A "valid" LinkML instance may not be "valid" in OWL terms, and vice versa. | Use SHACL shapes (via `linkml generate shacl`) for closed-world validation alongside OWL. |
| **`designates_type` generates non-standard blank nodes.** The type discriminator pattern produces anonymous restrictions that most OWL tools ignore. | The `type` field's polymorphism semantics are lost in OWL. | Acceptable for inspection; use JSON Schema for runtime validation. |
| **No SWRL rule generation (yet).** LinkML rules cannot currently be translated to SWRL. | Conditional constraints (like "REJECT_ALL implies no selected_cluster") cannot be expressed in OWL. | Document rules in LinkML for human readers; enforce in application code. |
| **Enum `meaning` URIs are not fully leveraged.** While `meaning` maps enum values to external ontology terms, the OWL generator's handling varies by version. | External vocabulary alignment for enum values may not appear in OWL. | Use `exact_mappings` on the enum itself as a fallback. |
| **`examples` are ignored.** The `examples` blocks in LinkML schemas are not translated to OWL. | No OWL instance data is generated from examples. | Generate example instances separately using `linkml-data`. |

---

## 5. Recommended Action Plan

### Phase 1: Quick wins (no model changes needed)

1. Update Makefile to use `--ontology-iri-suffix ""`,
   `--consolidate-cardinality-axioms`, and
   `--skip-vacuous-min-zero-cardinality-axioms`.
2. Verify that covering axioms for abstract classes are generated (or add
   manually via post-processing).

### Phase 2: Schema enrichment (low risk)

3. Add `exact_mappings` / `close_mappings` for properties with well-known
   equivalents (`created_at` -> `dct:created`, etc.).
4. Add `implements: [owl:NamedIndividual]` to the `UserActionType` enum.
5. Add `comments` to classes where future plans are mentioned.
6. Add `disjoint_with` between sibling classes.

### Phase 3: Structural improvements (moderate risk)

7. Promote shared attributes (`id`, `source_id`, `candidates`, `created_at`,
   `about_entity_mention`) to schema-level `slots` with `slot_usage` overrides.
8. Add `defining_slots` to concrete message classes.
9. Add `identifier: true` to key fields (`Decision.id`, `UserAction.id`).
10. Clarify whether `EREMessage` should be `mixin: true` or stay as
    `abstract: true`.

### Phase 4: Advanced enrichment (optional)

11. Add `classification_rules` for complex type discrimination.
12. Add `structured_aliases` for multilingual labels.
13. Consider `slot_uri` mappings to Dublin Core, PROV-O for selected properties.
14. Add `rules` for conditional constraints (for documentation value, even
    if not yet OWL-translatable).

---

## 6. Before / After Comparison

### Before (current `ClusterReference`):

```turtle
ers:ClusterReference a owl:Class ;
    rdfs:label "ClusterReference" ;
    rdfs:subClassOf
        [ owl:allValuesFrom xsd:string ; owl:onProperty ers:cluster_id ],
        [ owl:minCardinality 1 ; owl:onProperty ers:cluster_id ],
        [ owl:maxCardinality 1 ; owl:onProperty ers:cluster_id ],
        [ owl:minCardinality 1 ; owl:onProperty ers:confidence_score ],
        [ owl:maxCardinality 1 ; owl:onProperty ers:confidence_score ],
        # ... 8 restrictions total, including min-0 for optional fields
    skos:definition "A reference to a cluster..." .
```

### After (with all improvements applied):

```turtle
ers:ClusterReference a owl:Class ;
    rdfs:label "ClusterReference" ;
    rdfs:subClassOf
        [ owl:cardinality 1 ; owl:onProperty ers:cluster_id ],
        [ owl:allValuesFrom xsd:string ; owl:onProperty ers:cluster_id ],
        [ owl:cardinality 1 ; owl:onProperty ers:confidence_score ],
        [ owl:allValuesFrom [...xsd:float with facets...] ; owl:onProperty ers:confidence_score ],
        [ owl:cardinality 1 ; owl:onProperty ers:similarity_score ],
        [ owl:allValuesFrom [...xsd:float with facets...] ; owl:onProperty ers:similarity_score ] ;
    owl:disjointWith ers:EntityMention, ers:EntityMentionIdentifier ;
    skos:closeMatch <http://www.w3.org/2004/02/skos/core#Concept> ;
    skos:definition "A reference to a cluster..." ;
    rdfs:comment "Used in both request hints and response results." .

ers:confidence_score a owl:DatatypeProperty ;
    rdfs:label "confidence_score" ;
    skos:exactMatch <http://example.org/score-ontology#confidence> ;
    skos:definition "..." .
```

The "after" version is more compact (consolidated cardinality, no vacuous
axioms), richer (disjointness, mappings, comments), and better connected to the
broader semantic web.
