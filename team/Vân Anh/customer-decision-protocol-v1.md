# A+ Customer Decision Protocol v1

**DRI:** Vân Anh — Customer Psychology & Decision Science  
**Issue:** [#13 — ENGINE-01](https://github.com/anhnv14994/web-aff/issues/13)  
**Technical reviewer:** Hoàng — Decision Engine / schema contract  
**Domain reviewer:** A Long — product truth and category-specific criteria where needed  
**Version:** 1.0  
**Status:** Behavioral specification for technical review; not production-validated

> This protocol defines category-independent conversation semantics. It does not define product facts, product ranking formulas, numeric weights, commercial priorities, or a chatbot script. Its purpose is to help a person make a better-informed decision with the fewest necessary questions, including the valid decision not to buy.

## 1. Design principles and scope

1. **Decision support, not sales conversion.** The system helps clarify goals, constraints, trade-offs and evidence. A purchase is not the required outcome.
2. **Ask only when useful.** A question is justified only when its answer can change a decision, resolve a material blocker, or determine the next verification step.
3. **Preserve epistemic status.** User statements, observations, system-verified facts, inferences and unknowns remain distinguishable.
4. **Fail closed on hard requirements.** A verified hard-constraint failure excludes a candidate. An unknown hard check is not a pass.
5. **Do not harden preferences.** A soft preference remains tradeable unless the user explicitly promotes it to a requirement.
6. **Respect revision and autonomy.** Users may correct themselves, skip, defer, stop, or decide not to buy. Keep an audit trail without arguing or pressuring.
7. **Separate conversation from product truth.** User intent is not evidence of product capability. Product claims require trusted, current, variant-specific evidence.
8. **Category is configuration.** The core protocol knows generic field types and behavior, not monitor/audio/laptop-specific rules.
9. **No commercial influence.** Affiliate commission, payout, EPC, merchant relationship or inventory incentives must not affect question selection, eligibility, fit, explanation or ordering.
10. **No sensitive inference.** Do not infer protected or sensitive traits, personality, health status or financial vulnerability. Ask only for task-relevant context.

### Out of scope

- Selecting the MVP category or product candidates.
- Product specifications, price, availability, technical compatibility or product truth.
- Numeric preference weights, scoring formulas, ranking formulas or thresholds.
- Sales persuasion, urgency, conversion optimization or affiliate optimization.
- Technical implementation details beyond a representation-neutral behavioral contract.

## 2. Canonical state model

A decision session contains a **current decision profile**, a **session orchestration state**, and an **append-only event history**. These are logical partitions; they need not be three physical databases.

### 2.1 Current decision profile

| State group | Required meaning | Example | Provenance / rule |
|---|---|---|---|
| `user_goal` | What the person is trying to achieve | “Work comfortably across documents” | User-stated; do not substitute a product category |
| `use_case` | Task, environment and usage pattern | “Spreadsheets and programming” | User-stated or pending inference |
| `desired_outcomes[]` | Outcomes the person values | “Less eye strain”, “clear calls” | Preserve original meaning; normalize wording only |
| `hard_constraints[]` | Non-negotiable conditions | Must fit a measured space | Explicitly confirmed as mandatory; never inferred solely from emphasis |
| `soft_preferences[]` | Desirable, tradeable qualities | Quiet operation, preferred style | May be unknown or not important |
| `priority_order[]` | User's relative ordering when trade-offs arise | “Mic first, comfort second” | Ordinal user expression; no numeric conversion in this protocol |
| `context[]` | Relevant situation or environment | Device, room, duration, setup | Collect only if decision-relevant |
| `risk_blockers[]` | Concerns preventing confident decision | Compatibility, fit, reliability | Distinguish user concern from verified risk |
| `unknowns[]` | Missing, skipped, unanswerable or unverified values | Host model unknown | Unknown is a first-class state, not false/zero |
| `inferences[]` | Tentative interpretation needing confirmation | “Mượt” may mean motion smoothness | Must include rationale and confirmation status |
| `evidence_needs[]` | Facts needed to validate a criterion | Verified port support for exact variant | Product/domain evidence owner supplies facts |
| `unresolved_conflicts[]` | Contradictory or mutually incompatible inputs | Two incompatible budget/feature requirements | Do not silently choose one |
| `asked_question_keys[]` | Questions already asked in this session | `MON-Q3` | Unique keys; prevents accidental repetition |
| `skipped_question_keys[]` | Questions explicitly skipped | `MON-Q2` | Separate from asked/answered state |
| `current_lifecycle` | Current protocol phase | `CLARIFY` | Derived from transition conditions |
| `stop_record` | Terminal or paused outcome, if any | `DEFERRED` | Must include reason and unresolved blockers |

### 2.2 Provenance and value status

Use the following provenance vocabulary consistently:

| Provenance | Meaning | Permitted interpretation |
|---|---|---|
| `user_stated` | Explicitly stated or confirmed by the user | May populate intent/profile; does not prove product facts |
| `observed` | Directly observed interaction or context | Record observation and context; do not overgeneralize |
| `system_verified` | Verified against an authoritative system/source | May support product/domain assertions within its scope and freshness |
| `inferred_pending_confirmation` | Plausible interpretation not confirmed | May guide a clarifying question; must not become a hard constraint |
| `unknown` | Missing, skipped, unavailable, conflicting or not verified | Must remain unknown until resolved |

Confidence (if represented) describes confidence in an interpretation, not truth of an external product claim. Do not use confidence to upgrade an inference to verified fact.

**Three states that must never be conflated:**
- **Unknown:** the system does not know.
- **Not important / not required:** the user explicitly says it does not matter.
- **False / does not meet requirement:** a reliable source establishes the negative fact.

A user saying “I don't know” or “skip” sets unknown, not false and not “not important”.

### 2.3 Constraint and preference semantics

**Hard constraint**
- Must be explicitly designated mandatory by the user or be an applicable non-negotiable safety/legal boundary defined by policy.
- Store the criterion, operator, expected value, source, and whether it is decision-critical.
- Evaluate against candidate-specific evidence only.
- `pass`: evidence supports the criterion for the exact candidate/variant and applicable context.
- `fail`: evidence establishes the criterion is not met.
- `unknown`: absent, stale, ambiguous, conflicting or non-applicable evidence.
- Missing check defaults to `unknown`.
- Any verified hard failure excludes that candidate regardless of soft fit.
- Any unknown hard check means `verification_required`, never eligible.

**Soft preference**
- A desirable attribute that can be traded against other preferences.
- A preference may be unknown, explicitly unimportant, or ordered relative to others.
- Do not convert it to a hard constraint because the user repeats it or expresses enthusiasm.
- The user can promote or demote it; record the revision event.
- Scoring and numeric weighting are outside this protocol.

**Unknown**
- An unknown soft preference may be skipped without blocking progress if it cannot materially change the shortlist.
- An unknown hard criterion remains a verification blocker.
- A skipped non-critical question must not be asked again unless the user reopens it or new information makes it newly material; explain why if reopened.

## 3. Session lifecycle

The canonical lifecycle is:

`DISCOVER → CLARIFY → VERIFY → COMPARE → SUMMARIZE`

Alternative terminal/paused outcomes are `ABSTAIN`, `DEFER`, and `NO_MATCH`. They are outcomes, not ordinary sequential phases. The session can resume from DEFER when the user explicitly returns.

### 3.1 State definitions

| State | Purpose | Entry condition | Exit condition |
|---|---|---|---|
| `DISCOVER` | Understand goal and broad use case | New session or no usable goal/use case | Goal/use case is sufficiently clear to identify relevant criteria → CLARIFY |
| `CLARIFY` | Resolve material ambiguity, constraints and trade-offs | Goal/use case known, profile incomplete | Required intent fields are clear; identify evidence gaps → VERIFY, or no material question remains → VERIFY |
| `VERIFY` | Obtain or request evidence for hard constraints and material risks | Candidate comparison depends on external/product facts or unresolved blocker | Evidence is sufficient for comparison → COMPARE; evidence unavailable/conflicting → ABSTAIN; verified hard mismatch for all candidates → NO_MATCH |
| `COMPARE` | Compare only candidates with evidence status made explicit | Profile and candidate evidence are sufficiently complete for a fair comparison | Present transparent comparison → SUMMARIZE; material evidence gap discovered → VERIFY; no eligible candidate → NO_MATCH |
| `SUMMARIZE` | Present decision-ready synthesis and next steps | Comparison or decision support is ready | Session may end, user may ask follow-up (return to relevant state), defer, or decide no-buy |
| `ABSTAIN` | Withhold a claim/recommendation that cannot be supported | Critical information/evidence is missing, conflicting, stale or outside system competence | Resume only when new evidence/context arrives; otherwise remain unresolved |
| `DEFER` | Respect a user's wish to pause or postpone | User explicitly asks to pause, wait, revisit later or stop for now | Resume only on user's initiative or a separately authorized reminder; never keep asking in-session |
| `NO_MATCH` | State that no evaluated candidate meets all hard requirements | All relevant candidates have at least one verified hard failure, or no candidate is eligible after complete evaluation | Reopen only if user changes a hard requirement, candidate set changes, or new verified evidence arrives |

### 3.2 Transition rules

| From | To | Rule |
|---|---|---|
| DISCOVER | CLARIFY | A usable goal/use case is available; do not require every context field |
| DISCOVER | ABSTAIN | Goal cannot be understood after a reasonable clarification opportunity or request is outside competence |
| DISCOVER / CLARIFY | DEFER | User asks to pause/stop |
| CLARIFY | VERIFY | A hard requirement, material risk or candidate-specific evidence need must be checked |
| CLARIFY | COMPARE | No material unanswered question remains and relevant candidate evidence is already available |
| CLARIFY | ABSTAIN | A decision-critical unknown cannot be resolved and no safe evidence path is available |
| VERIFY | COMPARE | All hard checks for compared candidates have adequate evidence status; unknowns remain visibly marked and do not get called passes |
| VERIFY | ABSTAIN | Evidence is unavailable, conflicting, stale or outside system competence |
| VERIFY | NO_MATCH | Every relevant candidate is ruled out by verified hard failure |
| COMPARE | SUMMARIZE | Comparison is supported and trade-offs can be explained honestly |
| COMPARE | VERIFY | A newly discovered material evidence gap blocks a fair comparison |
| Any active state | DEFER | User explicitly defers or declines to continue |
| Any active state | ABSTAIN | System cannot responsibly support next claim/action |
| Any active state | NO_MATCH | Only when verified hard failures establish no candidate meets requirements |
| SUMMARIZE | CLARIFY / VERIFY / COMPARE | User asks a new question or changes relevant context; resume at the earliest affected phase |
| DEFER | DISCOVER / CLARIFY / VERIFY | User explicitly resumes; restore profile and event history, then reassess freshness |

Do not move to COMPARE merely because a fixed number of questions has been asked. Do not move to SUMMARIZE just to force closure. Lifecycle state describes decision readiness, not conversion progress.

## 4. Next-question policy

### 4.1 Eligibility gate: should the system ask?

Before selecting a question, apply these rules in order:

1. If user requested pause, no-buy or end of conversation, respect it; do not ask a sales-oriented follow-up.
2. If the session is blocked by an unverified hard constraint, ask only if a user answer can resolve the blocker. If only external evidence can resolve it, request/obtain verification rather than interrogating the user.
3. If a question key has already been answered or skipped, do not repeat it unless the user reopens it or new material context justifies re-asking.
4. If the missing field cannot change candidate eligibility, shortlist, meaningful trade-off or next evidence action, do not ask.
5. If there is no useful question, transition to VERIFY, COMPARE, SUMMARIZE or ABSTAIN as appropriate.

### 4.2 Question selection hierarchy

Among eligible questions, select the one with the strongest decision relevance using this qualitative precedence (not a numeric score):

1. **Hard-constraint clarification:** resolves what is mandatory, its exact meaning or an ambiguity that could exclude candidates.
2. **Eligibility/compatibility blocker:** determines whether any candidate can meet a hard condition.
3. **Material risk blocker:** resolves a safety, fit, reliability, setup or other risk that could invalidate the decision.
4. **Use-case discriminator:** distinguishes between materially different use cases and therefore different criteria.
5. **Priority conflict:** helps the user choose between competing soft preferences when the trade-off changes comparison.
6. **Evidence-path question:** identifies a device, environment, test or source needed to verify a claim.
7. **Secondary preference:** improves explanation or ordering but cannot change eligibility or shortlist.

Within the same tier, prefer the question that:
- is answerable by the user without unreasonable effort;
- resolves more than one genuinely related ambiguity without bundling unrelated questions;
- has the clearest expected impact on the next decision step;
- imposes the least cognitive burden;
- has not already been asked or skipped.

Do not define numeric weights, expected-information-gain formulas or scoring thresholds here. If two questions remain equally useful, choose the simpler one or let the user choose which uncertainty to resolve first.

### 4.3 Question construction rules

- Ask one primary question per turn. A short compound question is allowed only when its parts are inseparable (e.g. duration and fit issue for long-wear comfort).
- Explain briefly why a high-friction or sensitive-to-effort question matters.
- Offer “I don't know”, “skip”, or “not important” where appropriate.
- Do not ask for a fact the system can verify more reliably from an authorized source.
- Do not ask a user to repeat a value already present and current in the profile.
- Do not infer a hard requirement from adjectives such as “best”, “fast”, “smooth”, “quiet”, “safe” or “premium”; clarify what the word means in context.
- Do not ask budget by default if it is not needed for the user's goal or requested filtering.
- Never ask questions to improve affiliate conversion or collect unnecessary personal information.

### 4.4 Pseudo-rules

```text
on_user_turn(message):
    append_event(USER_MESSAGE, message)
    extract_explicit_updates_with_provenance(message)
    detect_corrections_and_preference_revisions()
    preserve_prior_values_in_event_history()
    update_current_profile_without_overwriting_unknown_as_false()

    if user_requests_no_buy_or_end:
        record(USER_DECISION_NO_BUY_OR_END)
        return SUMMARIZE_OR_END_WITHOUT_PRESSURE

    if user_requests_pause:
        record(DEFER_REQUESTED)
        return DEFER(stop_reason=USER_REQUESTED_PAUSE)

    if user_reopens_previously_skipped_or_answered_slot:
        mark_slot_reopened()
        allow_one_contextual_question_if_material()

    blockers = identify_material_unknowns_conflicts_and_evidence_needs()
    if no_material_question_can_resolve(blockers):
        if critical_evidence_missing_or_conflicting:
            return ABSTAIN(with_unresolved_blockers)
        if verified_hard_failures_cover_all_candidates:
            return NO_MATCH(with_failed_criteria)
        if comparison_is_supported:
            return COMPARE_OR_SUMMARIZE

    eligible_questions = filter_questions(
        relevant_to_current_goal,
        not_already_answered_or_skipped,
        answer_can_change_decision_or_next_evidence_step,
        not_resolvable_more_reliably_by_authorized_system
    )
    if eligible_questions is empty:
        return ABSTAIN_OR_ADVANCE_WITH_EXPLICIT_UNKNOWN

    question = choose_by_qualitative_hierarchy(eligible_questions)
    record(QUESTION_ASKED, question.key)
    return ASK_ONE_PRIMARY_QUESTION(question)
```

## 5. Special interaction semantics

### 5.1 User skips a question

When user says “skip”, “not now”, “don't know” or equivalent:
- Record a skip event with question key, turn and reason if volunteered.
- Set the field to unknown unless the user explicitly says it is unimportant.
- Do not convert the skip to false, zero, unconstrained or a default.
- Do not repeat the question in the same session.
- Continue with the next useful question if the skipped field is non-blocking.
- If it is a hard-constraint blocker, explain why comparison is limited and ask only for a viable alternative evidence path; if none, ABSTAIN.
- Reopen only if the user brings it up, changes the context so it becomes newly material, or explicitly asks to revisit skipped items.

### 5.2 User changes a priority or corrects an answer

- Treat the latest explicit statement as the current value for the affected field.
- Append an immutable revision event containing old value, new value, source, turn/session reference and timestamp when available.
- Mark prior value superseded; do not delete it.
- Recompute which questions and evidence needs are relevant.
- Do not preserve obsolete preference ordering in current comparison.
- Do not silently convert a soft preference into hard constraint; ask for explicit confirmation if mandatory status is unclear.
- Do not apply a numeric weight conversion unless a separately approved technical/product policy defines it.
- Do not ask the generic priority question again if the user already supplied a clear ordering.

### 5.3 Contradictory inputs

If two current statements conflict:
- Prefer a clear explicit correction over the earlier statement, retaining both in history.
- If the later statement does not clearly correct the earlier one, record an unresolved conflict and ask one neutral clarification only if it changes the decision.
- Never resolve contradictions by averaging, guessing, choosing the commercially convenient interpretation or selecting the more restrictive value without explanation.

### 5.4 User says “not important”

Record an explicit user preference of “not important / no preference” distinct from unknown. Do not ask again unless the user reopens the topic. Do not create a hard constraint.

### 5.5 User chooses not to buy

“No-buy” is a valid successful decision outcome, not a failure:
- Record the user's decision only if explicit; do not infer it from silence or hesitation.
- Summarize the reason if the user provided one (e.g. current product is sufficient, price/value not justified, timing not right).
- Offer useful non-purchase next steps only when relevant (keep current item, repair, borrow/test, wait for evidence, revisit later).
- Do not create urgency, shame, scarcity or repeated attempts to reverse the decision.
- No product ranking or affiliate action is required.

### 5.6 User defers

- Record `DEFERRED`, reason if supplied, unresolved blockers and resume point.
- Stop asking questions in the current session.
- Resume only when the user returns or an independently authorized reminder is due.
- A defer is not a no-match and not consent to marketing follow-up.

## 6. Stop, abstain and result contract

### 6.1 Canonical outcomes

| Outcome / code | Meaning | Required behavior |
|---|---|---|
| `READY_TO_COMPARE` | Profile and evidence permit a fair comparison | Compare candidates; still disclose unknowns and trade-offs |
| `NEEDS_VERIFICATION` | A material hard check or risk is unknown | Do not claim eligible/pass; identify exact verification needed |
| `INSUFFICIENT_EVIDENCE` | Evidence is missing, weak, stale or conflicting for a material claim | Abstain from that claim; state what evidence would resolve it |
| `NO_MATCH` | All evaluated candidates fail at least one applicable hard constraint | Explain failed hard criteria; invite user-led revision, never weaken constraints automatically |
| `USER_DEFERRED` | User asks to pause/postpone | Stop the session; retain resume context |
| `USER_NO_BUY` | User explicitly decides not to purchase | Respect decision; summarize only if useful |
| `USER_ENDED` | User ends conversation without an explicit no-buy decision | End politely; do not infer reason |
| `NONE` | No stop outcome yet | Continue only if a useful next action exists |

`ABSTAIN` is a next action, not itself a diagnosis of why. It must be paired with a reason/stop code such as `NEEDS_VERIFICATION` or `INSUFFICIENT_EVIDENCE`.

### 6.2 Minimal response envelope (semantic contract)

The orchestration response should carry the following fields. This is a semantic contract proposal, not a claim that these fields already exist in Hoàng's v1.0 schema.

```json
{
  "protocol_version": "1.0",
  "session_id": "stable-session-id",
  "lifecycle_state": "VERIFY",
  "next_action": "ABSTAIN",
  "stop_code": "NEEDS_VERIFICATION",
  "reason_code": "HARD_CHECK_UNKNOWN",
  "user_facing_explanation": "We cannot confirm this requirement yet.",
  "unresolved_blockers": [
    {
      "key": "host_video_output",
      "kind": "hard_constraint",
      "status": "unknown",
      "required_evidence": "Verified host model and video-output capability"
    }
  ],
  "next_question": null,
  "resume_state": "VERIFY",
  "profile_version": "1"
}
```

Rules:
- `next_action` is one of `ASK`, `VERIFY`, `COMPARE`, `SUMMARIZE`, `ABSTAIN`, `DEFER`, `NO_MATCH`, `END`.
- `stop_code` uses the canonical outcome vocabulary above; `NONE` when no stop outcome is active.
- `reason_code` is a stable machine-readable reason, with human-readable explanation alongside.
- `unresolved_blockers` lists each material blocker, its type/status and what could resolve it.
- `next_question` is null unless `next_action=ASK`; at most one primary question.
- `resume_state` is populated for DEFER/ABSTAIN when meaningful; do not imply automatic follow-up.
- The payload must never state a candidate is eligible unless all applicable hard checks pass with appropriate evidence.
- Product candidate evaluations remain separate from the user profile and conversation state.

### 6.3 When to stop asking

Stop asking and advance when:
- the goal/use case is sufficiently clear for the current decision;
- no unanswered user question can materially change eligibility, shortlist or next evidence action;
- remaining unknowns are non-blocking or can only be resolved by external evidence;
- the user explicitly skips, defers, ends or chooses no-buy;
- further questions would add burden without improving decision quality.

Do not use a fixed question count as a universal stopping threshold.

## 7. Category extension contract

A new category must be introduced through declarative configuration. Core behavior must not contain category-name conditionals or category-specific branches.

### 7.1 Category configuration

A category pack may define:

| Config section | Required content |
|---|---|
| `category_id` / `version` | Stable identifier and semantic version |
| `goal_prompts` | Neutral ways to identify goal/use case |
| `field_definitions[]` | Field key, type, description, allowed values, sensitivity, provenance rules |
| `question_catalog[]` | Stable question key, prompt, fields updated, prerequisites, skip behavior, answer type |
| `question_triggers[]` | Conditions under which a question becomes eligible |
| `hard_criteria[]` | Criterion key, user-facing explanation, operator/type, required evidence schema |
| `soft_criteria[]` | Preference key, trade-off explanation, optional evidence needs |
| `risk_taxonomy[]` | Category-specific risks and blocker descriptions |
| `evidence_requirements[]` | Accepted source types, freshness, variant/context scope, owner |
| `stop_guidance` | Category-specific blocker explanations; cannot override core stop semantics |
| `golden_fixtures[]` | At least one normal flow, one unknown/skip, one hard fail/verification, one preference revision, one defer/no-buy case |

### 7.2 Required configuration shape (illustrative)

```yaml
category_id: "example_category"
version: "1.0"
fields:
  - key: "primary_use_case"
    value_type: "string"
    provenance_required: true
questions:
  - key: "EX-Q1"
    prompt: "What are you mainly trying to do?"
    updates: ["primary_use_case", "desired_outcome"]
    triggers:
      - "profile.primary_use_case is unknown"
    skip_policy: "record_unknown_do_not_repeat"
criteria:
  hard: []
  soft: []
evidence_requirements: []
risk_taxonomy: []
golden_fixtures: []
```

This is an example shape only. Category teams must specify real field types and machine-evaluable trigger expressions in the approved technical config schema.

### 7.3 Core invariants for every category pack

A category pack may add prompts, fields, criteria and evidence types, but may not:
- override unknown/fail/pass semantics;
- make soft preferences hard by default;
- bypass hard-constraint fail-closed behavior;
- remove provenance or audit history;
- repeat skipped/answered questions automatically;
- alter defer/no-buy/abstain semantics;
- add affiliate/commercial fields to question selection or candidate eligibility;
- claim product truth without evidence;
- introduce sensitive inference or manipulative prompts.

### 7.4 Extension acceptance checklist

A category is accepted only when:
1. Every field has a definition, type, provenance and unknown behavior.
2. Every question has a stable key, trigger, purpose, fields updated and skip/repeat rule.
3. Every hard criterion has an evidence contract and pass/fail/unknown behavior.
4. Soft preferences remain tradeable and have no unapproved numeric weights.
5. At least one golden fixture covers skip/unknown and one covers revision.
6. At least one fixture covers hard failure or insufficient evidence.
7. Defer and no-buy paths are covered.
8. Core invariants pass without changing core code.
9. Product/domain expert approves product-specific terms and evidence requirements.
10. Technical reviewer validates configuration against the category-pack schema.

## 8. Golden fixture index and mapping

The six fixtures in [golden-conversation-fixtures-v1.md](./golden-conversation-fixtures-v1.md) remain valid semantic tests, with the following mapping and additions needed:

| Fixture | Protocol behavior | Lifecycle / expected result | Product fixture dependency |
|---|---|---|---|
| MON-01 | Discover work use case; do not infer gaming/color; host unknown | DISCOVER → CLARIFY → VERIFY → ABSTAIN / NEEDS_VERIFICATION | No candidate assertion; product fixture only for compatibility result |
| MON-02 | Explicit hard USB-C video requirement; verified incompatibility | CLARIFY → VERIFY → NO_MATCH | Yes, if asserting a specific candidate/host capability; current synthetic user fact alone tests conversation state |
| AUD-01 | Long wear, fit uncertainty, no universal comfort claim | CLARIFY → VERIFY → ABSTAIN / NEEDS_VERIFICATION | Yes, for candidate-specific fit claims |
| AUD-02 | User priority order; mic evidence needed | CLARIFY → VERIFY → ABSTAIN / NEEDS_VERIFICATION | Yes, for microphone/call test claims |
| EDGE-01 | User skips non-blocking desk-fit question | CLARIFY continues; skip retained unknown; no repeat | No, tests orchestration behavior |
| EDGE-02 | Priority revision with audit history | CLARIFY → VERIFY; current order updated, old order superseded | No for revision semantics; yes for candidate ranking assertions |
| EDGE-03 (add) | User explicitly defers | Any active state → DEFER / USER_DEFERRED; no further question | No |
| EDGE-04 (add) | User explicitly chooses not to buy | Active or summary state → USER_NO_BUY; no persuasion | No |

The existing six fixtures should not be silently edited to make an implementation pass. Add EDGE-03 and EDGE-04 as new fixtures in the next golden-fixture revision. The two additions must assert: (a) stop immediately after explicit defer/no-buy; (b) no extra product question; (c) unresolved profile and resume state retained for defer; (d) no automatic resume or follow-up implied; (e) no-buy is not classified as NO_MATCH.

### 8.1 Test coverage categories

**Behavior-only, executable without product data:** question ordering, no-repeat, skip, preference revision, defer, no-buy, provenance preservation, lifecycle transitions, response-envelope validation.

**Requires verified product fixtures:** candidate hard-check PASS/FAIL, exact compatibility, candidate fit, evidence coverage, ranking, model-specific trade-offs and product recommendation claims.

No candidate PASS/FAIL, product ranking or technical specification is invented in this protocol.

## 9. Technical mapping and ownership boundaries

### 9.1 Mapping to Hoàng's current v1.0 DecisionProfile

| Protocol concept | Current v1.0 representation | Gap / recommendation |
|---|---|---|
| Goal / use case | `use_case` | Add generic `user_goal` or define goal as separate orchestration field; do not overload use_case |
| Desired outcome | `desired_outcomes[]` | Direct mapping |
| Hard/soft constraints | `constraints[].constraint_type` | Direct mapping; require explicit user confirmation for hard |
| Preference priority | `preferences[].priority` | Numeric 0–5 exists; protocol only defines ordinal meaning. Conversion policy must be separately approved |
| Context | Partial in `use_case` / desired outcomes | Add typed generic `context` collection |
| Risk/blockers | `risk_concerns[]` | Add blocker status/type and link to unresolved evidence |
| Unknowns | `unresolved_slots[]` | Direct partial mapping; keep value/provenance unknown |
| Inferences | `ProvenancedValue.evidence_source=inferred_pending_confirmation` | Ensure every inference has rationale and confirmation question in orchestration layer |
| Evidence needs | `CandidateEvaluation.evidence_refs` | User-profile evidence needs are distinct; add orchestration field |
| Asked questions | `asked_question_keys[]` | Direct mapping |
| Skipped questions | Not represented | Add `skipped_question_keys[]` to session state/event log; do not overload asked keys |
| Current lifecycle | `journey_state` J1–J6 | Keep customer journey/psychological state distinct from protocol lifecycle DISCOVER/CLARIFY/VERIFY/COMPARE |
| Preference revision history | Not represented | Append-only event log; current profile stores latest values |
| Stop outcome | Not represented | Add typed response envelope with `next_action`, `stop_code`, `reason_code`, blockers and resume state |
| No-buy/defer | Not represented | Add explicit user-decision/session event and terminal/paused outcome |

### 9.2 Important distinction: journey state vs protocol lifecycle

Hoàng's J1–J6 fields describe the customer's decision journey (unclear need, need defined, exploring, hesitating, leaning, ready). The protocol lifecycle describes what the system is doing (discovering, clarifying, verifying, comparing, summarizing, abstaining or deferring). They are related but not interchangeable. Do not force a one-to-one enum mapping.

### 9.3 Ownership

- **Vân Anh:** behavioral semantics, question purpose/priority, user autonomy, stop rules, golden expected behavior.
- **Hoàng:** schema, state persistence, event model, API envelope, validator and implementation; must not silently change behavior semantics.
- **A Long:** product-specific truth, criteria interpretation and accepted evidence sources; must not infer user intent.
- **CEO:** scope/policy approval and final acceptance.
- **Trâm Anh:** may support source normalization or QA execution; no independent psychology/product/technical authority.

## 10. Review questions and acceptance criteria

### For Hoàng
1. Can the current DecisionProfile remain strict while orchestration state and event history live in a separate envelope?
2. Can the implementation preserve distinct lifecycle and J1–J6 journey states?
3. How will skip/revision/defer/no-buy events be stored append-only?
4. Can response validation enforce one primary question and the stop-code/next-action consistency rules?
5. How will missing candidate hard checks default to unknown at the contract boundary?

### For A Long
1. Are the generic terms “hard criterion”, “candidate-specific evidence”, “variant” and “verification requirement” compatible with product review workflow?
2. For each category pack, who owns source authority and freshness rules?

### Acceptance checklist
- [ ] Category-independent state dictionary and provenance are defined.
- [ ] Lifecycle transitions and terminal/paused outcomes are explicit.
- [ ] Question selection policy is deterministic enough to implement without numeric weights.
- [ ] Unknown, skip, hard/soft, revision and conflict semantics are explicit.
- [ ] Stop/abstain/defer/no-match/no-buy payload is specified.
- [ ] Category extension is configuration-only and preserves core invariants.
- [ ] Six existing fixtures are mapped; defer/no-buy fixture additions are specified.
- [ ] Technical gaps and ownership are explicit; no product facts or scoring formulas invented.

**Review status:** awaiting Hoàng's technical mapping review, A Long's terminology/evidence-boundary review where needed, and CEO acceptance. This is a behavioral specification, not user-tested or production-validated policy.
