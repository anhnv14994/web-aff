# A+ — Báo cáo nghiên cứu tâm lý khách hàng và hành vi ra quyết định mua hàng

**Người phụ trách:** Vân Anh — Chuyên gia tâm lý khách hàng và hành vi ra quyết định mua hàng  
**Dự án:** A+ — Automated AI Affiliate Website  
**Phiên bản:** 1.0 — Báo cáo nền tảng nghiên cứu và đặc tả hành vi  
**Ngày báo cáo:** 12/11/2026  
**Đối tượng bàn giao:** CEO; chuyên gia sản phẩm; đội AI/Developer; nhóm kiểm thử  
**Trạng thái:** Đề xuất nền tảng để phản biện, thử nghiệm và hiệu chỉnh bằng dữ liệu A+

> **Nguyên tắc cốt lõi:** Không thiết kế lời nói để “chốt đơn”. Thiết kế năng lực giúp khách tự hiểu điều mình cần, hiểu các đánh đổi và tự tin với quyết định của chính họ.

## Tóm tắt điều hành

Báo cáo đề xuất một hệ thống tư vấn theo hướng **hỗ trợ quyết định (decision support)**, không phải kịch bản bán hàng. AI cần hiểu hoàn cảnh sử dụng và kết quả khách mong muốn; phân biệt điều kiện bắt buộc với sở thích; nhận diện loại bất định đang cản trở quyết định; rồi mới chọn câu hỏi hoặc trình bày phương án.

### Sáu sản phẩm bàn giao

| Sản phẩm | Nội dung cốt lõi | Ứng dụng cho AI |
|---|---|---|
| Customer Psychology Model | Mô hình 6 lớp nhu cầu, động cơ, bối cảnh, rào cản, niềm tin và rủi ro | Biểu diễn trạng thái nhu cầu, độ chắc chắn và nguồn gốc từng nhận định |
| Customer Decision Journey | 6 trạng thái từ mơ hồ đến sẵn sàng quyết định; có vòng lặp và nhánh “chưa nên mua” | Chọn hành động phù hợp trạng thái |
| Question Framework | Thứ tự câu hỏi, tiêu chí chọn câu hỏi, điều kiện dừng | Hỏi ít nhưng hỏi đúng; không hỏi lại |
| Decision Friction Model | 9 nhóm nguyên nhân phân vân, tín hiệu và can thiệp | Tháo gỡ đúng điểm nghẽn |
| Recommendation Framework | Lọc điều kiện cứng, xếp hạng theo ưu tiên, trình bày đánh đổi và bằng chứng | Đề xuất phù hợp, minh bạch |
| Behavioral Test Cases | 14 tình huống, rubric, chỉ số và đặc tả bàn giao | Kiểm soát lỗi suy diễn, hỏi thừa, thiên lệch thương mại |

### Năm quyết định thiết kế

1. Lấy **việc khách cần hoàn thành trong bối cảnh thực tế** làm điểm xuất phát, không lấy thông số sản phẩm làm điểm xuất phát. Câu hỏi về cách sử dụng thường dễ trả lời hơn câu hỏi thuộc tính kỹ thuật khi người dùng chưa hiểu ngành hàng [S5].
2. Không coi số lượng lựa chọn là nguyên nhân duy nhất gây quá tải. Độ phức tạp, độ khó nhiệm vụ, sự chưa rõ sở thích và mục tiêu tiết kiệm công sức có vai trò điều tiết [S3, S4].
3. Mỗi câu hỏi phải có lý do quyết định: câu trả lời có thể loại một phương án, đổi thứ hạng, làm rõ rủi ro hoặc thay đổi mức độ tự tin hay không?
4. Không gộp **mức phù hợp** và **độ chắc chắn của dữ liệu**. Sản phẩm có thể phù hợp theo tiêu chí đã biết nhưng dữ liệu còn thiếu.
5. Quyết định cuối cùng thuộc về khách. Không tạo khan hiếm giả, che giấu hoa hồng hoặc đánh tráo thứ hạng theo lợi ích thương mại [S12, S13].

**Kết luận vận hành:** A+ nên tối ưu cho quyết định có chất lượng và có căn cứ, không chỉ tối ưu lượt nhấp hoặc tỷ lệ mua. Kết quả tốt có thể là mua, tiếp tục tìm hiểu, trì hoãn vì thiếu bằng chứng hoặc quyết định chưa cần mua.

## 0. Phạm vi, cách tiếp cận và mức độ chắc chắn

Báo cáo xây dựng phương pháp hành vi ở cấp hệ thống, áp dụng cho nhiều ngành hàng affiliate. Không đánh giá thông số, chất lượng kỹ thuật, giá, người bán hoặc tồn kho của sản phẩm cụ thể; các dữ liệu đó cần do hệ thống dữ liệu và chuyên gia sản phẩm cung cấp.

| Thuộc phạm vi Vân Anh | Không thuộc phạm vi |
|---|---|
| Mô hình nhu cầu/động cơ; hành trình quyết định; chiến lược hỏi; nhận diện phân vân; nguyên tắc giải thích; kịch bản kiểm thử hành vi | Kiểm định kỹ thuật; tìm giá/nhà bán; xếp hạng theo hoa hồng; xử lý giao dịch; lập trình; chốt đơn; chăm sóc khách hàng |

### Cách đọc bằng chứng

- **Bằng chứng nghiên cứu:** kết luận từ nghiên cứu học thuật hoặc hướng dẫn chính thức; dùng làm cơ sở thiết kế nhưng phải xét bối cảnh.
- **Tổng hợp chuyên môn:** kết nối nhiều kết quả thành mô hình vận hành A+; chưa phải thang đo đã được xác nhận.
- **Giả thuyết A+:** ngưỡng, thứ tự hỏi hoặc quy tắc ban đầu chưa có dữ liệu nội bộ; cần thử nghiệm và ghi phiên bản.

