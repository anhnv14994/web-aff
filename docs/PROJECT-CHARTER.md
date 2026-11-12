# A+ — Project Charter & Operating Process

> Phiên bản: 1.0  
> Trạng thái: Định hướng điều hành; ngành hàng MVP chưa được chốt  
> Thị trường khởi đầu: Việt Nam  
> Chủ dự án / CEO: ChatGPT trong vai trò CEO chiến lược và điều phối  
> Nhân sự hiện có: Vân Anh — Customer Psychology & Decision Science

## 1. Sứ mệnh

Xây dựng A+ thành một nền tảng affiliate tự động giúp người tiêu dùng Việt Nam hiểu rõ nhu cầu, đánh giá các lựa chọn và đưa ra quyết định mua hàng phù hợp — sau đó kết nối họ với nhà bán phù hợp thông qua affiliate.

A+ không phải website chỉ gom sản phẩm, bảng giá hoặc nội dung SEO hàng loạt. Giá trị cốt lõi là **giúp khách hàng ra quyết định tốt hơn**.

## 2. Mục tiêu kinh doanh và sản phẩm

### Mục tiêu chính

1. **Customer value:** giảm bối rối, giảm thời gian tìm hiểu, giúp khách hàng hiểu rõ ưu/nhược điểm và đánh đổi.
2. **Decision quality:** đề xuất dựa trên nhu cầu và bằng chứng; giải thích được vì sao phù hợp và khi nào không phù hợp.
3. **Automation:** tự động hóa thu thập, chuẩn hóa, kiểm tra, phân tích, xuất bản, cập nhật và đo lường.
4. **Affiliate revenue:** tạo clickout và hoa hồng có thể theo dõi, đối soát; phát triển doanh thu bền vững.
5. **Search & AI visibility:** nội dung hữu ích, đáng tin, có cấu trúc và dễ được công cụ tìm kiếm/hệ thống AI truy xuất, hiểu và trích dẫn.

**AI visibility là kênh phân phối, không phải đích đến.** Không đánh đổi chất lượng quyết định hoặc niềm tin để lấy lượt hiển thị.

### Chỉ số cần theo dõi

- Chất lượng dữ liệu: độ đầy đủ, độ chính xác, tỷ lệ model/variant ghép đúng, độ mới giá và tình trạng hàng.
- Chất lượng quyết định: tỷ lệ hoàn thành luồng tư vấn/so sánh, mức độ phù hợp qua đánh giá mẫu, tỷ lệ khách hàng hiểu được lý do đề xuất.
- Kinh doanh: clickout rate, outbound clicks, conversion nếu đối tác cung cấp, commission, EPC và doanh thu theo nguồn.
- Phân phối: organic impressions/clicks, landing pages có traffic, truy vấn và URL được AI/search trích dẫn khi có dữ liệu đo.
- Vận hành: tỷ lệ pipeline thành công, lỗi dữ liệu, nội dung cần sửa, chi phí vận hành trên mỗi model/trang.

Không dùng một chỉ số đơn lẻ làm đại diện cho thành công.

## 3. Nguyên tắc bất biến

1. **Fit trước commission:** xếp hạng theo mức độ phù hợp với khách hàng; hoa hồng không được làm thay đổi thứ hạng phù hợp.
2. **Evidence before claims:** không bịa thông số, giá, tồn kho, đánh giá, trải nghiệm hoặc nguồn dẫn.
3. **Nguồn gốc rõ ràng:** phân biệt dữ kiện từ nhà sản xuất, nhà bán, nguồn độc lập, dữ kiện đã kiểm chứng và giả thuyết.
4. **Không chắc thì không khẳng định:** dữ liệu thiếu/mâu thuẫn/rủi ro cao phải gắn cờ, giảm mức hiển thị hoặc chờ xác minh.
5. **Minh bạch đánh đổi:** nêu rõ ưu điểm, nhược điểm, giới hạn và trường hợp không nên mua.
6. **Không thao túng:** không tạo khan hiếm giả, không gây áp lực, không che giấu lợi ích affiliate.
7. **Human governance:** con người thiết lập chính sách, duyệt thay đổi quan trọng và audit định kỳ; vận hành thường ngày tự động.
8. **Scope discipline:** chưa mở rộng đa ngành, app, API B2B, tự huấn luyện model hoặc microservices nếu chưa có bằng chứng kinh doanh/kỹ thuật.
9. **Privacy by design:** chỉ thu thập dữ liệu cá nhân thực sự cần thiết; không suy đoán đặc điểm nhạy cảm của khách hàng.

