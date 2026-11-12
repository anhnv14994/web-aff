# Product Knowledge Contract v1

> DRI: A Long — Product Expert  
> Issue: https://github.com/anhnv14994/web-aff/issues/14  
> Status: Design contract / schema-neutral reference; not production implementation  
> Version: 1.0

## 1. Purpose and boundaries

This contract defines the minimum portable representation of product knowledge for A+'s Product Expert and Decision Engine. It separates (1) what a product is, (2) what is asserted about it, (3) why the assertion may be trusted, and (4) how a decision criterion evaluates it.

The core is category-neutral. Monitor, headphone, laptop or air-purifier specifics belong in declarative adapter metadata, not in core engine branches.

Out of scope: MVP/category selection; real-product expansion; retailer price, stock, warranty or affiliate offers; user psychology/preferences; production code, database choice or deployment.

**Authority:** Product Expert owns identity, technical semantics, evidence interpretation and evaluation criteria. Decision Science owns elicitation and user-stated priorities. Engineering maps this contract to implementation and must not reinterpret specifications. Commission, merchant economics and affiliate status are never product-fit inputs.

## 2. Domain model and relationship map

~~~text
Category (versioned taxonomy)
  └── ProductFamily (optional marketing grouping)
        └── Product (canonical exact model identity)
              ├── Variant (decision-relevant configuration)
              ├── Identifier* (manufacturer / standards / regional IDs)
              └── Fact* (atomic assertion about Product or Variant)
                    └── Evidence* (captured source + method + provenance)
Source* ───────────────────────────────┘

CriterionDefinition* ── evaluates applicable Product/Variant Facts
CategoryAdapter ─────── binds taxonomy + attributes + criteria + validators

RetailOffer (separate bounded context)
  └── seller SKU, price, stock, warranty, merchant, affiliate metadata
      may reference Product and optional Variant, never define identity alone.
~~~

A fact can have multiple supporting, contradicting or superseding evidence records. A source can support many facts. A criterion references fact keys and an explicit evaluation rule.

### 2.1 Product

Product is the canonical manufacturer-defined model identity used for comparison. It is not a family landing page, retailer listing or price/stock offer.

Required fields:
- product_id: immutable internal ID.
- category_id: exactly one active leaf category for v1.
- manufacturer: normalized manufacturer reference.
- manufacturer_model_name: verbatim official model name/code.
- canonical_key: deterministic internal identity key; not a display title.
- identity_status: verified, pending or conflicting.
- schema_version, created_at, updated_at.

Optional: product_family_id, generation, market_region, release_period, discontinued_at, aliases[], notes.

Identity is verified only when an adequate source identifies the exact manufacturer model. A family page can establish family membership but cannot prove a specific configuration. Fuzzy title similarity is not identity evidence.

### 2.2 ProductFamily

Optional marketing grouping. Fields: family_id, category_id, manufacturer, family_name, family_scope, source_refs[].

A family is never a substitute for Product in comparison, ranking or fact inheritance. Family-level claims remain family-scoped and cannot silently populate model facts.

### 2.3 Variant

A Variant is a configuration that changes a decision-relevant property, compatibility, performance, safety, included components or local identity.

Required: variant_id, product_id, variant_key, variant_attributes, identity_status.  
Optional: region, color, hardware_revision, firmware_baseline, bundle, effective_from, effective_to, identifier_refs[].

Create a distinct Product when the manufacturer defines a materially distinct model/generation (for example, a new model code or generation). Create a Variant when the same canonical model has a meaningful configuration difference (region, connector, capacity, panel option, bundle or color-specific part number). Cosmetic color alone may be a variant only if it changes an identifier, availability, included parts or a decision-relevant attribute. Adapter policy declares which dimensions constitute a variant.

No fact/evidence inheritance is allowed across different Product IDs by default. Product-to-Variant inheritance is allowed only when the fact scope explicitly says product_invariant, the adapter declares the attribute invariant, and no variant-specific source contradicts it. A Variant-scoped fact never flows upward to all variants.

### 2.4 Identifier

Identifiers are typed values, not free-form aliases.

Fields: identifier_id, subject_type (product|variant|offer), subject_id, scheme (manufacturer_model, MPN, GTIN, regional_PN, seller_SKU, etc.), value_raw, value_normalized, issuer, region, source_ref, status.

Uniqueness is scoped by issuer + scheme + region where applicable. Seller SKU identifies an Offer, not a canonical Product. GTIN/MPN is strong evidence but must still be checked for packaging, bundle and region ambiguity.

