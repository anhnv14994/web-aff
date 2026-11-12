# Hoàng — Technical Blueprint & MVP Engineering Baseline

**Vai trò:** Technical Lead · **Dự án:** A+ — Affiliate Decision Platform  
**Phiên bản:** 1.0 · **Ngày:** 12/11/2026  
**Trạng thái:** Đề xuất kỹ thuật; chưa phải production architecture được CEO phê duyệt.

## 1. Rà soát hiện trạng

Đã rà soát README, Project Charter, ROLE.md của Vân Anh, A Long, Trâm Anh, Hoàng và báo cáo tâm lý hành vi v1.0.

Repository tại thời điểm rà soát là workspace tài liệu; chưa thấy application source, dependency manifest, database migrations, test suite, CI workflow, deployment config hoặc runbook kỹ thuật. Không có căn cứ kết luận đã có ứng dụng chạy.

**Đầu vào còn thiếu:** ngành hàng MVP; taxonomy/specification dictionary/evaluation criteria và hard thresholds của A Long; nguồn dữ liệu và quyền ingest/cache/hiển thị; affiliate network/terms/attribution; hosting, ngân sách, stack, domain, auth, SLO và retention policy.

**Quyết định phạm vi:** tạo technical baseline dùng chung, schema drafts và reference Decision Engine có thể kiểm thử. Không tự tạo tiêu chí sản phẩm, connector thật, giá/tồn kho thật hoặc production deployment.

## 2. MVP scope

**Trong phạm vi:** modular monolith; canonical catalog tách model/variant/offer/evidence; pipeline có provenance, retry và idempotency; decision profile/candidate evaluation contract; hard gate, preference scoring và evidence coverage; API draft; clickout/event contracts; unit tests; logging, backup và release gates.

**Ngoài phạm vi:** chọn ngành hàng; tự đặt product criteria; ingest nguồn chưa duyệt; ranking theo commission; microservices, data lake, event streaming, ML training, mobile app, B2B API; production secrets/deployment trước phê duyệt.

## 3. Kiến trúc logic

Đề xuất **modular monolith + background worker**. Một codebase và một ranh giới triển khai giúp MVP dễ hiểu, test, deploy và rollback. Giữ module boundaries để có thể tách sau nếu tải hoặc ownership chứng minh cần thiết.

| Module | Trách nhiệm | Dữ liệu sở hữu |
|---|---|---|
| Catalog | Category, model, variant, canonical specifications | Product/model/variant |
| Source & Evidence | Source registry, raw snapshots, assertions, verification | Source/evidence |
| Offer | Merchant, offer, price observations, availability/freshness | Offer/merchant/price |
| Ingestion | Connectors, mapping, validation, retry, matching, exception queue | Run/job/exception |
| Decision | Profile, constraints, candidate evaluation, fit, coverage, explanation | Decision session/evaluation |
| Affiliate | Program, link, redirect, clickout status | Affiliate link/click |
| Analytics | Event ingestion and metrics | Events |
| Admin/QA | Review queue, approvals, audit history | Review/audit |

Affiliate và Analytics không được ghi vào suitability score. External providers phải đi qua adapters; domain core không phụ thuộc format riêng của provider.

## 4. Architecture Decision Records

### ADR-001 — Modular monolith
**Trạng thái:** Đề xuất cho MVP. Một codebase, module boundaries và worker process dùng chung domain contracts. Chọn vì team nhỏ, chưa có tải lớn hoặc lý do vận hành microservices. Xem xét lại nếu scale/ownership độc lập được chứng minh.

### ADR-002 — Relational canonical store + raw snapshots
**Trạng thái:** Đề xuất; hosting/vendor còn chờ duyệt. Relational DB cho quan hệ, uniqueness và transaction; lưu snapshot nguồn riêng. PostgreSQL là ứng viên, không phải stack đã được duyệt. Không overwrite làm mất provenance.

### ADR-003 — Evidence là dữ liệu hạng nhất
**Trạng thái:** Đề xuất chấp nhận. Claim quan trọng lưu source, timestamp, verification status, confidence và reviewer. Nguồn thiếu/mâu thuẫn phải giữ trạng thái, không âm thầm chọn giá trị.