## 4. Ba động cơ vận hành

### 4.1 Product & Offer Engine

- Thu thập dữ liệu sản phẩm, model, variant, thông số, giá, nhà bán, tồn kho và affiliate URL.
- Chuẩn hóa danh tính sản phẩm; tránh gộp nhầm model/phiên bản.
- Ghi nhận nguồn, thời điểm cập nhật, độ tin cậy và lịch sử thay đổi.
- Phát hiện giá bất thường, link hỏng, dữ liệu cũ, sai khác giữa các nguồn.
- Chỉ đưa dữ liệu đủ tin cậy vào luồng tư vấn/xuất bản.

### 4.2 Customer Decision Engine

- Tiếp nhận nhu cầu và ngữ cảnh sử dụng.
- Hỏi ít nhưng đúng; dừng hỏi khi đã đủ thông tin.
- Lọc lựa chọn không phù hợp trước, sau đó xếp hạng theo tiêu chí và trọng số có thể giải thích.
- Chuyển thông số kỹ thuật thành ý nghĩa thực tế với khách hàng.
- Trình bày trade-off, bằng chứng, điểm chưa chắc chắn và lựa chọn thay thế.
- Không biến hệ thống thành chatbot bán hàng gây áp lực.

### 4.3 Affiliate & Growth Engine

- Tạo trang sản phẩm, trang so sánh và nội dung giải thích có giá trị độc lập.
- Xây dựng SEO kỹ thuật, cấu trúc thông tin và khả năng truy xuất cho AI.
- Quản lý affiliate link, clickout tracking, attribution và đối soát khi dữ liệu cho phép.
- Đo hiệu quả từng trang, nhóm nhu cầu, sản phẩm, nhà bán và nguồn traffic.
- Tối ưu theo giá trị khách hàng và doanh thu thực, không tối ưu vanity metrics.

## 5. Cơ cấu nhân sự đề xuất

A+ hiện có CEO và Vân Anh. **Không cần tuyển đủ mọi vai trò ngay lập tức.** Cần phân định đủ năng lực; một người có thể kiêm nhiệm ở giai đoạn đầu.

### Vai trò hiện có

#### CEO — Strategy, Product & Business Owner

- Giữ mục tiêu, phạm vi, ưu tiên và ngân sách.
- Chọn ngành hàng MVP dựa trên bằng chứng.
- Quyết định mô hình kinh doanh, tiêu chuẩn chất lượng và mức rủi ro chấp nhận.
- Phân công, xử lý xung đột giữa chuyên môn, phê duyệt các quyết định quan trọng.
- Theo dõi KPI, yêu cầu thử nghiệm và quyết định tiếp tục/dừng/mở rộng.
- Không tự giả định chuyên môn kỹ thuật sản phẩm khi chưa có bằng chứng.

#### Vân Anh — Customer Psychology & Decision Science Advisor

- Nghiên cứu nhu cầu, động lực, nỗi lo, rào cản và hành vi ra quyết định.
- Thiết kế customer decision journey, adaptive question framework và decision-friction model.
- Đề xuất logic trình bày khuyến nghị, trade-off và bằng chứng.
- Xây dựng tình huống kiểm thử, golden dataset và tiêu chí đánh giá phản hồi của hệ thống.
- Phân biệt quan sát đã có bằng chứng với giả thuyết tâm lý.
- Review định kỳ trải nghiệm và đề xuất cải tiến.