### 2.5 Fact

A Fact is one atomic assertion about a Product or Variant. It is not a bag of unrelated specifications or a prose summary.

Required:
- fact_id: immutable assertion ID.
- subject_type, subject_id: Product or Variant.
- attribute_key: key declared by the category adapter.
- value_raw: exact source wording/value when available.
- value_normalized: typed normalized value, nullable if unsafe to normalize.
- data_type, unit: from attribute definition; unit null for unitless values.
- scope: explicit scope object.
- evidence_refs[]: one or more Evidence IDs, or empty only while pending.
- status, confidence, observed_at, recorded_at.

Optional: method, conditions, valid_from, valid_until, supersedes_fact_id, reviewer, notes.

Facts are append-only assertions. Corrections create a new assertion and link the superseded one; do not silently overwrite a previously published value. Preserve raw source text when normalization changes notation, units or terminology.

Scope object supports:
- level: family, product, variant, region, port, mode, condition or offer.
- region: explicit market/region or null.
- port_or_interface: exact port/interface or null.
- mode: e.g. native/overclocked, ANC on/off, wired/wireless.
- conditions: structured conditions such as resolution, bit depth, host OS, volume, test distance or firmware.
- applies_to_variant_ids[]: explicit allowlist when applicable.

Never use vague scope such as “model family” where port, region, mode or configuration changes the value.

### 2.6 Evidence and Source

Source describes the publisher/document endpoint. Evidence is a captured, attributable item from that source that supports, limits or contradicts a Fact.

Source fields: source_id, publisher, source_type, canonical_url, document_title, region, terms_status, trust_class.

Evidence fields: evidence_id, source_id, source_locator (page/section/table/test ID), captured_excerpt_or_value, captured_at, source_published_at (if known), source_version_or_snapshot_hash, subject_match, methodology, reviewer, status, confidence, limitations.

Evidence must be field-level or clearly linked to a bounded set of claims. A broad product-family URL is not sufficient to support every specification. Independent test evidence must identify exact model/sample and test conditions. Reviews for a sibling model, different generation or different port/variant are related context only, not evidence for the target fact.

## 3. CriterionDefinition contract

A criterion describes how a decision-relevant product property is interpreted. It is metadata, not a user preference and not a product fact.

| Field | Meaning |
|---|---|
| criterion_key | Stable namespaced key, e.g. display.native_refresh_hz |
| label | Human-readable neutral name |
| definition | Precise meaning and what it excludes |
| value_type / unit | Typed value and unit dimension |
| applicability | Category/segment/variant predicate |
| fact_keys | Fact attributes used |
| role | hard or soft; never inferred from product data |
| operator | eq, neq, gt, gte, lt, lte, in, contains, range, boolean, enum_match, custom_versioned |
| direction | higher_better, lower_better, target_range, categorical, boolean, not_ranked |
| normalization | Unit conversion, scale, enum mapping and rounding policy |
| evidence_requirement | Minimum acceptable evidence class/status |
| missing_data_behavior | unknown, verification_required or approved not_applicable |
| definition_version | Immutable semantic version |
| owner | Product Expert / approving authority |

Optional: default_threshold, threshold_by_use_case, weight (soft only), comparability_group, display_precision, explanation_template, valid_from, valid_until, adapter_extensions.

### 3.1 Hard and soft semantics

- **Hard criterion:** a customer-confirmed must-have or explicitly approved policy constraint. It is evaluated PASS / FAIL / UNKNOWN. Product Expert defines technical meaning; Decision Science/customer input establishes whether it is a user constraint. Never promote a soft preference to hard without explicit confirmation.
- **Soft criterion:** a preference used to explain trade-offs or calculate fit after hard eligibility. Weight and fit mapping are versioned policy inputs, not intrinsic product facts.
- **UNKNOWN:** missing, stale, conflicting, insufficiently scoped or below evidence requirement. It is neither FAIL nor PASS.
- **NOT_APPLICABLE:** allowed only when adapter applicability says the criterion genuinely does not apply. It is not missing data.
- **Direction:** “higher is better” is not universal. Brightness may have a target range; latency may be lower-is-better; codecs may be categorical and host-dependent.

### 3.2 Evaluation output and gates

For each candidate/criterion emit: criterion_key, definition_version, applicability_result, evaluation_status (pass|fail|unknown|not_applicable), observed_value, threshold_or_rule, fact_refs[], evidence_refs[], reason_code and explanation.