### ADR-004 — Fit độc lập commission
**Trạng thái:** Bất biến. Commission, EPC và revenue không nằm trong input/feature của Decision Engine. Cùng profile và candidate evaluations phải cho ranking giống nhau dù merchant/link/commission thay đổi.

### ADR-005 — Hard constraint UNKNOWN fail closed
**Trạng thái:** Đề xuất chấp nhận theo mô hình Vân Anh. FAIL → excluded; UNKNOWN/missing → verification_required; chỉ PASS mọi hard constraint mới eligible.

### ADR-006 — Không auto-merge identity khi mơ hồ
**Trạng thái:** Đề xuất chấp nhận. Matching dựa trên identifiers và variant signals; tên gần giống hoặc ảnh không đủ làm bằng chứng duy nhất. Ambiguous → review queue; threshold phải đo trên labeled set của ngành MVP.

## 5. Canonical data model

- **ProductModel:** model/series cụ thể trong category.
- **ProductVariant:** cấu hình/biến thể ảnh hưởng quyết định hoặc tương thích; Product Expert quyết định thuộc tính nào tạo variant.
- **SpecificationDefinition:** định nghĩa attribute, kiểu dữ liệu, unit dimension và version; A Long duyệt.
- **Evidence/Assertion:** claim về subject/attribute, gắn source, timestamp, verification status.
- **Source:** manufacturer, merchant, reviewer độc lập, regulator hoặc dataset đã duyệt; có terms status.
- **Merchant:** nhà bán và domain đã xác minh.
- **Offer:** điều kiện bán của merchant tại thời điểm kiểm tra.
- **PriceObservation:** lịch sử giá append-only; không overwrite.
- **AffiliateProgram/Link:** terms, routing và tracking; tách khỏi ranking.
- **IngestionRun/Exception:** trạng thái pipeline và lỗi cần xử lý.
- **DecisionSession/Evaluation:** snapshot profile, candidate evaluation và rule version để replay.
- **AnalyticsEvent/AuditLog:** event đo lường và lịch sử thay đổi.

| Entity | Trường cốt lõi | Quy tắc |
|---|---|---|
| Category | id, parent_id, slug, taxonomy_version | Versioned; CEO/Product Expert duyệt |
| ProductModel | id, category_id, brand, model_name, normalized_model_key | ID nội bộ bất biến; tên hiển thị không phải primary key |
| ProductVariant | id, model_id, variant_key, attributes, region | Tách biến thể ảnh hưởng quyết định |
| SpecificationDefinition | category_id, attribute_key, value_type, unit_dimension, version | A Long duyệt |
| Evidence | subject, claim_key, raw/normalized value, source_id, observed_at, verification_status, confidence | Giữ claim và nguồn, kể cả mâu thuẫn |
| Source | publisher, type, URL, accessed_at, terms_status | Allowlist; terms phải review |
| Merchant | id, name, country, verified_domain, status | Không tự coi domain là official |
| Offer | model_id, optional variant_id, merchant_id, currency, price, availability, source_id, checked_at | Có freshness status |
| PriceObservation | offer_id, amount, currency, observed_at, source_id | Append-only |
| AffiliateProgram/Link | program, terms_version, merchant, target, destination, status | Secret không lưu plain text |
| IngestionRun/Exception | run_id, source, state, counts, error_code, record_ref | Có correlation ID |
| DecisionSession/Evaluation | session, profile snapshot, candidate checks, fit, coverage, rule version | Có thể replay |
| AnalyticsEvent/AuditLog | event_id, actor/action, entity_ref, occurred_at | Minimize PII |

Mỗi record có stable internal ID, schema_version, UTC timestamps, status và source/evidence refs phù hợp. Confidence không thay thế verification status. JSON Schema drafts nằm trong thư mục schemas.

## 6. Data pipeline

Luồng: DISCOVER → FETCH → STORE_RAW → PARSE → NORMALIZE → VALIDATE → MATCH → REVIEW (if needed) → UPSERT_CANONICAL → PUBLISH.