**Ngoài phạm vi:** tư vấn trực tiếp khách hàng, bán hàng/chốt đơn, đánh giá kỹ thuật sản phẩm, thu thập/đối soát dữ liệu giá, lập trình hoặc triển khai hệ thống, tối ưu thứ hạng theo hoa hồng.

### Các vai trò cần bổ sung

#### 1. Product Domain Expert — Chuyên gia ngành hàng

**Ưu tiên: rất cao sau khi chốt ngành hàng.**

- Xây taxonomy và kiến thức nền của ngành.
- Xác định tiêu chí đánh giá, thông số quan trọng và giới hạn kỹ thuật.
- Phân biệt model/variant; giải thích khác biệt có ý nghĩa.
- Xác định sản phẩm phù hợp/không phù hợp theo tình huống.
- Cung cấp nguồn bằng chứng và rà soát các nhận định chuyên môn.

**Bàn giao:** Product Knowledge Base, Evaluation Criteria, Model Differentiation, Use-case Matrix, Evidence Register.

Có thể bắt đầu bằng chuyên gia cộng tác theo ngành hàng, chưa cần tuyển full-time.

#### 2. Technical Lead / Automation Engineer — Trưởng kỹ thuật và tự động hóa

**Ưu tiên: rất cao khi bắt đầu xây MVP.**

- Thiết kế kiến trúc vừa đủ, ưu tiên modular monolith trước khi có lý do tách dịch vụ.
- Xây pipeline thu thập → chuẩn hóa → kiểm tra → lưu trữ → xuất bản.
- Triển khai Customer Decision Engine và các API/UI cần thiết.
- Tích hợp affiliate tracking, analytics, logging, monitoring và alerting.
- Viết test, kiểm soát chất lượng dữ liệu/nội dung, bảo đảm backup và khả năng phục hồi.
- Biến quy tắc của chuyên gia thành cấu hình/logic có thể kiểm thử.

**Bàn giao:** architecture note, data schema, pipeline, application, test suite, deployment/runbook, monitoring.

Đây là vị trí kỹ thuật đầu tiên nên có người chịu trách nhiệm xuyên suốt; có thể là full-stack engineer giỏi automation ở giai đoạn đầu.

#### 3. Product & Market Data Analyst / Data Operations

**Ưu tiên: cao; có thể kiêm với kỹ thuật lúc MVP nhỏ.**

- Khảo sát nguồn dữ liệu và quyền sử dụng dữ liệu.
- Chuẩn hóa catalog, model, variant, thuộc tính và đơn vị đo.
- Đánh giá độ phủ, độ mới, độ chính xác và độ tin cậy của nguồn.
- Thiết lập quy tắc matching, deduplication, anomaly detection và data QA.
- Theo dõi giá, nhà bán, tồn kho và tình trạng affiliate URL.

**Bàn giao:** source map, canonical catalog, data dictionary, quality rules, exception queue, data quality report.

Không được tự suy luận thông số thiếu hoặc tự ghép model khi độ tin cậy thấp.

#### 4. Affiliate Partnerships & Operations — Đối tác và vận hành affiliate

**Ưu tiên: trung bình-cao; ban đầu CEO có thể kiêm.**

- Tìm và đánh giá network/chương trình affiliate phù hợp tại Việt Nam.
- Kiểm tra điều kiện tham gia, ngành hàng, cookie window, attribution, chính sách quảng cáo và điều kiện thanh toán.
- Quản lý tracking template, sub-ID, deeplink, link health và thay đổi chính sách.
- Đối soát click, đơn hàng, hủy/hoàn và hoa hồng khi đối tác cung cấp dữ liệu.
- Báo cáo hiệu quả theo network/merchant/category.