Hard gate:
- Any hard FAIL → candidate excluded.
- Any hard UNKNOWN → candidate verification_required, not eligible for a definitive ranked list.
- Hard-eligible only when every applicable hard criterion is PASS.
- If no hard criteria are configured, do not invent a hard gate; record that evaluation ran without hard constraints.

Soft scoring is defined by a versioned policy. Unknown soft values are excluded from the known-value numerator and reduce evidence coverage; never convert them to zero or best-in-class. Fit score and evidence coverage are separate. Score is not a probability or quality certification.

## 4. Evidence status lifecycle and usage policy

Evidence status and criterion evaluation status are distinct. These evidence states are mutually exclusive for one Evidence record:

| Evidence status | Meaning | Permitted use |
|---|---|---|
| verified_identity | Source confirms exact Product/Variant identity or identifier mapping | Identity gate only; does not prove every specification |
| manufacturer_claimed | Manufacturer publishes claim for scoped Product/Variant | Attribute as manufacturer-stated; not independent performance |
| independent_tested | Competent independent source tested exact model/sample under documented method | Only within sample, method, conditions and scope |
| pending | Not sufficiently checked or attached | No positive claim; keep null/unknown |
| conflicting | Credible evidence disagrees or scope cannot be reconciled | Preserve assertions; quarantine affected decision field |
| stale | Evidence may no longer represent current hardware/software/offer state | Historical use only with date until refreshed |
| not_disclosed | Source does not publish field after reasonable documented check | Keep unknown; do not infer from sibling products |
| not_applicable | Field structurally inapplicable under adapter rule | Exclude from completeness denominator only when explicitly authorized |

Confidence (high|medium|low) is orthogonal to status. High confidence in a manufacturer claim does not convert it to independent_tested. Confidence describes strength of source-to-claim mapping; status describes evidence class/lifecycle.

### 4.1 Lifecycle transitions

- pending → verified_identity: exact subject identity confirmed by adequate source.
- pending → manufacturer_claimed or independent_tested: claim and scope captured and reviewed.
- Any active state → conflicting: credible incompatible evidence appears; preserve both.
- Time-sensitive evidence → stale: validity expires, firmware/revision changes, source changes materially or refresh policy triggers.
- conflicting → manufacturer_claimed/independent_tested: only after reviewer resolves scope/method and records disposition; retain conflict history.
- not_disclosed: only after documented source search; may return to pending if a new source appears.
- not_applicable: only by adapter rule, never because data is missing.

No transition erases previous state, captured source or reviewer decision. A status change creates an audit event.

### 4.2 Evidence precedence and inheritance

There is no universal “newest source wins” rule. Prefer exact identity + exact scope + transparent method over broad or indirect sources. Manufacturer source is authoritative for what manufacturer claims; independent testing is authoritative only for the tested sample and method. If they disagree, retain both as distinct claim types.

Never:
- relabel manufacturer marketing as independently measured;
- inherit independent tests across generation/model/variant without explicit compatibility evidence;
- infer port capability from connector shape;
- infer battery/runtime/codec/ANC performance from sibling model;
- turn missing value into zero, false, minimum or family default;
- use retailer copy as sole proof of critical technical fields.

## 5. Category Adapter contract

A CategoryAdapter is a declarative, versioned package extending the shared core. The engine consumes adapter metadata and generic operators; it does not branch on category names.

Required adapter metadata:
- adapter_id, adapter_version, category_key.
- taxonomy: allowed subcategories and family relations.
- identity_policy: Product-vs-Variant dimensions, required identifiers, region rules.
- attribute_definitions[]: typed keys, units, enums, validation ranges and scope rules.
- criterion_definitions[]: CriterionDefinition set and version references.
- applicability_rules[]: when an attribute/criterion applies.
- normalizers[]: deterministic unit/enum conversions.
- validators[]: declarative constraints and cross-field invariants.
- evidence_policy: required evidence classes by attribute/criterion.
- freshness_policy: TTL/recheck triggers by fact class.
- fixture_set_version: synthetic fixtures and expected outcomes.

Optional extension points: adapter-owned enums, conditional fields, custom validation expressions from an allowlisted operator set, explanation vocabulary and display grouping. No arbitrary executable code or unreviewed scripts in adapter config.

