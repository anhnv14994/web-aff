# Hoàng — Báo cáo triển khai technical baseline

**Ngày:** 12/11/2026  
**Phiên bản:** 1.0  
**Repository:** anhnv14994/web-aff  
**Nhánh:** main  
**Trạng thái:** Technical baseline committed; chưa phải production MVP.

## 1. Tóm tắt kết quả

Đã đọc ROLE.md của Hoàng và đối chiếu với README, Project Charter, ROLE của A Long, Vân Anh, Trâm Anh cùng báo cáo hành vi của Vân Anh.

Đã triển khai phần nền tảng có thể làm an toàn khi ngành hàng MVP, stack và nguồn dữ liệu chưa được chốt:

- Technical blueprint với kiến trúc modular monolith + worker, module boundaries, 6 ADR, canonical data model, pipeline contract, Decision Engine contract, API draft, analytics, security, release gates và lộ trình.
- Canonical Catalog JSON Schema draft.
- Decision Profile / Candidate Evaluation JSON Schema draft.
- Reference Decision Engine thực thi hard gates, weighted preference fit, evidence coverage và deterministic ordering.
- 14 unit tests.
- Script kiểm tra cú pháp JSON Schema và local $ref.
- GitHub Actions workflow cho test engine và schema checks.

## 2. Các file đã commit

| File | Nội dung |
|---|---|
| [TECHNICAL-BLUEPRINT-v1.0.md](./TECHNICAL-BLUEPRINT-v1.0.md) | Kiến trúc, ADR, schema concept, pipeline, API/event contracts, quality/security/ops và decision gates |
| [canonical-catalog.schema.json](./schemas/canonical-catalog.schema.json) | Schema draft cho model, variant, source, evidence, merchant, offer và price observation |
| [decision-profile.schema.json](./schemas/decision-profile.schema.json) | Schema draft cho user decision profile và candidate evaluation |
| [decision_engine.py](./reference/decision_engine.py) | Reference implementation của hard gate và scoring tổng quát |
| [test_decision_engine.py](./reference/test_decision_engine.py) | Unit tests cho các bất biến của engine |
| [validate_schemas.py](./reference/validate_schemas.py) | Kiểm tra JSON parse và local JSON Schema references |
| [README.md](./reference/README.md) | Hướng dẫn chạy reference engine/tests |
| [hoang-reference.yml](../../.github/workflows/hoang-reference.yml) | CI workflow chạy unit tests và schema checks |

## 3. Kết quả kiểm tra đã thực hiện

| Kiểm tra | Kết quả |
|---|---|
| Python unit tests | **14/14 PASS** |
| Python bytecode compilation | PASS |
| Workflow YAML syntax parse | PASS |
| JSON Schema JSON parsing | PASS |
| Local $ref target existence | Không phát hiện tham chiếu nội bộ bị thiếu |

**Lưu ý CI:** Workflow đã được thêm vào repository. Chưa xác nhận được một GitHub Actions run hoàn tất; không coi việc tạo workflow là bằng chứng CI trên GitHub đã pass. Kiểm tra 14/14 được chạy cục bộ trên reference implementation và test suite tương ứng.

## 4. Các nguyên tắc được bảo vệ trong implementation

1. Hard constraint FAIL loại candidate.
2. Hard constraint UNKNOWN hoặc thiếu check đưa candidate vào nhóm verification_required, không xem như PASS.
3. Soft preference UNKNOWN không bị quy về điểm 0; evidence coverage được tính riêng.
4. Ranking chỉ dùng các trọng số và fit levels được truyền vào từ evaluator đã được duyệt.
5. Commission không phải input của Decision Engine.
6. Kết quả tie được xử lý deterministic bằng candidate ID.
7. Engine không tự đọc marketing copy, tự suy ra thông số hoặc tự định nghĩa tiêu chí ngành hàng.

## 5. Chưa triển khai / không được hiểu nhầm

Đây **không phải website MVP production**. Chưa có:

- Frontend, search UI, compare UI hoặc admin UI.
- Database migrations / live database.
- Ingestion connector cho nguồn sản phẩm thực.
- Canonical catalog chứa dữ liệu sản phẩm thật.
- Human review queue chạy trên application.
- Affiliate account, production clickout, partner attribution hoặc đối soát commission.
- Hosting, production secrets, deployment pipeline hoặc monitoring đang chạy.

Không triển khai các phần này vì chưa có các quyết định đầu vào và dữ liệu có thẩm quyền. Tự tạo chúng lúc này sẽ biến giả định thành sự thật, trái với ROLE.md và Project Charter.

## 6. Việc cần CEO / chuyên gia xác nhận để đi tiếp

### CEO
- Chọn ngành hàng MVP và xác nhận phạm vi user journey.
- Chốt stack, hosting, ngân sách, domain và quyền admin.
- Xác nhận nguồn dữ liệu được phép dùng, policy privacy/retention và KPI pilot.
- Chốt affiliate network và các điều khoản/tracking/disclosure liên quan.

### A Long — Product Expert
- Bàn giao taxonomy/version, model/variant identifiers và specification dictionary.
- Xác định use-case evaluation criteria, hard constraints, ngưỡng và evidence rules.
- Cung cấp labeled sample để thiết kế kiểm thử identity matching và product evaluator.

### Vân Anh — Customer Psychology
- Bàn giao golden fixtures T01–T14 với expected state/action và question keys đủ cấu trúc cho contract tests.
- Xác nhận journey transitions, required slots và explanation acceptance.

### Trâm Anh
- Thu thập catalog/source records vào template sau khi source/category được duyệt.
- Chạy manual QA và cung cấp defect evidence; không tự phê duyệt kết luận chuyên môn.

## 7. Đề xuất bước triển khai tiếp theo

Sau khi CEO chốt category, data authority và stack:

1. Chốt ADR và implementation stack.
2. Tạo migration/database layer theo hai JSON Schema đã được chuyên gia review.
3. Làm một data vertical slice từ một nguồn được duyệt: raw → normalize → validate → review → canonical publish.
4. Làm một decision vertical slice dùng evaluation rules do A Long duyệt và golden tests do Vân Anh sở hữu.
5. Chỉ sau khi các vertical slice pass mới triển khai UI, tracking partner thật và pilot có kiểm soát.

**Kết luận:** Hoàng đã bàn giao technical design và reference core có kiểm thử cho các quy tắc tổng quát. Các thành phần phụ thuộc ngành hàng, dữ liệu, affiliate và hạ tầng vẫn đang ở trạng thái chờ quyết định; chưa được tuyên bố là hoàn thành.
