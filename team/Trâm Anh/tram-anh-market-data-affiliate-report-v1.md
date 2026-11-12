# TRÂM ANH — MARKET DATA & AFFILIATE REPORT v1

**Dự án:** A+ — website tư vấn, so sánh và hỗ trợ quyết định mua hàng  
**Phạm vi:** Việt Nam · Màn hình máy tính · Thiết bị âm thanh · Máy lọc không khí · Laptop  
**Ngày kiểm tra nguồn:** 12/11/2026  
**Mốc bàn giao theo brief:** 16/11/2026  
**Phiên bản:** v1.0 — nghiên cứu nguồn công khai  
**Trạng thái:** Đã hoàn tất desk research bước đầu; chưa đăng ký tài khoản, chưa kiểm thử API có xác thực, chưa lấy báo giá/điều khoản riêng từ network.

> **Lưu ý phương pháp:** Báo cáo này không đưa ra quyết định chọn ngành hàng MVP. Các số liệu trên sàn là ước tính từ nguồn phân tích bên thứ ba và taxonomy/từ khóa khác nhau; không được cộng hoặc so sánh trực tiếp như cùng một mẫu thị trường. Những thông tin không có tài liệu công khai được ghi “chưa xác minh”, không tự điền bằng suy đoán.

## 1. Tóm tắt kết quả nghiên cứu

### 1.1. Tín hiệu thị trường chung

- Báo cáo thị trường nội địa 2025 của Cục Quản lý và Phát triển thị trường trong nước, Bộ Công Thương, trích dẫn PwC Voice of the Consumer Survey 2024 với 515 người trả lời tại Việt Nam: **67% người được khảo sát có mua sắm trực tuyến**. Cùng báo cáo ước tính tổng giao dịch TMĐT trong nước năm 2025 khoảng **830 nghìn tỷ đồng (~32 tỷ USD)**, trong đó bốn sàn lớn khoảng **455 nghìn tỷ đồng**. Đây là bối cảnh kênh bán, không phải quy mô riêng của bốn ngành A+. [S1]
- Báo cáo YouNet ECI H1/2026 ghi nhận nhóm **Điện gia dụng & Điện tử tăng 26% so với H1/2025** trên các sàn; Shopee chiếm 67,3% và TikTok Shop 28,2% thị phần nhóm này theo phạm vi báo cáo. Điều này củng cố tín hiệu mua online cho thiết bị điện tử/gia dụng, nhưng không chứng minh từng SKU hoặc ngách có lợi nhuận affiliate. [S2]
- Không có bộ dữ liệu Google Trends đã xuất và chuẩn hóa cho bốn ngành trong lần kiểm tra này. Do đó báo cáo **không tuyên bố volume từ khóa, CAGR tìm kiếm hoặc thứ hạng nhu cầu Google**. Link khám phá so sánh các cụm từ và hướng dẫn xuất dữ liệu được đưa vào phần 5. [S27]

### 1.2. Một số tín hiệu theo ngành hàng

| Ngành hàng | Tín hiệu từ Metric, dữ liệu sàn năm 2025 | Cách hiểu đúng / giới hạn | Nhận định sơ bộ |
|---|---:|---|---|
| Laptop | **6.631,8 tỷ đồng** cho taxonomy rộng “Máy tính, Laptop & Thiết bị văn phòng”; 27 triệu sản phẩm bán ra; 32.806 shop có bán. Một truy vấn hẹp “laptop, windows 11” ghi nhận 61,3 tỷ đồng và 4 nghìn sản phẩm. [S6][S7] | Số 6.631,8 tỷ bao gồm máy tính, phụ kiện và thiết bị văn phòng; không phải doanh thu laptop. Truy vấn laptop Windows 11 quá hẹp để đại diện toàn ngành. | Tín hiệu cầu lớn trong ngành máy tính rộng; sản phẩm giá trị cao và nhiều tiêu chí so sánh, nhưng rủi ro sai model/biến thể cao. |
| Thiết bị âm thanh — tai nghe | **3.308,7 tỷ đồng**, 17 triệu sản phẩm bán ra, 13.051 shop; TikTok chiếm 49,8% và Shopee 47,1% doanh số trong taxonomy “tai phone, tai nghe”. [S5] | Bao gồm nhiều loại tai nghe và phân khúc giá, không chỉ tai nghe ANC cao cấp hoặc audio chuyên dụng. Metric nêu dải giá bán phổ biến 200.000–500.000 đồng. | Tín hiệu giao dịch rất rõ; cạnh tranh đông, giá phân khúc thấp tạo áp lực khác biệt hóa. Cần chia nhỏ ngách để kiểm tra AOV và chất lượng đơn. |
| Máy lọc không khí | **798,7 tỷ đồng**, 316 nghìn sản phẩm bán ra, 1.382 shop; Shopee 80,3%, TikTok 16,9%; dải giá được nêu có doanh số cao nhất là 2–5 triệu đồng. [S4] | Dataset dùng từ khóa bắt buộc “máy, lọc không khí”; Metric cũng có báo cáo từ khóa “lọc không khí” và “air purifier” với số khác đáng kể. Không trộn các dataset này. | Có quy mô sàn đáng kể và vấn đề mua có thể tư vấn rõ (diện tích, CADR, độ ồn, chi phí lọc thay thế). Nhu cầu có thể chịu ảnh hưởng mùa/chất lượng không khí. |
| Màn hình máy tính | **73,9 tỷ đồng**, 36 nghìn sản phẩm, 241 shop; Shopee 83,6%, TikTok 14,1%; dải giá được Metric nêu là 2–5 triệu đồng. Ngách màn hình PC gaming ghi nhận 19,6 tỷ đồng. [S3][S8] | Phạm vi là keyword “màn hình monitor”; không bao gồm toàn bộ doanh số màn hình bán qua chuỗi bán lẻ, website hãng hoặc offline. | Quy mô sàn nhỏ hơn ba ngách trên trong dữ liệu hiện có; bù lại thông số tương đối chuẩn hóa và có thể giải quyết câu hỏi chọn theo công việc/game/đồ họa. |

**Cảnh báo so sánh:** Đây là các báo cáo riêng do Metric phân loại theo taxonomy và bộ từ khóa khác nhau. Số Laptop là taxonomy rất rộng, còn Tai nghe, Máy lọc không khí và Màn hình là từ khóa/nhóm sản phẩm hẹp hơn. Không nên xếp hạng quy mô tuyệt đối bốn ngành chỉ bằng các số này. Metric có nhiều báo cáo liên quan theo từ khóa hẹp; việc thay từ khóa làm thay đổi đáng kể kết quả máy lọc không khí. [S3]–[S8]

### 1.3. Kết quả về dữ liệu và affiliate

1. **Nguồn dữ liệu nền tốt nhất về độ đúng model/thông số:** website chính hãng. Ví dụ Xiaomi công bố mã model cụ thể cho màn hình A27i và máy lọc không khí AC-M18-SC; Sony công bố thông số WH-1000XM6. Đây là nguồn tham chiếu chuẩn cho catalog, nhưng không tự cung cấp giá bán/tồn kho đa nhà bán. [S9][S10][S11]
2. **Nguồn giá, SKU bán lẻ và tín hiệu sẵn hàng:** website nhà bán lẻ và sàn. Trang laptop của Thế Giới Di Động hiện liệt kê model kèm mã cấu hình như HP C3RU7AT, ASUS LY146W, Dell DC5R5973W1-2Y, thông số RAM/SSD và giá. Dữ liệu thực dụng nhưng biến động, có thể khác nhau theo chương trình, cửa hàng và cấu hình. [S12]
3. **Nguồn dữ liệu có API/feed rõ nhất tìm được:** ACCESSTRADE công khai tài liệu Publisher API với campaign, tracking link, giao dịch, thông tin sản phẩm và datafeed; tài liệu tích hợp TikTok Shop mô tả feed có product ID, tên, shop, ảnh, dải giá, inventory flag, commission và units sold. API cần token Publisher; lần kiểm tra này chưa đăng nhập hay chạy thử API. [S13][S14]
4. **Affiliate:** Shopee, Lazada, ACCESSTRADE và MasOffer đều có dấu hiệu chương trình/đăng ký Publisher công khai. Tuy nhiên, hoa hồng thiết bị điện tử cụ thể và quyền dùng feed đầy đủ không thể xác nhận chỉ từ trang công khai; phải kiểm tra trong dashboard hoặc bằng văn bản sau khi được CEO duyệt. [S15]–[S20]
5. **Không nên lấy tỷ lệ hoa hồng làm tiêu chí chọn SKU.** Cần tách `fit_score` sản phẩm khỏi `commission_rate`, và chỉ dùng commission làm thông tin kinh tế thứ cấp sau khi sản phẩm vượt tiêu chí phù hợp.

