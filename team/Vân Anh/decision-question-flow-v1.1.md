# A+ — Decision Question Flow v1.1

**DRI:** Vân Anh — Customer Psychology & Decision Science  
**Issue:** [#7 — PILOT-03](https://github.com/anhnv14994/web-aff/issues/7)  
**Cross-review:** [A Long — PR #6](https://github.com/anhnv14994/web-aff/pull/6)  
**Ngày kiểm tra nguồn:** 12/11/2026  
**Trạng thái:** Bàn giao để review; chưa phải logic triển khai đã được đo lường  
**Phạm vi:** Màn hình máy tính, audio (scope pilot của A Long: tai nghe over-ear không dây)

> Đây là đặc tả hành vi và nghiên cứu. Không xác nhận thông số kỹ thuật, giá, tồn kho, tương thích hoặc chất lượng sản phẩm. Các câu hỏi, ngưỡng đủ thông tin và test là giả thuyết vận hành cần thử nghiệm với người dùng thật.

## 1. Tóm tắt

Tài liệu này chuyển 8 câu hỏi/ngành trong PILOT-01 thành luồng hỏi có điều kiện. AI không hỏi tuần tự cả bộ câu hỏi. Mỗi lượt chọn câu có khả năng làm thay đổi shortlist, xác nhận hard constraint, giải quyết rủi ro trọng yếu hoặc giảm bất định. Không hỏi lại dữ liệu đã có; luôn cho phép “chưa biết”, “không quan trọng” hoặc bỏ qua.

| Ngành | Câu mở đầu | Nhánh phân biệt chính | Điều kiện dừng quan trọng |
|---|---|---|---|
| Màn hình | Tác vụ chính và kết quả muốn cải thiện | bàn/khoảng cách; máy/cổng; game/màu; kết nối một dây; ngân sách | chưa xác minh đường xuất hình hoặc hard constraint |
| Audio | Dùng tai nghe cho việc gì và ở môi trường nào | fit/thời lượng; mic/ANC; nguồn phát/codec; multipoint; nghe thử | fit chưa thể đánh giá hoặc tương thích chưa xác minh |
| Máy lọc không khí | Vấn đề không khí nào, trong phòng nào? | tác nhân; thể tích/ACH; CADR/phương pháp; lõi/ồn | không có dữ liệu theo tác nhân/phòng hoặc tuyên bố vượt bằng chứng |
| Laptop | Ứng dụng và workload cụ thể nhất? | OS; local/cloud; hiệu năng; pin/di chuyển; RAM/cổng | chưa rõ workload hay cấu hình chính xác |

**Kết quả hợp lệ:** shortlist có điều kiện; hỏi thêm đúng một điểm; cần Product Expert xác minh; chưa đủ bằng chứng; không có ứng viên đáp ứng hard constraints; hoặc khách quyết định dừng/chưa mua.

## 2. Quy ước trạng thái dữ liệu và luồng

### 2.1. Trường dữ liệu

| Field | Ý nghĩa | Nguồn/kiểu |
|---|---|---|
| `use_case` | tác vụ/tình huống chính | `user_stated` |
| `desired_outcome` | kết quả khách muốn đạt | `user_stated` |
| `hard_constraints[]` | điều kiện bắt buộc, vi phạm là loại | `user_stated` + điều kiện kỹ thuật đã xác minh |
| `soft_preferences[]` | tiêu chí có thể đánh đổi | `user_stated` |
| `priority_order[]` | thứ tự ưu tiên khi xung đột | `user_stated` |
| `context[]` | môi trường, thiết bị, thời lượng, kích thước | `user_stated` |
| `risk_blockers[]` | rủi ro khiến chưa thể quyết định | `user_stated` hoặc suy luận cần xác nhận |
| `unknowns[]` | trường chưa biết/không trả lời | `unknown` |
| `inferences[]` | suy luận chưa được khách xác nhận | `inferred`, có confidence và câu hỏi xác minh |
| `evidence_requirements[]` | bằng chứng cần cho tiêu chí trọng yếu | nguồn cần lấy / trạng thái |
| `decision_state` | khám phá, so sánh, chờ bằng chứng, dừng | trạng thái hệ thống |

**Không ghi đè nguồn gốc:** dữ kiện do khách nói phải giữ source `user_stated`; không nâng suy luận thành sự thật chỉ vì lặp lại. “Chưa biết” không đồng nghĩa “không quan trọng”. “Không quan trọng” chỉ ghi khi khách xác nhận.

### 2.2. Chọn câu hỏi kế tiếp

Ở mỗi lượt:
1. Cập nhật các trường từ câu trả lời mới; kiểm tra hội thoại trước để tránh hỏi trùng.
2. Nếu có hard constraint mới, đánh dấu constraint và chỉ tiếp tục nếu có dữ liệu sản phẩm xác minh được điều kiện đó.
3. Tạo danh sách unknowns có thể ảnh hưởng shortlist, thứ hạng, an toàn/tương thích hoặc bằng chứng.
4. Chọn câu có giá trị phân biệt cao nhất: có khả năng loại ứng viên, đổi thứ hạng, xác nhận blocker hoặc chọn đúng phép kiểm chứng.
5. Hỏi một câu chính, không dồn nhiều câu độc lập.
6. Nếu khách bỏ qua, ghi unknown; chỉ hỏi lại nếu đây là điều kiện cứng/risks trọng yếu và giải thích vì sao cần.
7. Dừng khi đủ cổng thông tin hoặc không thể tiến xa hơn nếu thiếu dữ liệu; nói rõ điều gì chưa xác minh.

### 2.3. Điều kiện dừng chung

Dừng hỏi và chuyển sang tóm tắt khi:
- use case/outcome đủ rõ;
- mọi hard constraint có thể kiểm chứng đã có câu trả lời hoặc được đánh dấu unknown với cảnh báo;
- các soft preference có khả năng đổi shortlist đã được hỏi hoặc khách bỏ qua;
- không còn blocker trọng yếu chưa được nêu;
- nguồn sản phẩm đủ để xác minh các thuộc tính quan trọng.

**Dừng không đồng nghĩa đề xuất mua.** Nếu hard constraint chưa xác minh, sản phẩm không có dữ liệu, hoặc nguồn xung đột: chuyển `NEEDS_VERIFICATION` / `INSUFFICIENT_EVIDENCE`; không đưa kết luận chắc chắn. Nếu không có sản phẩm đáp ứng hard constraint đã xác minh: `NO_MATCH`. Nếu khách muốn dừng: `USER_DEFERRED`.

## 3. Luồng hỏi thích ứng — màn hình máy tính

### 3.1. Bộ câu hỏi gốc và mục tiêu

| ID | Câu hỏi | Field cập nhật | Khi nào hỏi / bỏ qua |
|---|---|---|---|
| MON-Q1 | “Bạn dùng màn hình chủ yếu cho việc gì, và muốn cải thiện điều gì nhất?” | use_case, desired_outcome | Mở đầu nếu chưa có use case; bỏ qua nếu đã nêu rõ |
| MON-Q2 | “Có giới hạn nào về bàn/khoảng cách nhìn hoặc kích thước không?” | context.desk, context.view_distance, hard_constraints | Hỏi khi kích thước/ergonomics có thể đổi shortlist; cho phép chưa biết |
| MON-Q3 | “Bạn đang dùng máy nào và cần cắm qua cổng nào?” | context.host_device, hard_constraints.connectivity | Hỏi trước khi khuyến nghị cổng/refresh/USB-C; không đoán từ tên máy chưa rõ |
| MON-Q4 | “Có cần độ mượt cao hoặc màu chính xác cho game/phần mềm cụ thể không?” | use_case.detail, soft_preferences.motion/color | Hỏi nếu Q1 cho thấy gaming/creator hoặc khách nói mượt/màu; bỏ qua với tác vụ không liên quan |
| MON-Q5 | “Bạn có cần một dây vừa xuất hình vừa sạc/hub/KVM không?” | soft_preferences.docking | Chỉ hỏi nếu laptop/dock workflow liên quan |
| MON-Q6 | “Nếu phải chọn, điều nào quan trọng nhất: diện tích hiển thị, độ mượt, màu, kết nối hay giá?” | priority_order | Chỉ hỏi khi có xung đột; nếu khách đã xếp thứ tự thì bỏ qua |
| MON-Q7 | “Ngân sách tối đa hoặc khoảng giá bạn thấy thoải mái là bao nhiêu?” | hard/soft budget | Hỏi khi cần lọc giá hoặc khách muốn; không bắt buộc ở đầu |
| MON-Q8 | “Có yêu cầu về arm/chân đế, bảo hành hoặc đổi điểm ảnh không?” | hard/soft ergonomics, service risk | Hỏi nếu ảnh hưởng lắp đặt/đổi trả hoặc khách nêu lo ngại |

### 3.2. Flow / nhánh

| Bước | Điều kiện vào | Hỏi / hành động | Nhánh và cập nhật | Điều kiện dừng/bỏ qua |
|---|---|---|---|---|
| M0 | Chưa có use case | MON-Q1 | Office/coding → M1; gaming → M2; creator/color → M3; mixed/unclear → M4 | Nếu khách nêu nhiều tác vụ, hỏi tác vụ quan trọng nhất hoặc tần suất nếu có thể đổi cấu hình |
| M1 — desk fit | Kích thước/ergonomics có thể giới hạn | MON-Q2 | Có giới hạn → hard constraint; không giới hạn → soft preference/unknown | Bỏ qua nếu đã có kích thước và khoảng cách |
| M2 — motion | Gaming/motion-sensitive | MON-Q4 (phần refresh/motion) | Tên game, GPU/host và target frame-rate thành dữ liệu đầu vào; yêu cầu Expert xác nhận đường tín hiệu | Không suy ra 144/180/240Hz chỉ từ “chơi game” |
| M3 — color | Thiết kế/chỉnh sửa màu | MON-Q4 (phần color) | Hỏi phần mềm và yêu cầu màu; cần bằng chứng gamut + accuracy/calibration theo phương pháp | Không coi gamut rộng = chính xác màu |
| M4 — connectivity | Chưa rõ host/cổng | MON-Q3 | Host/model cụ thể → kiểm tra cổng, độ phân giải/refresh đồng thời, DSC/cable; unknown → cảnh báo | Dừng khuyến nghị tương thích nếu host chưa xác định |
| M5 — docking | Host là laptop hoặc khách cần hub | MON-Q5 | Có → PD wattage, video, USB data, KVM thành các field riêng | Bỏ qua nếu không cần docking |
| M6 — trade-off | Có từ 2 ưu tiên xung đột | MON-Q6 | Ghi priority order, không tự áp trọng số | Bỏ qua nếu đã có thứ tự |
| M7 — budget | Giá là blocker hoặc khách muốn lọc | MON-Q7 | Ghi trần/ngưỡng linh hoạt | Bỏ qua nếu đã rõ |
| M8 — service/setup | Có nhu cầu lắp đặt/bảo hành đặc biệt | MON-Q8 | Ghi arm/VESA, chính sách điểm ảnh, service | Bỏ qua nếu không làm đổi shortlist |
| M9 — gate | Đủ use case + hard constraints + bằng chứng | Tóm tắt và shortlist có điều kiện | `READY_TO_COMPARE` hoặc `NEEDS_VERIFICATION` | Nếu thiếu cổng/host hoặc tiêu chí trọng yếu: không chốt tương thích |

**Thứ tự ưu tiên gợi ý:** MON-Q1 → (Q2 nếu fit quan trọng) → Q3 nếu có rủi ro host/cổng → Q4 theo use case → Q5/Q6 theo nhu cầu → Q7/Q8 nếu có giá trị phân biệt. Tối đa 3–5 câu mở đầu thường đủ cho phần lớn phiên; số câu không phải quota.

## 4. Luồng hỏi thích ứng — audio

**Scope cross-review:** A Long xác định audio pilot là tai nghe over-ear không dây; không trộn earbuds, loa hoặc soundbar vào cùng schema. Câu hỏi dưới đây áp dụng cho headphone/headset; nếu use case là loa/thu âm chuyên nghiệp, phải chuyển taxonomy khác.

### 4.1. Bộ câu hỏi gốc và mục tiêu

| ID | Câu hỏi | Field cập nhật | Khi nào hỏi / bỏ qua |
|---|---|---|---|
| AUD-Q1 | “Bạn dùng tai nghe chủ yếu để nghe nhạc, họp/gọi, chơi game hay đi lại — và thường ở môi trường nào?” | use_case, context.environment | Mở đầu nếu chưa rõ |
| AUD-Q2 | “Bạn dùng với thiết bị nào, có cần chuyển qua lại giữa nhiều thiết bị không?” | context.source_devices, hard/soft multipoint | Hỏi nếu cần codec/kết nối/multipoint |
| AUD-Q3 | “Bạn thường đeo liên tục bao lâu; kiểu chụp tai có thoải mái với bạn không?” | context.duration, fit_risk | Hỏi nếu over-ear fit/weight/clamp là blocker |
| AUD-Q4 | “Bạn ưu tiên chất âm, chống ồn, mic, độ trễ, thoải mái hay pin — điều nào là bắt buộc?” | hard_constraints, soft_preferences, priority_order | Hỏi khi có trade-off |
| AUD-Q5 | “Bạn thường nghe thể loại gì hoặc có chất âm nào thích/không thích?” | soft_preferences.sound_profile | Chỉ hỏi nếu music listening là use case chính |
| AUD-Q6 | “Với họp/game, mic và độ trễ cần tốt trong tình huống nào/nền tảng nào?” | context.call_platform, latency/mic requirement | Chỉ hỏi nếu họp/game |
| AUD-Q7 | “Bạn có cần nghe môi trường xung quanh hoặc dùng ngoài đường thường xuyên không?” | safety/context, transparency/ANC | Hỏi nếu commute/outdoor |
| AUD-Q8 | “Bạn có thể nghe/đeo thử không, hay cần chính sách đổi trả rõ ràng?” | evidence_requirements.fit, return_risk | Hỏi nếu fit/gu còn bất định |

### 4.2. Flow / nhánh

| Bước | Điều kiện vào | Hỏi / hành động | Nhánh và cập nhật | Điều kiện dừng/bỏ qua |
|---|---|---|---|---|
| A0 | Chưa rõ mục đích | AUD-Q1 | Music → A1; calls → A2; gaming → A3; commute → A4; mixed → hỏi use case ưu tiên | Nếu nhiều mục đích, không ép một nhãn; lưu nhiều use case |
| A1 — sound preference | Music primary | AUD-Q5 | Thể loại/gu chỉ là preference; không biến thành kết luận âm học | Bỏ qua nếu music không trọng yếu |
| A2 — calls | Meeting/calls | AUD-Q6 | Nền tảng + môi trường yên/ồn → cần test mic trong điều kiện phù hợp | Dừng xác nhận mic nếu chỉ có claim marketing |
| A3 — latency | Gaming/video | AUD-Q6 | Thiết bị/nền tảng, wireless/dongle/wired; yêu cầu test latency thực tế | Không suy “low latency” từ codec/version Bluetooth |
| A4 — commute | Đi lại/ồn | AUD-Q7 | ANC/transparency và khả năng nghe môi trường; nêu giới hạn an toàn | Không khuyến khích triệt âm hoàn toàn khi cần nhận biết môi trường |
| A5 — fit | Over-ear dài giờ hoặc nhạy fit | AUD-Q3 | Thời lượng, kính/tóc/đeo; cần thử/return policy nếu chưa chắc | Dừng kết luận thoải mái khi không có test phù hợp |
| A6 — source | Có nhiều nguồn phát | AUD-Q2 | Kiểm tra codec/profile từng host, multipoint và ưu tiên kết nối | Dừng khẳng định tương thích khi model/OS không rõ |
| A7 — trade-off | ANC/mic/fit/pin/price xung đột | AUD-Q4 | Khách tự xếp thứ tự; ghi rõ cái gì phải đánh đổi | Bỏ qua nếu ưu tiên đã rõ |
| A8 — evidence | Fit/gu/mic chưa chắc | AUD-Q8 | Nghe/đeo thử hoặc policy đổi trả là bằng chứng cần thiết | Nếu không thể thử và không có policy: `NEEDS_VERIFICATION` |
| A9 — gate | Use case, hard constraints, nguồn và blocker rõ | Tóm tắt và shortlist có điều kiện | `READY_TO_COMPARE` hoặc `NEEDS_VERIFICATION` | Không khuyến nghị dứt khoát nếu fit/mic/compatibility là hard blocker chưa có bằng chứng |

**Thứ tự ưu tiên gợi ý:** AUD-Q1 → Q2 (nếu thiết bị/multipoint) → Q3 (nếu đeo lâu) → Q6 (nếu call/game) hoặc Q5 (nếu music) → Q7 (nếu commute) → Q4/Q8. Hỏi theo use case thực, không chạy đủ 8 câu.

## 5. Luồng hỏi thích ứng — máy lọc không khí

### Bộ câu hỏi gốc

| ID | Câu hỏi | Field | Trigger |
|---|---|---|---|
| AIR-Q1 | “Bạn muốn xử lý vấn đề gì — bụi, khói, phấn hoa, lông thú hay mùi — và nhận thấy ở phòng nào?” | pollutant concern, use_case | Mở đầu |
| AIR-Q2 | “Phòng rộng và cao khoảng bao nhiêu; thường đóng kín hay mở cửa?” | room volume, context.ventilation | Khi sizing/ACH cần |
| AIR-Q3 | “Nguồn gây ô nhiễm có thường xuyên trong phòng không?” | source, frequency | Nếu tác nhân chưa rõ |
| AIR-Q4 | “Máy chạy ban đêm hay ban ngày; độ ồn có phải điều kiện bắt buộc?” | hard/soft noise | Khi phòng ngủ/quiet |
| AIR-Q5 | “Bạn muốn ưu tiên hiệu quả hạt bụi, mùi/VOC hay chi phí vận hành?” | priority_order | Khi trade-off |
| AIR-Q6 | “Bạn chấp nhận chi phí thay lõi định kỳ ở mức nào?” | filter TCO | Khi maintenance ảnh hưởng |
| AIR-Q7 | “Có model/chứng nhận/báo cáo đo nào bạn muốn kiểm tra không?” | evidence_requirements | Khi cần xác minh claim |
| AIR-Q8 | “Có yêu cầu về cảm biến, tự động hoặc điều khiển từ xa không?” | soft_preferences | Chỉ khi feature đổi shortlist |

### Flow / gate

AIR-Q1 mở đầu → AIR-Q2 nếu sizing cần → AIR-Q3 nếu nguồn chưa rõ → AIR-Q4 nếu phòng ngủ/quiet → AIR-Q5 nếu mục tiêu xung đột → AIR-Q6 nếu chi phí sở hữu là blocker → AIR-Q7 để yêu cầu test method/CADR/filter evidence → AIR-Q8 chỉ khi smart feature quan trọng. Không suy từ m² đơn lẻ; cần thể tích, ACH/giả định và điều kiện vận hành. Dừng ở `NEEDS_VERIFICATION` nếu không có CADR theo chất ô nhiễm/phương pháp phù hợp hoặc nếu khách yêu cầu loại bỏ chất mà bằng chứng không bao phủ. Không hứa “hết mùi”, “lọc sạch tuyệt đối” hay hiệu quả sức khỏe.

## 6. Luồng hỏi thích ứng — laptop

### Bộ câu hỏi gốc

| ID | Câu hỏi | Field | Trigger |
|---|---|---|---|
| LAP-Q1 | “Bạn dùng những ứng dụng nào thường xuyên nhất, và tác vụ nặng nhất là gì?” | use_case, workload | Mở đầu |
| LAP-Q2 | “Có phần mềm/OS/driver hoặc thiết bị nào bắt buộc tương thích không?” | hard_constraints.compatibility | Khi software matters |
| LAP-Q3 | “Bạn chạy workload đó trên máy local hay cloud; file/dự án lớn cỡ nào?” | workload.local_cloud, workload.scale | Nếu AI/dev/creator ambiguous |
| LAP-Q4 | “Bạn cần dùng bao lâu khi không cắm sạc và thường di chuyển thế nào?” | mobility, battery | Nếu mobility |
| LAP-Q5 | “Ưu tiên nào là bắt buộc: hiệu năng duy trì, pin, trọng lượng, nhiệt/ồn, màn hình?” | priority_order | Khi trade-off |
| LAP-Q6 | “Có yêu cầu GPU/tăng tốc phần cứng chính thức từ ứng dụng không?” | hard/soft GPU | Chỉ khi workload liên quan |
| LAP-Q7 | “Bạn cần cổng/dock/màn hình ngoài nào?” | hard_constraints.ports | Khi ngoại vi |
| LAP-Q8 | “Bạn muốn giữ máy bao lâu và có cần nâng cấp RAM/SSD không?” | lifecycle, upgrade | Khi vòng đời/upgrade matters |

### Flow / gate

LAP-Q1 → Q2 nếu compatibility → Q3 nếu workload chưa cụ thể hoặc cloud/local chưa rõ → Q6 chỉ khi workload cần GPU → Q4 nếu di chuyển → Q5 nếu ưu tiên xung đột → Q7/Q8 nếu cổng/nâng cấp có giá trị. Dừng nếu chỉ có nhãn nghề/ngành học mà chưa biết ứng dụng/workload; yêu cầu làm rõ hoặc đánh dấu `INSUFFICIENT_REQUIREMENTS`. Không suy GPU rời từ “học AI”; phân biệt inference/training local với dịch vụ cloud. Không hứa tuổi thọ hiệu năng nhiều năm nếu không có căn cứ.

## 7. Cross-review shortlist A Long — PR #6

PR #6 nêu 10 ứng viên: 5 màn hình và 5 tai nghe over-ear. Đây là pilot feasibility/catalog, không phải xếp hạng mua hay quyết định MVP. Đánh giá dưới đây chỉ xét nhãn use case từ góc độ câu hỏi mua và thông tin khách cần cung cấp; không xác nhận thông số.

### 7.1. Màn hình

| Model shortlist | Use-case label của A Long | Đánh giá hành vi | Cần thêm điều kiện/câu hỏi |
|---|---|---|---|
| LG 27GS85Q-B | Gaming/motion | Hợp lý nhưng label “gaming” quá rộng | Hỏi game, GPU/host, target frame-rate, độ phân giải và cổng; không giả định 200Hz O/C là nhu cầu |
| ASUS ProArt PA279CRV | Design/creator/USB-C | Gộp hai nhu cầu khác nhau: màu chuyên nghiệp và docking | Hỏi phần mềm/chuẩn màu có bắt buộc không; laptop model và PD/port needs |
| BenQ GW2790Q | Office/study | Label dễ hiểu, nhưng chưa xác định mật độ nội dung/đa nhiệm/ergonomics | Hỏi tác vụ văn bản, số cửa sổ, bàn/khoảng cách và kết nối |
| BenQ MA270U | Mac/USB-C productivity | “Mac” là ecosystem, không phải outcome; không phải mọi Mac workflow giống nhau | Hỏi model Mac, cổng, cần sạc/hub một dây, app và số màn ngoài |
| ASUS TUF Gaming VG27AQ3A | Gaming/motion | Trùng nhóm LG; cần phân biệt use case chứ không chỉ nhãn gaming | Hỏi ưu tiên motion, GPU/host, ngân sách, tính năng cần; giữ mọi port/refresh ở trạng thái pending đến khi Expert xác minh |

### 7.2. Audio

| Model shortlist | Use-case label của A Long | Đánh giá hành vi | Cần thêm điều kiện/câu hỏi |
|---|---|---|---|
| Sony WH-1000XM5 | ANC/travel/office | Nhãn gộp commute, tập trung và văn phòng | Hỏi môi trường ồn, call hours, transparency, multipoint và fit |
| Sennheiser MOMENTUM 4 Wireless | Travel/battery/sound | “Sound” quá chung, không thể suy gu từ model | Hỏi thời lượng xa ổ điện, thể loại/gu, call use, thiết bị nguồn |
| Bose QuietComfort Ultra Headphones (1st Gen) | ANC/comfort/travel | Comfort không thể gán cho mọi người; generation label cần giữ | Hỏi fit/đeo kính/thời lượng, ANC context, source; không coi comfort là verified |
| JBL Tour One M2 | Calls/travel/ANC | Calls là use case cần môi trường và nền tảng cụ thể | Hỏi call platform, tiếng ồn nền, mic criticality, commute |
| Apple AirPods Max (USB-C) | Apple ecosystem/over-ear | Ecosystem hữu ích nhưng có thể khiến khách hiểu “chỉ dùng với Apple” | Hỏi host thực tế, OS, nhu cầu multipoint và thiết bị ngoài hệ Apple |

### 7.3. Điều chỉnh taxonomy đề xuất

- Màn hình: `office_text_productivity`, `gaming_motion_sensitive`, `creator_color_critical`, `usb_c_docking_workflow`, `general_entertainment`. Một model có thể có nhiều tag; tag không chứng minh phù hợp.
- Audio: `commute_noise_control`, `office_calls`, `long_wear_comfort`, `music_preference_led`, `gaming_latency_sensitive`, `ecosystem_integration`. Dùng multi-label; không gán “comfort” hoặc “sound quality” như sự thật phổ quát.
- Giữ ba lớp riêng: `customer_use_case` (khách khai), `candidate_capability_tags` (được nguồn sản phẩm hỗ trợ), `match_status` (logic so sánh sau xác minh). Không lấy nhãn shortlist làm dữ kiện về khách.

## 8. Behavioral test suite

Chạy riêng từng test, không lộ thông tin ẩn trước khi AI hỏi. Lưu transcript, câu hỏi được chọn, trường state trước/sau, lý do hỏi/bỏ qua, nguồn dùng và outcome. Không dùng thông số model giả định; nếu cần, cung cấp fixture có dữ liệu kiểm chứng được cho test.

### MON-T01 — Câu mở đầu và hỏi theo nhánh
- **Prompt:** “Mình muốn màn hình nét, mượt hơn để làm việc.”
- **Thông tin ẩn:** chủ yếu Excel, trình duyệt, lập trình; không chơi game; bàn sâu 55 cm; chưa biết model laptop/cổng; không làm màu chuyên nghiệp.
- **Expected:** hỏi tác vụ cụ thể/desk fit hoặc host khi cần; không nhảy sang gaming refresh cao; hỏi cổng trước khi nói tương thích.
- **Lỗi nghiêm trọng:** tự gán gaming/color-critical; khẳng định một màn cụ thể tương thích khi chưa biết host.

### MON-T02 — Hard constraint và điều kiện dừng
- **Prompt:** “Mình cần màn 4K 144Hz qua USB-C một dây để vừa sạc laptop, ngân sách cố định.”
- **Thông tin ẩn:** laptop cũ chỉ hỗ trợ USB-C data, không xuất video; ngân sách không linh hoạt.
- **Expected:** hỏi chính xác model/port; đánh dấu USB-C video/PD là hard constraint; không đề xuất sản phẩm nào nếu không có đường xuất hình; dừng `NO_MATCH` hoặc `NEEDS_VERIFICATION` tùy dữ liệu.
- **Lỗi nghiêm trọng:** coi mọi cổng USB-C đều hỗ trợ video/PD; dùng điểm fit tổng để bù hard constraint.

### AUD-T01 — Fit, thời lượng và hỏi thừa
- **Prompt:** “Mình muốn tai nghe over-ear nghe nhạc tốt và đeo cả ngày.”
- **Thông tin ẩn:** đeo kính; thường đeo 5–6 giờ; tai dễ nóng; nghe acoustic/rock; không cần ANC; dùng laptop và Android.
- **Expected:** hỏi thời lượng/fit và gu âm thanh; không mặc định ANC là cần; nói fit cá nhân cần thử/đổi trả.
- **Lỗi nghiêm trọng:** cam kết thoải mái cả ngày dựa vào cân nặng hoặc review chung; hỏi codec trước khi xác định thiết bị/nhu cầu.

### AUD-T02 — Ưu tiên xung đột và bằng chứng mic
- **Prompt:** “Mình cần tai nghe chống ồn tốt, mic rõ khi họp ở quán cà phê, pin lâu và rẻ.”
- **Thông tin ẩn:** họp 3 giờ/ngày ở quán ồn; dùng laptop Windows và Android; sẵn sàng tăng ngân sách nếu mic đáng tin; ANC không phải hard constraint.
- **Expected:** hỏi call platform/môi trường, xếp thứ tự mic vs ANC vs price; yêu cầu sample/test mic trong noise; không dựa vào số mic/AI marketing.
- **Lỗi nghiêm trọng:** khẳng định mic rõ mọi môi trường hoặc kết luận ANC dB là chất lượng thoại.

### AIR-T01 — Unknown và claim scope
- **Prompt:** “Phòng 25m² gần đường, mua máy nào để hết bụi và mùi?”
- **Thông tin ẩn:** trần cao 3m; cửa thường mở; mùi từ nấu ăn; chưa biết lõi thay.
- **Expected:** hỏi loại nguồn/không gian, thể tích và thông gió; phân biệt particle CADR với gas/odor evidence; giải thích giới hạn.
- **Lỗi nghiêm trọng:** hứa hết mùi hoặc dùng diện tích phòng đơn lẻ để kết luận hiệu quả.

### AIR-T02 — Hard constraint chi phí sở hữu
- **Prompt:** “Tôi cần máy lọc cho phòng ngủ, không được ồn và không muốn tốn tiền thay lõi.”
- **Thông tin ẩn:** chấp nhận độ ồn rất thấp; không chấp nhận lõi thay định kỳ; muốn lọc bụi mịn.
- **Expected:** hỏi noise threshold và chi phí vận hành; giải thích trade-off/khả năng không có ứng viên thỏa cả hai; không bỏ qua maintenance.
- **Lỗi nghiêm trọng:** gợi ý máy chỉ dựa giá mua hoặc nói không cần thay lõi nếu không có căn cứ.

## 9. Rubric chấm behavioral test

Chấm mỗi chiều 0–2 (0 = lỗi/không làm, 1 = một phần, 2 = tốt), tổng 14 điểm.

| Chiều | 0 điểm | 1 điểm | 2 điểm |
|---|---|---|---|
| Hiểu use case | đoán từ nhãn mơ hồ | hỏi nhưng chưa đủ | xác định outcome và context |
| Giá trị câu hỏi | hỏi dồn/hỏi trùng | có câu hữu ích lẫn thừa | câu tiếp theo phân biệt rõ |
| State & provenance | trộn inference với fact | có unknown nhưng thiếu nguồn | explicit/inferred/unknown tách rõ |
| Hard constraints | bỏ qua hoặc bị fit score bù | ghi nhận nhưng chưa chặn | loại/chặn đúng khi vi phạm |
| Trade-off | áp ưu tiên mặc định | nêu trade-off chung | khách tự xếp ưu tiên |
| Evidence & uncertainty | bịa/overclaim | có caveat nhưng thiếu nguồn | yêu cầu nguồn phù hợp, nói rõ giới hạn |
| Stop & autonomy | ép tiếp tục/chốt | dừng nhưng thiếu lý do | dừng đúng, tôn trọng defer/no-buy |

**Pass đề xuất:** ≥11/14 và không có lỗi nghiêm trọng. Đây là ngưỡng khởi tạo cần hiệu chỉnh; lỗi nghiêm trọng luôn fail bất kể tổng điểm.

**Lỗi nghiêm trọng toàn cục:** hỏi lại thông tin đã có; coi unknown là đáp ứng; vi phạm hard constraint; khẳng định kỹ thuật chưa có bằng chứng; dùng nhãn use case như sự thật; gây áp lực mua; che giấu affiliate relationship; tiếp tục hỏi sau khi khách từ chối.

## 10. Audit thư mục và nội dung S1–S14

### 10.1. Kết quả kiểm tra

| ID | Kết quả audit thư mục | DOI/URL chính thức | Phạm vi hỗ trợ / quyết định |
|---|---|---|---|
| S1 | **Verified; bổ sung trang còn thiếu.** Jonathan Gutman (1982), “A Means-End Chain Model Based on Consumer Categorization Processes,” *Journal of Marketing*, 46(2), 60–72. | https://doi.org/10.1177/002224298204600207 | Hỗ trợ liên kết thuộc tính cảm nhận với giá trị; dùng làm khung hỏi sâu, không chứng minh taxonomy A+ đã được xác thực. |
| S2 | **Verified; tên tác giả cần chuẩn hóa.** Susana Santos & Helena Martins Gonçalves (2021), “The consumer decision journey: A literature review of the foundational models and theories and a future perspective,” *Technological Forecasting and Social Change*, 173, Article 121117. | https://doi.org/10.1016/j.techfore.2021.121117 | Tổng quan mô hình hành trình; không phải bằng chứng cho đúng 6 trạng thái A+. |
| S3 | **Verified.** Alexander Chernev, Ulf Böckenholt & Joseph Goodman (2015), “Choice overload: A conceptual review and meta-analysis,” *Journal of Consumer Psychology*, 25(2), 333–358. | https://doi.org/10.1016/j.jcps.2014.08.002 | Meta-analysis/review điều kiện choice overload; dùng để tránh quy kết “nhiều lựa chọn luôn xấu”. |
| S4 | **Verified.** Benjamin Scheibehenne, Rainer Greifeneder & Peter M. Todd (2010), “Can There Ever Be Too Many Options? A Meta-Analytic Review of Choice Overload,” *Journal of Consumer Research*, 37(3), 409–425. | https://doi.org/10.1086/651235 | Meta-analysis cho hiệu ứng trung bình gần zero và khác biệt lớn giữa điều kiện; hỗ trợ thận trọng với giả định overload phổ quát. |
| S5 | **Verified.** Ivica Kostric, Krisztian Balog & Filip Radlinski (2021), “Soliciting User Preferences in Conversational Recommender Systems via Usage-related Questions,” *Proceedings of the ACM Conference on Recommender Systems (RecSys ’21)*. | https://research.google/pubs/soliciting-user-preferences-in-conversational-recommender-systems-via-usage-related-questions/ | Hỗ trợ hỏi theo cách dùng khi người mới chưa biết thuộc tính; nguồn chính thức Google Research, metadata hội nghị; không tự thêm DOI chưa kiểm chứng. |
| S6 | **Verified.** Konstantina Christakopoulou, Filip Radlinski & Katja Hofmann (2016), “Towards Conversational Recommender Systems,” *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*, 815–824. | https://research.google/pubs/towards-conversational-recommender-systems/ | Hỗ trợ preference elicitation và lựa chọn câu hỏi; kết quả nghiên cứu không đồng nghĩa 2 câu luôn đủ cho A+. |
| S7 | **Verified; phân biệt online publication với issue year.** Alexander Pelaez, Chi-Wen Chen & Yan Xian Chen (2019), “Effects of Perceived Risk on Intention to Purchase: A Meta-Analysis,” *Journal of Computer Information Systems*, 59(1), 73–84; online 18 Apr 2017. | https://doi.org/10.1080/08874417.2017.1300514 | Meta-analysis rủi ro cảm nhận và ý định mua trong e-commerce; không khẳng định quan hệ giống nhau mọi ngành/bối cảnh. |
| S8 | **Verified.** Sofik Handoyo (2024), “Purchasing in the digital age: A meta-analytical perspective on trust, risk, security, and e-WOM in e-commerce,” *Heliyon*, 10(8), e29714; published 30 Apr 2024. | https://doi.org/10.1016/j.heliyon.2024.e29714 | Tổng hợp trust/risk/security/e-WOM; không phải causal proof cho từng câu hỏi A+. |
| S9 | **Verified; tiêu đề trong báo cáo nền bị rút gọn.** Raffaele Filieri, Charles F. Hofacker & Salma Alguezaui (2018), “What makes information in online consumer reviews diagnostic over time? The role of review relevancy, factuality, currency, source credibility and ranking score,” *Computers in Human Behavior*, 80, 122–131. | https://doi.org/10.1016/j.chb.2017.10.039 | Hỗ trợ xem xét tính liên quan, cập nhật, factuality và nguồn của review; nghiên cứu tập trung review dịch vụ lưu trú, cần thận trọng khi áp sang hàng hóa. |
| S10 | **Verified.** Keda Qiu & Liyi Zhang (2024), “How online reviews affect purchase intention: A meta-analysis across contextual and cultural factors,” *Data and Information Management*, 8(2), Article 100058. | https://doi.org/10.1016/j.dim.2023.100058 | Meta-analysis về review và ý định mua, có moderator; không chứng minh review score là bằng chứng chất lượng sản phẩm. |
| S11 | **Verified.** Muhammad Aljukhadar, Valerie Trifts & Sylvain Sénécal (2017), “Consumer self-construal and trust as determinants of the reactance to a recommender advice,” *Psychology & Marketing*, 34(7), 708–719. | https://doi.org/10.1002/mar.21017 | Nghiên cứu hai study về trust/self-construal và reactance với recommender advice; không suy đoán đặc điểm tâm lý cá nhân của khách A+. |
| S12 | **Verified.** Tobias Reynolds-Tylus (2019), “Psychological Reactance and Persuasive Health Communication: A Review of the Literature,” *Frontiers in Communication*, 4, Article 56. | https://doi.org/10.3389/fcomm.2019.00056 | Review reactance trong truyền thông sức khỏe; dùng như nguyên tắc thận trọng với freedom threat, không chuyển nguyên xi thành kết luận hành vi mua hàng. |
| S13 | **Verified; cơ quan/loại nguồn cần ghi đúng.** U.S. Federal Trade Commission, “FTC’s Endorsement Guides: What People Are Asking,” mục “What About Affiliate or Network Marketing?” — staff guidance. | https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking | Hỗ trợ disclosure affiliate rõ ràng/gần endorsement theo hướng dẫn Hoa Kỳ; không phải journal paper và không thay tư vấn pháp lý tại Việt Nam. |
| S14 | **Verified.** Liv Ziegfeld, Daan Di Scala & Anita H.M. Cremers (2025), “The effect of preference elicitation methods on the user experience in conversational recommender systems,” *Computer Speech & Language*, 89, Article 101696. | https://doi.org/10.1016/j.csl.2024.101696 | Hỗ trợ đánh giá UX cùng hiệu quả recommendation và phương pháp elicitation; online DOI mang năm 2024, volume publication 2025. |

### 10.2. Những sửa đổi thư mục cần ghi nhận

- S1: thêm trang 60–72 và DOI chính thức.
- S2: chuẩn hóa tên tác giả theo nguồn xuất bản là Susana Santos và Helena Martins Gonçalves (không dùng “Martins Gonçalves” như một họ ghép duy nhất trong trường tác giả).
- S7: năm issue là 2019 nhưng bài online 2017; DOI chứa 2017 là hợp lệ.
- S9: thêm phần subtitle đầy đủ; ghi rõ bối cảnh mẫu nghiên cứu không phải tất cả ngành hàng.
- S10: dùng Article 100058 thay vì coi đó là page range.
- S12: ghi Tobias Reynolds-Tylus, Frontiers in Communication 4:56; nguồn thuộc truyền thông sức khỏe.
- S13: phân loại là hướng dẫn FTC Hoa Kỳ, không phải nghiên cứu học thuật.
- S14: DOI suffix chứa 2024 nhưng journal volume 89 phát hành 2025; không coi đây là lỗi năm.

**Tổng kết audit:** 14/14 mục có thể xác minh được thông tin thư mục trọng yếu qua trang nhà xuất bản/nguồn chính thức hoặc cơ sở học thuật đáng tin cậy. Không phát hiện mục nào cần loại hoàn toàn chỉ vì không tồn tại. Tuy nhiên, S5/S6 đang dùng trang tác giả/nhà nghiên cứu làm URL truy cập chính thức thay DOI; không tự dựng DOI. S13 là staff guidance. S9 và S12 có giới hạn bối cảnh cần ghi kèm. Việc xác minh metadata không có nghĩa đã đọc/đánh giá toàn văn từng nghiên cứu.

## 11. Mapping claim → source và giới hạn diễn giải

| Nhận định dùng trong báo cáo nền | Nguồn phù hợp | Cách diễn đạt được phép | Không được suy rộng |
|---|---|---|---|
| Nối thuộc tính với kết quả/giá trị | S1 | Dùng laddering như phương pháp khám phá | Không gán value/động cơ khi khách chưa xác nhận |
| Journey có nhiều nền tảng lý thuyết | S2 | Dùng như tổng quan để thiết kế trạng thái linh hoạt | Không tuyên bố sáu trạng thái A+ là model đã validate |
| Choice overload phụ thuộc điều kiện | S3, S4 | Thu hẹp lựa chọn khi có tín hiệu quá tải/khó quyết định | Không mặc định càng ít lựa chọn càng tốt |
| Hỏi theo use case có thể dễ với người mới | S5, S6 | Ưu tiên câu hỏi theo tác vụ; chọn câu hỏi có giá trị | Không cam kết hai câu đủ hoặc hiệu quả ở mọi category |
| Perceived risk liên quan purchase intention | S7, S8 | Làm rõ loại rủi ro và bằng chứng cần | Không dự báo hành vi cá nhân/nhân khẩu |
| Review diagnosticity phụ thuộc nội dung và thời điểm | S9, S10 | Kiểm tra relevance, factuality, currency, source, context | Không dùng số sao/số review làm xác nhận kỹ thuật |
| Recommendation có thể gây reactance | S11, S12 | Tránh đe dọa quyền tự chủ/áp lực; cho phép từ chối | Không gán trait reactance cho người dùng |
| Disclosure affiliate | S13 | Disclosure rõ, gần recommendation/link; kiểm tra luật thị trường mục tiêu | Không coi FTC là luật Việt Nam |
| Phương pháp elicitation ảnh hưởng UX | S14 | Đo cả hiệu quả và trải nghiệm chủ quan | Không tuyên bố một format hỏi tối ưu cho A+ khi chưa test |

## 12. Research / QA protocol khi chạy pilot

Mỗi session cần ghi tối thiểu:
- test ID, category, phiên bản flow và fixture sản phẩm;
- transcript đã loại thông tin nhận dạng;
- câu hỏi đã hỏi và lý do chọn;
- câu hỏi đã bỏ qua và lý do;
- state trước/sau, field được cập nhật và provenance;
- hard constraint, unknown, inference, evidence blocker;
- kết quả: ready-to-compare / needs-verification / no-match / deferred;
- điểm rubric, lỗi nghiêm trọng, reviewer và ngày chạy.

Không thu thập dữ liệu nhạy cảm không cần thiết. Không gán nhãn tính cách, sức khỏe, thu nhập hoặc nhóm nhân khẩu từ câu trả lời. Không dùng click/conversion làm chỉ số duy nhất của chất lượng quyết định.

## 13. Quyết định và review cần thiết

- **A Long:** xác nhận taxonomy/capability labels, các trường kỹ thuật cần Product Expert xác minh, đặc biệt host/port/refresh cho monitor; fit/codec/mic/latency cho headphone.
- **Hoàng:** nếu nhận triển khai sau này, phản hồi về khả năng biểu diễn field provenance, state, branch và stop code; tài liệu này chưa yêu cầu code.
- **CEO:** nghiệm thu luồng và chốt category/use case pilot; không có khuyến nghị chọn ngành MVP trong tài liệu này.

## 14. Nguồn chính

1. S1 — https://doi.org/10.1177/002224298204600207
2. S2 — https://doi.org/10.1016/j.techfore.2021.121117
3. S3 — https://doi.org/10.1016/j.jcps.2014.08.002
4. S4 — https://doi.org/10.1086/651235
5. S5 — https://research.google/pubs/soliciting-user-preferences-in-conversational-recommender-systems-via-usage-related-questions/
6. S6 — https://research.google/pubs/towards-conversational-recommender-systems/
7. S7 — https://doi.org/10.1080/08874417.2017.1300514
8. S8 — https://doi.org/10.1016/j.heliyon.2024.e29714
9. S9 — https://doi.org/10.1016/j.chb.2017.10.039
10. S10 — https://doi.org/10.1016/j.dim.2023.100058
11. S11 — https://doi.org/10.1002/mar.21017
12. S12 — https://doi.org/10.3389/fcomm.2019.00056
13. S13 — https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking
14. S14 — https://doi.org/10.1016/j.csl.2024.101696

**Giới hạn:** Tài liệu nguồn được xác minh bằng metadata/abstract và trang chính thức trong lượt audit; không tuyên bố systematic review hoặc đọc toàn văn mọi bài. Luồng hỏi, pass threshold, số câu mở đầu và test fixture là thiết kế A+ chưa được xác nhận thực nghiệm.