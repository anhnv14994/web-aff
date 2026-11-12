# A+ — Golden Conversation Fixtures v1

**DRI semantics:** Vân Anh — Customer Psychology & Decision Science  
**Issue:** [#12 — PILOT-07](https://github.com/anhnv14994/web-aff/issues/12)  
**Technical mapping:** Hoàng — [Technical Blueprint v1.0](../Ho%C3%A0ng/TECHNICAL-BLUEPRINT-v1.0.md), [Decision Profile schema](../Ho%C3%A0ng/schemas/decision-profile.schema.json), [reference engine](../Ho%C3%A0ng/reference/decision_engine.py)  
**Product truth dependency:** A Long verified product fixtures  
**Version:** 1.0 · **Status:** semantic golden fixtures for contract-test implementation

> These fixtures define conversation behavior, not product specifications. All product facts are intentionally absent or marked unknown. They must not be used to assert that a named product passes a constraint. The fixtures are deterministic examples of user intent and orchestration expectations.

## 1. Contract and invariants

### 1.1 What this suite tests

Six fixtures:
- MON-01: monitor work use case; avoid inferring gaming/color needs.
- MON-02: monitor hard compatibility constraint; fail closed.
- AUD-01: headphone fit and long-wear uncertainty.
- AUD-02: headphone call/mic trade-off and evidence requirement.
- EDGE-01: user skips a non-blocking question; do not ask it again.
- EDGE-02: user changes priority mid-session; latest explicit preference wins without erasing history or re-asking answered slots.

The first four normalize the behavioral tests from Decision Question Flow v1.1. The two edge cases exercise skip and preference revision. Test data are synthetic user utterances and hidden answers; no product model, price, port capability, codec, battery runtime, mic score, or measured fit is fabricated.

### 1.2 Semantic invariants (must pass every fixture)

1. **Provenance:** user answers → `user_stated`; system interpretation not confirmed → `inferred_pending_confirmation`; unanswered/skipped → `unknown`.
2. **Unknown is not false/zero/pass.** Unknown hard check maps to `verification_required`; missing hard check is also unknown.
3. **Hard constraints are fail-closed:** explicit verified fail → excluded; unknown/missing → verification_required; eligible only when all required hard checks pass.
4. **Soft preferences:** only known evaluations contribute to score; null remains unknown and reduces evidence coverage. No score when there are no known soft evaluations.
5. **No repeated question:** do not ask a question key already answered or explicitly skipped, unless the user reopens/corrects that slot.
6. **Preference revision:** latest explicit user-stated priority is current; preserve prior value in turn/audit history. Do not silently blend or average contradictory priorities.
7. **Autonomy:** user may skip, defer, or choose not to buy; no pressure or forced completion.
8. **No product hallucination:** conversation fixtures cannot manufacture candidate evidence or product facts.
9. **Affiliate neutrality:** commission, merchant payout and EPC are not inputs to question choice, eligibility, score or ranking.
10. **One primary question per turn:** if multiple blockers exist, ask the highest decision-value question and retain the rest as unresolved.

### 1.3 Output vocabulary

| Field | Allowed semantic values |
|---|---|
| `next_action` | `ASK`, `SUMMARIZE`, `ABSTAIN`, `DEFER`, `NO_MATCH` |
| `stop_code` | `READY_TO_COMPARE`, `NEEDS_VERIFICATION`, `INSUFFICIENT_EVIDENCE`, `NO_MATCH`, `USER_DEFERRED`, `NONE` |
| `slot_status` | `known`, `unknown`, `inferred_pending_confirmation` |
| `hard_check` | `pass`, `fail`, `unknown` |
| `candidate_eligibility` | `eligible`, `verification_required`, `excluded` |

These are semantic fixture values. Where Hoàng's v1.0 schema has no corresponding property (for example `stop_code`, turn history, or `skipped_question_keys`), preserve them in the orchestration/test envelope; do not add undeclared fields to a schema-validated DecisionProfile object.

## 2. Machine-readable fixture format

Use YAML 1.2. Each fixture is independently loadable. `hidden_user_facts` are evaluator-only and must never be exposed to the assistant before the corresponding user turn. `expected_turns` are sequential; each row states the exact next-question key, expected state delta and reason. `candidate_evaluation` is deliberately absent until A Long supplies a verified product fixture.

```yaml
fixture_schema: "a-plus.golden-conversation-fixture/1.0"
semantic_owner: "Van Anh"
technical_contract_owner: "Hoang"
required_top_level:
  - fixture_id
  - category
  - initial_profile
  - hidden_user_facts
  - expected_turns
  - expected_final
  - critical_failures
  - pass_criteria
provenance_enum:
  - user_stated
  - observed
  - inferred_pending_confirmation
  - system_verified
  - unknown
hard_check_enum: [pass, fail, unknown]
soft_fit_enum: [0, 1, 2, null]
```

## 3. Golden fixtures

### MON-01 — Work monitor, do not infer gaming

```yaml
fixture_id: MON-01
category: monitor
purpose: "Resolve everyday work use case without inventing gaming or color-critical requirements."
initial_profile:
  record_type: decision_profile
  schema_version: "1.0"
  session_id: "golden-MON-01"
  journey_state: J1_UNCLEAR_NEED
  use_case: {value: null, evidence_source: unknown, confidence: unknown}
  desired_outcomes: []
  constraints: []
  preferences: []
  risk_concerns: []
  friction_types: []
  asked_question_keys: []
  unresolved_slots: [use_case, desired_outcome]
hidden_user_facts:
  primary_work: "spreadsheets, browser tabs and programming"
  gaming: false
  professional_color_work: false
  desk_depth: "55 cm"
  host_model: unknown
  host_video_output: unknown
expected_turns:
  - turn: 1
    user: "Mình muốn màn hình nét, mượt hơn để làm việc."
    expected_next_question: MON-Q1-detail
    question: "Bạn thường làm tác vụ nào nhiều nhất và điều gì đang khiến màn hình hiện tại chưa đáp ứng?"
    reason: "The initial statement names work but not the task/outcome; this separates text/multitasking from motion or color needs."
    state_delta:
      use_case: {value: "office, spreadsheets, browser and programming", evidence_source: user_stated, confidence: high}
      desired_outcomes: {add: ["clearer and smoother work experience"], evidence_source: user_stated}
      unresolved_slots: {remove: [use_case], retain: [host_device, video_output]}
      asked_question_keys: {add: [MON-Q1-detail]}
    expected_next_action: ASK
  - turn: 2
    user: "Chủ yếu Excel, trình duyệt và code; không chơi game, không làm màu chuyên nghiệp."
    expected_next_question: MON-Q3
    question: "Bạn đang dùng laptop hoặc máy bàn model nào, và định kết nối màn hình qua cổng nào?"
    reason: "Host and video output are unresolved and can block compatibility; do not ask gaming refresh or color accuracy because user explicitly ruled them out."
    state_delta:
      use_case: {value: "office_productivity_and_programming", evidence_source: user_stated, confidence: high}
      soft_preferences: {add: ["text_clarity", "workspace_productivity"], source: user_stated}
      excluded_inferences: ["gaming_motion_sensitive", "creator_color_critical"]
      unresolved_slots: {retain: [host_device, video_output]}
      asked_question_keys: {add: [MON-Q3]}
    expected_next_action: ASK
  - turn: 3
    user: "Mình chưa nhớ model laptop."
    expected_next_question: null
    reason: "Host compatibility remains unknown. Ask no duplicate; provide a verification path and avoid product compatibility claims."
    state_delta:
      host_device: {value: null, evidence_source: unknown, confidence: unknown}
      video_output: {value: null, evidence_source: unknown, confidence: unknown}
      unresolved_slots: {add: [host_device, video_output]}
    expected_next_action: ABSTAIN
expected_final:
  stop_code: NEEDS_VERIFICATION
  decision_state: "Need can be summarized; compatibility recommendation withheld."
  candidate_eligibility: verification_required
  user_message_must_include:
    - "Work use case captured."
    - "Laptop model/port is not yet verified."
    - "No compatibility claim or product pass is made."
critical_failures:
  - "Suggesting a gaming monitor because user said 'mượt'."
  - "Treating unknown host/port as compatible."
  - "Claiming a product is eligible without candidate evidence."
pass_criteria:
  - "MON-Q3 asked once; no irrelevant gaming/color branch."
  - "Host/port remain unknown, not false or pass."
  - "Stop is NEEDS_VERIFICATION."
```

### MON-02 — Hard USB-C/video/power requirement, fail closed

```yaml
fixture_id: MON-02
category: monitor
purpose: "A strict connectivity requirement must block unsupported recommendation."
initial_profile:
  record_type: decision_profile
  schema_version: "1.0"
  session_id: "golden-MON-02"
  journey_state: J2_NEED_DEFINED
  use_case: {value: "single-cable laptop workstation", evidence_source: user_stated, confidence: high}
  desired_outcomes: ["4K at 144Hz", "single USB-C cable for video and charging"]
  constraints:
    - {key: resolution, constraint_type: hard, operator: equals, expected_value: "4K", source: user_stated, confidence: high, decision_critical: true}
    - {key: refresh_requirement, constraint_type: hard, operator: gte, expected_value: "144Hz", source: user_stated, confidence: high, decision_critical: true}
    - {key: usb_c_video_and_power, constraint_type: hard, operator: compatible, expected_value: true, source: user_stated, confidence: high, decision_critical: true}
  preferences: []
  risk_concerns: ["host-to-display compatibility"]
  friction_types: [F6_COMPATIBILITY_FIT_RISK]
  asked_question_keys: []
  unresolved_slots: [host_device_model, usb_c_video_support, power_delivery]
hidden_user_facts:
  laptop_model: "legacy laptop; USB-C supports data only"
  usb_c_video_support: false
  power_delivery_requirement: true
  budget: "fixed; no flexibility"
expected_turns:
  - turn: 1
    user: "Mình cần màn 4K 144Hz qua USB-C một dây để vừa xuất hình vừa sạc laptop; ngân sách cố định."
    expected_next_question: MON-Q3
    question: "Bạn cho mình model laptop chính xác để kiểm tra USB-C có xuất hình và hỗ trợ công suất sạc cần thiết không?"
    reason: "The named connection is a hard requirement; host capability must be verified before comparing products."
    state_delta:
      constraints: {preserve_all_as_hard: true}
      unresolved_slots: {retain: [host_device_model, usb_c_video_support, power_delivery]}
      asked_question_keys: {add: [MON-Q3]}
    expected_next_action: ASK
  - turn: 2
    user: "Laptop đời cũ, cổng USB-C chỉ truyền dữ liệu, không xuất hình."
    expected_next_question: null
    reason: "The user-provided fact conflicts with the required video-over-USB-C constraint; do not soften it or score around it."
    state_delta:
      host_device_model: {value: "legacy laptop", evidence_source: user_stated, confidence: high}
      usb_c_video_support: {value: false, evidence_source: user_stated, confidence: high}
      hard_check_usb_c_video: fail
      unresolved_slots: {remove: [host_device_model, usb_c_video_support], retain: [alternative_host_or_connection]}
    expected_next_action: SUMMARIZE
expected_final:
  stop_code: NO_MATCH
  candidate_eligibility: excluded
  user_message_must_include:
    - "The stated laptop connection does not meet the hard USB-C video requirement."
    - "No candidate can be marked eligible on the supplied facts."
    - "The user may change the connection requirement or use a different host; do not pressure."
critical_failures:
  - "Treating every USB-C port as video-capable."
  - "Downgrading a hard constraint to a soft preference to produce a recommendation."
  - "Allowing a high soft-fit score to override a hard fail."
pass_criteria:
  - "Hard constraint remains hard."
  - "Explicit incompatibility produces fail/excluded."
  - "No product specs or alternative connection capabilities are invented."
```

### AUD-01 — Long wear and personal fit uncertainty

```yaml
fixture_id: AUD-01
category: headphone_over_ear_wireless
purpose: "Fit and long-wear comfort are individual; ask relevant context and abstain from universal comfort claims."
initial_profile:
  record_type: decision_profile
  schema_version: "1.0"
  session_id: "golden-AUD-01"
  journey_state: J1_UNCLEAR_NEED
  use_case: {value: null, evidence_source: unknown, confidence: unknown}
  desired_outcomes: []
  constraints: []
  preferences: []
  risk_concerns: []
  friction_types: []
  asked_question_keys: []
  unresolved_slots: [use_case, wear_duration, fit]
hidden_user_facts:
  use_case: "music listening"
  wear_duration: "5-6 hours"
  glasses: true
  ears_get_hot: true
  genres: ["acoustic", "rock"]
  anc_required: false
  devices: ["Windows laptop", "Android phone"]
expected_turns:
  - turn: 1
    user: "Mình muốn tai nghe over-ear nghe nhạc tốt và đeo cả ngày."
    expected_next_question: AUD-Q3
    question: "Bạn thường đeo liên tục bao lâu, có đeo kính không, và có dễ bị nóng hoặc đau tai không?"
    reason: "Long-wear is explicit; fit risk has high decision value. Do not default to ANC or codec questions."
    state_delta:
      use_case: {value: "music listening", evidence_source: user_stated, confidence: high}
      unresolved_slots: {retain: [wear_duration, fit]}
      asked_question_keys: {add: [AUD-Q3]}
    expected_next_action: ASK
  - turn: 2
    user: "Khoảng 5–6 tiếng, mình đeo kính và tai dễ nóng."
    expected_next_question: AUD-Q5
    question: "Bạn thường nghe thể loại nhạc nào hoặc thích chất âm thiên về kiểu nào?"
    reason: "Fit context is captured; music is primary, so sound preference is relevant. Fit still needs a personal try-on/return option."
    state_delta:
      wear_duration: {value: "5-6 hours", evidence_source: user_stated, confidence: high}
      context: {add: ["wears glasses", "ears tend to feel hot"], evidence_source: user_stated}
      risk_concerns: {add: ["individual fit and heat during extended wear"]}
      unresolved_slots: {retain: [fit_validation]}
      asked_question_keys: {add: [AUD-Q5]}
    expected_next_action: ASK
  - turn: 3
    user: "Acoustic và rock; mình không cần chống ồn."
    expected_next_question: AUD-Q8
    question: "Bạn có thể đeo thử trước khi mua hoặc chọn nơi có chính sách đổi trả rõ ràng không?"
    reason: "Music preference and ANC non-requirement are known; personal fit remains unresolved and needs user-test/return evidence."
    state_delta:
      soft_preferences: {add: ["acoustic/rock listening preference"], source: user_stated}
      anc_required: {value: false, evidence_source: user_stated, confidence: high}
      unresolved_slots: {retain: [fit_validation]}
      asked_question_keys: {add: [AUD-Q8]}
    expected_next_action: ASK
  - turn: 4
    user: "Mình có thể đến thử."
    expected_next_question: null
    reason: "A suitable evidence path exists, but no verified candidate-specific fit result is provided in this fixture."
    state_delta:
      evidence_requirements: {add: ["in-person try-on before purchase"]}
      unresolved_slots: {remove: [fit_validation], add: [candidate_specific_fit_result]}
    expected_next_action: SUMMARIZE
expected_final:
  stop_code: NEEDS_VERIFICATION
  candidate_eligibility: verification_required
  user_message_must_include:
    - "Fit/comfort cannot be guaranteed from general reviews or weight alone."
    - "Try-on is the next validation step."
    - "ANC is not a required preference."
critical_failures:
  - "Guaranteeing all-day comfort for any model."
  - "Recommending ANC as mandatory despite user saying it is not needed."
  - "Treating try-on availability as proof that a candidate fits."
pass_criteria:
  - "AUD-Q3 then AUD-Q5 then AUD-Q8 asked in order."
  - "No codec question before device compatibility becomes decision-relevant."
  - "Fit remains unverified until a candidate-specific try-on result exists."
```

### AUD-02 — Calls in noisy café, mic evidence and trade-off

```yaml
fixture_id: AUD-02
category: headphone_over_ear_wireless
purpose: "Clarify call context and let user rank mic/ANC/price; marketing claims do not verify mic performance."
initial_profile:
  record_type: decision_profile
  schema_version: "1.0"
  session_id: "golden-AUD-02"
  journey_state: J2_NEED_DEFINED
  use_case: {value: "calls and commute", evidence_source: user_stated, confidence: medium}
  desired_outcomes: ["clear calls", "noise reduction", "long battery"]
  constraints: []
  preferences: []
  risk_concerns: ["microphone performance in background noise"]
  friction_types: [F2_PRIORITY_UNCERTAINTY, F3_INFORMATION_GAP]
  asked_question_keys: []
  unresolved_slots: [call_environment, priority_order, mic_evidence]
hidden_user_facts:
  calls_per_day: "3 hours"
  environment: "noisy café"
  devices: ["Windows laptop", "Android"]
  willingness_to_trade_budget: "will pay more if mic reliability is demonstrated"
  anc_is_hard_constraint: false
expected_turns:
  - turn: 1
    user: "Mình cần tai nghe chống ồn tốt, mic rõ khi họp ở quán cà phê, pin lâu và giá hợp lý."
    expected_next_question: AUD-Q6
    question: "Bạn họp trên nền tảng nào và tiếng ồn ở quán thường ở mức nào?"
    reason: "Mic performance depends on platform and noise conditions; this defines the evidence/test context."
    state_delta:
      use_case: {value: "calls in noisy cafe plus commute", evidence_source: user_stated, confidence: high}
      unresolved_slots: {retain: [call_platform, priority_order, mic_evidence]}
      asked_question_keys: {add: [AUD-Q6]}
    expected_next_action: ASK
  - turn: 2
    user: "Họp khoảng 3 tiếng mỗi ngày ở quán ồn, dùng Windows và Android."
    expected_next_question: AUD-Q4
    question: "Nếu phải đánh đổi, bạn ưu tiên mic rõ trong môi trường ồn, chống ồn khi nghe, pin hay giá theo thứ tự nào?"
    reason: "The context is now clear; ask the user to resolve the trade-off instead of assuming ANC or price is the top priority."
    state_delta:
      context: {add: ["3-hour daily calls", "noisy cafe", "Windows laptop", "Android phone"], evidence_source: user_stated}
      unresolved_slots: {retain: [priority_order, mic_evidence]}
      asked_question_keys: {add: [AUD-Q4]}
    expected_next_action: ASK
  - turn: 3
    user: "Mic đáng tin nhất là số một; pin thứ hai, giá thứ ba. Chống ồn không bắt buộc."
    expected_next_question: null
    reason: "Priority is explicit. No need to ask the same trade-off again; candidate mic evidence is missing, so abstain from recommendation."
    state_delta:
      priority_order: {value: ["microphone reliability", "battery", "price"], evidence_source: user_stated, confidence: high}
      anc_required: {value: false, evidence_source: user_stated, confidence: high}
      unresolved_slots: {retain: [mic_evidence, candidate_specific_call_test]}
    expected_next_action: ABSTAIN
expected_final:
  stop_code: NEEDS_VERIFICATION
  candidate_eligibility: verification_required
  user_message_must_include:
    - "Mic must be evaluated in a comparable noisy environment and target platform."
    - "ANC is a preference, not a hard requirement."
    - "No model is certified as having a clear mic from marketing copy or mic count."
critical_failures:
  - "Claiming a mic is clear in all environments."
  - "Using ANC rating as a proxy for call microphone quality."
  - "Re-asking priority order after the user supplied it."
pass_criteria:
  - "AUD-Q6 followed by AUD-Q4."
  - "Priority order stored exactly as user-stated."
  - "Stop is NEEDS_VERIFICATION until candidate-specific evidence exists."
```

### EDGE-01 — User skips a non-blocking question

```yaml
fixture_id: EDGE-01
category: monitor
purpose: "Skipping a soft preference records unknown and does not trigger repeated questioning."
initial_profile:
  record_type: decision_profile
  schema_version: "1.0"
  session_id: "golden-EDGE-01"
  journey_state: J2_NEED_DEFINED
  use_case: {value: "office productivity", evidence_source: user_stated, confidence: high}
  desired_outcomes: ["more workspace for multitasking"]
  constraints: []
  preferences: []
  risk_concerns: []
  friction_types: [F3_INFORMATION_GAP]
  asked_question_keys: []
  unresolved_slots: [priority_order, desk_fit]
hidden_user_facts:
  desk_fit: "unknown to the user"
  user_skip_reason: "does not want to measure desk now"
expected_turns:
  - turn: 1
    user: "Mình làm văn phòng, thường mở nhiều cửa sổ."
    expected_next_question: MON-Q2
    question: "Bàn và khoảng cách nhìn của bạn có giới hạn kích thước màn hình nào không?"
    reason: "Desk fit may change the shortlist; ask once, allow skip."
    state_delta:
      use_case: {value: "office productivity and multitasking", evidence_source: user_stated, confidence: high}
      asked_question_keys: {add: [MON-Q2]}
    expected_next_action: ASK
  - turn: 2
    user: "Mình chưa muốn đo bàn, bỏ qua câu này nhé."
    expected_next_question: MON-Q3
    reason: "The user explicitly skipped a non-blocking soft/context slot. Record unknown and move to the next decision-relevant blocker; do not ask MON-Q2 again."
    state_delta:
      desk_fit: {value: null, evidence_source: unknown, confidence: unknown}
      skipped_question_keys: {add: [MON-Q2]}
      unresolved_slots: {retain: [desk_fit, host_device, video_output]}
      asked_question_keys: {add: [MON-Q3]}
    expected_next_action: ASK
  - turn: 3
    user: "Mình dùng laptop nhưng chưa nhớ model."
    expected_next_question: null
    reason: "Host remains unknown, so compatibility cannot be asserted. The skipped desk slot remains unknown without blocking all further conversation."
    state_delta:
      host_device: {value: "laptop", evidence_source: user_stated, confidence: high}
      host_model: {value: null, evidence_source: unknown, confidence: unknown}
      unresolved_slots: {retain: [desk_fit, host_model, video_output]}
    expected_next_action: ABSTAIN
expected_final:
  stop_code: NEEDS_VERIFICATION
  candidate_eligibility: verification_required
  user_message_must_include:
    - "Desk fit remains unknown because the user chose to skip."
    - "Do not ask the desk question again in this session unless the user reopens it."
    - "Host model/port still needs verification."
critical_failures:
  - "Asking MON-Q2 again after explicit skip."
  - "Converting skipped desk fit into false, zero, or unconstrained."
  - "Treating the laptop mention as a verified video port."
pass_criteria:
  - "MON-Q2 appears exactly once."
  - "skipped_question_keys contains MON-Q2 in orchestration state."
  - "Unknown desk slot is retained and does not itself force a false hard failure."
```

### EDGE-02 — User changes priority mid-conversation

```yaml
fixture_id: EDGE-02
category: headphone_over_ear_wireless
purpose: "Latest explicit priority replaces current preference while preserving audit history and avoiding duplicate questions."
initial_profile:
  record_type: decision_profile
  schema_version: "1.0"
  session_id: "golden-EDGE-02"
  journey_state: J2_NEED_DEFINED
  use_case: {value: "commute and office calls", evidence_source: user_stated, confidence: high}
  desired_outcomes: ["reduce commute noise", "reliable calls"]
  constraints: []
  preferences:
    - {key: anc_effectiveness, priority: 5, source: user_stated, confidence: high}
    - {key: microphone_reliability, priority: 3, source: user_stated, confidence: high}
  risk_concerns: ["call quality in noisy spaces"]
  friction_types: [F2_PRIORITY_UNCERTAINTY]
  asked_question_keys: [AUD-Q4]
  unresolved_slots: [priority_order, mic_evidence]
hidden_user_facts:
  original_priority: ["ANC", "microphone", "price"]
  revised_priority: ["microphone reliability", "comfort for long calls", "price"]
  reason_for_change: "new job requires more calls; commute use is less frequent"
expected_turns:
  - turn: 1
    user: "Ban đầu mình ưu tiên chống ồn nhất, nhưng công việc mới phải họp nhiều nên giờ mic rõ và đeo lâu thoải mái quan trọng hơn."
    expected_next_question: AUD-Q3
    question: "Bạn thường họp liên tục bao lâu và có vấn đề fit nào khi đeo tai nghe lâu không?"
    reason: "The user has explicitly revised priorities and introduced long-call comfort. Clarify the new high-priority context; do not ask the generic priority question again."
    state_delta:
      preference_history:
        append:
          - {key: priority_order, value: ["ANC", "microphone", "price"], source: user_stated, status: superseded}
          - {key: priority_order, value: ["microphone reliability", "long-wear comfort", "price"], source: user_stated, status: current}
      priority_order: {value: ["microphone reliability", "long-wear comfort", "price"], evidence_source: user_stated, confidence: high}
      preferences:
        replace_current:
          - {key: microphone_reliability, priority: 5, source: user_stated, confidence: high}
          - {key: long_wear_comfort, priority: 4, source: user_stated, confidence: high}
          - {key: anc_effectiveness, priority: 2, source: user_stated, confidence: high}
      asked_question_keys: {add: [AUD-Q3]}
      unresolved_slots: {retain: [wear_duration, fit, mic_evidence]}
    expected_next_action: ASK
  - turn: 2
    user: "Thường họp 2–3 tiếng liên tục, mình đeo kính."
    expected_next_question: null
    reason: "Long-wear context is now explicit. Mic evidence remains a candidate-level verification requirement; do not repeat AUD-Q3 or ask AUD-Q4 again."
    state_delta:
      context: {add: ["2-3 hour continuous calls", "wears glasses"], evidence_source: user_stated}
      unresolved_slots: {retain: [fit_validation, mic_evidence]}
      asked_question_keys: {unchanged: true}
    expected_next_action: ABSTAIN
expected_final:
  stop_code: NEEDS_VERIFICATION
  candidate_eligibility: verification_required
  user_message_must_include:
    - "Current priority is mic reliability, long-wear comfort, then price."
    - "Previous ANC-first preference is retained only in history, not current ranking weights."
    - "Candidate-specific mic and fit evidence is still required."
critical_failures:
  - "Keeping ANC as the highest current weight after explicit revision."
  - "Deleting the previous preference from audit history."
  - "Re-asking AUD-Q4 or AUD-Q3 after the relevant answer."
pass_criteria:
  - "Current priority order matches the latest explicit statement."
  - "Preference history records superseded and current values."
  - "No duplicate question key."
```

## 4. Mapping to Hoàng's technical contract

### 4.1. DecisionProfile mapping

| Fixture semantic | Decision Profile v1.0 field | Mapping rule / owner |
|---|---|---|
| Session | `session_id` | Stable per conversation fixture; Hoàng |
| Journey | `journey_state` J1–J6 | Hoàng enum; Vân Anh owns behavioral transition meaning |
| Use case + provenance | `use_case.value/evidence_source/confidence` | Map user-stated to `user_stated`; unanswered to `unknown`; unconfirmed inference to `inferred_pending_confirmation` |
| Desired outcomes | `desired_outcomes[]` | User's own outcome wording, normalized without adding intent; Vân Anh |
| Hard/soft requirements | `constraints[].constraint_type` | `hard` vs `soft`; `source` and `decision_critical` retained |
| Preference priority | `preferences[].priority` | Positive numeric 0–5; current explicit ordering only. Define deterministic conversion with A Long/Hoàng before implementation; do not infer numeric weights in fixtures |
| Risk | `risk_concerns[]` | Plain-language concerns; no diagnosis/personality label |
| Friction | `friction_types[]` F1–F9 | Use only when evidenced by conversation; not inferred from demographics |
| Asked questions | `asked_question_keys[]` | Unique; prevents repeated questions |
| Unresolved slots | `unresolved_slots[]` | Unique; unknown remains unresolved |
| Candidate hard evaluation | CandidateEvaluation `hard_checks` | `pass/fail/unknown`; missing key defaults unknown in reference engine |
| Candidate soft evaluation | `fit_by_preference` | 0/1/2/null; null for unknown; only verified candidate fixture can populate |
| Evidence refs | `evidence_refs` | Source/evidence IDs per criterion; must come from A Long verified fixtures |
| Stop/abstain | Not present in DecisionProfile v1.0 | Add to orchestration response/envelope, not schema object: `next_action`, `stop_code`, `reason` |
| Skip history | Not present in DecisionProfile v1.0 | Orchestration/session event log; `asked_question_keys` alone cannot distinguish answered vs skipped |
| Preference revision history | Not present in DecisionProfile v1.0 | Append-only profile/audit event; current `preferences[]` holds latest state |
| Turn-by-turn state delta | Not present in schema | Contract-test envelope / session event log |

### 4.2. Journey state mapping

| Semantic condition | Suggested journey state | Notes |
|---|---|---|
| Use case still unclear | J1_UNCLEAR_NEED | MON-01 before initial answer |
| Need/use case defined; constraints being elicited | J2_NEED_DEFINED | MON-01 after use case; MON-02; AUD-01/02; EDGE fixtures |
| Candidate exploration/comparison with sufficient profile | J3_EXPLORE_COMPARE | Only after profile and product data gates |
| Hesitation / decision friction | J4_HESITATING | Use only if user expresses hesitation |
| Leaning to a choice but lacks confidence | J5_LEANING_NOT_CONFIDENT | Requires explicit user signal |
| Ready to decide | J6_READY_TO_DECIDE | Does not mean product is eligible; hard/evidence gates remain separate |

Do not force a journey-state transition just because a question was asked. State meaning belongs to Vân Anh; state persistence/validation belongs to Hoàng.

### 4.3. Reference engine mapping

Hoàng's `decision_engine.py` accepts:
- `DecisionProfile(hard_constraints, preference_weights)`
- `CandidateEvaluation(candidate_id, hard_checks, fit_by_preference)`

It returns:
- `eligibility_status`: eligible / verification_required / excluded
- `hard_failures`, `hard_unknowns`
- `fit_score` and `evidence_coverage`

Expected contract behavior:
- MON-02 hard compatibility fail → `excluded`.
- MON-01, AUD-01, AUD-02, EDGE-01, EDGE-02 have unresolved critical product evidence → `verification_required` if evaluated against candidates.
- No candidate evaluation supplied → orchestration returns `ABSTAIN` / `NEEDS_VERIFICATION`; do not synthesize an empty candidate or score.
- EDGE-01 skip of a non-blocking preference does not create hard failure.
- EDGE-02 changes current preference weights only; prior weights retained in audit history. A deterministic priority-to-weight mapping must be agreed before executable tests; this fixture deliberately avoids inventing one.

### 4.4. Contract gaps to resolve before implementation

1. **Stop envelope:** add typed `next_action` and `stop_code` to API response contract; values defined in §1.3.
2. **Question orchestration state:** add `skipped_question_keys` and an append-only turn/event log. Do not overload `asked_question_keys` to encode both answer and skip.
3. **Preference audit:** store revision events with old/new values, source, turn ID, timestamp and superseded/current status. Profile contains only current preferences.
4. **Preference scale:** schema allows priority >0 and ≤5, but fixture semantics use ordinal order. Agree conversion (or preserve ordered list as separate field) before mapping to numeric weights.
5. **Hard check evidence:** reference engine consumes status strings; contract layer must ensure PASS/FAIL is backed by verified evidence refs. User assertion of a host limitation can be captured as user-stated context, but product candidate capability still needs product evidence.
6. **User-deferred state:** engine has no user-defer behavior. Orchestrator must support `USER_DEFERRED` and no further question/recommendation until user resumes.
7. **No product fixtures yet:** candidate-level hard checks, fit values, evidence coverage and actual rankings remain untestable until A Long supplies verified model/variant evidence fixtures.

## 5. Acceptance matrix

| ID | Expected next question | State transition / key delta | Stop outcome | Critical failure |
|---|---|---|---|---|
| MON-01 | MON-Q1-detail → MON-Q3 | work use case user-stated; host/port unknown | NEEDS_VERIFICATION | infer gaming/color; claim compatibility |
| MON-02 | MON-Q3 then none | USB-C video hard check fail | NO_MATCH | soften hard constraint; score overrides fail |
| AUD-01 | AUD-Q3 → AUD-Q5 → AUD-Q8 | wear/fit risk and sound preference captured; fit evidence pending | NEEDS_VERIFICATION | universal comfort claim |
| AUD-02 | AUD-Q6 → AUD-Q4 → none | call context + user priority order | NEEDS_VERIFICATION | mic claim without test evidence |
| EDGE-01 | MON-Q2 → skip → MON-Q3 | skipped slot unknown; no repeat | NEEDS_VERIFICATION | re-ask skipped question |
| EDGE-02 | AUD-Q3 → none | current priority revised; history retained | NEEDS_VERIFICATION | stale priority remains active |

Pass condition per fixture: all expected question keys/order, state deltas, provenance and stop code match; no critical failure; no product assertion without evidence. A fixture fails regardless of any aggregate score if a critical failure occurs.

## 6. What is and is not executable now

**Ready for contract tests now**
- Parsing fixture envelope and validating required fields/enums.
- Expected question sequence and reason codes.
- State deltas for user-stated/unknown/inferred values.
- No-repeat behavior and skip tracking at orchestration layer.
- Preference revision/current-vs-history behavior.
- Stop/abstain outcome mapping.
- Decision Engine hard fail/unknown and soft null behavior using synthetic status values (not product claims).

**Blocked pending A Long**
- Candidate IDs tied to verified model/variant records.
- Real product hard-check PASS/FAIL and evidence refs.
- Per-criterion fit levels, score and evidence coverage based on reviewed criteria.
- Candidate ranking and explanation assertions.
- Any product-specific technical claim (monitor ports/refresh; headphone codec/mic/ANC/fit/battery).

**Owner handoff**
- **Vân Anh:** expected conversation behavior, question semantics, priority meaning, stop conditions and critical failures.
- **Hoàng:** schema/API envelope, state persistence, validator and executable contract tests; must not reinterpret semantics silently.
- **A Long:** product truth, criteria, evidence refs and verified candidate fixtures.
- **CEO:** resolve contract gaps / approve scope when product and technical owners have reviewed.

## 7. Versioning and change control

- Fixture IDs are stable. A semantic change to expected question, hard/soft classification, stop condition or critical failure requires a version update and reviewer note.
- Wording-only change may preserve fixture ID if semantic behavior is unchanged.
- Do not edit a golden expected result merely to make implementation pass; record defect, agree semantic owner and then update fixture with rationale.
- Fixtures are synthetic test cases, contain no customer PII, and are not production training data.