## 2. So sánh 4 ngành hàng

### 2.1. Bảng so sánh định tính

Thang đánh giá dưới đây là **đánh giá vận hành sơ bộ**, không phải market share hay dự báo doanh thu. “Cao” ở cột rủi ro nghĩa là khó kiểm soát hơn.

| Tiêu chí | Màn hình | Âm thanh | Máy lọc không khí | Laptop |
|---|---|---|---|---|
| Tín hiệu cầu từ sàn 2025 | Trung bình theo dữ liệu quan sát; 73,9 tỷ đồng | Cao; tai nghe 3.308,7 tỷ đồng | Khá cao; máy lọc không khí 798,7 tỷ đồng | Cao trong nhóm máy tính rộng; chưa có số laptop toàn ngành cùng chuẩn |
| Độ đông cạnh tranh | Cao: hãng, retailer, marketplace, site so sánh giá, reviewer | Rất cao: hãng, shop audio, reviewer, KOL/KOC, marketplace | Cao nhưng chuyên môn sản phẩm và chi phí thay lõi tạo chỗ cho nội dung sâu | Rất cao: retailer lớn, diễn đàn, báo công nghệ, reviewer, site cấu hình/so sánh |
| Khả năng lấy thông số chính thức | Cao | Khá–cao; nhiều tính năng khó quy về một thang | Cao về thông số hãng; cần kiểm chứng cách đo | Cao nhưng cấu hình/SKU biến thể phức tạp |
| Độ tin cậy khi ghép đúng model | Khá–cao sau chuẩn hóa model code | Trung bình–khá; tên dòng và phiên bản gần giống nhau | Khá–cao nếu giữ mã máy và mã lõi lọc | Trung bình; nguy cơ ghép nhầm SKU cao nhất |
| Khả năng tự động hóa catalog | Khá–cao với feed được cấp phép; retailer feed chưa xác minh | Khá; feed marketplace hữu ích nhưng thiếu chất lượng âm thanh/lab test | Khá; có thể tự động hóa thông số và giá, nhưng filter consumables cần mapping riêng | Trung bình; cần xử lý cấu hình, hậu tố model, RAM/SSD/GPU/Màn hình |
| Khả năng tư vấn tạo khác biệt | Cao: panel/size/resolution/refresh/ergonomics theo use-case | Cao: comfort/ANC/mic/codec/latency/tuning theo người dùng | Cao: CADR/diện tích/độ ồn/lõi lọc/chi phí sở hữu | Rất cao: workload, pin, màn hình, GPU, nhiệt, nâng cấp, tương thích phần mềm |
| Rủi ro vận hành | Trung bình | Cao về tính chủ quan và đánh giá chất âm | Trung bình–cao do tuyên bố sức khỏe/diện tích lọc và chi phí filter | Cao nhất về nhầm cấu hình, giá trị đơn hàng lớn, hàng xách tay/khác bảo hành |
| Cơ hội affiliate cần xác minh | Giá trị đơn hàng có thể tốt; tỷ lệ commission chưa xác minh | Nhiều SKU và nhu cầu; AOV ngành rất phân tán | Giá máy và vật tư thay thế tạo hai loại chuyển đổi; network coverage chưa xác minh | Giá trị đơn hàng cao; tracking, điều kiện campaign và tỷ lệ huỷ/hoàn cần xác minh |

### 2.2. Màn hình máy tính

**Nhóm nhu cầu có thể kiểm tra:** văn phòng đa cửa sổ; học tập/làm việc tại nhà; gaming cạnh tranh (tần số quét/độ trễ); đồ họa/ảnh/video (độ phủ màu và độ chính xác); console; màn hình di động. Đây là phân nhóm nhu cầu để nghiên cứu tiếp, chưa phải kết quả khảo sát định lượng.

**Vấn đề khi mua:** kích thước và khoảng cách ngồi; FHD/QHD/4K; IPS/VA/OLED; 60/100/144/240 Hz; độ sáng và HDR thực; sRGB/DCI-P3/Delta E; cổng USB-C/DP/HDMI; chân đế công thái học; bảo hành điểm chết/panel. Thông số “response time” của hãng có thể không so sánh tương đương nếu điều kiện đo khác nhau.

**Tín hiệu cụ thể:** Metric ghi nhận màn hình monitor 73,9 tỷ đồng, 36 nghìn đơn vị, 241 shop trong 2025; riêng màn hình PC gaming 19,6 tỷ đồng và 8 nghìn sản phẩm. Dải giá bán có doanh số cao nhất của nhóm màn hình theo trang Metric là 2–5 triệu đồng. [S3][S8]

**Cạnh tranh:** Websosanh có trang so sánh giá nhiều mẫu màn hình Philips từ nhiều nơi bán; hãng như ASUS có bộ lọc danh mục theo độ phân giải, tần số quét, tấm nền và kích thước; Xiaomi công bố thông số model và có catalog màn hình theo dòng. [S9][S21][S22]

**Khoảng trống nội dung A+ có thể kiểm chứng:** không chỉ liệt kê “màn nào tốt”, mà lọc theo bàn làm việc/khoảng cách/loại tác vụ, sau đó giải thích trade-off: 27-inch FHD so với QHD; refresh rate so với màu; OLED so với IPS; USB-C dock so với giá; giá mua so với chân đế/arm cần mua thêm. Cần A Long duyệt tiêu chí kỹ thuật trước khi xuất bản.

### 2.3. Thiết bị âm thanh

**Cần tách ngành thành các catalog con:** tai nghe TWS; tai nghe chụp tai/ANC; gaming headset; tai nghe có dây; loa Bluetooth/portable; loa máy tính/desktop; audio hi-fi/monitoring. Không nên gom các loại này vào một bảng xếp hạng.

**Nhóm nhu cầu có thể kiểm tra:** gọi họp/đàm thoại; di chuyển và chống ồn; nghe nhạc/gu âm; gaming và voice chat; thể thao; học ngoại ngữ; làm nội dung/monitoring. Các tiêu chí gồm dạng đeo, codec, ANC, mic, độ trễ, pin, multipoint, tương thích, chống nước và chất âm.

**Tín hiệu cụ thể:** Metric ghi nhận tai nghe 3.308,7 tỷ đồng, 17 triệu sản phẩm bán ra, 63.805 sản phẩm có lượt bán và 13.051 shop trong 2025. Cơ cấu doanh số: TikTok 49,8%, Shopee 47,1%, Lazada 2,9%, Tiki 0,3%. Phân khúc 200.000–500.000 đồng là khoảng giá có doanh số cao nhất theo trang này. [S5]

**Cạnh tranh:** VnReview có bài đánh giá tai nghe Redmi và JBL; Tinhte có nội dung trên tay/review laptop và các thiết bị công nghệ; RTINGS công khai phương pháp test tai nghe theo âm thanh, thiết kế, isolation, microphone, active features và connectivity. RTINGS là chuẩn tham khảo phương pháp, không thể thay thế kiểm thử sản phẩm/giá có bán tại Việt Nam. [S23][S24][S25]