Adapter rules:
1. Adapter may add attributes/criteria but cannot weaken core identity, provenance, unknown or evidence invariants.
2. Shared field names retain shared semantics; category-specific meaning gets a new namespaced key.
3. Unit conversions preserve raw values and identify conversion version.
4. Cross-field rules declare required inputs and return UNKNOWN if inputs are missing.
5. Adapter version is pinned to every evaluation; semantic changes create a new version.
6. Category cannot publish until adapter fixtures and QA pass.
7. Adapter cannot introduce commission, merchant ranking or psychological inference into product fit.

Illustrative monitor keys: display.native_refresh_hz, display.overclock_refresh_hz, motion.response_gtg_ms, motion.response_mprt_ms, connectivity.max_refresh_by_port, connectivity.usb_c_pd_w. These are separate attributes with different scope/method requirements.

Illustrative headphone keys: audio.codec_support, audio.anc_mode, audio.runtime_anc_on_h, audio.runtime_anc_off_h, calls.microphone_configuration, wireless.host_compatibility. Runtime retains volume, codec, firmware and ANC state; codec support alone does not prove host compatibility.

The core does not contain category-specific branches. It validates types, scope, provenance, evidence and generic criterion operators.

## 6. Synthetic fixtures (illustrative; no real product claims)

These fixtures test schema shape and edge behavior only. IDs, manufacturer names and values are synthetic.

### Fixture A — Monitor with port/mode-scoped facts

~~~json
{
  "fixture_id": "SYN-MON-001",
  "category_key": "display.monitor",
  "adapter_version": "0.1.0",
  "product": {
    "product_id": "SYN-PROD-MON-A",
    "manufacturer": "Example Display Co.",
    "manufacturer_model_name": "EXAMPLE-Q27",
    "identity_status": "verified"
  },
  "variants": [
    {"variant_id": "SYN-VAR-MON-A-R1", "product_id": "SYN-PROD-MON-A",
     "variant_key": "region-1", "variant_attributes": {"region": "R1", "panel_revision": "rev-a"}}
  ],
  "facts": [
    {"fact_id": "SYN-F01", "subject_type": "product", "subject_id": "SYN-PROD-MON-A",
     "attribute_key": "display.native_refresh_hz", "value_raw": "165 Hz native",
     "value_normalized": 165, "unit": "Hz", "scope": {"level": "product", "mode": "native"},
     "status": "manufacturer_claimed", "evidence_refs": ["SYN-E01"]},
    {"fact_id": "SYN-F02", "subject_type": "variant", "subject_id": "SYN-VAR-MON-A-R1",
     "attribute_key": "connectivity.max_refresh_hz", "value_raw": "144 Hz via HDMI",
     "value_normalized": 144, "unit": "Hz",
     "scope": {"level": "port", "region": "R1", "port_or_interface": "HDMI", "conditions": {"resolution": "QHD"}},
     "status": "manufacturer_claimed", "evidence_refs": ["SYN-E02"]}
  ],
  "evidence": [
    {"evidence_id": "SYN-E01", "source_id": "SYN-SRC-01", "status": "manufacturer_claimed",
     "source_locator": "Synthetic spec table / display mode"},
    {"evidence_id": "SYN-E02", "source_id": "SYN-SRC-01", "status": "manufacturer_claimed",
     "source_locator": "Synthetic timing table / HDMI"}
  ]
}
~~~

Expected: a request for HDMI refresh uses F02, not native refresh F01; DisplayPort remains UNKNOWN unless separately asserted. Product-level native refresh does not imply every port supports it.

### Fixture B — Headphone with host/mode-dependent facts

~~~json
{
  "fixture_id": "SYN-AUD-001",
  "category_key": "audio.headphone",
  "adapter_version": "0.1.0",
  "product": {
    "product_id": "SYN-PROD-AUD-A",
    "manufacturer": "Example Audio Co.",
    "manufacturer_model_name": "EXAMPLE-OVER-EAR",
    "identity_status": "verified"
  },
  "facts": [
    {"fact_id": "SYN-F11", "subject_type": "product", "subject_id": "SYN-PROD-AUD-A",
     "attribute_key": "audio.codec_support", "value_raw": "Codec-X supported",
     "value_normalized": ["CODEC_X"], "unit": null,
     "scope": {"level": "condition", "conditions": {"connection": "Bluetooth"}},
     "status": "manufacturer_claimed", "evidence_refs": ["SYN-E11"]},
    {"fact_id": "SYN-F12", "subject_type": "product", "subject_id": "SYN-PROD-AUD-A",
     "attribute_key": "audio.runtime_h", "value_raw": "up to 30 hours",
     "value_normalized": 30, "unit": "h",
     "scope": {"level": "mode", "mode": "ANC_off", "conditions": {"volume": "synthetic 50%", "codec": "CODEC_X"}},
     "status": "manufacturer_claimed", "evidence_refs": ["SYN-E12"]}
  ],
  "evidence": [
    {"evidence_id": "SYN-E11", "source_id": "SYN-SRC-11", "status": "manufacturer_claimed"},
    {"evidence_id": "SYN-E12", "source_id": "SYN-SRC-11", "status": "manufacturer_claimed"}
  ]
}
~~~