| Stage | Gate | Xử lý lỗi |
|---|---|---|
| Discover | Source allowlisted và terms approved | Stop nếu chưa duyệt |
| Fetch | Response + request metadata; respect rate limits | Retry transient; tôn trọng 429/Retry-After |
| Store raw | Payload gốc, hash, fetched_at đã lưu | Không normalize nếu raw chưa lưu |
| Parse | Parser version nhận biết format | Dead-letter khi schema nguồn đổi |
| Normalize | Unit/currency/enum mapping có version | Không chuyển đổi khi dimension mơ hồ |
| Validate | Required fields, range, currency, URL, timestamp hợp lệ | Exception queue |
| Match | Identifier và variant signals đủ tin cậy | Human review nếu ambiguous |
| Upsert | Transactional, idempotent theo source key/fingerprint | Rollback và retry an toàn |
| Publish | Qua data/freshness/evidence gates | Hold/suppress; không âm thầm publish |

- Mỗi run có run_id; record có source_record_key hoặc stable fingerprint.
- Replay cùng snapshot không tạo duplicate canonical record.
- Retry lỗi transient có exponential backoff + jitter; validation/schema errors không retry vô hạn.
- Sau retry limit → dead-letter/exception + alert.
- Model và evidence writes phải transactionally consistent.
- Giữ raw snapshot theo retention policy được duyệt.

**Publish severity:** Block sai identity nghiêm trọng, claim quan trọng thiếu evidence, currency/amount sai hoặc URL không allowlist. Hold khi variant ambiguous, nguồn mâu thuẫn, required value thiếu hoặc giá/availability quá cũ. Chỉ allow missing soft attribute nếu không ảnh hưởng hard fit và policy category cho phép.

Matching có thể dùng GTIN/MPN, manufacturer + model code, variant identifiers, region/capacity/config. Không dùng similarity tên/ảnh làm chứng cứ duy nhất. Threshold phải đo trên labeled examples; chưa tự đặt ở v1.0.

## 7. Customer Decision Engine contract

### Input boundary
Decision Engine nhận decision profile; candidate evaluations theo rules đã được Product Expert duyệt; evidence metadata; freshness/verification flags; rule version. Không tự đọc vendor marketing copy để suy specs, không tự chọn tiêu chí ngành hàng, không nhận commission.

### Hard gates
- PASS: có đánh giá và bằng chứng đáp ứng.
- FAIL: có bằng chứng không đáp ứng → excluded.
- UNKNOWN/missing → verification_required.

Chỉ candidate PASS tất cả hard constraints mới vào nhóm eligible.

### Soft preference score
Fit level theo báo cáo Vân Anh: 0 = không đáp ứng; 1 = một phần; 2 = tốt; null/UNKNOWN = chưa có bằng chứng.

`fit_score = 100 × Σ(weight_i × fit_i) / [2 × Σ(weight_i của tiêu chí đã biết)]`

`evidence_coverage = Σ(weight_i đã biết) / Σ(weight_i của toàn bộ soft preferences)`

- Score chỉ dùng soft criteria đã biết; unknown không tự quy về 0 hoặc 2.
- Coverage độc lập score; coverage thấp phải được trình bày rõ.
- Candidate hard UNKNOWN không vào ranked list dù điểm soft cao.
- Score không phải xác suất, chứng nhận chất lượng hoặc bảo đảm kết quả.
- Tie-breaker deterministic bằng stable candidate ID, không dùng giá/commission.
- Reference implementation chỉ xử lý hard checks và weighted aggregation đầu vào; không tính fit từ raw specs.

Mỗi candidate output cần candidate_id, eligibility_status, hard checks + evidence refs, fit score (nullable), evidence coverage, per-criterion fit/weight/evidence, strengths, tradeoffs, unknowns, source updated_at và rule version.

Question orchestration sử dụng state J1–J6, friction F1–F9 và question value filter của Vân Anh. Không hỏi slot đã trả lời; ưu tiên làm rõ hard blockers; dừng hỏi khi không còn câu hỏi có decision value.

## 8. API contract draft