**Khoảng trống nội dung A+ có thể kiểm chứng:** bảng so sánh theo tình huống sử dụng (văn phòng ồn, gọi họp nhiều, đi xe/di chuyển, gaming, bass-heavy, nghe lâu) thay vì thứ hạng chung. Dữ liệu của hãng không đủ cho chất âm, mic trong môi trường thật, độ thoải mái và ANC; cần dùng review thử nghiệm độc lập và gắn mức tin cậy rõ ràng. Không khẳng định “chất âm hay nhất” chỉ từ codec hoặc đáp tuyến do hãng công bố.

### 2.4. Máy lọc không khí

**Nhóm nhu cầu có thể kiểm tra:** phòng ngủ nhỏ; phòng khách; nhà có trẻ nhỏ/thú cưng; người nhạy với bụi/phấn hoa; phòng gần đường lớn; người cần thiết bị yên tĩnh khi ngủ; nhà cần chi phí thay filter dễ dự tính.

**Vấn đề khi mua:** CADR (bụi/khói/phấn hoa nếu tách), diện tích phòng và số lần thay không khí/giờ, độ ồn ở từng mức, loại lọc, mã lõi lọc thay thế, giá lõi, vòng đời lõi, cảm biến PM2.5, mức tiêu thụ điện, bảo hành và nguồn cung lõi. Diện tích quảng cáo tối đa không nên dùng thay cho phép tính theo CADR và ACH/ACPH.

**Tín hiệu cụ thể:** Metric ghi nhận truy vấn bắt buộc “máy, lọc không khí” đạt 798,7 tỷ đồng, 316 nghìn sản phẩm bán ra, 3.610 sản phẩm có lượt bán và 1.382 shop. Shopee chiếm 80,3% doanh số, TikTok 16,9%, Lazada 2,7%, Tiki 0,1%; dải giá có doanh số cao nhất là 2–5 triệu đồng. Metric ghi nhận doanh thu sáu tháng gần nhất giảm so với sáu tháng trước đó trong dataset này; không đủ dữ liệu công khai ở snippet để nêu phần trăm giảm. [S4]

**Độ nhạy từ khóa:** cùng một chủ đề, trang “air purifier” tiếng Anh hiển thị 169,4 tỷ đồng; trang “lọc không khí” hiển thị 831,4 tỷ đồng. Đây là dấu hiệu taxonomy/keyword có thể làm thay đổi mạnh kết quả; báo cáo chọn truy vấn tiếng Việt “máy lọc không khí” làm số tham khảo chính và không cộng các bản ghi. [S4][S26]

**Nhu cầu nền:** IQAir ghi nhận PM2.5 trung bình năm 2025 của Hà Nội là 45,9 µg/m³. Đây là chỉ báo môi trường cho Hà Nội, không chứng minh tất cả hộ gia đình cần máy lọc hoặc hiệu quả sức khỏe cụ thể của một SKU. Không sử dụng dữ liệu này để đưa ra tuyên bố y tế. [S27]

**Cạnh tranh:** Websosanh có trang so sánh giá máy lọc không khí Philips AC0850/20 với 86 nơi bán và AC1715/20 với 75 nơi bán ở thời điểm truy xuất; Xiaomi công bố CADR, khoảng diện tích hiệu quả và mã sản phẩm/lõi cho model. [S21][S28]

**Khoảng trống nội dung A+ có thể kiểm chứng:** tính chi phí sở hữu 1–3 năm: giá mua + lõi lọc dự kiến + tần suất thay lõi + điện; khớp CADR với diện tích/phòng; chỉ rõ khi nào thông số là công bố hãng, khi nào có test độc lập. Đây là cơ hội tư vấn hữu ích nhưng cần kiểm tra giá và tình trạng lõi lọc liên tục.

### 2.5. Laptop

**Nhóm nhu cầu có thể kiểm tra:** văn phòng/học tập; lập trình; data/AI; thiết kế 2D/3D; biên tập video; gaming; doanh nhân/di chuyển; máy pin lâu. Không dùng một điểm tổng duy nhất cho tất cả workload.

**Vấn đề khi mua:** CPU/GPU đúng phiên bản; giới hạn công suất và hiệu năng bền; RAM hàn/nâng cấp; dung lượng và khe SSD; loại panel/độ sáng/độ phủ màu/tần số quét; pin thực tế; trọng lượng và sạc; cổng; tản nhiệt/độ ồn; bảo hành; hệ điều hành và phần mềm kèm theo. Cùng tên dòng có thể có nhiều CPU, RAM, panel và hậu tố SKU khác nhau.

**Tín hiệu cụ thể:** Metric ghi nhận 6.631,8 tỷ đồng cho toàn ngành máy tính–laptop–thiết bị văn phòng (không chỉ laptop); 27 triệu sản phẩm bán ra và 32.806 shop. Dataset hẹp “laptop, windows 11” ghi nhận 61,3 tỷ đồng và 4 nghìn sản phẩm, nhưng không đại diện thị trường laptop nói chung. [S6][S7]

**Cạnh tranh:** Thế Giới Di Động hiển thị 432 laptop, bộ lọc theo thương hiệu/giá/use-case/kích thước và thông số cấu hình; Dân Trí, Tinhte, GenK, VnReview có bài đánh giá/tiêu chí mua theo use-case. Một repository công khai `laptop-report-vn` tự mô tả đang so sánh 3.364 laptop từ 13 nhà bán; cần kiểm tra trực tiếp chất lượng và độ cập nhật trước khi coi là đối thủ có quy mô đáng kể. [S12][S23][S24][S29][S30]

**Khoảng trống nội dung A+ có thể kiểm chứng:** gợi ý theo workload + giới hạn ngân sách + yêu cầu pin/di động + khả năng nâng cấp, giải thích đánh đổi CPU/GPU/RAM/panel và đối chiếu đúng SKU ở từng retailer. Đây có thể tạo giá trị ra quyết định rõ, nhưng cũng là catalog khó nhất để tự động ghép đúng phiên bản.

## 3. Nguồn dữ liệu sản phẩm và đánh giá chất lượng

### 3.1. Ma trận nguồn