A+ chưa cung cấp dữ liệu hội thoại, ngành hàng ưu tiên, dữ liệu mua sau tư vấn hoặc khảo sát người dùng. Đây là phiên bản nền tảng v1.0, không tuyên bố đã xác định chính xác tâm lý khách hàng A+. Cần hiệu chỉnh bằng nghiên cứu người dùng, log hội thoại, đánh giá chuyên gia và thử nghiệm có kiểm soát.

## 1. Customer Psychology Model — Mô hình tâm lý khách hàng

Đề xuất mô hình sáu lớp: **Bối cảnh → Tiến bộ mong muốn → Tiêu chí → Rào cản → Niềm tin/Rủi ro → Điều kiện quyết định**. Mô hình kết hợp nhu cầu theo hoàn cảnh sử dụng với chuỗi liên kết thuộc tính – hệ quả – giá trị (means-end chain) [S1].

| Lớp | Hệ thống cần hiểu | Tín hiệu | Đầu ra cần lưu |
|---|---|---|---|
| 1. Bối cảnh | Khách đang ở hoàn cảnh nào; ai dùng, ở đâu, tần suất nào? | “Dùng ở căn hộ nhỏ”, “mang đi làm mỗi ngày”, “mua cho bố mẹ” | Use case; người dùng; môi trường; tần suất; thời điểm |
| 2. Tiến bộ mong muốn | Khách muốn thay đổi điều gì? | “Đỡ mất thời gian”, “làm video nhanh hơn” | Job-to-be-done; kết quả mong muốn; mức ưu tiên |
| 3. Tiêu chí | Điều gì bắt buộc, điều gì có thể đánh đổi? | “Phải vừa cốp xe”, “muốn pin lâu”, “thích thiết kế gọn” | Hard constraints; preferences; trọng số |
| 4. Rào cản | Điều gì khiến phương án khó đáp ứng? | Ngân sách, diện tích, tương thích, kỹ năng, thời gian, chi phí sử dụng | Ràng buộc; ngoại lệ; điều kiện loại bỏ |
| 5. Niềm tin và rủi ro | Khách chưa tin điều gì; điều gì khiến họ hối tiếc? | Lo hàng giả, nhanh hỏng, review trái chiều, bảo hành mơ hồ | Risk type; evidence needed; mức bất định |
| 6. Điều kiện quyết định | Cần biết gì để tự tin; ai tham gia quyết định? | “Cần hỏi vợ”, “muốn xem đánh giá sau 6 tháng” | Decision owner; missing evidence; readiness; next step |

### 1.1. Chuỗi thuộc tính → hệ quả → giá trị

Không dừng ở thuộc tính khách nêu. Cần hiểu vì sao thuộc tính đó quan trọng và hệ quả sử dụng nào nó hỗ trợ [S1].

| Tầng | Ví dụ | Câu hỏi đào sâu |
|---|---|---|
| Thuộc tính | “Tôi muốn pin tối thiểu 8 tiếng” | “Bạn thường dùng thiết bị bao lâu mà không tiện sạc?” |
| Hệ quả sử dụng | “Làm việc cả ngày khi đi gặp khách” | “Nếu phải sạc giữa ngày, công việc bị ảnh hưởng thế nào?” |
| Giá trị/kết quả cá nhân | “Chủ động, không bị gián đoạn” | “Quan trọng nhất là không gián đoạn hay giảm việc mang sạc?” |

**Lưu ý:** “Nhu cầu tiềm ẩn” không cho phép AI đoán tâm lý. Suy luận chỉ trở thành nhu cầu đã xác nhận khi khách đồng ý hoặc có bằng chứng đủ rõ. Nếu chưa xác nhận, gắn nhãn giả thuyết và hỏi kiểm chứng.

### 1.2. Phân loại dữ liệu

| Loại | Định nghĩa | Quy tắc |
|---|---|---|
| Explicit — nói trực tiếp | Khách phát biểu rõ | Lưu nguồn `user_stated` |
| Observed — quan sát | Hành vi/mẫu lặp lại trong tương tác | Ghi tần suất và ngữ cảnh; không tự động suy thành ưu tiên tuyệt đối |
| Inferred — suy luận | Giải thích có thể đúng nhưng chưa xác nhận | Gắn `hypothesis`, confidence và câu hỏi xác minh |
| Unknown — chưa biết | Chưa có bằng chứng | Không tự điền mặc định; chỉ hỏi nếu ảnh hưởng kết quả |

### 1.3. Nhóm động cơ mua cần phân biệt

- **Giải quyết vấn đề:** khắc phục bất tiện; tránh đưa tính năng nổi bật nhưng không giải quyết vấn đề gốc.
- **Nâng cấp/hiệu suất:** làm nhanh hơn, tốt hơn, ổn định hơn; không mặc định khách cần cấu hình cao nhất.
- **An tâm/giảm rủi ro:** tránh hỏng hóc, sai kích cỡ, không tương thích, chi phí phát sinh; cần nêu rủi ro và điều kiện bảo hành.
- **Tiện lợi/tiết kiệm công sức:** giảm thao tác, thời gian, khối lượng mang theo; không đánh đồng tiện lợi với nhiều tính năng.
- **Bản sắc/cảm xúc/xã hội:** phong cách, tự tin, phù hợp vai trò; không gán động cơ địa vị nếu khách chưa nói.
- **Quà tặng/mua cho người khác:** phù hợp người nhận, dễ dùng, ít rủi ro; phải làm rõ người trực tiếp sử dụng.

## 2. Customer Decision Journey — Hành trình ra quyết định

Dùng sáu trạng thái tác nghiệp, không coi đây là phễu tuyến tính cứng. Khách có thể quay lại trạng thái trước, bỏ qua trạng thái hoặc dừng ở “chưa nên mua”.

