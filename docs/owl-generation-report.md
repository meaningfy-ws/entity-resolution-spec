# OWL Generation Report: ERS/ERE LinkML Schemas

**Date:** 2026-04-01
**Schemas analysed:** `core-schema-v0.1.0.yaml`, `ere-service-schema-v0.1.0.yaml`
**Generator:** `linkml generate owl` (default options)
**Output:** `resources/schemas/ere-service-schema-v0.1.0.owl.ttl`

---

## 1. Executive Summary

The current LinkML schemas use only a small fraction of the OWL generator's
capabilities, and some features are used incorrectly. The generated OWL is
**structurally shallow**: it captures a basic class hierarchy with cardinality
restrictions, but lacks equivalence axioms, disjointness, external vocabulary
mappings, proper enum modelling, and key declarations — all of which the
generator already supports.

Out of **20+ OWL-relevant LinkML features**, the schemas exercise roughly **4**
(class hierarchy, cardinality, range restrictions, descriptions). Several
constructs are arguably misused (enum-as-classes, abstract-vs-mixin confusion,
attributes-vs-slots). The model can be **considerably improved** without
changing the domain semantics, simply by using LinkML more idiomatically.

This report first assesses the current state, then catalogues the inherent
limitations of the LinkML OWL generator, and finally provides a detailed
action plan with concrete recommendations.

---

## 2. Current State Assessment

### 2.1 What the generator produces today

| Feature | Status |
|---------|--------|
| Class hierarchy (`is_a`) | `rdfs:subClassOf` chain generated |
| Cardinality constraints | Verbose (separate `minCardinality` / `maxCardinality` axioms instead of consolidated `cardinality`) |
| Range constraints | `owl:allValuesFrom` restrictions generated |
| Numeric facets (min/max value) | `xsd:minInclusive` / `xsd:maxInclusive` via `owl:withRestrictions` generated |
| Enum translation | Default strategy: `owl:Class`-based `owl:unionOf` — arguably wrong for value enums (see 5.2.2) |
| Property classification | `owl:ObjectProperty` vs `owl:DatatypeProperty` based on range |
| Descriptions | Mapped to `skos:definition` |
| Abstract classes | Rendered as plain `owl:Class` — no covering axiom, no guard against instantiation |
| Ontology IRI | Auto-generated with `.owl.ttl` file extension baked in |

### 2.2 What the generator CAN produce but we are NOT using

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
This is a direct consequence of using class-level `attributes` instead of
schema-level `slots` — see recommendation 5.3.1.

---

## 3. Limitations of the LinkML OWL Generator

These are inherent limitations of the generator that **cannot** be worked around
by improving the schemas. They should be understood before investing effort in
OWL-oriented schema enrichment, as they bound what is achievable.

### 3.1 No native `abstract` in OWL

OWL has no concept of an abstract class. Classes marked `abstract: true` in
LinkML become regular `owl:Class` in OWL. Nothing prevents an OWL reasoner or
tool from instantiating them. Covering axioms (`owl:equivalentClass` with
`owl:unionOf` over subclasses) can partially compensate, but they only constrain
membership — they do not prevent direct instantiation.

### 3.2 Open-world vs. closed-world mismatch

LinkML validates under closed-world assumptions (if a slot is absent, it is
absent). OWL reasons under open-world assumptions (if a slot is absent, it
might still exist — we just do not know). This fundamental mismatch means:

- A "valid" LinkML instance may not be "valid" in OWL terms, and vice versa.
- Required fields in LinkML become `owl:minCardinality 1`, but an OWL reasoner
  will not flag a missing field as invalid — it will assume the field exists
  somewhere.

**Workaround:** Use SHACL shapes (via `linkml generate shacl`) alongside OWL
for closed-world validation.

### 3.3 `designates_type` generates non-standard blank nodes

The `type` slot with `designates_type: true` produces anonymous restriction
blank nodes at the bottom of the OWL output (using `owl:someValuesFrom`). This
is LinkML's attempt to encode the JSON type discriminator pattern in OWL, but:

- Most OWL tools (Protege, reasoners) ignore these triples.
- The polymorphism semantics of the `type` field are effectively lost in OWL.

**Workaround:** Acceptable for inspection; use JSON Schema for runtime
type-based validation.

### 3.4 No SWRL rule generation