| Nguồn | Có thể lấy tự động? | Cấu trúc / định danh | Giá & tồn kho | Độ tin cậy | Trạng thái / rủi ro |
|---|---|---|---|---|---|
| Website chính hãng (ASUS, Xiaomi, Sony, Philips, Sharp, Dell, Lenovo, HP, Apple…) | Chưa xác minh API/feed mở. Website có trang danh mục và PDP; khả năng đọc HTML không đồng nghĩa có quyền crawl/sử dụng lại. | Thường tốt: model, model code/part number, bảng specs; khác biệt về hậu tố quốc gia/region cần giữ lại. | Thường không có giá nhiều retailer; đôi khi có giá/đại lý. Tồn kho thường không phản ánh toàn hệ thống phân phối. | **Cao** cho thông số hãng công bố; trung bình cho claim marketing. | Đã xác minh sự hiện diện của các trang thông số cụ thể [S9][S10][S11][S28]. **Chưa xác minh** API công khai hoặc quyền tái sử dụng dữ liệu hàng loạt. |
| Nhà bán lẻ: Thế Giới Di Động, FPT Shop, CellphoneS, Phong Vũ, GearVN, An Phát, HACOM… | Dữ liệu PDP/catalog có thể đọc trên web; **API/feed công khai chưa xác minh**. | Có tên model, mã SKU, giá, cấu hình, một số tồn kho/chi nhánh. Mức chuẩn hóa khác nhau giữa nhà bán. | Giá/promo/tồn kho cập nhật động, nhưng thường theo cửa hàng, phương thức thanh toán và voucher. | **Trung bình–cao** cho offer tại thời điểm kiểm tra; cần hãng xác nhận specs. | Đã quan sát ví dụ Thế Giới Di Động công khai mã cấu hình và spec [S12]. Phong Vũ bị chặn 403 khi truy xuất tự động trong phiên kiểm tra; không suy ra rằng họ không có feed. |
| Sàn TMĐT: Shopee, TikTok Shop, Lazada, Tiki | Có thể tự động qua API/affiliate feed nếu được cấp quyền; truy xuất website công khai không bảo đảm được phép hoặc bền vững. | Product ID, variation/SKU, shop, ảnh, giá, review, sold count có thể có; dữ liệu tiêu đề/biến thể do seller nhập, cần kiểm chứng. | Giá và hàng thay đổi nhanh; có voucher theo user/giờ, stock theo variation và shop. | **Trung bình hoặc thấp** cho chuẩn model; tốt hơn cho chỉ báo thị trường tổng hợp. | Metric dùng dữ liệu sàn để ước tính GMV; ACCESSTRADE có feed TikTok Shop trong tài liệu API [S3]–[S8][S14]. |
| Price-comparison site: Websosanh | Có danh sách so sánh và liên kết nơi bán; **API/feed cấp cho A+ chưa xác minh**. | Có mẫu/model và nhiều offer, tuy nhiên cần kiểm tra việc gộp model/region/đời sản phẩm. | Có giá tham khảo/đếm nơi bán; phải mở nguồn retailer để xác minh giá còn hiệu lực. | **Trung bình** cho phát hiện nơi bán/giá tham khảo; không phải nguồn chuẩn thông số. | Đã kiểm tra trang mẫu Philips máy lọc và màn hình, nhiều nơi bán/model [S21]. |
| Review/testing độc lập: RTINGS, VnReview, Tinhte, GenK và báo công nghệ | Không mặc định có API/license. Nội dung bài review có thể được tìm kiếm và dẫn link; không sao chép test text/ảnh nếu chưa được phép. | Model thường rõ; phép đo/test có chiều sâu tùy site và sản phẩm họ đã test. | Không phải nguồn cập nhật giá/tồn kho đầy đủ tại Việt Nam. | **Cao** cho test cụ thể có phương pháp công bố; trung bình nếu là trải nghiệm ngắn/không có số đo. | RTINGS công khai quy trình test monitor/headphones; VnReview/Tinhte/GenK cho thấy cạnh tranh nội dung Việt [S23]–[S25]. |
| Metric / YouNet ECI (dữ liệu thị trường) | Dashboard/report; API xuất dữ liệu hoặc license bulk chưa xác minh. | Taxonomy, keyword, seller, SKU trends; phụ thuộc cách phân loại và lọc dữ liệu. | Không thay thế nguồn price/inventory theo từng nhà bán. | **Trung bình–cao** cho tín hiệu thị trường có phương pháp, nhưng cần mua/đọc full report để kiểm tra dữ liệu ẩn. | Metric public excerpts cho thấy nhiều chỉ tiêu bị ẩn/khác taxonomy. Không lấy làm dữ liệu catalog SKU trực tiếp. [S3]–[S8] |

### 3.2. Khuyến nghị chuẩn hóa catalog (đề xuất cho Hoàng và A Long thẩm định)

**Định danh canonical đề xuất:**

`brand + model_family + exact_model_code/part_number + market_region + configuration_signature`

Không gộp chỉ dựa trên tên dòng. Mỗi offer của retailer/sàn là một bản ghi riêng, trỏ về canonical product sau khi xác minh.

| Ngành | Trường tối thiểu cần lưu |
|---|---|
| Màn hình | Model code; kích thước; resolution; panel; refresh; brightness; contrast; color gamut/Delta E (kèm nguồn/phương pháp); HDR; response-time claim; ports; USB-C power; stand/ergonomics; warranty; ngày kiểm tra. |
| Âm thanh | Exact model/region; form factor; connection/codecs; ANC/transparency; microphone; battery; IP rating; multipoint; app support; compatibility; measured sound/isolation/voice test nếu có; warranty. |
| Máy lọc không khí | Exact model; particle CADR và test source; CADR other pollutants nếu có; diện tích hiệu quả + ACH/ACPH/method; noise by mode; filter code/type; retail filter price; filter life; PM sensor; energy; warranty. |
| Laptop | Exact SKU/part number; CPU exact SKU; GPU exact SKU/TGP; RAM size/type/soldered/slots; SSD capacity/slots; display panel/brightness/color/refresh; battery Wh; weight; ports; charger; OS/software; warranty and region. |

**Trường offer nên tách khỏi sản phẩm:** `merchant`, `seller_id`, `seller_type/official_store`, `offer_sku`, `price_list`, `price_sale`, `voucher_condition`, `stock_status`, `location/warehouse`, `shipping`, `warranty_provider`, `affiliate_network`, `tracking_link`, `last_checked_at`, `source_url`.

**Kiểm tra định kỳ đề xuất (chưa phải SLA của nhà cung cấp):** giá/stock 4–12 giờ hoặc theo feed; product specs theo thay đổi PDP hoặc kiểm tra hàng tuần; model mapping khi phát hiện title/SKU mới; kiểm tra ngẫu nhiên 20–50 SKU/ngành/tuần để phát hiện drift. Tần suất thực tế cần Hoàng xác nhận chi phí và API quota.

### 3.3. Các lỗi dữ liệu cần chặn trước khi xuất bản

- **Trùng model và sai SKU:** cùng dòng nhưng khác màn hình, GPU, RAM, panel, mã vùng hoặc bảo hành.
- **Giá không so sánh được:** giá sau voucher, giá thành viên, trade-in, trả góp, bundle quà và giá niêm yết bị trộn.
- **Tồn kho sai:** còn hàng trên PDP nhưng hết tại chi nhánh/variation; hàng đặt trước và hàng có sẵn bị gom chung.
- **Model giả/nhái hoặc listing sai taxonomy:** tên sản phẩm marketplace có thể chứa nhiều model/brand để kéo traffic.
- **Thông số hãng và phép đo độc lập bị gộp:** claim hãng (ví dụ diện tích phòng tối đa) không đồng nhất với CADR/ACH đo được.
- **Review không đại diện:** rating có thể gộp biến thể khác nhau hoặc bao gồm đánh giá shop/giao hàng.
- **Ảnh/nội dung có bản quyền:** không tải và tái xuất bản ảnh/spec narrative/review nguyên văn nếu chưa có license.
- **Crawl/API:** không coi HTML scrape là quyền sử dụng thương mại. Cần đọc Terms/robots/rate limits, xin phép hoặc dùng feed/API hợp lệ.

## 4. Chương trình affiliate và điều khoản

### 4.1. Bảng so sánh