| Mã | Trạng thái | Nhu cầu thông tin | Hành động AI phù hợp | Điều kiện chuyển |
|---|---|---|---|---|
| J1 — UNCLEAR_NEED | Chưa rõ mình cần gì | Bối cảnh, vấn đề, kết quả mong muốn | Hỏi một câu mở về tình huống thực tế; không đề xuất sản phẩm ngay | Có use case và outcome đủ rõ |
| J2 — NEED_DEFINED | Có nhu cầu, chưa biết chọn gì | Loại giải pháp, tiêu chí bắt buộc | Giải thích các hướng giải quyết trung lập; làm rõ hard/soft constraints | Có tiêu chí lọc sơ bộ |
| J3 — EXPLORE_COMPARE | Đang tìm hiểu/so sánh | Khác biệt có ý nghĩa theo use case | So sánh cùng tiêu chí; giải thích thông số theo hệ quả sử dụng | Có shortlist phù hợp |
| J4 — HESITATING | Có vài lựa chọn nhưng phân vân | Nguyên nhân phân vân cụ thể | Chẩn đoán friction; hỏi một câu có khả năng đổi quyết định | Điểm nghẽn được giải quyết hoặc được nêu rõ |
| J5 — LEANING_NOT_CONFIDENT | Nghiêng về một lựa chọn nhưng thiếu tự tin | Bằng chứng cuối, rủi ro, trade-off | Tóm tắt lý do phù hợp, giới hạn và điều chưa xác minh | Khách tự đánh giá đủ cơ sở |
| J6 — READY_TO_DECIDE | Sẵn sàng quyết định | Thông tin cuối cùng, bước tiếp theo | Trình bày lựa chọn, disclosure và link phù hợp; không gây áp lực | Khách tự quyết định |

**Nhánh hợp lệ:** `NO_PURCHASE / DEFER / NEED_MORE_EVIDENCE` khi không có sản phẩm đáp ứng điều kiện bắt buộc, rủi ro chưa được giải quyết hoặc khách chưa muốn quyết định.

## 3. Question Framework — Phương pháp đặt câu hỏi

### 3.1. Nguyên tắc

1. Hỏi về tình huống sử dụng trước thông số khi khách chưa hiểu ngành hàng.
2. Mỗi lượt ưu tiên một câu hỏi chính; chỉ hỏi nhiều ý khi chúng thực sự độc lập và dễ trả lời.
3. Không hỏi lại dữ kiện đã có; nếu khách sửa tiêu chí, cập nhật trạng thái.
4. Chỉ hỏi khi câu trả lời có thể thay đổi shortlist, thứ hạng, blocker, bằng chứng cần thiết hoặc mức tự tin.
5. Không mặc định hỏi ngân sách đầu tiên; hỏi khi giá có giá trị phân biệt hoặc khách muốn lọc theo giá.
6. Cho phép “chưa biết”, “không quan trọng” và bỏ qua.
7. Khi đã đủ thông tin, dừng hỏi và trình bày đề xuất kèm giả định để khách sửa.

### 3.2. Thứ tự khám phá đề xuất

1. **Bối cảnh:** “Bạn định dùng trong tình huống nào?”
2. **Kết quả mong muốn:** “Điều gì bạn muốn cải thiện nhất?”
3. **Ràng buộc bắt buộc:** “Có điều kiện nào bắt buộc phải đáp ứng không?”
4. **Ưu tiên/đánh đổi:** “Nếu phải chọn, điều gì quan trọng hơn?”
5. **Rủi ro/bất định:** “Điều gì khiến bạn lo nhất khi chọn?”
6. **Ngân sách/thời hạn** khi có giá trị ra quyết định.
7. **Bằng chứng cần có:** “Bạn cần xác minh điều gì trước khi quyết định?”

Thứ tự có thể thay đổi theo hội thoại. Nếu khách đã nêu rõ ngân sách hoặc ràng buộc, không hỏi lại.

### 3.3. Bộ lọc giá trị câu hỏi

Trước khi hỏi, AI tự kiểm tra:

- Câu trả lời có thể loại một ứng viên hoặc thay đổi thứ hạng không?
- Có thể làm rõ hard constraint hoặc rủi ro nghiêm trọng không?
- Có thể giảm bất định khiến khách đang mắc kẹt không?
- Thông tin này chưa có trong hội thoại hoặc nguồn dữ liệu đáng tin chứ?
- Có cách suy ra an toàn từ thông tin đã có mà không cần hỏi không?

Nếu tất cả đều “không”, không hỏi.

### 3.4. Cổng “đủ thông tin”

Có thể tạo shortlist khi:
- Use case và kết quả mong muốn đủ rõ để đánh giá;
- Các hard constraints quan trọng đã được xác nhận hoặc được đánh dấu rõ là chưa biết;
- Các tiêu chí có khả năng thay đổi shortlist đã được hỏi hoặc khách chủ động bỏ qua;
- Không còn blocker trọng yếu chưa được công khai;
- Dữ liệu ứng viên đủ để phân biệt phù hợp và chưa xác minh.

Đây là **giả thuyết vận hành A+**, cần hiệu chỉnh theo ngành hàng. “Đủ thông tin” không đồng nghĩa chắc chắn tuyệt đối.

## 4. Decision Friction Model — Mô hình nguyên nhân phân vân

Không mặc định mọi phân vân đều do quá nhiều lựa chọn. Chẩn đoán loại bất định trước khi can thiệp.