LinkML `rules` (preconditions/postconditions) cannot currently be translated to
SWRL or any other OWL rule language. The documentation mentions SWRL generation
as a future goal. This means conditional constraints (like "if `action_type` is
`REJECT_ALL`, then `selected_cluster` must be null") cannot be expressed in OWL
today.

**Workaround:** Declare rules in LinkML for documentation and for other
generators (JSON Schema, SHACL). Enforce in application code.

### 3.5 Enum `meaning` URIs are inconsistently leveraged

While the `meaning` metamodel slot maps enum values to external ontology terms,
the OWL generator's handling varies by version and by the interaction with
`implements`. External vocabulary alignment for enum values may or may not
appear in the OWL output depending on the combination of options used.

**Workaround:** Use `exact_mappings` on individual enum values as a more
reliable fallback for external alignment.

### 3.6 `examples` are ignored

The `examples` blocks in LinkML schemas are not translated to OWL. No instance
data is generated. This is by design — the OWL generator maps schemas to
ontologies, not data to instances.

**Workaround:** Generate example instances separately using `linkml-data` or
manual RDF authoring.

### 3.7 OWL-DL vs. OWL-Full boundary

LinkML constructs with unrestricted ranges (e.g., the `Any` type) cannot be
expressed as OWL-DL properties, since each property must commit to being either
an `owl:DatatypeProperty` or an `owl:ObjectProperty`. Schemas using `Any` will
produce output in the OWL-Full profile, which most reasoners do not fully
support. Our schemas do not use `Any`, so this is not a current issue, but it
is worth knowing for future schema evolution.

### 3.8 No `rdfs:domain` / `rdfs:range` on global properties

The generator does not emit `rdfs:domain` or `rdfs:range` on properties. All
type constraints are expressed locally via `owl:Restriction` on each class.
This is valid OWL-DL practice (and actually safer for open-world reasoning),
but it means properties are opaque in isolation — you cannot look at
`ers:content` and know it belongs to `EntityMention` without reading the class
restrictions. This is a style choice by the generator, not a bug.

---

## 4. Before / After Comparison

To illustrate what the recommendations in section 5 would achieve, here is
`ClusterReference` as it is today vs. what it could look like:

### Before (current output):

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

### After (with recommendations applied):

```turtle
ers:ClusterReference a owl:Class ;
    rdfs:label "ClusterReference" ;
    rdfs:subClassOf
        [ owl:cardinality 1 ; owl:onProperty ers:cluster_id ],
        [ owl:allValuesFrom xsd:string ; owl:onProperty ers:cluster_id ],
        [ owl:cardinality 1 ; owl:onProperty ers:confidence_score ],
        [ owl:allValuesFrom [...xsd:float with facets...] ;
          owl:onProperty ers:confidence_score ],
        [ owl:cardinality 1 ; owl:onProperty ers:similarity_score ],
        [ owl:allValuesFrom [...xsd:float with facets...] ;
          owl:onProperty ers:similarity_score ] ;
    owl:disjointWith ers:EntityMention, ers:EntityMentionIdentifier ;
    skos:closeMatch <http://www.w3.org/2004/02/skos/core#Concept> ;
    skos:definition "A reference to a cluster..." ;
    rdfs:comment "Used in both request hints and response results." .

ers:confidence_score a owl:DatatypeProperty ;
    rdfs:label "confidence_score" ;
    skos:exactMatch <http://example.org/score-ontology#confidence> ;
    skos:definition "..." .
```

More compact (consolidated cardinality, no vacuous axioms), richer
(disjointness, mappings, comments), and better connected to external
vocabularies.

---

## 5. Recommended Action Plan

### 5.1 Phase 1: Quick wins (no model changes needed)

These are purely CLI flag changes in the Makefile.

#### 5.1.1 Fix ontology IRI

**Current:** `<https://data.europa.eu/ers/schema/ere.owl.ttl>`

**Problem:** The `.owl.ttl` suffix is a serialisation artefact, not a semantic
identifier. It will cause confusion when referencing the ontology from other
systems and violates common practice for persistent ontology IRIs.

**Fix:** Pass `--ontology-iri-suffix ""` to the generator.

#### 5.1.2 Consolidate cardinality axioms

**Current:** Each required single-valued slot generates three separate
restrictions: `owl:minCardinality 1`, `owl:maxCardinality 1`, and
`owl:allValuesFrom`. For `Decision` alone, this produces 17 restrictions.

**Fix:** Use `--consolidate-cardinality-axioms` to emit a single
`owl:cardinality 1` when min equals max.

#### 5.1.3 Remove vacuous axioms

**Current:** Optional slots generate `owl:minCardinality 0`, which is
tautologically true (every class trivially satisfies "zero or more of X").

**Fix:** Use `--skip-vacuous-min-zero-cardinality-axioms` to suppress these.

#### 5.1.4 Consider metadata profile

**Current:** Default `linkml` profile.

**Options:**
- `--metadata-profile rdfs` — uses `rdfs:comment` instead of `skos:definition`,
  which is more conventional for standalone OWL ontologies.
- `--metadata-profile ols` — adds annotations for the Ontology Lookup Service,
  useful if this ontology will be published on an EU ontology portal.

Since this is a `data.europa.eu` schema, `ols` may be the most appropriate
profile for future portal publication.

#### 5.1.5 Updated Makefile target

```makefile
$(OWL_SCHEMA_PATH): $(ALL_SCHEMA_SOURCES)
	@poetry run linkml generate owl \
		--ontology-iri-suffix "" \
		--consolidate-cardinality-axioms \
		--skip-vacuous-min-zero-cardinality-axioms \
		$(ERE_SCHEMA_PATH) 2>/dev/null > $(OWL_SCHEMA_PATH)
```

---

### 5.2 Phase 2: Schema enrichment (low risk)

These changes add information to the schemas without altering structure.

#### 5.2.1 Add external ontology mappings

**Current:** Zero `exact_mappings`, `close_mappings`, `broad_mappings`,
`narrow_mappings`, or `related_mappings` are declared. The OWL output is a
self-contained island with no links to the broader semantic web.

For an EU `data.europa.eu` ontology, this is a significant gap. Relevant
external vocabularies exist:

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

**Fix:** Add the necessary prefixes and mappings:

```yaml
prefixes:
  dct: http://purl.org/dc/terms/
  prov: http://www.w3.org/ns/prov#
  adms: http://www.w3.org/ns/adms#

# In the schema where these attributes/slots are defined:
  created_at:
    exact_mappings:
      - dct:created
  updated_at:
    exact_mappings:
      - dct:modified
```

These generate `skos:exactMatch`, `skos:closeMatch`, etc. in the OWL output.

#### 5.2.2 Fix enum modelling — values should be individuals, not classes

**Current:** `UserActionType` enum values (`ACCEPT_TOP`, `ACCEPT_ALTERNATIVE`,
`REJECT_ALL`) are rendered as OWL classes via `owl:unionOf` over subclasses.

**Problem:** This is arguably wrong. These are discrete values, not types.
Modelling `ACCEPT_TOP` as a class means it represents a *category of things*,
not a single thing. In instance data, writing
`myAction ere:action_type ere:ACCEPT_TOP` asserts that the action type is a
*class*, which is OWL punning and can confuse reasoners.

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
classes — the standard OWL modelling for a closed set of values.

#### 5.2.3 Add disjointness between sibling classes

**Current:** No `disjoint_with` declarations anywhere.

**Problem:** Without disjointness, an OWL reasoner cannot rule out that
`ERERequest` and `EREResponse` are the same class, or that a `Decision` is
simultaneously a `UserAction`. In an open-world model, this is a real gap.

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

#### 5.2.4 Add comments and notes

**Current:** Only `description` is used across all elements.

**Opportunity:** The `comments` metamodel slot maps to `rdfs:comment` (or
`skos:note` depending on profile), providing a separate annotation channel.
Several classes have future-facing remarks embedded in their description
(e.g., batch support plans in `EntityMentionResolutionResponse`) that would
be better placed as `comments`:

```yaml
EntityMentionResolutionResponse:
    description: An entity resolution response returned by the ERE.
    comments:
      - Future versions may support batch responses with entityIndex/totalEntities.
    notes:
      - Implementation should validate that candidates list is non-empty.
```

#### 5.2.5 Add `deprecated` or `status` where applicable

If any classes or slots are experimental or may change, marking them generates
`owl:deprecated true` in OWL:

```yaml
parsed_representation:
    description: JSON representation of the parsed entity data.
    status: testing
```

---

### 5.3 Phase 3: Structural improvements (moderate risk)

These changes alter the schema structure and may affect other generators
(Pydantic, JSON Schema). They should be tested carefully.

#### 5.3.1 Promote shared attributes to schema-level slots

**Current:** All properties are declared as class-level `attributes`.

**Problem:** When the same attribute name (e.g., `id`, `source_id`, `candidates`,
`created_at`) appears in multiple classes, the OWL generator must merge them
into a single global property. This causes:
- "Ambiguous attribute" warnings (see section 2.3).
- Loss of class-scoping: in OWL, `ers:id` is one property shared by `Decision`
  and `UserAction` with no distinction.
- If the ranges ever diverge across classes, the OWL becomes inconsistent.

**Fix (option A — preferred):** Promote shared attributes to schema-level `slots`
with `slot_usage` to specialise per class:

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

**Fix (option B — if class-scoping is essential):** Use distinct names:
`decision_id`, `user_action_id`, `lookup_source_id`, etc.

#### 5.3.2 Add `defining_slots` for OWL equivalence axioms

**Current:** No class uses `defining_slots`.

**Why it matters:** `defining_slots` is the LinkML mechanism for generating
`owl:equivalentClass` axioms — the most powerful OWL construct for automated
classification. For example, `EntityMentionResolutionRequest` *is* an
`ERERequest` *that has* an `entity_mention`:

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

This generates:

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

**Candidates:**

| Class | Defining slots | Rationale |
|-------|---------------|-----------|
| `EntityMentionResolutionRequest` | `entity_mention` | A request *with* an entity mention |
| `EntityMentionResolutionResponse` | `entity_mention_id`, `candidates` | A response *with* mention ID and candidates |
| `EREErrorResponse` | `error_type` | A response *with* an error type |

#### 5.3.3 Add `identifier: true` on key fields

**Current:** Fields like `Decision.id`, `UserAction.id`, and
`CanonicalEntityIdentifier.identifier` are marked `required: true` but not
`identifier: true`.

**Why it matters:** The `identifier` metamodel slot tells LinkML (and downstream
generators) that this field uniquely identifies instances. In OWL, this can
generate `owl:hasKey` axioms (OWL 2 feature), enabling key-based reasoning.

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

#### 5.3.4 Clarify `EREMessage`: mixin or abstract base class?

**Current:** `EREMessage` is declared `abstract: true` and uses `is_a` for the
subclass chain. The description says "This is modelled as a mixin in LinkML" —
but the schema actually uses `abstract: true` on a regular class, not the
`mixin: true` metamodel slot.

**Problem:** This is an inconsistency between the documentation comment and the
actual schema. The choice matters for OWL:

- If `EREMessage` is an **abstract base class**: the current `is_a` approach is
  correct. The generator can produce covering axioms.
- If `EREMessage` is a **mixin** (providing shared attributes like an
  interface): it should use `mixin: true` and consumers should use `mixins:`.
  With `--mixins-as-expressions`, the generator produces General Class Inclusion
  (GCI) axioms instead of `rdfs:subClassOf`.

```yaml
# If mixin is the intent:
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
```

**Recommendation:** Clarify the design intent and pick one consistently.

#### 5.3.5 Stabilise URIs with explicit `class_uri` / `slot_uri`

**Current:** No class or slot declares an explicit `class_uri` or `slot_uri`.
All URIs are auto-generated from `default_prefix + name`.

**Problem:** Renaming a class or slot in LinkML silently changes its OWL URI —
a breaking change for anyone consuming the ontology.

**Fix:** Add explicit URIs where stability matters:

```yaml
classes:
  EntityMention:
    class_uri: ers:EntityMention
```

**Caveat:** `slot_uri` overrides the default URI entirely. If you want to keep
the `ers:` URI and merely *link* to an external term, use `exact_mappings`
instead.

#### 5.3.6 Declare `tree_root`

**Current:** No class is marked `tree_root: true`.

While `tree_root` primarily affects JSON Schema and data validation, it
documents which class is the intended top-level serialisation entry point.
`EREMessage` (or its concrete subclasses) would be natural roots.

---

### 5.4 Phase 4: Advanced enrichment (optional)

These are lower-priority improvements that push the OWL output further but
have limited immediate practical impact.

#### 5.4.1 Classification rules

LinkML `classification_rules` can generate `owl:equivalentClass` axioms based
on slot conditions, offering more expressive power than `defining_slots`:

```yaml
EREErrorResponse:
    is_a: EREResponse
    classification_rules:
      - is_a: EREResponse
        slot_conditions:
          error_type:
            required: true
```

#### 5.4.2 Rules for conditional constraints

The schema has implicit conditional constraints that could be formalised. For
example, in `UserAction`: "if `action_type` is `REJECT_ALL`, then
`selected_cluster` must be null". While OWL translation is limited today
(see limitation 3.4), declaring rules in LinkML is still valuable for
documentation and for other generators (JSON Schema, SHACL):

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

#### 5.4.3 Structured aliases for multilingual support

Since this is an EU project (`data.europa.eu`), multilingual labels could be
valuable. These generate `skos:prefLabel` with language tags in OWL:

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

#### 5.4.4 `slot_uri` mappings to standard vocabularies

For properties that are direct equivalents of well-known terms, `slot_uri`
replaces the auto-generated URI entirely:

```yaml
slots:
  created_at:
    slot_uri: dct:created
    range: datetime
```

This is stronger than `exact_mappings` (which adds a link but keeps the
original URI). Use with care — it changes the property's identity.