**Bàn giao:** affiliate partner matrix, terms register, tracking specification, reconciliation report, issue log.

Không can thiệp vào suitability score hoặc ép hệ thống đề xuất nhà bán trả hoa hồng cao hơn.

#### 5. SEO / GEO & Content Growth Specialist

**Ưu tiên: trung bình; nên thuê theo dự án hoặc part-time ở giai đoạn đầu.**

- Nghiên cứu truy vấn và search intent theo nhu cầu thực tế.
- Thiết kế information architecture, internal linking và template trang.
- Đảm bảo nội dung có nguồn, có cấu trúc, dễ đọc và trích xuất.
- Theo dõi indexation, organic performance và AI citation/visibility khi nền tảng có báo cáo.
- Kiểm tra nội dung mỏng, trùng lặp, lỗi canonical, schema không khớp nội dung hiển thị.
- Đề xuất thử nghiệm tăng trưởng và đo lường.

**Bàn giao:** keyword/intent map, page architecture, content brief, technical SEO checklist, growth experiment report.

Không dùng thủ thuật schema/llms.txt hay nội dung hàng loạt với kỳ vọng bảo đảm được AI trích dẫn.

#### 6. QA / Research Evaluator — Kiểm định chất lượng

**Ưu tiên: chưa cần tuyển riêng.** Có thể phân công chéo giữa CEO, Vân Anh, Product Expert và kỹ thuật.

- Kiểm thử dữ liệu, matching, câu hỏi, thứ hạng, giải thích và affiliate clickout.
- Chạy golden dataset, regression test và audit mẫu nội dung.
- Ghi nhận lỗi theo mức độ nghiêm trọng, nguyên nhân và người xử lý.
- Kiểm tra các tình huống dễ gây hại: sai model, sai giá, khuyến nghị không phù hợp, claim thiếu nguồn.

**Bàn giao:** test cases, QA checklist, defect log, release sign-off.

### Cơ cấu gọn khuyến nghị cho MVP

| Năng lực | Cách bố trí ban đầu |
|---|---|
| CEO / Product Owner | CEO hiện tại |
| Customer Psychology | Vân Anh |
| Product Expertise | 1 chuyên gia cộng tác theo ngành hàng |
| Engineering / Automation | 1 Technical Lead hoặc Full-stack Automation Engineer |
| Data & Market Intelligence | CEO + kỹ thuật, bổ sung Data Ops part-time khi catalog tăng |
| Affiliate Operations | CEO kiêm trước, thuê chuyên trách khi có nhiều network |
| SEO/GEO & Growth | Part-time / theo dự án |
| QA | Chia sẻ trách nhiệm giữa các vai trò |

**Khuyến nghị tuyển/thuê theo thứ tự:** (1) chốt ngành hàng và tìm Product Expert cộng tác; (2) có Technical Lead chịu trách nhiệm triển khai; (3) kiểm chứng nguồn dữ liệu và affiliate; (4) bổ sung Data Ops hoặc Affiliate Ops khi khối lượng thực tế chứng minh cần thiết; (5) thuê SEO/GEO theo milestone.

## 6. Ranh giới trách nhiệm và quyền quyết định

- Customer Psychology sở hữu hiểu biết về khách hàng và logic hành vi; không quyết định sự thật kỹ thuật sản phẩm.
- Product Expert sở hữu tiêu chí và nhận định chuyên môn; không tự xác nhận giá/tồn kho nếu không có nguồn dữ liệu.
- Data Operations sở hữu chất lượng, nguồn gốc và độ tin cậy dữ liệu; không tự tạo nhận định tâm lý hoặc kết luận kỹ thuật.
- Affiliate Operations sở hữu quan hệ đối tác, điều kiện và đối soát; không quyết định mức độ phù hợp của sản phẩm.
- SEO/Growth sở hữu phân phối và thử nghiệm tăng trưởng; không được làm sai lệch nội dung vì traffic.
- Engineering sở hữu triển khai kỹ thuật, độ ổn định và khả năng kiểm thử; không tự đặt quy tắc chuyên môn.
- CEO quyết định ưu tiên, phạm vi, trade-off và phê duyệt cuối cùng.