| Đơn vị / mạng | Ngành hàng có thể liên quan | Hoa hồng công khai | Cookie / attribution | API / feed | Điều kiện, thanh toán và hạn chế |
|---|---|---|---|---|---|
| **Shopee Affiliate** | Sàn có ngành laptop, màn hình, âm thanh, thiết bị gia dụng; cần kiểm tra availability theo SKU/campaign. | **Không xác minh được tỷ lệ cố định công khai** cho bốn ngành. Cần xem mức theo sản phẩm/campaign trong hệ thống. | Điều khoản cập nhật 08/07/2026 nêu **cookie 7 ngày** cho app và website. [S15] | Không tìm thấy tài liệu public xác nhận product feed/API dành cho Publisher ngoài link tạo trong hệ thống; chưa xác minh. | Có nhiều hình thức KOL/KOC, doanh nghiệp, Seller Affiliate, Short-tail; điều kiện khác nhau. KOL yêu cầu ít nhất 5.000 follower TikTok/YouTube hoặc 10.000 Facebook/Instagram; KOC có tiêu chí riêng. Có giới hạn quảng cáo, cấm cookie dropping/auto redirect; nghĩa vụ hồ sơ thuế/thanh toán. [S15] |
| **Lazada Affiliate** | Danh mục public có Laptop, Audio, Monitors, Small Appliances; máy lọc không khí cần kiểm tra campaign/SKU thực tế. [S16] | Không xác minh được tỷ lệ theo category ở trang public; cần dashboard/campaign sheet. | Điều khoản public mô tả **last-click**; thời lượng cookie hiện không xác minh được ở trang được truy xuất. Điều khoản được hiển thị ngày cập nhật 30/09/2020 nên cần xác nhận phiên bản hiện hành. [S17] | Không tìm thấy tài liệu public xác nhận feed/API dành cho affiliate Publisher; cần hỏi affiliate team trực tiếp. Không suy diễn từ API khác của Lazada sang quyền dùng affiliate feed. | Trang hỗ trợ nói hồ sơ được duyệt trong khoảng 5 ngày làm việc; hoa hồng tháng T được chốt đầu T+1; ngưỡng thanh toán tối thiểu 500.000 đồng; chuyển khoản trong vòng 45 ngày kể từ khi Lazada xuất hóa đơn. [S16] |
| **ACCESSTRADE Publisher** | Phụ thuộc các campaign advertiser; cần vào dashboard để xác nhận FPT Shop, CellphoneS, GearVN, Điện Máy Xanh hoặc nhà bán cụ thể còn chạy hay không. | Không có một mức chung; theo campaign/offer. **Chưa xác minh tỷ lệ cho SKU của bốn ngành.** | Cookie tùy từng campaign và ghi trong dashboard; trung tâm trợ giúp nói cơ chế cookie không ghi đè áp dụng cho hầu hết campaign, nhưng cần kiểm tra campaign cụ thể. [S19] | **Có tài liệu API Publisher**: campaigns, tracking link, transactions, order/product details, datafeeds, vouchers/deals. TikTok Shop API có tìm kiếm feed và tạo affiliate link. Token Publisher cần được cấp. [S13][S14] | Đăng ký Publisher, khai báo kênh, được duyệt campaign rồi tạo link. Việc dùng API cần credential/quyền tương ứng. Commission và cookie khác nhau theo campaign. [S20] |
| **MasOffer** | Mạng affiliate Việt Nam; có công cụ tạo link theo sản phẩm/danh mục và tài liệu publisher. Campaign điện tử cụ thể chưa xác minh. | Không xác minh được mức công khai cho bốn ngành. | FAQ nêu cơ chế **last-click**; số ngày cookie không xác minh được. [S21] | Có portal Publisher API; tài liệu endpoint không đọc được trong lần truy xuất, nên field schema/feed status chưa xác minh. [S18] | FAQ nêu đơn được ghi nhận sau khi thanh toán và kết thúc thời gian hoàn trả (nếu có); thanh toán từ ngày 20–25 hàng tháng. [S21] |
| **TikTok Shop Affiliate Creator** | Nhiều product category trên TikTok Shop; commission tùy seller/SKU. Nhưng chương trình creator trong app không đồng nghĩa với affiliate website publisher. | Commission per product/seller. Công thức trên tài liệu: (Revenue − Refunds) × commission rate; tỷ lệ khác theo sản phẩm, không có mức chuẩn cho ngành. [S22] | Không xác minh được cookie dành cho website từ tài liệu creator; commission chỉ được ghi nhận cho đơn đủ điều kiện theo TikTok Shop. | Publisher API feed TikTok Shop có thể truy cập thông qua ACCESSTRADE; không nên nhầm với quyền API trực tiếp từ TikTok dành cho website A+. [S14] | Tài liệu Creator cập nhật 22/07/2026 yêu cầu ít nhất 1.000 follower, 18 tuổi, xác minh danh tính; cần CCCD với creator Việt. Quy tắc commission cập nhật 30/01/2026: commission ước tính biến động theo coupon/giá thực trả; payout phụ thuộc kỳ settle seller; có thể mất commission khi đơn bị huỷ/hoàn. [S22][S23] |

### 4.2. Các điều khoản đáng lưu ý

**Shopee**

- Điều khoản có phiên bản cập nhật 08/07/2026; cookie 7 ngày được nêu rõ. “Đơn hàng thành công” trong định nghĩa có mốc 30 ngày từ khi đưa khách vào sàn, nhưng đây không thay thế thời lượng cookie 7 ngày; cần phân biệt hai định nghĩa. [S15]
- Điều khoản phân loại nhiều mô hình KOL/KOC/doanh nghiệp/MCN/Seller Affiliate/Short-tail. A+ là website so sánh, cần hỏi đúng loại hình đăng ký được chấp thuận; không tự giả định website độc lập được tham gia như creator cá nhân. [S15]
- Không được sử dụng cookie stuffing, pop-under/auto redirect hoặc quảng cáo gây nhầm lẫn. Việc sử dụng tên/logo/tài liệu Shopee và quảng bá qua kênh/phương tiện cần tuân thủ yêu cầu phê duyệt trong điều khoản. [S15]
- Thuế, chứng từ thanh toán và quyền giữ/đối soát commission có điều khoản riêng; CEO cần duyệt chủ thể nhận thu nhập trước khi ký/đăng ký. [S15]

**Lazada**

- Hỗ trợ public nêu registration, reporting, payment threshold và thời hạn thanh toán; không công bố đầy đủ commission theo category hoặc cookie length trên trang FAQ được kiểm tra. [S16]
- Affiliate Terms được page hiển thị cập nhật 30/09/2020; tài liệu mô tả last-click, nhưng do phiên bản cũ nên không dùng làm căn cứ vận hành trước khi Lazada xác nhận điều khoản hiện hành. [S17]
- API Open Platform không được đánh đồng với quyền truy cập product affiliate feeds. Cần hỏi affiliate team về feed, field, quyền lưu cache, ảnh, refresh policy, attribution app/web và giới hạn deep link.

**ACCESSTRADE**

- Có bộ tài liệu Publisher API công khai; mục lục gồm API lấy campaign, tracking links, transactions, orders, products, datafeeds, vouchers và tích hợp TikTok Shop. [S13]
- API TikTok Shop v2 mô tả các trường: product ID/title/shop, ảnh, trạng thái có hàng, dải giá gốc/giá sale, commission và units sold. `units_sold` có thể không xuất hiện nếu creator chưa cho phép chia sẻ dữ liệu chính xác. Vì vậy không nên giả định mọi sản phẩm đều có đầy đủ dữ liệu bán. [S14]
- Tài liệu API xác nhận có trường commission theo từng product feed; giá trị trả về cần xem tại campaign/SKU thực tế và **không phải commission được cam kết** cho A+ nếu chưa có token và quyền truy cập. [S14]
- Cookie là theo từng campaign; yêu cầu dashboard kiểm tra trước khi tính dự báo doanh thu. [S19]

**MasOffer**

- FAQ xác nhận last-click và chu kỳ thanh toán ngày 20–25 hàng tháng; điều kiện ghi nhận order có phụ thuộc hoàn tất thanh toán và thời gian trả hàng. [S21]
- Portal Publisher API tồn tại nhưng phần docs không hiển thị nội dung được máy đọc trong lần kiểm tra. Chưa xác minh schema, feed, cadence, field tồn kho hoặc quyền tải dữ liệu hàng loạt. [S18]

**TikTok Shop**

- Chương trình creator yêu cầu xác minh danh tính/độ tuổi; điều kiện follower tối thiểu 1.000 trong tài liệu apply creator. Đây không phải bằng chứng A+ website thuần đủ điều kiện creator affiliate trực tiếp. [S22]
- Commission tính trên doanh thu thực tế sau coupon/refund; payout phụ thuộc settlement của shop. Một số đơn huỷ/hoàn không có commission. [S23]
- Hướng khả thi cho A+ website là **kiểm tra campaign TikTok Shop qua network có API Publisher** (ví dụ ACCESSTRADE), không mặc định vận hành theo mô hình creator video/showcase. [S14]