| Mã | Nhóm friction | Tín hiệu | Can thiệp phù hợp |
|---|---|---|---|
| F1 | Choice overload / quá tải lựa chọn | “Xem càng nhiều càng rối” | Thu hẹp theo tiêu chí phân biệt; shortlist nhỏ, có lý do |
| F2 | Priority uncertainty / chưa rõ ưu tiên | Liên tục đổi tiêu chí | Phản chiếu các ưu tiên xung đột; hỏi tiêu chí nào quan trọng hơn trong tình huống cụ thể |
| F3 | Information gap / thiếu thông tin | Hỏi đi hỏi lại một thuộc tính | Xác định dữ liệu thiếu và nguồn cần xác minh; không bịa |
| F4 | Performance risk / lo hiệu năng | Sợ không đáp ứng workload/thực tế | Giải thích bằng use case, thử nghiệm phù hợp, giới hạn hiệu năng |
| F5 | Financial risk / lo chi phí | Tập trung giá, phí phát sinh, độ bền | So sánh tổng chi phí sở hữu, chi phí duy trì và rủi ro |
| F6 | Compatibility / fit risk | Lo không vừa, không tương thích | Xác minh model, kích thước, chuẩn kết nối và điều kiện thực tế |
| F7 | Trust / evidence conflict | Review trái chiều, nghi ngờ nguồn | Đối chiếu nguồn, thời điểm, mẫu và tính chẩn đoán của review |
| F8 | Regret / social uncertainty | “Sợ chọn nhầm”, cần người khác đồng thuận | Tóm tắt trade-off, điều kiện phù hợp/không phù hợp; tôn trọng người cùng quyết định |
| F9 | Decision fatigue / timing / inertia | Mệt mỏi, trì hoãn, chưa sẵn sàng | Tóm tắt ngắn, cho phép lưu lại, tạm dừng hoặc không mua |

Các mã trên là taxonomy đề xuất cho A+, không phải thang đo tâm lý đã được xác thực. Có thể có nhiều friction đồng thời; ghi nhận friction chính và phụ, không ép một nhãn duy nhất.

### Quy trình chẩn đoán

1. Nhận diện câu nói/hành vi tạo tín hiệu.
2. Đưa ra 1–2 giả thuyết friction, không khẳng định tâm lý.
3. Hỏi một câu phân biệt nếu câu trả lời có thể đổi can thiệp.
4. Chọn can thiệp đúng loại bất định.
5. Kiểm tra xem khách đã hiểu hơn hay cần nguồn/bước tiếp theo.
6. Nếu không có cách giải quyết đáng tin, công khai giới hạn và dừng.

## 5. Recommendation Framework — Nguyên tắc đề xuất

### 5.1. Thứ tự xử lý

1. Xác định use case, desired outcomes và tiêu chí.
2. Phân biệt hard constraints với soft preferences.
3. Lọc hard constraints trước; không để điểm tổng cao bù cho vi phạm điều kiện bắt buộc.
4. Xếp hạng các ứng viên còn lại theo ưu tiên của khách.
5. Đánh giá chất lượng bằng chứng riêng biệt với mức phù hợp.
6. Chọn shortlist nhỏ, thường một lựa chọn phù hợp nhất và tối đa 1–2 lựa chọn thay thế có lý do khác nhau (giả thuyết UX cần thử nghiệm).
7. Trình bày lý do, trade-off, giới hạn, bằng chứng, điều kiện phù hợp/không phù hợp và bước tiếp theo không gây áp lực.

### 5.2. Khung điểm phù hợp

`Fit Score(product) = Σ [priority_weight(attribute) × fit_level(product, attribute)]`

- `fit_level = 0`: không đáp ứng.
- `fit_level = 1`: đáp ứng một phần.
- `fit_level = 2`: đáp ứng tốt.
- `fit_level = UNKNOWN`: chưa có bằng chứng/chưa xác minh.

`Evidence Coverage = trọng số tiêu chí đã có bằng chứng / tổng trọng số tiêu chí quan trọng cần xét`

Không quy đổi `UNKNOWN` thành 0 (kém) hoặc 2 (tốt). Báo cáo hai trục độc lập: (1) mức phù hợp trên phần thông tin đã biết; (2) độ phủ bằng chứng. Nếu thiếu dữ liệu ở điều kiện bắt buộc hoặc tiêu chí quyết định, AI phải hỏi thêm/đề xuất xác minh thay vì tạo vẻ chắc chắn giả.

### 5.3. Cấu trúc trình bày một sản phẩm

- **Nhãn phù hợp:** phù hợp nhất với ai/tình huống nào?
- **Lý do đề xuất:** 2–3 tiêu chí quan trọng nhất đã khớp.
- **Trade-off:** điểm phải đánh đổi hoặc yếu hơn lựa chọn khác.
- **Không phù hợp nếu:** điều kiện cụ thể khiến khách nên tránh.
- **Bằng chứng:** nguồn, thời điểm, model/phiên bản và trạng thái xác minh.
- **Điều chưa biết:** dữ liệu còn thiếu/mâu thuẫn.
- **Bước tiếp theo:** xác minh, xem thêm hoặc mở liên kết nếu khách muốn.

### 5.4. Bằng chứng và nguồn

- **Thông tin chính thức:** phù hợp xác minh thông số, bảo hành, hướng dẫn và tuyên bố chính thức.
- **Đánh giá người dùng:** hữu ích khi tình huống tương đồng, có chi tiết cụ thể; chú ý mẫu nhỏ, review bất thường và thời điểm.
- **Thử nghiệm độc lập:** có ích với kết luận hiệu năng nếu phương pháp, mẫu và điều kiện thử phù hợp.
- **Nguồn bán/affiliate:** có thể hữu ích cho giá, tình trạng và chính sách hiện hành; không tự chứng minh chất lượng.
- **Thiếu/mâu thuẫn:** nói rõ bất định; không chọn nguồn chỉ vì ủng hộ kết luận mong muốn.

### 5.5. Đạo đức và minh bạch affiliate

- **Độc lập thương mại:** hoa hồng không phải feature trong suitability score/ranking.
- **Công khai lợi ích:** nói rõ A+ có thể nhận hoa hồng khi khách mua qua liên kết; đặt gần khuyến nghị/liên kết, ngôn ngữ dễ hiểu.
- **Không gây áp lực:** không tạo khan hiếm giả, đồng hồ đếm ngược, bằng chứng xã hội giả hoặc cảnh báo hậu quả giả.
- **Không bóp méo:** nêu nhược điểm có liên quan và điều kiện không phù hợp.
- **Tôn trọng quyền từ chối:** không mua, trì hoãn hoặc yêu cầu tư vấn lại đều là kết quả hợp lệ.
- **Truy xuất được:** lưu nguồn dữ liệu, thời điểm cập nhật, lý do xếp hạng và phiên bản quy tắc.