| Method | Path | Mục đích |
|---|---|---|
| GET | /api/v1/categories | Category đã publish |
| GET | /api/v1/products?query=&category_id= | Search models, pagination |
| GET | /api/v1/products/{model_id} | Model + variants + evidence summary |
| POST | /api/v1/decision-sessions | Tạo anonymous session mặc định |
| PATCH | /api/v1/decision-sessions/{id}/profile | Cập nhật validated profile |
| POST | /api/v1/decision-sessions/{id}/next-question | Next question hoặc no-question |
| POST | /api/v1/decision-sessions/{id}/recommendations | Evaluate/rank candidates |
| POST | /api/v1/compare | So sánh shortlist cùng tiêu chí |
| GET | /go/{affiliate_link_id} | Controlled clickout redirect |
| POST | /api/v1/events | Event ingestion + dedupe |

API phải validate schema/size, rate-limit public endpoints, version breaking changes, không expose raw source payload/secrets/internal notes. Clickout chỉ resolve URL từ affiliate link record active, allowlisted; không nhận arbitrary destination URL từ client.

## 9. Affiliate tracking & analytics

| Event | Properties tối thiểu |
|---|---|
| search_submitted | event_id, session_id, query_class, category_id |
| decision_question_shown | journey_state, question_key, rule_version |
| decision_answered | question_key, answer_type, skipped |
| recommendation_impression | candidate_ids, decision_version, evidence_coverage_bucket |
| comparison_viewed | candidate_ids, comparison_keys |
| affiliate_clickout | click_id, affiliate_link_id, merchant_id, model_id, variant_id, session_id |
| recommendation_feedback | candidate_id, feedback_type |

Không gửi raw PII trong analytics; event_id idempotent; không đưa user identifiers vào sub-ID khi chưa duyệt.

Clickout: UI gọi /go/{affiliate_link_id} → lookup active record → validate host/program → create click_id + event/outbox → redirect destination cấu hình. Link invalid/inactive → fallback message; không redirect arbitrary. Chưa bật partner clickout thật nếu CEO/Affiliate owner chưa xác nhận network, terms, attribution, disclosure và link tests.

## 10. Quality engineering & acceptance

### P0 — release blocking
- Không auto-merge model/variant ambiguous.
- Không publish critical claim thiếu source/evidence.
- Hard FAIL không lọt eligible; hard UNKNOWN không hiển thị như PASS.
- UNKNOWN spec không thành default value.
- Commission không đi vào fit/ranking.
- Clickout không redirect host ngoài allowlist.
- Không leak secret/PII trong API, logs, fixtures hoặc analytics.

| ID | Scenario | Expected result |
|---|---|---|
| DATA-01 | Thiếu required ID/category | Reject + reason |
| DATA-02 | Tên gần giống nhưng MPN khác | Không auto-merge |
| DATA-03 | Region/config khác | Variant riêng hoặc review |
| DATA-04 | Claim quan trọng thiếu source | Không publish |
| DATA-05 | Nguồn mâu thuẫn | Disputed; giữ assertions |
| PIPE-01 | Replay snapshot | Không duplicate |
| PIPE-02 | Timeout transient | Retry hữu hạn; state rõ |
| PIPE-03 | HTTP 429 | Respect Retry-After |
| PIPE-04 | Currency/URL/timestamp invalid | Reject/hold |
| DEC-01 | Hard FAIL | Excluded |
| DEC-02 | Hard UNKNOWN/missing | Verification required |
| DEC-03 | Soft UNKNOWN | Không thành 0; coverage giảm |
| DEC-04 | Thay commission | Ranking không đổi |
| DEC-05 | Input + rule version giống | Output deterministic |
| DEC-06 | Candidate được rank | Có criteria/evidence explanation |
| API-01 | Profile invalid | Safe 4xx validation error |
| API-02 | Arbitrary clickout URL | Reject; no open redirect |
| API-03 | Event chứa PII ngoài policy | Redact/drop |
| AFF-01 | Click hợp lệ | Một click_id/event trước redirect |
| AFF-02 | Link inactive/unsupported host | Không redirect |
| OPS-01 | Worker restart | Resume/idempotent hoặc fail rõ |
| OPS-02 | Restore backup | Phục hồi trong RPO/RTO đã duyệt |