Mỗi đầu ra chuyên gia phải có: mục tiêu, dữ liệu/bằng chứng, giả thuyết (nếu có), quy tắc đề xuất, điều kiện áp dụng, ngoại lệ/rủi ro, ví dụ và cách kiểm thử.

## 7. Quy trình vận hành chuẩn (SOP)

### Gate 0 — Chọn ngành hàng

Đánh giá mỗi ngành theo thang điểm có trọng số:

- Khả năng tiếp cận dữ liệu sản phẩm và giá.
- Khả năng định danh chính xác model/variant.
- Sự tồn tại và điều kiện của affiliate program.
- Mức độ khách hàng cần tư vấn/so sánh.
- Khả năng tạo khác biệt bằng chuyên môn và bằng chứng.
- Mức cạnh tranh và khả năng tiếp cận traffic.
- Biên lợi nhuận/commission và khả năng tạo doanh thu.

Không chốt ngành hàng chỉ vì CEO/chuyên gia thích lĩnh vực đó. Phải có khảo sát nguồn và economics. Audio là ứng viên, chưa phải quyết định.

### Gate 1 — Nghiên cứu khách hàng và ngành hàng

- Product Expert xây khung đánh giá và bản đồ model.
- Vân Anh xây decision journey, câu hỏi tối thiểu và tình huống phân vân.
- CEO xác định nhóm khách hàng/use case ưu tiên.
- Kết quả phải được chuyển thành tài liệu có thể triển khai và kiểm thử.

### Gate 2 — Kiểm chứng dữ liệu và affiliate

- Lập danh sách nguồn và quyền/điều kiện sử dụng.
- Thu thập mẫu đại diện; đo coverage, freshness, accuracy và matching.
- Kiểm tra deeplink, tracking, attribution và điều kiện commission.
- Chỉ tiếp tục khi có nguồn dữ liệu và mô hình doanh thu đủ khả thi.

### Gate 3 — Xây MVP

MVP chỉ cần một ngành hàng tập trung, một luồng tìm hiểu/so sánh/ra quyết định, catalog giới hạn và nguồn affiliate khả thi.

Quy mô thử nghiệm tham khảo: 100–300 canonical product models và 1–2 affiliate sources; đây là giả định để kiểm chứng, không phải KPI cứng.

### Gate 4 — Kiểm định trước phát hành

- Kiểm tra dữ liệu và model matching.
- Kiểm thử câu hỏi thích ứng và tiêu chí xếp hạng.
- Xác nhận mọi khuyến nghị có lý do và trade-off.
- Kiểm tra link, tracking, nội dung, nguồn dẫn, SEO kỹ thuật và quyền riêng tư.
- Chặn phát hành nếu có lỗi nghiêm trọng về model, giá, claim hoặc suitability.

### Gate 5 — Phát hành giới hạn và đo lường

- Theo dõi lỗi dữ liệu, hành vi người dùng, clickout và doanh thu.
- Audit mẫu các đề xuất và trang nội dung.
- Thu thập phản hồi, phân tích điểm rơi trong decision journey.
- Ghi rõ giả thuyết và thiết kế thử nghiệm; không quy kết nguyên nhân chỉ từ tương quan.

### Gate 6 — Cải tiến hoặc mở rộng

Chỉ mở rộng catalog, nguồn affiliate hoặc ngành hàng khi:
- Dữ liệu đủ chính xác và có thể duy trì.
- Khách hàng thực sự sử dụng giá trị tư vấn/so sánh.
- Có tín hiệu clickout/commission hoặc bằng chứng kinh tế hợp lý.
- Chi phí vận hành và chất lượng tự động hóa nằm trong ngưỡng chấp nhận.
- Không có suy giảm đáng kể về niềm tin hoặc suitability.