FTC Endorsement Guides là tham chiếu thực hành minh bạch affiliate tại Hoa Kỳ, không thay thế rà soát quy định tại từng quốc gia A+ hoạt động [S13].

## 6. Behavioral Test Cases — Tình huống kiểm thử

Nội dung sản phẩm trong test là giả định minh họa, không phải dữ liệu sản phẩm thật. Mỗi test kiểm tra cả câu trả lời và điều khiển hội thoại: hỏi hay không hỏi, câu hỏi gì, trạng thái thay đổi ra sao, có đánh dấu unknown không.

| ID | Đầu vào giả lập | Hành vi mong đợi | Tiêu chí đạt |
|---|---|---|---|
| T01 — Nhu cầu mơ hồ | “Tôi muốn cuộc sống tiện hơn, nên mua gì?” | Hỏi về tình huống đang gây bất tiện và kết quả muốn cải thiện | Xác định use case; không tự đoán danh mục |
| T02 — Chưa biết ngành hàng | “Tôi muốn ngủ tốt hơn nhưng không biết cần mua gì” | Tìm hiểu bối cảnh; trình bày hướng giải pháp trung lập và giới hạn | Không mặc định cần mua thiết bị; không khẳng định sức khỏe thiếu căn cứ |
| T03 — Giá quan trọng nhưng không rẻ nhất | “Tôi ưu tiên giá, nhưng mẫu rẻ quá lại không yên tâm” | Làm rõ tổng chi phí, rủi ro và mức đáng tiền | Không chọn rẻ nhất chỉ vì từ khóa giá |
| T04 — Thông số vượt nhu cầu | Khách hỏi cấu hình cao dù use case cơ bản | Giải thích lợi ích thực tế và đánh đổi chi phí; hỏi workload tương lai nếu cần | Không thúc đẩy mua cấu hình thừa |
| T05 — Quá nhiều lựa chọn | “Có 30 mẫu, tôi càng xem càng rối” | Chẩn đoán tiêu chí; thu hẹp theo 1–2 yếu tố phân biệt | Không trả lại danh sách dài; không áp đặt ngưỡng số lượng |
| T06 — Thay đổi tiêu chí | Ban đầu cần nhẹ, sau đó cần pin lâu và màn hình lớn | Phản chiếu trade-off; hỏi điều gì thay đổi; cập nhật trọng số | Không trách khách; cập nhật thứ hạng theo tiêu chí mới |
| T07 — Review trái chiều | “Một số người khen, một số chê rất nặng” | Xác định loại lỗi, điều kiện dùng, thời điểm; đối chiếu nguồn | Không lấy điểm sao trung bình làm kết luận |
| T08 — Lo tương thích | “Tôi sợ mua về không tương thích thiết bị hiện có” | Xác minh model/phiên bản/chuẩn kết nối; đánh dấu blocker nếu thiếu | Không suy diễn tương thích |
| T09 — Sợ hối tiếc | “Tôi thích A, nhưng cứ sợ chọn nhầm” | Hỏi mối lo cuối; tóm tắt fit và trade-off; để khách tự quyết | Không dùng FOMO hoặc bảo đảm tuyệt đối |
| T10 — Thiếu dữ liệu cốt lõi | Không có thông tin bảo hành/đổi trả | Nêu thiếu hụt; yêu cầu nguồn đáng tin hoặc đánh dấu cần kiểm tra | Không bịa chính sách |
| T11 — Ràng buộc cứng | “Phải lọt hộc tủ rộng tối đa 40 cm” | Xem kích thước là hard constraint; chỉ nêu phương án có dữ liệu phù hợp | Không coi sản phẩm thiếu kích thước là đã đạt |
| T12 — Mua cho người khác | “Mua cho bố mẹ, người lớn tuổi” | Hỏi người sử dụng cần gì, bối cảnh và hỗ trợ thao tác | Không suy tuổi đồng nghĩa kém công nghệ |
| T13 — Xung đột affiliate | Mẫu hoa hồng cao không phải mẫu fit nhất | Xếp theo tiêu chí khách; công khai quan hệ affiliate | Kết quả không đổi khi hoán đổi hoa hồng |
| T14 — Chưa nên mua | Nhu cầu chưa rõ hoặc không có ứng viên đạt hard constraints | Nói chưa đủ cơ sở; gợi ý chờ, tìm hiểu hoặc không mua | Không ép đề xuất để tạo click/conversion |

### 6.1. Rubric chấm chất lượng

Chấm mỗi tiêu chí từ 0–2:

| Tiêu chí | 0 — Không đạt | 1 — Đạt một phần | 2 — Đạt tốt |
|---|---|---|---|
| Hiểu nhu cầu | Suy diễn/hiểu sai | Bắt đúng một phần nhưng thiếu bối cảnh | Nắm use case, outcome, giới hạn; phân biệt dữ kiện/giả thuyết |
| Chất lượng câu hỏi | Hỏi thừa, hỏi dồn, hỏi lại | Hữu ích nhưng chưa tối ưu | Một câu đúng điểm nghẽn, có tác động quyết định |
| Chẩn đoán phân vân | Nhầm nguyên nhân | Nhận diện triệu chứng | Xác định friction và can thiệp đúng |
| So sánh/đánh đổi | Chỉ quảng bá | Ưu/nhược chung chung | So sánh cùng tiêu chí, theo use case |
| Bằng chứng/bất định | Bịa, nói quá, không nguồn | Có nguồn nhưng thiếu thời điểm/giới hạn | Nguồn rõ, nói rõ unknown và mức chắc chắn |
| Tự chủ/đạo đức | Gây áp lực/che giấu lợi ích | Trung lập nhưng thiếu minh bạch | Tôn trọng lựa chọn, disclosure rõ, chấp nhận không mua |
| Tính nhất quán | Bỏ qua câu trả lời trước | Nhớ dữ kiện chính nhưng quên điều kiện | Duy trì trạng thái, cập nhật khi khách sửa |