Expected: codec compatibility with a customer's host is UNKNOWN until host/OS support is checked. The 30-hour claim cannot be reused as ANC-on runtime or independent battery measurement.

## 7. Reusable QA invariants (all categories)

| ID | Invariant | Failure behavior |
|---|---|---|
| PKC-01 | Every Product has one category and stable internal ID; family is not a comparison identity | Reject invalid record |
| PKC-02 | Product identity requires exact-model evidence; family/title similarity is insufficient | Pending/quarantine |
| PKC-03 | Variant belongs to exactly one Product; variant key unique within Product | Reject or identity conflict |
| PKC-04 | Offer/Seller SKU never defines or overwrites canonical Product identity | Reject identity merge |
| PKC-05 | Every Fact has typed attribute, subject, unit and explicit scope | Reject fact |
| PKC-06 | Every decision-usable Fact has Evidence meeting criterion policy | UNKNOWN / verification_required |
| PKC-07 | Evidence source, locator, capture time and source-to-subject match are traceable | Hold publication |
| PKC-08 | Manufacturer claim never becomes independent_tested by confidence or repetition | Reject status escalation |
| PKC-09 | Conflicting evidence is preserved; no silent winner selection | Mark conflicting; block affected field |
| PKC-10 | Pending, stale, not_disclosed and missing never satisfy hard criteria | UNKNOWN / verification_required |
| PKC-11 | not_applicable is emitted only by adapter applicability rule | Reject or UNKNOWN |
| PKC-12 | Facts/tests do not inherit across different Products or incompatible Variants | Reject inheritance |
| PKC-13 | Scoped facts cannot be generalized across region, port, mode, host, firmware or test conditions | UNKNOWN outside scope |
| PKC-14 | Normalization preserves raw value, unit and normalizer version | Reject lossy conversion |
| PKC-15 | Criterion, adapter and evaluation policy are version-pinned and replayable | Reject unversioned evaluation |
| PKC-16 | Hard FAIL excludes; hard UNKNOWN requires verification; only all applicable PASS is eligible | Reject invalid eligibility |
| PKC-17 | Soft UNKNOWN is not zero or best; fit and evidence coverage remain separate | Reject invalid score |
| PKC-18 | Changing merchant, price or commission cannot change product-fit output | Determinism regression failure |
| PKC-19 | Identical facts, profile, adapter and rule versions produce deterministic evaluation | Replay mismatch failure |
| PKC-20 | Retail Offer freshness is separate from canonical Product fact freshness | Reject status leakage |
| PKC-21 | Superseded Fact remains auditable and cannot silently reappear as current | Hold / audit failure |
| PKC-22 | Every published explanation traces criterion → fact → evidence → source | Block publication |

Core tests cover identity, typed facts, provenance, evidence states, unknown handling, hard/soft semantics, versioning, deterministic evaluation and commercial independence.

Adapter tests cover category-specific identity dimensions, valid units/ranges, conditional fields, applicability, cross-field consistency, measurement conditions and misleading-claim traps. Every new adapter must prove compliance with all core invariants.

### Release gates

- **P0 block:** identity conflict; missing critical provenance; hard UNKNOWN shown as PASS; cross-model test inheritance; conflict silently resolved; invalid unit/scope; commission affects fit.
- **P1 hold:** stale evidence; incomplete soft criteria; unreviewed adapter version; unresolved non-critical attribute.
- **Allow with disclosure:** missing soft field when policy permits and evidence coverage/unknowns are shown.
- **Never silently default:** absent fact, source, unit, region, mode, test condition or retail offer.

## 8. Mapping to Engineering / Technical Blueprint