## 8. Chu trình phối hợp hằng tuần

1. CEO xác định 1–3 ưu tiên và tiêu chí hoàn thành.
2. Mỗi chuyên gia nhận một brief có vấn đề, phạm vi, đầu ra và deadline.
3. Chuyên gia bàn giao tài liệu có cấu trúc; không chỉ đưa ý kiến chung.
4. CEO kiểm tra tính nhất quán và ra quyết định.
5. Engineering chuyển các quy tắc đã duyệt thành cấu hình, code và test.
6. QA chạy test; lỗi được phân loại và giao người xử lý.
7. CEO xem KPI, quyết định giữ/sửa/dừng và cập nhật roadmap.

Không khởi động task mới nếu đầu ra, người chịu trách nhiệm hoặc tiêu chí hoàn thành chưa rõ.

## 9. Lộ trình ưu tiên

### Phase 1 — Validate

- So sánh 3–5 ngành hàng ứng viên.
- Chọn một ngành MVP bằng scorecard.
- Kiểm chứng Product Expert, nguồn dữ liệu và affiliate economics.
- Hoàn thiện mô hình khách hàng và bộ tiêu chí đánh giá.

### Phase 2 — Define

- Chốt canonical data model và source map.
- Chốt decision framework và test dataset.
- Chốt MVP scope, KPI và kiến trúc kỹ thuật tối thiểu.

### Phase 3 — Build

- Xây pipeline dữ liệu.
- Xây catalog và decision flow.
- Xây trang nội dung, clickout tracking và analytics.
- Kiểm thử end-to-end.

### Phase 4 — Launch & Learn

- Phát hành giới hạn.
- Audit chất lượng và đo KPI.
- Sửa các điểm nghẽn lớn nhất.
- Chỉ mở rộng khi có bằng chứng.

## 10. Những quyết định hiện tại

- Thị trường: Việt Nam.
- Sản phẩm: website affiliate hỗ trợ quyết định mua hàng.
- Ngành hàng MVP: chưa chốt.
- Audio: ứng viên cần đánh giá, không mặc định lựa chọn.
- Mô hình tổ chức: CEO + Vân Anh hiện tại; bổ sung chuyên gia theo nhu cầu, ưu tiên Product Expert cộng tác và Technical Lead.
- Phạm vi MVP: một ngành hàng, một luồng quyết định cốt lõi, dữ liệu và affiliate được kiểm chứng.
- Không tuyển đủ sáu vai trò ngay từ đầu.

## 11. Mẫu brief giao việc cho nhân sự

Mỗi nhiệm vụ phải có cấu trúc:

- **Mục tiêu:** vấn đề cần giải quyết.
- **Bối cảnh:** thông tin đã biết và nguồn hiện có.
- **Phạm vi:** việc cần làm và việc không làm.
- **Đầu ra:** tài liệu, bảng dữ liệu, quy tắc, prototype hoặc báo cáo cụ thể.
- **Bằng chứng:** nguồn, dữ liệu, giả thuyết và mức độ tin cậy.
- **Tiêu chí nghiệm thu:** điều kiện để CEO chấp nhận.
- **Phối hợp:** ai cung cấp đầu vào, ai review, ai triển khai.
- **Rủi ro/ngoại lệ:** trường hợp chưa thể kết luận.
- **Đề xuất bước tiếp theo:** việc cần CEO quyết định.

---

**Nguyên tắc điều hành cuối cùng:** A+ không xây một đội ngũ đông người để làm website. A+ xây một hệ thống có thể biến kiến thức chuyên môn, dữ liệu đáng tin và hiểu biết khách hàng thành quyết định mua hàng tốt hơn — một cách tự động, đo lường được và tạo ra doanh thu affiliate bền vững.