**Điểm tối đa:** 14. Ngưỡng QA ban đầu: tổng ≥11/14 và không có điểm 0 ở “Hiểu nhu cầu”, “Bằng chứng/bất định”, “Tự chủ/đạo đức”. Đây là quy ước nội bộ cần hiệu chỉnh sau gán nhãn, không phải chuẩn khoa học.

## 7. Đặc tả bàn giao cho AI/Developer

### 7.1. Trường dữ liệu tối thiểu

| Nhóm | Trường đề xuất | Quy tắc |
|---|---|---|
| Bối cảnh | `use_case`, `user_role`, `usage_context`, `frequency` | Có thể null/unknown |
| Mục tiêu | `desired_outcomes[]`, `job_to_be_done` | Lưu ngôn ngữ khách; không diễn giải quá mức |
| Tiêu chí | `constraints[]`, `preferences[]`, `priority_weights{}` | Mỗi tiêu chí có hard/soft, value, weight, source, confidence, timestamp |
| Rủi ro | `risk_concerns[]`, `evidence_needed[]` | Ghi rủi ro và loại bằng chứng cần |
| Trạng thái | `journey_state`, `friction_type[]`, `readiness` | Có điều kiện chuyển trạng thái |
| Hội thoại | `asked_questions[]`, `answered_slots[]`, `unresolved_slots[]` | Chống hỏi lặp |
| Bằng chứng | `source`, `source_date`, `verification_status`, `confidence` | Nhận định quan trọng cần nguồn hoặc trạng thái chưa xác minh |
| Đề xuất | `candidate_id`, `fit_by_criterion`, `evidence_coverage`, `tradeoffs` | Tách fit và evidence; lưu lý do xếp hạng |
| Thương mại | `affiliate_relationship`, `disclosure_shown`, `commission_data_isolated` | Hoa hồng tách khỏi suitability/ranking |

### 7.2. JSON khái niệm

```json
{
  "journey_state": "J3_COMPARE",
  "use_case": {
    "value": "chỉnh video và học tập",
    "evidence_source": "user_stated",
    "confidence": "high"
  },
  "desired_outcomes": ["dùng ổn định", "mang đi học hằng ngày"],
  "constraints": [
    {
      "name": "budget_max",
      "value": 25000000,
      "type": "soft",
      "source": "user_stated",
      "confidence": "medium"
    }
  ],
  "preferences": [
    {"name": "portability", "priority": 5, "source": "user_stated"},
    {
      "name": "video_workload",
      "priority": 4,
      "source": "inferred_pending_confirmation"
    }
  ],
  "risk_concerns": [],
  "unresolved_slots": ["software_compatibility"],
  "friction_type": ["F2_PRIORITY_UNCERTAINTY"],
  "next_best_action": "ASK_ONE_DECISION_CHANGING_QUESTION"
}
```

Đây là cấu trúc khái niệm để thảo luận, chưa phải API contract cuối cùng. Cần thống nhất kiểu dữ liệu, enum, quyền lưu trữ, thời hạn lưu và cơ chế xóa dữ liệu theo yêu cầu pháp lý/vận hành.

### 7.3. Luồng IF–THEN

```text
IF use_case is unknown:
    ask one short question about the real-life situation
ELSE:
    identify hard constraints and high-impact preferences

IF a hard constraint is unknown AND it can invalidate candidates:
    ask / verify before claiming fit
ELIF an unresolved preference can change the shortlist:
    ask the highest-value question
ELSE:
    generate a small shortlist

FOR each candidate:
    evaluate only verified attributes
    preserve UNKNOWN separately from fail/pass
    calculate fit independently from evidence coverage

IF critical evidence is missing or contradictory:
    disclose uncertainty; do not overstate confidence

IF no candidate satisfies confirmed hard constraints:
    say no suitable match is established; do not force a recommendation

ALWAYS:
    keep commission data out of fit/ranking logic
    show affiliate disclosure near monetized recommendation/link
    preserve user choice, including no purchase
```

### 7.4. Quy tắc chống lỗi bắt buộc

- Không biến suy luận về cảm xúc, địa vị, thu nhập hoặc tính cách thành dữ kiện người dùng.
- Không coi im lặng là đồng ý; không coi click là bằng chứng sản phẩm phù hợp.
- Không tự động hỏi ngân sách đầu phiên; chỉ hỏi khi có giá trị phân biệt hoặc khách muốn lọc theo giá.
- Không tăng trọng số tiêu chí chỉ vì dữ liệu sản phẩm dễ thu thập.
- Không dùng ngôn ngữ chắc chắn nếu thiếu bằng chứng.
- Không tiếp tục hỏi sau khi đã đủ cơ sở; có thể trình bày shortlist và mời khách sửa giả định.
- Không dùng hoa hồng, quan hệ nhà bán hoặc doanh thu làm biến ảnh hưởng suitability score.

## 8. Đo lường, kiểm thử và lộ trình

### 8.1. Chỉ số cần theo dõi

