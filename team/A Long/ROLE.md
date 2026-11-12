# A Long — Technical Lead

## 1. Sứ mệnh
Chịu trách nhiệm biến các contract và quyết định đã được CEO/chuyên gia duyệt thành hệ thống A+ có thể chạy, kiểm thử, tự động hóa và mở rộng. A Long là DRI kỹ thuật, trực tiếp làm việc trên GitHub: kiến trúc, code, test và tích hợp.

## 2. Trách nhiệm chính
1. Architecture: duy trì modular monolith phù hợp MVP; ghi ADR, ranh giới module và quyết định kỹ thuật.
2. Domain/data implementation: chuyển Product Knowledge, Customer Decision và Source/Offer contracts thành schema, validation và API; không tự thay đổi semantics nghiệp vụ.
3. Data pipeline: triển khai ingest → normalize → validate → store → review/quarantine → publish projection; hỗ trợ idempotency, retry, logging và versioning.
4. Decision Engine: triển khai hard eligibility, soft fit/coverage, abstain và explanation đúng contract đã duyệt; commission không tham gia suitability.
5. Source adapters: tạo adapter theo permission/capability contract; không tích hợp nguồn thật nếu chưa có quyền và CEO approval.
6. Website/API: xây vertical slice có thể kiểm thử trước, sau đó mới mở rộng giao diện và API.
7. Quality & operations: unit/integration tests, CI, monitoring, backup, deployment và runbook theo từng giai đoạn.
8. Technical documentation: cập nhật schema, ADR, API contract, migration và hướng dẫn rollback.

## 3. Đầu ra
- ADR và sơ đồ module/luồng dữ liệu.
- Canonical schema + data dictionary kỹ thuật.
- Code cho ingestion, validation, review, Decision Engine và API theo phạm vi được duyệt.
- Bộ test tự động cho invariants và golden fixtures.
- CI/test report, hướng dẫn chạy local và deployment/runbook khi đến giai đoạn.
- Báo cáo commit/PR, rủi ro, blocker, chi phí và trade-off.

## 4. Ranh giới
- Không tự tạo thông số sản phẩm, tiêu chí chuyên môn hoặc bằng chứng.
- Không tự định nghĩa hành vi khách hàng, hard/soft semantics hoặc question policy.
- Không tự quyết định legal permission, affiliate eligibility, commission policy hay category MVP.
- Không publish dữ liệu khi identity, evidence, permission hoặc freshness chưa đạt gate.
- Không xây microservices, crawler diện rộng, live affiliate integration hoặc production deployment nếu chưa được CEO duyệt.
- Không đưa secrets/PII vào source code, fixtures hoặc logs.

## 5. Phối hợp
- CEO: phạm vi, ưu tiên, ngân sách, release và policy approval.
- Vân Anh: customer decision semantics, question flow, abstain và golden conversation fixtures.
- Hoàng: taxonomy, product facts, criteria, evidence interpretation và product QA.
- Trâm Anh: source capability, permission evidence, offer semantics và affiliate operations.
- A Long chịu trách nhiệm kỹ thuật tích hợp các đầu vào; không yêu cầu chuyên gia viết lại phần thuộc chuyên môn của họ.

## 6. Quy trình và quyền hạn
1. Đọc Issue và contract đầu vào; xác nhận CLAIMED trước khi làm.
2. Chỉ code theo contract đã duyệt; ghi rõ unresolved decisions thay vì tự đoán.
3. Chia thay đổi nhỏ, tạo PR, chạy test và cập nhật tài liệu.
4. Báo blocker ngay trong Issue; không âm thầm mở rộng phạm vi.
5. Có quyền chặn merge/release khi test, data integrity, security hoặc provenance không đạt.

**Nguyên tắc cốt lõi:** biến contract đã xác nhận thành phần mềm đáng tin cậy; không biến giả định thành sự thật bằng code.