| Product contract concept | Suggested technical mapping |
|---|---|
| Category / ProductFamily / Product / Variant | Catalog domain records with stable IDs and foreign keys |
| Identifier | Typed identifier record with scoped uniqueness |
| AttributeDefinition / CriterionDefinition | Versioned schema/config registry owned by Product Expert |
| Fact | Append-only assertion record; typed normalized value + raw payload reference |
| Evidence / Source | Evidence and source registry; snapshots/locators and access metadata |
| Evaluation result | Decision candidate criterion result with fact/evidence refs and rule version |
| CategoryAdapter | Declarative config package; pinned adapter version |
| RetailOffer | Separate Offer module/context; references canonical Product/Variant |

Engineering may choose relational tables, JSON columns or another representation, but must preserve semantics, cardinality, versioning and invariants. This contract does not mandate a database or implementation language.

Alignment with Technical Blueprint: canonical Product/Variant remains separate from Offer; evidence is first-class; hard UNKNOWN fails closed; ambiguous identity is reviewed rather than auto-merged; commission remains outside fit; evaluation is versioned and replayable. This contract adds explicit ProductFamily, Identifier, Fact scope, evidence lifecycle and CategoryAdapter semantics.

## 9. Ownership and change control

- **A Long / Product Expert:** approves taxonomy, identity rules, attribute semantics, evidence requirements, criterion definitions and adapter QA.
- **Vân Anh / Decision Science:** confirms hard-vs-soft user constraint semantics, elicitation boundary and unknown/skip behavior; does not validate technical facts.
- **Hoàng / Engineering:** reviews schema mapping, type safety, persistence, versioning and testability; does not invent product thresholds or reinterpret measurements.
- **CEO:** approves scope, category rollout and business policy.

Changes to a field's meaning, unit dimension, identity policy, criterion operator, evidence minimum or missing-data behavior are breaking semantic changes and require a version increment plus fixture/test review. Editorial label changes may be patch-level if meaning is unchanged.

## 10. Open decisions / review requests

1. **Vân Anh:** confirm that a hard criterion is only a customer-confirmed must-have or explicitly approved policy constraint; soft preferences remain trade-offs, and UNKNOWN is not a negative preference.
2. **Hoàng:** review whether Product/Variant/Identifier/Fact/Evidence and adapter versioning map cleanly to the Technical Blueprint without losing scope or provenance.
3. **CEO:** accept the v1 domain boundaries and approve whether future category adapters should be separate versioned files/packages.

No real model values, retail SKUs, thresholds, category MVP choice or production schema are introduced here.

## Appendix A — Minimal field dictionary

| Object | Minimum required fields |
|---|---|
| Category | category_id, slug, parent_id, taxonomy_version |
| ProductFamily | family_id, category_id, manufacturer, family_name |
| Product | product_id, category_id, manufacturer, manufacturer_model_name, canonical_key, identity_status, schema_version |
| Variant | variant_id, product_id, variant_key, variant_attributes, identity_status |
| Identifier | identifier_id, subject_type, subject_id, scheme, value_raw, issuer, region, status |
| AttributeDefinition | attribute_key, label, definition, data_type, unit_dimension, allowed_scope, validation, definition_version |
| CriterionDefinition | criterion_key, definition, value_type, unit, applicability, fact_keys, role, operator, direction, normalization, evidence_requirement, missing_data_behavior, definition_version, owner |
| Fact | fact_id, subject_type, subject_id, attribute_key, value_raw, value_normalized, data_type, unit, scope, evidence_refs, status, confidence, observed_at, recorded_at |
| Source | source_id, publisher, source_type, canonical_url, region, terms_status, trust_class |
| Evidence | evidence_id, source_id, source_locator, captured_excerpt_or_value, captured_at, source_version_or_snapshot_hash, subject_match, methodology, status, confidence, limitations |
| CategoryAdapter | adapter_id, adapter_version, category_key, taxonomy, identity_policy, attribute_definitions, criterion_definitions, applicability_rules, normalizers, validators, evidence_policy, freshness_policy, fixture_set_version |

## Appendix B — Glossary

- **Claim:** source-originated statement; stored as a Fact assertion only after subject/scope mapping.
- **Evidence:** captured and reviewable support for a claim; URL alone is not the complete evidence record.
- **Fact:** atomic assertion with value, subject, scope, time and evidence.
- **Product:** canonical exact model identity.
- **ProductFamily:** marketing grouping, not comparison identity.
- **Variant:** decision-relevant configuration under one Product.
- **RetailOffer:** seller's time-bound commercial listing, separate from Product knowledge.
- **Unknown:** insufficient evidence to decide; not false, zero or fail.
- **Adapter:** declarative category extension constrained by core invariants.