### 4.3. Thông tin affiliate còn thiếu bắt buộc phải hỏi trước khi triển khai

1. Có thể đăng ký dưới pháp nhân/website A+ chưa có traffic lớn không? Có yêu cầu domain, nội dung mẫu, traffic source hoặc mức traffic tối thiểu không?
2. Có advertiser nào đang hoạt động cho laptop, màn hình, tai nghe/loa và máy lọc không khí? Gửi campaign ID, landing domain, category eligibility và danh sách SKU.
3. Commission cơ bản/bonus theo brand/category/SKU là bao nhiêu? Base commission tính trên giá trước hay sau voucher, phí vận chuyển, thuế?
4. Cookie window, last-click/first-click, cross-device, in-app attribution, app-deeplink và thời gian pending/approval/lock là gì?
5. API/feed cung cấp product ID, model code, SKU variant, price, sale price, stock, image, affiliate URL, commission, updated_at và returns/cancellations không?
6. Tần suất cập nhật, rate limit, pagination, SLA, quyền cache/hiển thị giá và ảnh, thời gian giữ dữ liệu, điều khoản khi campaign dừng?
7. Quy định traffic Google SEO, email, paid search, social, coupon, comparison site và sub-ID tracking có cho phép không?
8. Quy trình xuất hóa đơn, khấu trừ thuế, threshold, kỳ thanh toán và chứng từ cho doanh nghiệp/cá nhân kinh doanh?

## 5. Rủi ro, dữ liệu còn thiếu và thông tin chưa xác minh

### 5.1. Rủi ro thị trường và nghiên cứu

- **Search demand chưa đo:** Google Trends chưa xuất file so sánh 5 năm cho bộ keyword tiếng Việt/tiếng Anh và không có Google Ads Keyword Planner/search-volume report. Không đưa con số search volume vào quyết định MVP. [S27]
- **Metric taxonomy chưa đồng nhất:** số ngành Laptop bao gồm phụ kiện/thiết bị văn phòng; số tai nghe có nhiều mặt hàng giá thấp; số máy lọc khí biến động theo keyword. Cần mua/được cấp full report và định nghĩa taxonomy trước khi so sánh trực tiếp. [S3]–[S8]
- **Competitor/SERP audit chưa định lượng:** đã xác định ví dụ Websosanh, VnReview, Tinhte, GenK và retailer content, nhưng chưa crawl/đo SERP theo 50–100 truy vấn cho 4 ngành, chưa kiểm tra traffic/ranking/backlink hoặc YouTube views ở cùng thời điểm. [S21][S23][S24][S25]
- **Không có số liệu conversion/commission thực:** chưa có publisher account, dashboard, lịch sử click-to-order và return/cancel rates. Doanh thu affiliate không thể suy ra trực tiếp từ GMV sàn hoặc mức hoa hồng niêm yết.
- **Mùa vụ:** máy lọc không khí có thể nhạy với mùa ô nhiễm; laptop và màn hình chịu tác động mùa tựu trường, gaming releases và sales campaigns; audio có thể lệch mạnh sang social commerce. Cần chuỗi theo tháng 24 tháng trước kết luận về xu hướng.

### 5.2. Rủi ro kỹ thuật và dữ liệu

- Chưa có API/feed chính thức được cấp quyền từ retailer hoặc Shopee/Lazada; ACCESSTRADE API mới xác minh tài liệu, chưa kiểm thử endpoint qua token hợp lệ.
- API TikTok Shop feed được mô tả có `has_inventory`, commission, giá theo min/max SKU, title, product ID và shop, nhưng product title không thay thế exact model code; units_sold có thể vắng mặt. [S14]
- Chưa có kiểm tra tính đúng của stock, price, commission và deep link trên dữ liệu thực. Cần mẫu kiểm thử với tối thiểu 100 SKU/ngành trước khi coi là feed production-ready.
- Giá có thể khác giữa PDP, checkout, voucher cá nhân, flash sale và store/location; hiển thị giá phải ghi thời điểm xác minh và điều kiện khuyến mãi.
- Với laptop/audio/monitor, cần kiểm soát hàng xách tay, hàng cũ/refurbished và bảo hành khác thị trường. Với air purifier, cần mapping lõi lọc thay thế theo đúng model và đời.

### 5.3. Rủi ro pháp lý và quy định nền tảng

- Luật Thương mại điện tử số 122/2025/QH15 có hiệu lực từ 01/07/2026. Điều 25–26 quy định trách nhiệm của đơn vị cung cấp dịch vụ tiếp thị liên kết và affiliate trong TMĐT, gồm xác minh danh tính ở phía cung cấp dịch vụ, loại bỏ liên kết vi phạm và cung cấp thông tin hoạt động khi cơ quan quản lý yêu cầu. Phân loại vai trò A+ cần được tư vấn pháp lý; báo cáo này không kết luận A+ là affiliate service provider hay affiliate marketer theo luật trong mọi cấu trúc hợp đồng. [S31]
- Bộ Công Thương công bố Luật và Nghị định 248/2026/NĐ-CP cùng có hiệu lực từ 01/07/2026; hướng dẫn của Bộ nhấn mạnh minh bạch vai trò các bên, affiliate link/referral code, nội dung không gây hiểu lầm về công dụng, chất lượng, nguồn gốc, giá, bảo hành và sẵn hàng. [S32]
- Luật sửa đổi, bổ sung một số điều của Luật Quảng cáo số 75/2025/QH15 có hiệu lực từ 01/01/2026. Trước khi phát hành nội dung gắn link, cần rà soát nghĩa vụ nhận diện nội dung quảng cáo/tài trợ, trách nhiệm người chuyển tải và các văn bản hướng dẫn có hiệu lực tại thời điểm xuất bản. [S33]
- Khuyến nghị vận hành: hiện rõ ghi chú “A+ có thể nhận hoa hồng khi bạn mua qua liên kết; điều này không làm thay đổi tiêu chí đánh giá/đề xuất”; lưu lịch sử nguồn và ngày giá; cho phép người dùng mở nơi bán và chính sách bảo hành/đổi trả.

### 5.4. Dữ liệu chưa có / trạng thái

| Hạng mục | Hiện trạng | Trạng thái | Tin cậy |
|---|---|---|---|
| Google Trends 5 năm, 4 ngành, keyword Việt/Anh | Có link công cụ, chưa export dữ liệu định lượng | Chưa xác minh | Thấp |
| Google search SERP & YouTube competition audit | Có ví dụ đối thủ, chưa đo toàn bộ truy vấn | Chưa xác minh | Thấp–trung bình |
| Laptop-only TAM trên sàn | Chưa có taxonomy laptop rộng nhưng sạch | Chưa xác minh | Thấp |
| Commission/cookie chi tiết theo campaign điện tử của Shopee/Lazada/AT/MasOffer | Phải truy cập dashboard hoặc hỏi account manager | Chưa xác minh | Thấp |
| API/feed retailer (TGDD, FPT, CellphoneS, Phong Vũ, GearVN, HACOM) | Chưa có tài liệu quyền truy cập công khai | Chưa xác minh | Thấp |
| API/feed affiliate Shopee và Lazada cho publisher | Chưa có bằng chứng feed được cấp cho A+ | Chưa xác minh | Thấp |
| ACCESSTRADE product feed/API | Tài liệu công khai xác nhận chức năng; chưa test token | Đã xác minh tài liệu; chưa xác minh vận hành | Cao về tài liệu, thấp về runtime |
| TikTok Shop creator program | Tài liệu eligibility/commission được công bố | Đã xác minh | Cao |
| Mapping mã model, exact SKU, regional SKU trên 4 ngành | Có ví dụ trang hãng/retailer; chưa lập master catalog | Chưa xác minh | Trung bình |