Vân Anh sở hữu behavioral expectations T01–T14. A Long sở hữu product truth và evaluation rules. Hoàng biến expected outcomes đã duyệt thành tests; không tự thay đổi chuyên môn. Trâm Anh hỗ trợ manual checklist/defect log; người phụ trách chuyên môn xác nhận lỗi.

## 11. Security, privacy & operations

- Secrets qua environment/secret manager; không commit hoặc log.
- Least privilege cho service accounts, DB users và CI.
- Source adapters allowlist; outbound validation chống SSRF/open redirect.
- HTTPS; encryption-at-rest theo hosting.
- Input validation, output encoding, size/rate limits; audit admin/publish/rule changes.
- Anonymous random session ID mặc định; minimize PII; retention/deletion/consent cần CEO/legal review trước production.
- Structured logs: timestamp, severity, module, request_id/run_id, entity_ref, error_code; không log credentials/PII.
- Metrics: ingestion counts/retries/duration, rejected records, match ambiguity, stale offers, invalid links, API latency/errors, verification-required rate, coverage, clickout status.
- Alerts: source failure/schema change, validation spike, invalid clickout host, API 5xx, backup failure, stale catalog.
- Backup DB theo budget/hosting; chốt RPO/RTO/retention; test restore; migration có rollback note; không dùng fixtures ghi đè production.

## 12. Decision gates / phối hợp

| Owner | Cần bàn giao hoặc phê duyệt | Hoàng thực hiện |
|---|---|---|
| CEO | MVP category, budget/hosting, stack constraints, scope, KPI, risk acceptance | Chốt ADR triển khai, environment, API scope, release plan |
| A Long | Taxonomy, identifiers, spec dictionary, use-case criteria, hard thresholds, evidence rules | Mapping schema, validators, evaluator config, product tests |
| Vân Anh | Golden fixtures T01–T14, state transitions, question keys, required slots | Contract tests cho journey/question/explanation |
| Affiliate owner/CEO | Network, approved sources, terms, attribution, disclosure | Adapter, redirect, link health, event mapping |
| Trâm Anh | Catalog/source spreadsheet có nguồn; manual QA findings | Import validation, exception queue, triage |

Câu hỏi trước production: ngành hàng và taxonomy owner? Nguồn nào được phép ingest/cache? Freshness SLA? Ai duyệt hard constraints? Stack/hosting/domain/admin access? Affiliate terms/attribution/disclosure? Retention/consent/deletion policy?

## 13. Lộ trình kỹ thuật

| Phase | Công việc | Exit criteria |
|---|---|---|
| E0 — Align | Chốt category candidates, data ownership, stack/budget | Scope và data authority rõ |
| E1 — Foundation | Repo structure, migrations, schema validation, logging, CI, secrets | Build/test CI chạy; schema versioned |
| E2 — Data vertical slice | Approved adapter → raw → normalize → validate → review → canonical | End-to-end idempotent, có audit |
| E3 — Decision vertical slice | Profile, hard gate, scoring, coverage, explanation, golden tests | T01–T14 liên quan pass; commission isolation pass |
| E4 — User journey | Search/detail/compare/session/question/recommendation UI + events | Journey end-to-end với data đã duyệt |
| E5 — Affiliate pilot | Approved clickout, disclosure, monitoring, backup/restore | Clickout tests + release sign-off |

Không estimate ngày hoặc cloud cost khi chưa biết stack, hosting, source, network và category.

## 14. Deliverables của baseline

1. Blueprint kiến trúc, ADR và MVP gates.
2. Canonical catalog JSON Schema draft.
3. Decision profile/candidate evaluation JSON Schema draft.
4. Reference Decision Engine tổng quát, không có product-specific rules hoặc commission input.
5. Unit tests cho hard gates, UNKNOWN, score, coverage, deterministic ordering và validation.
6. Technical acceptance matrix, security/operations/release checklist.

**Giới hạn:** Đây là technical baseline và executable reference core, không phải website production. Chưa có connector thật, database migration, frontend, affiliate account, deploy pipeline hoặc ngành hàng MVP được duyệt.