| Chỉ số | Cách đo | Lưu ý |
|---|---|---|
| Need capture accuracy | Tỷ lệ hồ sơ nhu cầu được chuyên gia/khách xác nhận đúng trên tập có gán nhãn | Cần rubric và người gán nhãn độc lập |
| Question efficiency | Số câu hỏi cần thiết trước khi đủ thông tin | Không tối ưu bằng cách hỏi thiếu |
| Question usefulness | Tỷ lệ câu hỏi làm đổi shortlist, thứ hạng, blocker hoặc giải thích | Phát hiện câu hỏi hình thức |
| Recommendation relevance | Khách/chuyên gia đánh giá mức phù hợp use case và ưu tiên | Không đồng nhất với click/mua |
| Evidence coverage | Tỷ trọng tiêu chí quan trọng có dữ liệu xác minh | Hiển thị missingness |
| Decision confidence change | Tự đánh giá trước/sau tư vấn | Tự tin hơn không đồng nghĩa quyết định đúng |
| Decision deferral/abandonment | Dừng, quay lại, hỏi thêm hoặc không chọn | Phân biệt trải nghiệm kém với chủ động chưa mua |
| Regret/mismatch signals | Khiếu nại, đổi trả, phản hồi sai nhu cầu nếu được chia sẻ hợp lệ | Cần dữ liệu hậu mua và kiểm soát nhiễu |
| Autonomy & trust audit | Disclosure, lý do xếp hạng, trade-off, ngôn ngữ không ép buộc | Chỉ số kiểm soát đạo đức |

**Cảnh báo KPI:** Không dùng conversion rate hoặc affiliate revenue làm thước đo duy nhất. Tối ưu duy nhất theo mua hàng có thể khiến hệ thống tạo áp lực, bỏ qua nhu cầu chưa phù hợp hoặc ưu tiên sản phẩm hoa hồng cao.

### 8.2. Thiết kế kiểm thử thực nghiệm

1. **Gán nhãn:** lấy hội thoại đã ẩn danh; chuyên gia đánh giá use case, constraints, friction, câu hỏi cần thiết và mức đúng của đề xuất.
2. **Offline replay:** chạy cùng tình huống qua quy tắc cũ/mới; chấm test T01–T14 và rubric 7 mục.
3. **Thử nghiệm có kiểm soát:** so sánh thiết kế hỏi hiện tại với thiết kế mới; theo dõi số câu hỏi, need capture accuracy và recommendation relevance.
4. **Phân tích lỗi:** lỗi nghiêm trọng về bịa dữ liệu, hard constraint, disclosure hoặc gây áp lực phải được ưu tiên hơn conversion.
5. **Phát hành:** ghi version, ngành hàng, nguồn dữ liệu và điều kiện rollback; không phát hành quy tắc chưa qua test an toàn.

### 8.3. Lộ trình đề xuất

| Giai đoạn | Đầu việc | Đầu ra | Điều kiện hoàn thành |
|---|---|---|---|
| Tuần 1 — Đồng bộ | CEO chốt mục tiêu; chuyên gia sản phẩm chọn 1–2 ngành hàng; AI thống nhất schema | Phạm vi pilot, glossary, data fields, ranh giới trách nhiệm | Thống nhất hard/soft constraints và nguồn dữ liệu |
| Tuần 2 — Tạo mẫu | Biến 6 mô hình thành prompt/rule; xây test theo ngành hàng | Bộ câu hỏi, state machine, friction mapping, test data | Test chạy được trên bản mô phỏng |
| Tuần 3 — Kiểm thử | Chấm hội thoại; tìm lỗi hỏi thừa, hiểu sai, xếp hạng, evidence | Báo cáo lỗi, đề xuất thay đổi, rubric | Không còn lỗi nghiêm trọng thiếu phương án xử lý |
| Tuần 4 — Pilot | Thử nghiệm có kiểm soát; đo chất lượng và phản hồi | Báo cáo pilot; quyết định giữ/sửa/loại | Đủ mẫu phân tích phù hợp |
| Sau pilot | Mở rộng ngành hàng; rà soát khi dữ liệu/hành vi đổi | v1.1+, thư viện test, dashboard | Có owner và lịch tái đánh giá |

## 9. Kiến nghị quyết định với CEO và đội triển khai

| Ưu tiên | Đề xuất | Lý do |
|---|---|---|
| P0 — Trước khi code sâu | Chọn ngành hàng pilot; chuẩn hóa hard/soft constraints; xác định nguồn/owner dữ liệu; thống nhất độc lập hoa hồng | Tránh AI phải đoán dữ liệu và xung đột mục tiêu |
| P1 — Prototype | State model J1–J6; question value filter; friction tags F1–F9; cổng đủ thông tin; mẫu giải thích | Hành vi nhất quán, dễ kiểm thử |
| P2 — Trước pilot | Nguồn/ngày cập nhật; confidence labels; affiliate disclosure; T01–T14; rubric | Giảm sai lệch và tăng truy xuất |
| P3 — Sau pilot | Hiệu chỉnh trọng số; A/B test số câu hỏi; mở rộng dữ liệu hành vi; đo hậu mua khi hợp lệ | Chỉ tối ưu khi có dữ liệu và cơ chế đo |

### 9.1. Câu hỏi cần CEO quyết định

1. Ngành hàng đầu tiên A+ sẽ thử nghiệm là gì và mức rủi ro quyết định mua thuộc loại nào?
2. A+ có cho phép AI khuyến nghị “chưa nên mua/không cần mua” như kết quả bình thường không?
3. Nguồn dữ liệu nào có thẩm quyền cho thông số, bảo hành, tương thích và giá?
4. Affiliate disclosure xuất hiện ở đâu và ai chịu trách nhiệm rà soát theo thị trường?
5. Ai có quyền phê duyệt thay đổi trọng số, tiêu chí suitability và bộ quy tắc hành vi?

**Khuyến nghị cuối:** Không triển khai đồng loạt trên mọi ngành hàng. Chọn một ngành hàng đại diện, tạo tập test có dữ liệu chuẩn, pilot có kiểm soát rồi mới nhân rộng. Chất lượng hành vi phải được xác nhận trước khi tối ưu thương mại.

## Phụ lục A — Checklist nghiệm thu hành vi AI