## 6. Đề xuất hướng nghiên cứu tiếp theo (để CEO quyết định ưu tiên)

1. **Định lượng cầu:** xuất Google Trends Việt Nam 5 năm với nhóm từ khóa chính/phụ cho bốn ngành; thêm keyword intent như “nên mua”, “so sánh”, “cho phòng 20m2”, “gaming 144hz”, “tai nghe chống ồn họp”, “laptop lập trình”. So sánh theo vùng và mùa vụ, không chỉ tổng quốc gia.
2. **Kiểm tra nguồn catalog:** chọn 30–50 SKU tiêu biểu/ngành từ hãng và ít nhất 3 nhà bán; đo tỷ lệ khớp exact model code, coverage thông số quan trọng, giá/stock còn hiệu lực và số giờ cập nhật. Ghi riêng lỗi mapping và nguồn nào làm chuẩn.
3. **Kiểm thử feed affiliate:** sau phê duyệt của CEO, xin ACCESSTRADE sample API key/sandbox hoặc Publisher token; lấy mẫu TikTok Shop và danh sách campaign electronics, đo số lượng SKU phù hợp, độ đầy đủ model code, giá/stock, commission, link tracking. Song song gửi câu hỏi feed cho Shopee/Lazada/MasOffer.
4. **Đối chiếu với Vân Anh:** xác nhận top use-cases, ngôn ngữ người mua, mức giá sẵn sàng trả và các câu hỏi gây khó trong quyết định mua; không tự suy luận persona chỉ từ doanh số sàn.
5. **Đối chiếu với A Long:** xác thực tiêu chí/spec, chuẩn đo, sự khác biệt claim marketing và test độc lập; đặc biệt CADR/ACH cho máy lọc, panel/HDR/response cho màn hình, pin/mic/ANC cho audio và cấu hình/TGP/panel cho laptop.
6. **Đối chiếu với Hoàng:** xác nhận khả năng lấy feed hợp lệ, lịch cập nhật, chi phí API, dedupe/canonical mapping, job retry, rate limit, stock/price cache và audit trail.
7. **Gửi CEO bảng bằng chứng và trade-off:** không chốt ngành; trình bày data coverage, độ tin cậy, phạm vi campaign, rủi ro pháp lý, khả năng vận hành và mức công sức cần thiết cho từng ngành.

## Danh mục nguồn tham khảo

**Ngày kiểm tra các URL dưới đây: 12/11/2026**, trừ khi nêu rõ ngày công bố/cập nhật. “Đã xác minh” nghĩa là thông tin được nhìn thấy trong tài liệu/trang nguồn tại lần truy cập; không hàm ý đã kiểm chứng bằng giao dịch hoặc API runtime.

| ID | Nguồn / nội dung | URL | Ngày nguồn / kiểm tra | Độ tin cậy | Trạng thái |
|---|---|---|---|---|---|
| S1 | Cục Quản lý và Phát triển thị trường trong nước — Báo cáo thị trường nội địa 2025 (67% online; 830 nghìn tỷ đồng TMĐT; 455 nghìn tỷ đồng bốn sàn) | https://dms.gov.vn/documents/d/guest/bc-ttnd-2025-pdf | Báo cáo 2025; kiểm tra 12/11/2026 | Cao — cơ quan nhà nước, khảo sát PwC được trích dẫn | Đã xác minh |
| S2 | YouNet ECI — Báo cáo toàn cảnh TMĐT Việt Nam H1/2026 (HA & CE +26%; share Shopee/TikTok) | https://youneteci.com/vi/bao-cao-toan-canh-tmdt-viet-nam-nua-dau-nam-2026/ | H1/2026; kiểm tra 12/11/2026 | Trung bình–cao — đơn vị nghiên cứu có phương pháp riêng | Đã xác minh |
| S3 | Metric — Màn hình monitor (73,9 tỷ đồng; 36 nghìn sản phẩm; 241 shop; taxonomy/keyword) | https://metric.vn/ereport/man-hinh-monitor | Data 01–12/2025; trang cập nhật 2026; kiểm tra 12/11/2026 | Trung bình — vendor analytics; full data có phần ẩn | Đã xác minh excerpt |
| S4 | Metric — Máy lọc không khí (798,7 tỷ đồng; 316 nghìn sản phẩm; 1.382 shop) | https://metric.vn/ereport/may-loc-khong-khi | Data 01–12/2025; kiểm tra 12/11/2026 | Trung bình — vendor analytics; cần đối chiếu taxonomy | Đã xác minh excerpt |
| S5 | Metric — Tai nghe (3.308,7 tỷ đồng; 17 triệu sản phẩm; cơ cấu sàn) | https://metric.vn/ereport/tai-nghe | Data 01–12/2025; kiểm tra 12/11/2026 | Trung bình — vendor analytics; keyword rộng | Đã xác minh excerpt |
| S6 | Metric — Máy tính, Laptop & Thiết bị văn phòng (6.631,8 tỷ đồng; 27 triệu sản phẩm; 32.806 shop) | https://metric.vn/ereport/nganh-hang-may-tinh-laptop-thiet-bi-van-phong | Data 01–12/2025; kiểm tra 12/11/2026 | Trung bình — taxonomy rộng hơn laptop | Đã xác minh excerpt |
| S7 | Metric — Laptop Windows 11 (61,3 tỷ đồng; truy vấn hẹp) | https://metric.vn/ereport/laptop-windows-11 | Data 01–12/2025; kiểm tra 12/11/2026 | Trung bình — keyword hẹp, không đại diện toàn ngành | Đã xác minh excerpt |
| S8 | Metric — Màn hình PC gaming (19,6 tỷ đồng; 8 nghìn sản phẩm) | https://metric.vn/ereport/man-hinh-pc-gaming | Data 01–12/2025; kiểm tra 12/11/2026 | Trung bình — vendor analytics, niche keyword | Đã xác minh excerpt |
| S9 | Xiaomi Việt Nam — Xiaomi Monitor A27i specs (P27FBA-RAGL) | https://www.mi.com/vn/product/xiaomi-monitor-a27i/specs/ | Kiểm tra 12/11/2026 | Cao — trang thông số hãng | Đã xác minh |
| S10 | Sony Việt Nam — WH-1000XM6 specifications | https://www.sony.com.vn/electronics/support/wireless-headphones-bluetooth-headphones/wh-1000xm6/specifications | Kiểm tra 12/11/2026 | Cao — trang hỗ trợ hãng | Đã xác minh |
| S11 | Xiaomi Việt Nam — Smart Air Purifier 4 Compact specs (AC-M18-SC) | https://www.mi.com/vn/product/xiaomi-smart-air-purifier-4-compact/specs/ | Kiểm tra 12/11/2026 | Cao — trang thông số hãng | Đã xác minh |
| S12 | Thế Giới Di Động — danh mục laptop (SKU, cấu hình, giá, filter) | https://www.thegioididong.com/laptop | Kiểm tra 12/11/2026 | Trung bình–cao — retailer trực tiếp; giá biến động | Đã xác minh |
| S13 | ACCESSTRADE — Publisher API documentation index | https://developers.accesstrade.vn/api-publisher-vietnamese | Kiểm tra 12/11/2026 | Cao về sự tồn tại của tài liệu; chưa test API | Đã xác minh tài liệu |
| S14 | ACCESSTRADE — TikTok product search API v2 (feed fields, pagination, inventory, price, commission) | https://developers.accesstrade.vn/api-publisher-vietnamese/tich-hop-api-publisher-at-cho-chien-dich-tiktok-shop/version-2-updated-version/tiktok-product-search-v2 | Last updated theo docs; kiểm tra 12/11/2026 | Cao về schema công bố; chưa test API | Đã xác minh tài liệu |
| S15 | Shopee — Affiliate T&C, cập nhật 08/07/2026 | https://help.shopee.vn/portal/10/article/122944 | 08/07/2026; kiểm tra 12/11/2026 | Cao — điều khoản nền tảng | Đã xác minh |
| S16 | Lazada — Affiliate support FAQ (approval, threshold, payment timing) | https://pages.lazada.vn/wow/i/vn/corp/affiliate-support?hybrid=1 | Kiểm tra 12/11/2026 | Trung bình–cao — trang hỗ trợ nền tảng | Đã xác minh |
| S17 | Lazada — Affiliate terms and conditions (last-click; page hiển thị updated 30/09/2020) | https://pages.lazada.vn/wow/i/vn/corp/affiliate-terms | 30/09/2020 hiển thị trên trang; kiểm tra 12/11/2026 | Trung bình/thấp cho trạng thái 2026 vì có thể cũ | Đã xác minh nội dung trang; phiên bản hiện hành chưa xác minh |
| S18 | MasOffer — Publisher API portal (trang tài liệu không hiển thị schema khi truy xuất) | https://publisher-api.masoffer.net/docs/ | Kiểm tra 12/11/2026 | Thấp–trung bình — xác nhận portal tồn tại, không xác nhận field/API hoạt động | Đã xác minh portal; schema chưa xác minh |
| S19 | ACCESSTRADE — FAQ publisher về cookie và attribution | https://help.accesstrade.vn/faq/van-de-ve-ky-thuat/cac-thuat-ngu-thuong-gap/thoi-gian-luu-cookie-la-gi/ | Kiểm tra 12/11/2026 | Cao về hướng dẫn chung; campaign-specific cần dashboard | Đã xác minh |
| S20 | ACCESSTRADE — các bước gia nhập Publisher | https://help.accesstrade.vn/faq/welcome/cac-buoc-gia-nhap/ | Kiểm tra 12/11/2026 | Cao — help center network | Đã xác minh |
| S21 | MasOffer — FAQ sau đăng ký và cơ chế last-click/payout | https://masoffer.com/faq/sau-khi-dang-ky/ | Kiểm tra 12/11/2026 | Trung bình–cao — help page mạng affiliate | Đã xác minh |
| S22 | TikTok Shop — Apply as Affiliate Creator (Vietnam eligibility; 1.000 followers) | https://seller-vn.tiktok.com/university/essay?knowledge_id=6837838528808705&lang=en | Updated 22/07/2026; kiểm tra 12/11/2026 | Cao — tài liệu nền tảng | Đã xác minh |
| S23 | TikTok Shop — Affiliate Commission Rules & FAQ (Vietnam) | https://seller-vn.tiktok.com/university/essay?knowledge_id=7904880287155985&lang=en | Updated 30/01/2026; kiểm tra 12/11/2026 | Cao — tài liệu nền tảng | Đã xác minh |
| S24 | VnReview — tag review, ví dụ bài đánh giá laptop/tai nghe | https://vnreview.vn/tags/review/ | Kiểm tra 12/11/2026 | Trung bình — publisher/editorial content | Đã xác minh ví dụ |
| S25 | RTINGS — headphone/monitor testing methodology | https://www.rtings.com/headphones/learn/how-we-test ; https://www.rtings.com/monitor/learn/how-we-test | Cập nhật 2026; kiểm tra 12/11/2026 | Cao cho phương pháp họ công bố; phạm vi thử nghiệm không đại diện Việt Nam | Đã xác minh |
| S26 | Metric — truy vấn “lọc không khí” và “air purifier” cho thấy khác biệt taxonomy/keyword | https://metric.vn/ereport/loc-khong-khi ; https://metric.vn/ereport/air-purifier | Data 01–12/2025; kiểm tra 12/11/2026 | Trung bình — vendor analytics | Đã xác minh excerpt |
| S27 | IQAir — World most polluted cities / Hanoi PM2.5 2025; Google Trends Explore | https://www.iqair.com/world-most-polluted-cities?cities=ZPGtcusBx9JWBKYxm ; https://trends.google.com/trends/explore?date=today%205-y&geo=VN&q=laptop,monitor,m%C3%A1y%20lọc%20kh%C3%B4ng%20kh%C3%AD,tai%20nghe | IQAir 2025 dataset; kiểm tra 12/11/2026 | Trung bình–cao cho PM2.5 theo IQAir; Google Trends chưa export | IQAir đã xác minh; Trends chưa xác minh |
| S28 | Xiaomi Việt Nam — Smart Air Purifier 4 Compact product/spec page | https://www.mi.com/vn/product/xiaomi-smart-air-purifier-4-compact/ | Kiểm tra 12/11/2026 | Cao — trang hãng; thông số hiệu quả theo phương pháp nêu tại trang | Đã xác minh |
| S29 | Tinhte / GenK — ví dụ bài review laptop | https://tinhte.vn/thread/danh-gia-asus-vivobook-s16-s5608qa-26-trieu-cho-chiec-may-nay-thi-qua-ngon.4182508/ ; https://genk.vn/trai-nghiem-vivobook-s14-chay-intel-panther-lake-mong-nhe-on-dinh-va-san-sang-cho-mua-back-to-school-165261307110928546.chn | 2026; kiểm tra 12/11/2026 | Trung bình — nội dung biên tập/ trải nghiệm | Đã xác minh ví dụ |
| S30 | GitHub public repository — laptop-report-vn, so sánh laptop đa nhà bán (tự khai báo 3.364 laptop/13 shop) | https://github.com/PerfectDraft/laptop-report-vn | Kiểm tra 12/11/2026 | Thấp–trung bình — project công khai, số liệu do maintainer tự công bố | Đã xác minh repository; hiệu năng/độ chính xác chưa xác minh |
| S31 | Chính phủ — Luật Thương mại điện tử 122/2025/QH15, Điều 25–26 | https://en.baochinhphu.vn/viet-nams-law-on-e-commerce-111260825143234285.htm | Ban hành 10/12/2025, hiệu lực 01/07/2026; kiểm tra 12/11/2026 | Cao — nguồn Chính phủ | Đã xác minh |
| S32 | Bộ Công Thương — Law on E-commerce & Decree 248/2026/NĐ-CP; transparency requirements | https://moit.gov.vn/en/news/ministry-of-industry-and-trade-disseminates-the-law-on-e-commerce-and-government-decree-no.-248-2026-nd-cp.html | 03/07/2026; kiểm tra 12/11/2026 | Cao — cơ quan quản lý | Đã xác minh |
| S33 | Cổng thông tin Chính phủ — Luật sửa đổi Luật Quảng cáo 75/2025/QH15 | https://vanban.chinhphu.vn/?classid=1&docid=214561&pageid=27160&typegroupid=3ypegroupid%3D3 | Ban hành 16/06/2025, hiệu lực 01/01/2026; kiểm tra 12/11/2026 | Cao — văn bản pháp luật | Đã xác minh thông tin hiệu lực |

---

**Kết luận bàn giao:** Dữ liệu công khai hiện chứng minh có nhu cầu online đáng kể ở bốn nhóm, có nguồn hãng để chuẩn hóa thông số, có retailer/marketplace để kiểm tra offer và có ít nhất một lộ trình feed/API affiliate được tài liệu hóa qua ACCESSTRADE. Tuy nhiên, chưa đủ bằng chứng để kết luận ngành hàng nào có khả năng tạo doanh thu affiliate tốt nhất: còn thiếu search demand định lượng, campaign commission/cookie theo SKU, quyền truy cập feed, dữ liệu conversion và tỷ lệ hoàn/hủy. Quyết định ưu tiên ngành hàng thuộc CEO.