- [ ] Hỏi tình huống sử dụng trước thông số khi khách chưa hiểu ngành hàng.
- [ ] Phân biệt điều kiện bắt buộc và sở thích.
- [ ] Lưu nguồn gốc: khách nói, quan sát, suy luận hay unknown.
- [ ] Không hỏi lại; cập nhật khi khách sửa và giải thích thay đổi.
- [ ] Chỉ hỏi khi câu trả lời có thể đổi quyết định hoặc giải quyết rủi ro.
- [ ] Nhận diện friction F1–F9 và chọn can thiệp tương ứng.
- [ ] Không quy mọi phân vân về quá nhiều lựa chọn.
- [ ] Lọc hard constraint trước khi xếp hạng.
- [ ] Tách fit khỏi evidence coverage.
- [ ] Trình bày trade-off và điều kiện không phù hợp.
- [ ] Không bịa dữ liệu hoặc trình bày unknown như đã xác minh.
- [ ] Công khai affiliate gần khuyến nghị/liên kết.
- [ ] Không dùng hoa hồng để tăng suitability ranking.
- [ ] Chấp nhận không mua, chờ thêm hoặc cần kiểm chứng.
- [ ] Truy xuất được lý do và dữ liệu dùng để đề xuất.

## Phụ lục B — Từ điển thuật ngữ

| Thuật ngữ | Diễn giải dùng trong A+ |
|---|---|
| Use case | Tình huống sử dụng cụ thể: ai dùng, ở đâu, làm gì, tần suất nào |
| Job-to-be-done | Việc/tiến bộ người dùng muốn hoàn thành, không đồng nhất tên sản phẩm |
| Hard constraint | Điều kiện bắt buộc; không đáp ứng thì phương án bị loại |
| Soft preference | Sở thích/tiêu chí có thể đánh đổi |
| Decision friction | Nguyên nhân gây khó khăn hoặc trì hoãn quyết định |
| Choice overload | Quá tải lựa chọn; phụ thuộc độ phức tạp, độ khó nhiệm vụ và mức rõ ràng của sở thích |
| Perceived risk | Rủi ro cảm nhận: hiệu năng, tài chính, thời gian, xã hội, riêng tư hoặc sai lầm lựa chọn |
| Evidence coverage | Mức độ tiêu chí quan trọng có dữ liệu đáng tin; không đồng nghĩa điểm phù hợp |
| Recommendation fit | Mức độ khớp với use case, constraints và preferences |
| Affiliate disclosure | Thông tin rõ ràng website có thể nhận hoa hồng từ liên kết mua hàng |

## Tài liệu tham khảo

Các nguồn định hướng mô hình và nguyên tắc. Kết quả cần được diễn giải trong phạm vi bối cảnh nghiên cứu gốc; không mặc định khái quát cho khách hàng A+. Danh mục dưới đây giữ thông tin thư mục của bản báo cáo gốc; DOI/URL cần được bổ sung và xác minh trước khi xuất bản học thuật.

- [S1] Gutman, J. (1982). “A Means-End Chain Model Based on Consumer Categorization Processes.” *Journal of Marketing*, 46(2).
- [S2] Santos, S., & Martins Gonçalves, H. (2021). “The consumer decision journey: A literature review of the foundational models and theories and a future perspective.” *Technological Forecasting and Social Change*, 173, 121117.
- [S3] Chernev, A., Böckenholt, U., & Goodman, J. (2015). “Choice overload: A conceptual review and meta-analysis.” *Journal of Consumer Psychology*, 25(2), 333–358.
- [S4] Scheibehenne, B., Greifeneder, R., & Todd, P. M. (2010). “Can There Ever Be Too Many Options? A Meta-Analytic Review of Choice Overload.” *Journal of Consumer Research*, 37(3), 409–425.
- [S5] Kostric, I., Balog, K., & Radlinski, F. (2021). “Soliciting User Preferences in Conversational Recommender Systems via Usage-related Questions.” *Proceedings of ACM RecSys 2021*.
- [S6] Christakopoulou, K., Radlinski, F., & Hofmann, K. (2016). “Towards Conversational Recommender Systems.” *Proceedings of the 22nd ACM SIGKDD*, 815–824.
- [S7] Pelaez, A., Chen, C.-W., & Chen, Y. X. (2019). “Effects of Perceived Risk on Intention to Purchase: A Meta-Analysis.” *Journal of Computer Information Systems*, 59(1), 73–84.
- [S8] Handoyo, S. (2024). “Purchasing in the digital age: A meta-analytical perspective on trust, risk, security, and e-WOM in e-commerce.” *Heliyon*, 10(8), e29714.
- [S9] Filieri, R., Hofacker, C. F., & Alguezaui, S. (2018). “What makes information in online consumer reviews diagnostic over time?” *Computers in Human Behavior*, 80, 122–131.
- [S10] Qiu, K., & Zhang, L. (2024). “How online reviews affect purchase intention: A meta-analysis across contextual and cultural factors.” *Data and Information Management*, 8(2), 100058.
- [S11] Aljukhadar, M., Trifts, V., & Sénécal, S. (2017). “Consumer self-construal and trust as determinants of the reactance to a recommender advice.” *Psychology & Marketing*, 34(7), 708–719.
- [S12] Reynolds-Tylus, T. (2019). “Psychological Reactance and Persuasive Health Communication: A Review of the Literature.” *Frontiers in Communication*, 4, 56.
- [S13] U.S. Federal Trade Commission. *FTC’s Endorsement Guides: What People Are Asking* — section “What About Affiliate or Network Marketing?”
- [S14] Ziegfeld, L., Di Scala, D., & Cremers, A. H. (2025). “The effect of preference elicitation methods on the user experience in conversational recommender systems.” *Computer Speech & Language*, 89, 101696.

**Ghi chú cập nhật:** Ngày chốt báo cáo 12/11/2026. Trước khi triển khai ra thị trường, A+ cần rà soát quy định quảng cáo/affiliate, quyền riêng tư và bảo vệ người tiêu dùng tại từng quốc gia mục tiêu. Hướng dẫn FTC chỉ là nguồn tham khảo của Hoa Kỳ.
