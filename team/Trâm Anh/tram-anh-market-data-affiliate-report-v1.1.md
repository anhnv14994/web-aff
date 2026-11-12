# TRÂM ANH — MARKET DATA & AFFILIATE REPORT v1.1

**Dự án:** A+ — website tư vấn, so sánh và hỗ trợ quyết định mua hàng  
**Task:** PILOT-05 — Kiểm chứng thị trường, publisher eligibility và nguồn dữ liệu  
**Phạm vi:** Việt Nam · Màn hình máy tính · Thiết bị âm thanh · Máy lọc không khí · Laptop  
**Ngày kiểm tra nguồn:** 12/11/2026  
**Phiên bản:** v1.1  
**Trạng thái bàn giao:** Nghiên cứu desk-research đã cập nhật; 20 mẫu model đã lập danh mục; SERP đã kiểm tra sơ bộ qua chỉ mục tìm kiếm web. **Google Trends CSV chưa xuất được** và được ghi rõ là hạng mục còn mở, không giả lập dữ liệu.

> **Quy tắc bằng chứng:** “Đã xác minh” nghĩa là trang/tài liệu công khai được truy xuất và thông tin có thể nhìn thấy tại lần kiểm tra. Điều này không đồng nghĩa đã kiểm thử giao dịch, đăng nhập publisher, gọi API có xác thực hoặc kiểm tra checkout/tồn kho trực tiếp. Giá và tồn kho không được xem là dữ liệu hiện hành nếu chỉ xuất hiện trong bản cache/index của trang bán lẻ.

## 1. Tóm tắt kết quả PILOT-05

| Hạng mục được giao | Kết quả | Trạng thái | Mức tin cậy |
|---|---|---|---|
| Xuất Google Trends 5 năm | Đã tạo 4 Explore links theo Việt Nam và khoảng 12/11/2021–12/11/2026; chưa lấy được CSV/chuỗi điểm dữ liệu từ giao diện động trong phiên nghiên cứu này | **Chưa hoàn tất — không có số liệu định lượng** | Cao về phương pháp/link; thấp về kết quả chưa export |
| Kiểm tra SERP theo truy vấn mua hàng | Đã rà 8 nhóm truy vấn (2/ngành) và các trang kết quả/landing page tìm kiếm được; ghi nhận loại đối thủ và dạng nội dung | **Đã kiểm tra sơ bộ**; chưa phải ảnh chụp Google SERP theo vị trí/thiết bị | Trung bình |
| Xác minh affiliate dành cho website publisher | ACCESSTRADE có định nghĩa Publisher bao gồm chủ website/blog và API dành cho Publisher; Shopee có loại hình Short-tail nhưng có điều kiện và quyền từ chối; Lazada/MasOffer chưa đủ điều khoản publisher hiện hành để xác nhận | **Xác minh được một phần** | Cao cho ACCESSTRADE/Shopee; thấp cho Lazada/MasOffer |
| Kiểm tra pháp lý | Đối chiếu Luật TMĐT 122/2025/QH15, Nghị định 248/2026/NĐ-CP, Luật Quảng cáo sửa đổi 75/2025/QH15 và thông báo Cục TMĐT tháng 10/2026 | **Đã xác minh văn bản và ngày hiệu lực**; cần luật sư rà vai trò pháp lý cụ thể của A+ | Cao về văn bản; trung bình về áp dụng vào mô hình A+ |
| Lấy mẫu nguồn dữ liệu 20 model | 5 model/ngành, từ hãng và retailer; ghi nhận mã model/variant, nguồn thông số và nguồn catalog | **Đã hoàn thành desk sample**; chưa test API/feed runtime | Trung bình–cao tùy model |

### Kết luận điều hành

1. **Nguồn publisher phù hợp nhất đã xác minh ở cấp tài liệu là ACCESSTRADE:** Publisher có thể là tổ chức/cá nhân sở hữu website, blog hoặc kênh truyền thông; API Publisher có endpoint campaign, tracking link, giao dịch, thông tin sản phẩm và datafeed. Tuy nhiên, quyền truy cập thực tế và campaign điện tử phải được duyệt theo tài khoản/campaign.
2. **Shopee không thể coi là “website publisher tự động đủ điều kiện”:** điều khoản 15/09/2026 có loại hình Short-tail dành cho đối tác dịch vụ quảng bá/mạng lưới truyền thông; chỉ doanh nghiệp được liệt kê đủ loại hình này và Shopee được toàn quyền duyệt/từ chối. Cookie được định nghĩa 7 ngày. Cần hỏi Shopee xác nhận chính thức A+ thuộc loại hình nào.
3. **SERP cho thấy retailer/category pages đang chiếm vị trí nổi bật trong tập kết quả được tìm thấy**, cùng với website so sánh giá và bài tư vấn. A+ có cơ hội khác biệt bằng catalog chuẩn hóa model/variant + tư vấn theo nhu cầu, nhưng chưa có số liệu đủ để kết luận độ khó SEO hoặc traffic.
4. **Google Trends chưa có CSV:** mọi nhận định tăng/giảm tìm kiếm trong 5 năm vẫn để trống cho đến khi export đúng từ Google Trends. Không dùng số liệu Metric/sàn để thay thế search demand.
5. **20 model mẫu cho thấy độ khó chuẩn hóa khác nhau:** màn hình và máy lọc có thể đối chiếu khá trực tiếp theo model; laptop cần exact machine type/config code; audio có tên dòng gần nhau và bản TWS/headphone khác loại. Mẫu này mới kiểm tra độ sẵn có nguồn, không phải audit đủ 100 SKU/ngành.

## 2. Tín hiệu thị trường và cạnh tranh nền

Các số Metric dưới đây kế thừa baseline v1.0, dùng dữ liệu sàn 01–12/2025. Taxonomy và từ khóa từng báo cáo khác nhau nên **không thể so sánh như cùng một mẫu thị trường hoặc TAM**.

| Ngành hàng | Tín hiệu Metric 2025 | Giới hạn quan trọng | Diễn giải thận trọng |
|---|---:|---|---|
| Laptop | 6.631,8 tỷ đồng cho nhóm rộng “Máy tính, Laptop & Thiết bị văn phòng” | Bao gồm máy tính/phụ kiện/thiết bị văn phòng, không phải laptop-only | Có tín hiệu giao dịch lớn ở nhóm rộng; phải tách laptop-only và exact configuration trước khi suy ra cơ hội affiliate |
| Tai nghe | 3.308,7 tỷ đồng, nhóm từ khóa tai nghe rộng | Có nhiều TWS/tai nghe phổ thông, không tương đương audio hi-fi/ANC cao cấp | Nhu cầu sàn mạnh nhưng danh mục giá và form factor rất phân mảnh |
| Máy lọc không khí | 798,7 tỷ đồng | Kết quả thay đổi tùy cụm “máy lọc không khí”, “lọc không khí”, “air purifier” | Có thể tư vấn bằng diện tích/CADR/độ ồn/lõi thay; cần phân biệt model và mã filter |
| Màn hình monitor | 73,9 tỷ đồng | Là từ khóa monitor trên sàn, không gồm toàn bộ website retailer/offline; niche gaming có bộ dữ liệu riêng | Nhỏ hơn trong taxonomy đã quan sát, nhưng thông số tương đối chuẩn hóa và có nhiều intent cụ thể |

Nguồn baseline: [Metric — Màn hình monitor](https://metric.vn/ereport/man-hinh-monitor), [Máy lọc không khí](https://metric.vn/ereport/may-loc-khong-khi), [Tai nghe](https://metric.vn/ereport/tai-nghe), [Máy tính/Laptop/Thiết bị văn phòng](https://metric.vn/ereport/nganh-hang-may-tinh-laptop-thiet-bi-van-phong). Đơn vị Metric là nguồn analytics thương mại; độ tin cậy trung bình; số hiển thị công khai là excerpt và có thể phụ thuộc taxonomy/keyword.

Bối cảnh chung: [Báo cáo thị trường nội địa 2025 — Bộ Công Thương](https://dms.gov.vn/documents/d/guest/bc-ttnd-2025-pdf) ghi nhận TMĐT Việt Nam ước khoảng 830 nghìn tỷ đồng năm 2025 (bốn sàn lớn khoảng 455 nghìn tỷ đồng) và trích dẫn khảo sát PwC về hành vi mua online. Đây là bối cảnh kênh bán, **không phải quy mô của bốn ngành A+**. [YouNet ECI — Toàn cảnh TMĐT H1/2026](https://youneteci.com/vi/bao-cao-toan-canh-tmdt-viet-nam-nua-dau-nam-2026/) cho thấy tín hiệu tăng trong nhóm Điện gia dụng & Điện tử trên các sàn; cũng không thể suy thẳng thành doanh thu từng ngách.

## 3. Google Trends — 5 năm

### 3.1. Thiết lập truy vấn đề xuất

**Cấu hình thống nhất:** Việt Nam (`geo=VN`); 12/11/2021–12/11/2026; Web Search; danh mục All categories; dùng Search terms, không trộn Search term với Topic trong cùng bảng. Các truy vấn đã chuẩn bị theo 4 ngành:

| Nhóm | Các cụm so sánh (tối đa 5 cụm/biểu đồ) | Explore link |
|---|---|---|
| Màn hình | “màn hình máy tính”; “màn hình 27 inch”; “màn hình gaming”; “màn hình văn phòng”; “màn hình 2K” | [Mở Google Trends — Màn hình](https://trends.google.com/trends/explore?date=2021-11-12%202026-11-12&geo=VN&q=%22m%C3%A0n%20h%C3%ACnh%20m%C3%A1y%20t%C3%ADnh%22,%22m%C3%A0n%20h%C3%ACnh%2027%20inch%22,%22m%C3%A0n%20h%C3%ACnh%20gaming%22,%22m%C3%A0n%20h%C3%ACnh%20v%C4%83n%20ph%C3%B2ng%22,%22m%C3%A0n%20h%C3%ACnh%202K%22) |
| Âm thanh | “tai nghe”; “tai nghe bluetooth”; “tai nghe chống ồn”; “tai nghe chụp tai”; “tai nghe gaming” | [Mở Google Trends — Tai nghe](https://trends.google.com/trends/explore?date=2021-11-12%202026-11-12&geo=VN&q=%22tai%20nghe%22,%22tai%20nghe%20bluetooth%22,%22tai%20nghe%20ch%E1%BB%91ng%20%E1%BB%93n%22,%22tai%20nghe%20ch%E1%BB%A5p%20tai%22,%22tai%20nghe%20gaming%22) |
| Máy lọc không khí | “máy lọc không khí”; “máy lọc không khí phòng ngủ”; “máy lọc không khí phòng 20m2”; “máy lọc không khí Xiaomi”; “máy lọc không khí Sharp” | [Mở Google Trends — Máy lọc không khí](https://trends.google.com/trends/explore?date=2021-11-12%202026-11-12&geo=VN&q=%22m%C3%A1y%20l%E1%BB%8Dc%20kh%C3%B4ng%20kh%C3%AD%22,%22m%C3%A1y%20l%E1%BB%8Dc%20kh%C3%B4ng%20kh%C3%AD%20ph%C3%B2ng%20ng%E1%BB%A7%22,%22m%C3%A1y%20l%E1%BB%8Dc%20kh%C3%B4ng%20kh%C3%AD%20ph%C3%B2ng%2020m2%22,%22m%C3%A1y%20l%E1%BB%8Dc%20kh%C3%B4ng%20kh%C3%AD%20Xiaomi%22,%22m%C3%A1y%20l%E1%BB%8Dc%20kh%C3%B4ng%20kh%C3%AD%20Sharp%22) |
| Laptop | “laptop”; “laptop văn phòng”; “laptop gaming”; “laptop sinh viên”; “laptop đồ họa” | [Mở Google Trends — Laptop](https://trends.google.com/trends/explore?date=2021-11-12%202026-11-12&geo=VN&q=%22laptop%22,%22laptop%20v%C4%83n%20ph%C3%B2ng%22,%22laptop%20gaming%22,%22laptop%20sinh%20vi%C3%AAn%22,%22laptop%20%C4%91%E1%BB%93%20h%E1%BB%8Da%22) |

### 3.2. Trạng thái export và cách đọc

- **CSV thực tế:** chưa được tải về trong phiên này. Google Trends Explore là trang động và không truy xuất được qua môi trường web hiện có; môi trường container cũng không có kết nối outbound để gọi endpoint Trends. Vì thế báo cáo không ghi giả trị index, không tạo chuỗi tháng giả và không tuyên bố đã hoàn thành export.
- **Cách export thủ công để đóng hạng mục:** mở từng Explore link → kiểm tra đúng khoảng thời gian/geo/search type → tại biểu đồ Interest over time chọn Download CSV → lưu tên `trends-vn-5y-monitor.csv`, `trends-vn-5y-audio.csv`, `trends-vn-5y-air-purifier.csv`, `trends-vn-5y-laptop.csv` → ghi ngày tải, term type và region. Dùng cùng một bộ term khi so sánh các khoảng thời gian.
- **Cách hiểu dữ liệu:** Google Trends chuẩn hóa mức quan tâm theo thời gian và vị trí, chia tỷ lệ trên tổng tìm kiếm của phạm vi tương ứng, rồi đưa về thang 0–100. Đây không phải search volume tuyệt đối, không được diễn giải “100 = 100 lượt tìm kiếm”. Kết quả là mẫu dữ liệu tìm kiếm, không phải census. [Google Trends — FAQ dữ liệu](https://support.google.com/trends/answer/4365533?hl=vi), [Google — Export and cite Trends data](https://support.google.com/trends/answer/4365538?hl=en).
- **Không trộn dữ liệu Google Trends với Google Ads Keyword Planner:** Google xác định đây là hai nguồn khác nhau. Trends dùng đo quan tâm tương đối theo thời gian; Ads Keyword Planner mới phù hợp để lấy ước tính số lượt tìm kiếm/nhóm keyword theo cách riêng của Ads. [Google — Export, embed and cite Trends](https://support.google.com/trends/answer/4365538?hl=en).

**Bảng ghi dữ liệu cần điền sau khi CSV được tải:** `date | search_term | geo | search_type | interest_0_100 | category | source_file | exported_at`. Sau khi export, cần kiểm tra seasonality, trung bình 12 tháng, đỉnh/đáy, YoY, vùng địa lý và các term có index quá thấp/zero. Không so sánh mức 0–100 giữa hai biểu đồ độc lập nếu không dùng chung term neo.

## 4. SERP — truy vấn có ý định mua

### 4.1. Phương pháp và giới hạn

Ngày rà soát: **12/11/2026**. Đã gửi 8 truy vấn mua hàng/so sánh, 2 cho mỗi ngành, tới công cụ tìm kiếm web và kiểm tra các trang đích được trả về. Đây là **SERP reconnaissance qua chỉ mục tìm kiếm web**, không phải bản chụp vị trí xếp hạng chính thức của Google tại Hà Nội trên desktop/mobile. Không kết luận rank #1–#10, search volume, CTR hoặc độ khó SEO. Direct Google SERP page và Trends dynamic page không truy xuất được trong môi trường này.

### 4.2. Truy vấn và dạng đối thủ quan sát được

| Ngành | Truy vấn mua hàng đã kiểm tra | Dạng kết quả/đối thủ quan sát được | Hàm ý cho A+ | Trạng thái |
|---|---|---|---|---|
| Màn hình | `mua màn hình 27 inch 2K 144Hz giá Việt Nam mua online` | Trang danh mục retailer có bộ lọc kích thước/độ phân giải/tấm nền/refresh rate; danh sách ASUS, Samsung, Philips, Dell, Xiaomi, AOC, MSI và Gaming SKU. [TGDĐ — màn hình 27 inch](https://www.thegioididong.com/man-hinh-may-tinh-27-inch) | Category page thỏa intent tìm hàng/giá. Cơ hội A+ nằm ở giải thích 27-inch FHD vs QHD, panel, độ sáng/màu, chân đế/cổng kết nối và suitability theo game/workflow. | Đã xem snapshot kết quả; không xác minh Google rank |
| Màn hình | `màn hình máy tính văn phòng 27 inch so sánh sản phẩm giá tốt Việt Nam` | Trang brand/product spec và danh mục bán lẻ; ví dụ Samsung S3 S30GD có spec model rõ, Philips Evnia có model code riêng; Dell U2725QE hướng tới phân khúc premium. [Samsung S3](https://www.samsung.com/vn/monitors/full-hd-1080p/essential-monitor-s3-s30gd-27-inch-fhd-ips-100hz-ls27d300gaexxv/), [Philips Evnia](https://www.philips.com.vn/c-p/27M2N2500NF_71/fast-ips-gaming-monitor-quad-hd-gaming-monitor) | Nên tạo bộ lọc use-case; tên chung “27 inch” không đủ — mã sản phẩm, độ phân giải, Hz, panel và cổng phải khớp. | Đã xem trang hãng/retailer; chưa có rank audit |
| Âm thanh | `tai nghe chống ồn ANC làm việc online giá Việt Nam Sony JBL` | Danh mục retailer xếp headphone ANC, TWS và earbuds chung hệ; Sony WH-1000XM6, JBL Live 780NC cùng nhiều TWS xuất hiện. [TGDĐ — tai nghe Bluetooth](https://www.thegioididong.com/tai-nghe-bluetooth), [tai nghe chụp tai](https://www.thegioididong.com/tai-nghe-chup-tai) | Cần tách form factor, ANC, mic call quality, multipoint, latency, codec và comfort. Search intent “ANC làm việc” không nên điều hướng sang TWS phổ thông chỉ vì giá/hoa hồng. | Đã xem snapshot kết quả; không xác minh Google rank |
| Âm thanh | `mua tai nghe chụp tai bluetooth chống ồn chính hãng giá Việt Nam 2026` | Retailer product/category results, hãng và bài review công nghệ; thấy Sony WH-1000XM6, JBL Live 780NC, JBL Tune/CH series, cùng lựa chọn TWS/earbuds trong cùng catalog. [TGDĐ — tai nghe chụp tai](https://www.thegioididong.com/tai-nghe-chup-tai), [VnReview — review tag](https://vnreview.vn/tags/review/) | Cơ hội content: so sánh call, độ ồn văn phòng/di chuyển, độ thoải mái lâu, pin và khả năng dùng có dây; cần phân biệt ANC thật với cách mô tả marketing. | Đã xem snapshot kết quả; cần SERP screenshot để xác minh rank |
| Máy lọc không khí | `máy lọc không khí phòng 20m2 CADR chọn mua giá Việt Nam` | Retailer có filter diện tích phòng (dưới 20m², 20–30m², 30–40m², trên 40m²), bụi PM1/PM2.5 và công suất; trang hãng Philips cho biết CADR và area theo model. [TGDĐ — máy lọc không khí](https://www.thegioididong.com/may-loc-khong-khi), [Philips catalog](https://www.philips.com.vn/c-m-ho/climate-care/air-purifier/latest) | Cơ hội lớn cho tư vấn fit theo diện tích thực/chiều cao trần/ACH/CADR, độ ồn mức ngủ và chi phí lõi thay. Tránh khẳng định y tế hoặc “lọc sạch 100%”. | Đã xem snapshot kết quả; không xác minh Google rank |
| Máy lọc không khí | `mua máy lọc không khí Xiaomi Sharp Philips chính hãng giá tốt Việt Nam` | Retailer danh mục và catalog của thương hiệu; Bếp Xanh hiển thị nhiều nhãn hàng và số model theo danh mục, TGDĐ liệt kê Xiaomi/Sharp/LG/Philips/Dreame/Daikin. [Bếp Xanh](https://bepxanh.com/may-loc-khong-khi/), [TGDĐ](https://www.thegioididong.com/may-loc-khong-khi) | Nên làm content total cost of ownership (máy + filter), mã lõi tương thích, CADR theo test condition và chi phí thay theo năm. Cần xác nhận model/filter code; không map theo hình ảnh/tên thương mại. | Đã xem trang catalog; giá/tồn không được đóng băng |
| Laptop | `laptop văn phòng 16GB 512GB mỏng nhẹ giá Việt Nam 2026` | Retailer category có filter RAM/SSD/form factor; nhà bán chuyên laptop và cửa hàng CNTT có danh mục 20–25 triệu; trang so sánh laptop có exact model codes và mức giá đa cửa hàng. [TGDĐ — laptop](https://www.thegioididong.com/laptop), [Hanoinew](https://hanoinew.vn/laptop-may-tinh-xach-tay?filter=22-969-972-984&max=25000000&min=20000000), [Sogia](https://sogia.com.vn/laptop/trang-2) | Cần so cấu hình thực theo machine type/part number, CPU suffix, RAM hàn/nâng cấp, panel, battery, Windows/Office, bảo hành; không ghép hai cấu hình cùng tên dòng. | Đã xem trang retailer/so sánh; chưa có rank/traffic estimate |
| Laptop | `so sánh laptop 14 inch dưới 25 triệu Việt Nam ASUS Lenovo HP Dell 2026` | Trang retailer, bảng giá và bài tư vấn theo budget/use-case; nhiều cấu hình 14 inch, RAM 16GB, SSD 512GB nhưng SKU khác nhau. [Sintech 20–25 triệu](https://sintech.vn/collections/laptop-20-25-trieu), [Hanoinew 20–25 triệu](https://hanoinew.vn/laptop-may-tinh-xach-tay?filter=22-969-972-984&max=25000000&min=20000000), [TGDĐ](https://www.thegioididong.com/laptop) | A+ cần làm “decision page” theo workload, pin, màn hình, cân nặng và nâng cấp thay vì chỉ lọc theo CPU/RAM. SKU laptop đặc biệt dễ bị sai mapping. | Đã xem trang retailer; chưa có rank audit |

### 4.3. Cạnh tranh nội dung và vị trí khác biệt

- **Retailer PDP/category:** mạnh về giá, tồn kho, khuyến mãi, bộ lọc và giao hàng; yếu hơn về giải thích trade-off và trung lập giữa nhiều nhà bán. Giá/tồn có thể thay đổi theo khu vực, voucher và thời điểm.
- **Website so sánh giá:** có lợi thế tổng hợp nhiều cửa hàng/mã máy; chất lượng có thể giảm nếu cấu hình/phiên bản gộp sai hoặc không cập nhật.
- **Review/editorial:** giúp trải nghiệm thực tế, test và cảm nhận; khó phủ hết SKU, khó cập nhật giá/stock và có thể thiếu dữ liệu máy/phiên bản đang bán.
- **A+ có thể tạo khác biệt:** canonical product identity + variant matching + use-case decision flow + trade-off rõ ràng + ngày xác minh giá/stock + nhiều nhà bán. Không được tự đặt tiêu chí chuyên môn khi chưa nhận input từ A Long; không tự gán persona khi chưa nhận input Vân Anh.

## 5. Xác minh publisher eligibility và affiliate

### 5.1. Ma trận điều kiện dành cho website A+

| Network / chương trình | Bằng chứng về website publisher | Điều kiện/giới hạn đã xác minh | Dữ liệu/API | Kết luận cho A+ |
|---|---|---|---|---|
| **ACCESSTRADE Publisher** | Terms định nghĩa Publisher là tổ chức/cá nhân sở hữu website, blog hoặc kênh truyền thông quảng bá sản phẩm/dịch vụ của Advertiser. FAQ xác nhận có website/blog riêng có thể dùng API lấy offer, giao dịch, sản phẩm, khuyến mãi về website. [Terms](https://merchant.accesstrade.me/dieu-khoan/), [Publisher FAQ](https://help.accesstrade.vn/faq-publisher/) | Cần CCCD, tài khoản ngân hàng, mã số thuế chính chủ và hợp đồng điện tử để định danh/thanh toán theo FAQ. Publisher phải đăng ký campaign và chờ duyệt trước khi tạo link/đăng nội dung. Cookie theo từng campaign; tài liệu ghi trong nội dung campaign. [FAQ](https://help.accesstrade.vn/faq-publisher/) | API docs công khai có authentication, campaign listing, tracking link, transactions/orders, product details, datafeeds và tích hợp TikTok Shop. [API Publisher docs](https://developers.accesstrade.vn/api-publisher-vietnamese) | **Khả thi nhất ở cấp publisher model đã xác minh.** A+ vẫn phải được phê duyệt account/campaign; chưa xác minh campaign electronics còn hiệu lực/commission/cookie theo SKU. |
| **Shopee Affiliate — Short-tail / KOL Affiliate doanh nghiệp** | Điều khoản cập nhật 15/09/2026 phân loại KOL/KOC, KOL Affiliate doanh nghiệp, MCN, Seller Affiliate và Short-tail. Short-tail được mô tả là đối tác dịch vụ quảng bá/phát triển mạng lưới truyền thông. [Shopee T&C](https://help.shopee.vn/portal/10/article/206429?previousPage=other+articles) | Bảng loại hình cho biết Short-tail chỉ áp dụng cho Doanh nghiệp, không áp dụng cá nhân kinh doanh/hộ kinh doanh. Shopee giữ toàn quyền chấp nhận/từ chối. KOL Affiliate doanh nghiệp cần account hợp lệ, đạt yêu cầu đơn hàng hàng ngày theo từng thời điểm, hoạt động theo loại hình doanh nghiệp/hộ kinh doanh đáp ứng hóa đơn, và đủ điều kiện ký hợp đồng. Short-tail phải khai rõ network/phương tiện TTLK công khai, truy cập được. [T&C §2, §4, §5](https://help.shopee.vn/portal/10/article/206429?previousPage=other+articles) | Cookie: 7 ngày theo định nghĩa điều khoản. Commission xem trong hệ thống/chính sách hoặc thỏa thuận riêng; không có một rate cố định công khai cho 4 ngành A+. API/feed product cho publisher website A+ chưa xác minh. | **Có lộ trình hỏi Short-tail nếu A+ vận hành dưới doanh nghiệp; không có bảo đảm được nhận.** Cần hỏi Shopee xác nhận website so sánh độc lập có thuộc “phương tiện TTLK” được duyệt hay không. |
| **Lazada Affiliate** | Có trang hỗ trợ affiliate/đăng ký, nhưng trong lần rà soát này chưa xác minh được điều khoản publisher hiện hành năm 2026 và tiêu chí dành riêng cho website so sánh. | Bản terms được baseline v1.0 ghi nhận có timestamp cũ; không dùng làm căn cứ cookie/attribution hiện hành. Cần yêu cầu bản điều khoản mới từ Lazada. | Chưa có bằng chứng công khai về product feed/API affiliate được cấp cho A+ website. Open Platform API không tự chứng minh quyền dùng affiliate feed. | **Chưa xác minh** — chỉ đưa vào shortlist hỏi network, chưa đưa vào doanh thu base case. |
| **MasOffer Publisher** | Có portal Publisher/API và FAQ public, nhưng tài liệu truy xuất được chưa cho thấy điều kiện hiện hành dành riêng cho website publisher A+. | Chưa xác minh approval criteria, campaign coverage cho 4 ngành, current cookie windows, commission và attribution. | Portal API tồn tại không đồng nghĩa API datafeed đang được cấp; schema/fields và quyền sử dụng feed chưa xác minh. | **Chưa xác minh** — cần câu trả lời bằng văn bản/portal sau phê duyệt. |
| **TikTok Shop Affiliate Creator** | Tài liệu Creator thường gắn với kênh creator/video; không nên đồng nhất với website publisher độc lập. | Điều kiện Creator, follower, xác minh danh tính và commission theo seller/SKU thay đổi; không lấy điều kiện creator áp vào A+ website. | A+ có thể khảo sát TikTok Shop product feed qua network (ví dụ AT) nếu campaign/permission cấp; không giả định có TikTok API trực tiếp. | **Không xác minh được website-only eligibility trực tiếp.** Ưu tiên kiểm tra campaign TikTok Shop qua AT sau phê duyệt. |

### 5.2. Các điểm cần xác nhận trước khi đưa vào business case

1. Tài khoản A+ đứng tên pháp nhân nào; website/domain đã công khai, có trang giới thiệu, chính sách biên tập, disclosure affiliate, privacy/contact chưa?
2. Network xem A+ là website review/comparison, publisher content site hay Short-tail partner? Cần xác nhận category và legal entity phù hợp.
3. Có thể chạy các advertiser/brand nào trong 4 ngành; danh sách campaign ID, landing domain và model/SKU nào được commission?
4. Commission thực nhận tính theo SKU/category ra sao; giá tính hoa hồng trước/sau voucher; tỷ lệ hủy/hoàn/đơn không hợp lệ và approval/locking period?
5. Cookie duration và attribution rule (first/last click, app/web, cross-device, deep link, voucher overwrite) theo campaign?
6. API/feed gồm product ID, model/part number, SKU variant, image, attributes, price, sale price, stock, commission, tracking URL, updated_at; rate limit, pagination, cadence và SLA?
7. Quyền lưu cache/ảnh/giá, quyền sửa đổi dữ liệu, thời gian giữ data sau khi campaign kết thúc, điều kiện gỡ nội dung và ảnh hưởng khi offer bị pause?
8. Doanh thu được xuất hóa đơn/khấu trừ thuế, threshold và lịch thanh toán theo tư cách doanh nghiệp/hộ kinh doanh ra sao?

## 6. Pháp lý và policy cần chú ý

> Phần này là checklist nghiên cứu vận hành, không phải ý kiến tư vấn pháp lý. Cần luật sư/đơn vị pháp chế phân loại tư cách của A+ và rà bản tiếng Việt chính thức trước khi ra mắt.

### 6.1. Luật Thương mại điện tử 122/2025/QH15

- Luật được ban hành **10/12/2025**, có hiệu lực **01/07/2026**. Nguồn: [Cổng văn bản Chính phủ — Luật số 122/2025/QH15](https://vanban.chinhphu.vn/?classid=1&docid=216503&pageid=27160&typegroupid=3) và [bản tiếng Anh trên Cổng thông tin Chính phủ](https://en.baochinhphu.vn/viet-nams-law-on-e-commerce-111260825143234285.htm).
- **Điều 25** quy định trách nhiệm của tổ chức/cá nhân cung cấp dịch vụ tiếp thị liên kết trong TMĐT: xác thực điện tử danh tính người affiliate trước khi thiết lập link/referral code; từ chối dịch vụ cho hàng hóa/dịch vụ hoặc nền tảng vi phạm theo phạm vi luật; ngăn chặn/gỡ link vi phạm; cung cấp thông tin hoạt động khi cơ quan quản lý yêu cầu.
- **Điều 26** quy định trách nhiệm người tiếp thị liên kết: cung cấp thông tin phục vụ xác minh danh tính; từ chối hoạt động trên nền tảng vi phạm được công bố hoặc nội dung vi phạm các điều kiện nêu trong luật; gỡ link cho hàng hóa/dịch vụ vi phạm hoặc theo yêu cầu; cung cấp thông tin hoạt động theo yêu cầu cơ quan quản lý.
- A+ cần rà liệu trong cấu trúc dịch vụ và cách vận hành mình chỉ là **người tiếp thị liên kết** (publisher) hay có chức năng khiến mình bị phân loại là **đơn vị cung cấp dịch vụ tiếp thị liên kết**. Không tự kết luận vai trò theo tên gọi “website affiliate”.

### 6.2. Nghị định 248/2026/NĐ-CP và thông báo triển khai

- [Nghị định 248/2026/NĐ-CP](https://vanban.chinhphu.vn/?docid=218747&orggroupid=2&pageid=27160) được ban hành **30/06/2026**, hiệu lực **01/07/2026**.
- [Cục Thương mại điện tử — Thông báo triển khai quy định pháp luật về TMĐT](https://www.idea.gov.vn/default.aspx?category_id=6e3f3b28-3917-4816-83c5-a331259dd181&do=detail&id=184e0d3f-daab-42a5-a33e-782c78e579c0&page=news), ngày **14/10/2026**, nhắc lại hiệu lực Luật/Nghị định từ 01/07/2026 và một mốc khác: từ **01/01/2027**, chủ quản nền tảng TMĐT trung gian/mạng xã hội hoạt động TMĐT phải thực hiện xác thực điện tử danh tính người bán và người livestream bán hàng theo quy định. Đây là nghĩa vụ liên quan chủ quản nền tảng; không tự động suy ra website publisher A+ là nền tảng trung gian.
- Cần đọc Nghị định bản tiếng Việt đầy đủ theo cấu trúc hoạt động A+ và yêu cầu cụ thể từ cơ quan quản lý; không dùng bài tóm tắt để thay luật.

### 6.3. Luật Quảng cáo sửa đổi 75/2025/QH15

- [Luật 75/2025/QH15](https://vanban.chinhphu.vn/?classid=1&docid=214561&pageid=27160) được ban hành **16/06/2025**, hiệu lực **01/01/2026**.
- Nội dung quảng cáo trên mạng có nghĩa vụ nhận diện rõ ràng để phân biệt với nội dung không phải quảng cáo; quy định cũng đề cập trách nhiệm người quảng cáo, người phát hành và người chuyển tải sản phẩm quảng cáo. Cần xác định nội dung nào trên A+ được coi là quảng cáo/chuyển tải quảng cáo trong bối cảnh affiliate và áp dụng quy định tương ứng.
- **Thực hành thận trọng đề xuất:** disclosure cạnh CTA/link và trong trang phương pháp: “A+ có thể nhận hoa hồng khi bạn mua qua một số liên kết; hoa hồng không làm thay đổi tiêu chí đánh giá và xếp hạng phù hợp.” Lưu log nguồn, ngày kiểm tra giá/stock, quan hệ affiliate và bản nội dung đã phát hành. Đây là control đề xuất để minh bạch, không được trình bày như câu chữ bắt buộc nguyên văn trong luật.

### 6.4. Checklist pháp lý vận hành nội bộ

- Hiển thị disclosure affiliate dễ thấy trước hoặc cạnh liên kết thương mại; phân biệt phần giải thích biên tập và khối quảng bá.
- Không tạo claim sai về hiệu năng, sức khỏe, chất lượng lọc, thông số, xuất xứ, giá hoặc tình trạng hàng.
- Không dùng review giả, tự đặt đơn rồi hoàn, cookie stuffing, auto-redirect hoặc cơ chế khiến người dùng click nhầm; rà policy từng network.
- Có quy trình gỡ link khi sản phẩm/nhà bán bị cảnh báo hoặc campaign bị dừng.
- Lưu bằng chứng model, giá, điều kiện khuyến mãi, warranty và nguồn dữ liệu tại thời điểm xuất bản.
- Hoàn thiện pháp nhân/thuế/hóa đơn và hợp đồng network trước khi ghi nhận affiliate revenue trong forecast.

## 7. Mẫu nguồn dữ liệu 20 model — 5 model/ngành

### 7.1. Cách đọc bảng

Đây là **mẫu model để kiểm tra nguồn catalog**, không phải bảng xếp hạng hay khuyến nghị mua. Một số trang retailer đang dùng tên thương mại, model code hoặc cấu hình; nếu model code chưa có ở nguồn hãng thì đánh dấu “chưa map”, không tự ghép dựa vào tên gần giống. Các listing retailer được index/crawl trong khoảng vài tuần trước ngày 12/11/2026; giá/tồn không được copy vào master catalog vì chưa xác minh lại ở checkout trong cùng thời điểm.

### A. Màn hình máy tính — 5 model

| # | Model / định danh nhìn thấy | Nguồn hãng (spec/identity) | Nguồn retail/catalog | Chất lượng dữ liệu lấy được | Trạng thái & rủi ro |
|---:|---|---|---|---|---|
| 1 | Xiaomi Monitor A27i — mã trang spec `P27FBA-RAGL` | [Xiaomi specs](https://www.mi.com/vn/product/xiaomi-monitor-a27i/specs/) | [TGDĐ 27-inch monitor list](https://www.thegioididong.com/man-hinh-may-tinh-27-inch) — có tên A27i 2026 trong catalog | Hãng có model code, kích thước, resolution, refresh, brightness, ports. Retail list có tên/giá theo biến thể. | **Một phần đã xác minh.** Trang hãng P27FBA-RAGL là record cũ; listing “A27i 2026” trên retailer không được tự động coi là cùng SKU. Phải map lại part number 2026. |
| 2 | ASUS TUF Gaming `VG27AQE5A` | [ASUS Global product page](https://www.asus.com/displays-desktops/monitors/tuf-gaming/tuf-gaming-vg27aqe5a/) | [TGDĐ 27-inch monitor list](https://www.thegioididong.com/man-hinh-may-tinh-27-inch) | Trang hãng xác nhận 27-inch QHD Fast IPS, 165Hz OC, 0.3ms; retailer có record model/giá snapshot. | **Đã xác minh model/spec hãng và listing.** Giá/stock tại retailer chưa xác minh realtime. |
| 3 | Samsung Essential Monitor S3 `LS27D300GAEXXV` | [Samsung Vietnam spec](https://www.samsung.com/vn/monitors/full-hd-1080p/essential-monitor-s3-s30gd-27-inch-fhd-ips-100hz-ls27d300gaexxv/) | [TGDĐ 27-inch monitor list](https://www.thegioididong.com/man-hinh-may-tinh-27-inch) | Hãng có exact code, FHD, IPS, 100Hz, brightness/ports; retailer có product listing cùng code. | **Đã xác minh model và spec chính.** Có khả năng lấy cấu trúc từ hãng; giá/tồn cần feed hoặc crawl có phép. |
| 4 | Philips Evnia `27M2N2500NF/71` | [Philips Vietnam spec](https://www.philips.com.vn/c-p/27M2N2500NF_71/fast-ips-gaming-monitor-quad-hd-gaming-monitor) | [TGDĐ 27-inch monitor list](https://www.thegioididong.com/man-hinh-may-tinh-27-inch) | Hãng có suffix region `/71`, 27-inch QHD, 144Hz và 0.5ms Smart MBR; retailer có tên model 27M2N2500NF. | **Đã xác minh trang hãng cho SKU `/71`; retailer chỉ hiển thị tên model rút gọn, crosswalk chính xác tới `/71` chưa xác minh. Giữ suffix và không gộp biến thể khu vực khác. |
| 5 | Dell UltraSharp `U2725QE` | [Dell product spec](https://www.dell.com/en-us/shop/monitors/apd/dell-ultrasharp-27-4k-thunderbolt-hub-monitor-u2725qe/u2725qe_monitor/-) | [TGDĐ 27-inch monitor list](https://www.thegioididong.com/man-hinh-may-tinh-27-inch) | Hãng có Manufacturer Part Number và exact model; 27-inch 4K/Thunderbolt. Retailer có listing 27-inch 4K. | **Đã xác minh model hãng và retailer listing;** SKU/điện áp/bảo hành region Việt Nam cần đối chiếu trước khi map offer. |

### B. Thiết bị âm thanh — 5 model

| # | Model / định danh nhìn thấy | Nguồn hãng (spec/identity) | Nguồn retail/catalog | Chất lượng dữ liệu lấy được | Trạng thái & rủi ro |
|---:|---|---|---|---|---|
| 6 | Sony `WH-1000XM6` | [Sony Vietnam specifications](https://www.sony.com.vn/electronics/support/wireless-headphones-bluetooth-headphones/wh-1000xm6/specifications) | [TGDĐ tai nghe Bluetooth](https://www.thegioididong.com/tai-nghe-bluetooth), [tai nghe chụp tai](https://www.thegioididong.com/tai-nghe-chup-tai) | Hãng công bố pin ANC/off, Bluetooth, codec, trọng lượng, driver, mic; retail list có model và offer snapshot. | **Đã xác minh model/spec hãng.** Dữ liệu codec/tính năng phải map theo đúng firmware/market variant nếu có. |
| 7 | JBL `Live 780NC` | [JBL headphone category](https://www.jbl.com/headphones.html) | [TGDĐ tai nghe chụp tai](https://www.thegioididong.com/tai-nghe-chup-tai) | Retailer hiển thị exact product name, form factor và giá snapshot; trang danh mục hãng chưa nối được trực tiếp tới exact Vietnam SKU trong lần kiểm tra. | **Một phần đã xác minh.** Exact part number/market suffix và bảng spec chưa được chốt. |
| 8 | Apple `AirPods Pro 3` | [Apple AirPods Pro](https://www.apple.com/vn/airpods-pro/) | [TGDĐ tai nghe](https://www.thegioididong.com/tai-nghe) | Retailer có product line và listing; Apple công bố tính năng ở cấp sản phẩm nhưng không phải lúc nào cũng hiển thị SKU thương mại theo màu/bộ sạc. | **Một phần đã xác minh.** Cần exact part number theo màu/region/charging case; không map chỉ theo AirPods Pro 3. |
| 9 | Samsung Galaxy Buds4 Pro `R640N` | [Samsung Vietnam audio](https://www.samsung.com/vn/audio-sound/) | [TGDĐ tai nghe](https://www.thegioididong.com/tai-nghe) | Retailer hiển thị mã `R640N`; landing hãng theo dòng có thể cần chọn đúng country/variant. | **Một phần đã xác minh.** Chưa có product PDP hãng trả về đúng mã vùng trong lần kiểm tra; xác minh lại mã part. |
| 10 | Soundcore Liberty 5 Pro `D1203` | [Soundcore](https://www.soundcore.com/) | [TGDĐ tai nghe Bluetooth](https://www.thegioididong.com/tai-nghe-bluetooth) | Retailer hiện mã D1203 và tên sản phẩm; các thuộc tính marketing/ANC/call chưa có bản spec official đối chiếu cùng mã. | **Một phần đã xác minh.** Cần xác nhận exact D1203 product page, codec, mic, battery/ANC test conditions. |

### C. Máy lọc không khí — 5 model

| # | Model / định danh nhìn thấy | Nguồn hãng (spec/identity) | Nguồn retail/catalog | Chất lượng dữ liệu lấy được | Trạng thái & rủi ro |
|---:|---|---|---|---|---|
| 11 | Xiaomi Smart Air Purifier 4 Compact `AC-M18-SC` | [Xiaomi Vietnam specs](https://www.mi.com/vn/product/xiaomi-smart-air-purifier-4-compact/specs/) | [TGDĐ Xiaomi purifier list](https://www.thegioididong.com/may-loc-khong-khi-xiaomi) — listing có biến thể `BHR5860EU` | Hãng có area 16–27m², CADR 230m³/h, noise và exact AC-M18-SC. Retailer variant code BHR5860EU. | **Đã xác minh AC-M18-SC và record BHR5860EU tách biệt.** Chưa có crosswalk chính thức chứng minh hai mã cùng SKU; không gộp cho tới khi Xiaomi xác nhận. |
| 12 | Sharp `FX-S82V-B` | [Sharp Vietnam purifier catalog](https://vn.sharp/en/products/air-purifier) | [TGDĐ purifier catalog](https://www.thegioididong.com/may-loc-khong-khi) | Hãng có tên model, coverage area và filter claim; retailer có exact FX-S82V-B listing. | **Đã xác minh identity ở hai nguồn.** Cần thu thông số CADR/năng suất theo đúng điều kiện test, không suy từ diện tích đề xuất. |
| 13 | LG PuriCare 360 HIT `AS60GHHG0.ABAE` | [LG Vietnam product page](https://www.lg.com/vn/cham-soc-khong-khi/may-loc-khong-khi/as60ghhg0/) | [TGDĐ purifier catalog](https://www.thegioididong.com/may-loc-khong-khi) | Hãng có model name, model code, bộ lọc, sensor PM1.0/gas, filter replacement indicator và Wi-Fi; retailer listing ghi mã. | **Đã xác minh model/spec chính.** Cần map đúng bộ lọc thay thế và phiên bản `AS60GHHG0.ABAE`/tên thương mại. |
| 14 | Sharp `FP-J80EV-H` | [Sharp Vietnam purifier catalog](https://vn.sharp/en/products/air-purifier) | [TGDĐ purifier catalog](https://www.thegioididong.com/may-loc-khong-khi) | Hãng hiển thị 99.97% capture claim cho 0.3μm, ion density và recommended area; retailer có listing FP-J80EV-H. | **Đã xác minh identity/claim hãng.** Không diễn giải claim capture thành hiệu suất CADR; cần tìm phương pháp thử. |
| 15 | Philips `AC1715/20` Series 1000i | [Philips Vietnam air purifier catalog](https://www.philips.com.vn/c-m-ho/climate-care/air-purifier/latest) | Retailer-specific listing trong mẫu này chưa xác minh trực tiếp | Hãng công bố area up to 78m², CADR 300m³/h, HEPA/carbon, app Air+. | **Đã xác minh official model/spec overview.** Retail availability/price/affiliate link chưa xác minh. |

### D. Laptop — 5 model / configuration

| # | Model / định danh nhìn thấy | Nguồn hãng (spec/identity) | Nguồn retail/catalog | Chất lượng dữ liệu lấy được | Trạng thái & rủi ro |
|---:|---|---|---|---|---|
| 16 | HP 240R G10 `C3RU7AT` | [HP Vietnam laptops](https://www.hp.com/vn-en/shop/) | [TGDĐ laptop catalog](https://www.thegioididong.com/laptop) | Retailer hiển thị product family, `C3RU7AT`, RAM 16GB/SSD 512GB ở bản snapshot. | **Một phần đã xác minh.** Chưa nối được exact HP SKU PDP/spec sheet tại Việt Nam trong lần kiểm tra; không map theo tên 240R G10 thôi. |
| 17 | ASUS Vivobook S14 `S3407VA` / `LY146W` | [ASUS Vietnam laptops](https://www.asus.com/vn/laptops/) | [TGDĐ laptop catalog](https://www.thegioididong.com/laptop), [TGDĐ slim-light list](https://www.thegioididong.com/laptop?g=mong-nhe-thoi-trang&p=20-25-trieu) | Retailer hiển thị exact reseller SKU `LY146W`, CPU Core 5 210H, RAM 16GB/SSD 512GB trên snapshot. | **Một phần đã xác minh.** `LY146W` là cấu hình/part number; cần full ASUS P/N và xác nhận RAM soldered, screen, OS/warranty. Không nhầm với S5406SA. |
| 18 | Dell Inspiron 14 5440 `NDY5V1` | [Dell support/product](https://www.dell.com/support/home/en-vn) | [HACOM exact product page](https://hacom.vn/laptop-ai-dell-inspiron-14-5440-ndy5v1) | Retailer có exact code, CPU/RAM/SSD/display/OS/price snapshot và order status. | **Đã xác minh retailer SKU/spec listing.** Chưa đối chiếu Dell service tag/region part number; ghi rõ trạng thái đặt trước trên retailer snapshot. |
| 19 | MacBook Air 13-inch M4 `16GB / 256GB` | [Apple MacBook Air](https://www.apple.com/vn/macbook-air/) | [Mac Center product/config page](https://www.maccenter.vn/MacBookAir-13-M4-256GB-16GB.aspx), [TGDĐ MacBook Air](https://www.thegioididong.com/laptop-apple-macbook-air) | Retailer tách cấu hình RAM/SSD; có CPU/GPU, display/ports ở trang sản phẩm. | **Đã xác minh configuration listing.** Đây là cấu hình thương mại, không thay cho SKU/part number region; bảo hành và adapter bundle phải lấy theo order code. |
| 20 | Lenovo V14 Gen 5 `83HD005JVN` | [Lenovo PSREF](https://psref.lenovo.com/) | [Hanoinew filtered list](https://hanoinew.vn/laptop-may-tinh-xach-tay?filter=22-969-972-984&max=25000000&min=20000000) | Retailer hiển thị machine type `83HD005JVN`, CPU, RAM, SSD, display, battery, weight và OS. | **Đã xác minh retailer model code/spec listing.** Cần xác nhận Lenovo PSREF row trùng đúng `83HD005JVN`, không chỉ product family V14 Gen 5. |

### 7.2. Đánh giá chất lượng của mẫu 20 model

| Hạng mục | Kết quả mẫu | Nhận xét |
|---|---|---|
| Có exact model code/identifier ở nguồn retail hoặc hãng | Phần lớn có; một số tên/audio configuration mới chỉ là product line | Laptop và audio cần chuẩn hóa code mạnh nhất; không dùng fuzzy name match để nối feed |
| Có nguồn hãng chứa spec | Rất tốt ở màn hình/máy lọc; có Sony audio; laptop có thể dùng PSREF/part number nhưng cần map từng configuration | Manufacturer PIM/spec page nên là source of truth cho specs, không phải giá |
| Có nguồn retailer để lấy giá/offer/listing | Có cho 20 mẫu ở dạng category/PDP snapshot, nhưng không phải lúc nào cũng là direct product URL | Giá, promo, stock là dynamic fields; phải lưu `observed_at` và kiểm tra checkout hoặc API feed |
| SKU / regional variant risk | Cao: Xiaomi A27i 2026 vs model ID trang cũ; AC-M18-SC vs BHR5860EU; laptop part number và adapter/OS; audio color/region code | Bắt buộc xây crosswalk: manufacturer model → region P/N → retailer SKU → affiliate product ID |
| API/feed runtime | Chưa test | Tất cả 20 mẫu mới là sample từ website công khai; chưa được tính là proof of automated feed |

## 8. Thiết kế catalog và kiểm thử dữ liệu tiếp theo

### 8.1. Bản ghi tối thiểu cần lưu cho mỗi sản phẩm

`canonical_model_id`, `brand`, `category`, `marketing_name`, `manufacturer_model_code`, `regional_part_number`, `retailer_sku`, `variant_attributes`, `spec_source_url`, `retailer_source_url`, `affiliate_network`, `affiliate_product_id`, `tracking_url`, `price`, `sale_price`, `currency`, `stock_status`, `commission_rate`, `currency/commission_basis`, `observed_at`, `source_updated_at`, `data_source`, `confidence`, `verification_status`.

### 8.2. Luật ghép canonical product

- Exact model/part number là khóa chính nếu nhà sản xuất công bố; không nối chỉ dựa trên tên marketing.
- Laptop: khóa phải bao gồm machine type/part number + CPU + RAM + SSD + GPU/display nếu các trường làm thay đổi cấu hình bán.
- Monitor: khóa gồm model code + suffix khu vực + panel/resolution/refresh nếu có biến thể đáng kể.
- Air purifier: khóa gồm model code + region SKU; filter/consumable phải là entity riêng có quan hệ compatibility rõ.
- Audio: khóa gồm model code + form factor + color/region; không map sản phẩm ANC over-ear sang TWS cùng tên dòng.
- Affiliate product ID không bao giờ là canonical ID; một canonical product có thể có nhiều offer/merchant/affiliate links.

### 8.3. Kế hoạch kiểm thử với Hoàng (chưa thực hiện)

1. Xin sample datafeed/Publisher API access chính thức từ ACCESSTRADE sau khi CEO phê duyệt.
2. Chạy 20 model mẫu: tìm product title/model ID/merchant/price/stock/commission/tracking URL; lưu nguyên payload và timestamp.
3. So với manufacturer source và retailer listing cùng giờ; đo `exact_model_match_rate`, `required_spec_coverage`, `price_match_rate`, `stock_match_rate`, `missing_commission_rate`, `duplicate_offer_rate`.
4. Chạy lại sau 24 giờ và 7 ngày để đo freshness và thay đổi ID/price/stock.
5. Không scrape hoặc giữ ảnh/giá hàng loạt khi chưa kiểm tra Terms of Service, robots/rate limits và quyền sử dụng dữ liệu. Feed API được cấp phép là phương án ưu tiên.

## 9. Rủi ro, thiếu dữ liệu và việc cần quyết định

| Vấn đề | Vì sao quan trọng | Trạng thái hiện tại | Chủ sở hữu phối hợp |
|---|---|---|---|
| Google Trends CSV chưa có | Không có bằng chứng search interest 5y; chưa đo seasonality | Chưa hoàn tất | Trâm Anh (export), CEO quyết định cần thêm Ads Keyword Planner hay không |
| SERP Google geo/device chưa capture | Chưa kết luận organic competition, top-10 domains hoặc SERP features | Sơ bộ | Trâm Anh; có thể nhờ Hoàng hỗ trợ browser/screenshot nếu có công cụ hợp lệ |
| Website eligibility Shopee Short-tail | Có điều kiện doanh nghiệp và quyền duyệt riêng; cần classification cho A+ | Chưa được network xác nhận | CEO/pháp nhân + Trâm Anh làm việc với Shopee sau phê duyệt |
| Lazada/MasOffer current publisher terms | Không đủ bằng chứng cập nhật 2026 và product feeds | Chưa xác minh | Trâm Anh |
| AT campaign/category list, commission/cookie | Các thông tin này quyết định business case affiliate | Chưa đăng nhập/test | CEO duyệt account; Trâm Anh thu thập |
| Retailer feeds/API | Chưa có public contractual access | Chưa xác minh | Hoàng + Trâm Anh |
| SKU mapping | Một số tên/model variant chưa map | Mẫu ban đầu đã phát hiện mismatch | Hoàng (canonical mapping) + A Long (spec) |
| Dùng nội dung chuyên môn trong tư vấn | Tránh đánh giá sai claim/spec/test | Chưa thẩm định toàn bộ | A Long |
| Use-case/persona và intent | Tránh tự giả định nhu cầu/từ khóa của khách hàng | Chưa có khảo sát định lượng trong PILOT-05 | Vân Anh |
| Phân loại pháp lý A+ | Quy định có hiệu lực từ 01/07/2026; cần phân biệt publisher với service provider/platform | Cần tư vấn pháp lý | CEO/pháp chế |

## 10. Đề xuất bước tiếp theo (không phải quyết định chọn ngành)

1. **Đóng Google Trends:** người có quyền thao tác trình duyệt export 4 CSV theo link ở Mục 3; sau đó bổ sung biểu đồ monthly index, YoY và seasonality. Không để trống này bị thay bằng số liệu suy diễn.
2. **Làm SERP audit thật:** mở 8 query trong Google Search bằng chế độ ẩn danh, khu vực Việt Nam, ghi ngày/thiết bị/locale, chụp top 10 organic + shopping/ads/AI Overview/Video, domain, loại trang, title và vị trí. Làm thêm 2 truy vấn long-tail theo từng ngành khi đã nhận keyword intent từ Vân Anh.
3. **Xác minh affiliate bằng email/tài liệu:** gửi câu hỏi đến ACCESSTRADE về publisher website/comparison, campaign electronics, feed field/cadence/rights; gửi Shopee về Short-tail criteria và có chấp nhận website A+ không; yêu cầu bản terms 2026 từ Lazada và MasOffer.
4. **Kiểm thử 20 model qua feed:** chỉ sau khi CEO duyệt quyền truy cập; lấy exact offers, không lấy hoa hồng làm tiêu chí ưu tiên sản phẩm.
5. **Họp liên phòng ban:** Vân Anh xác nhận search/use-case intent; A Long rà spec và các điểm trade-off; Hoàng đánh giá ingestion/dedupe/freshness; Trâm Anh tổng hợp bằng chứng; CEO quyết định có tiếp tục pilot/ngành nào.
6. **Rà pháp lý:** xin ý kiến tư vấn về entity classification, disclosure affiliate, thuế/hóa đơn, chính sách dữ liệu, dùng hình ảnh/spec/giá và việc cung cấp thông tin khi cơ quan quản lý yêu cầu.

## 11. Danh mục nguồn và ngày kiểm tra

Ngày kiểm tra link: **12/11/2026** trừ khi ghi riêng trong nguồn. Tin cậy cao = văn bản/website chính hãng; trung bình = retailer/analytics/research vendor; thấp = nguồn chưa có tài liệu/phiên bản hiện hành.

| ID | Nguồn | URL | Ngày / tình trạng | Tin cậy |
|---|---|---|---|---|
| T1 | Google Trends — FAQ dữ liệu, sampling và normalization | https://support.google.com/trends/answer/4365533?hl=vi | Kiểm tra 12/11/2026; đã xem | Cao |
| T2 | Google Trends — export CSV/cite data | https://support.google.com/trends/answer/4365538?hl=en | Kiểm tra 12/11/2026; đã xem | Cao |
| T3 | Google Trends — Explore link 5y Màn hình | Link ở Mục 3 | Prepared 12/11/2026; CSV chưa export | Cao về cấu hình; thấp về metric |
| T4 | Google Trends — Explore link 5y Audio | Link ở Mục 3 | Prepared 12/11/2026; CSV chưa export | Cao về cấu hình; thấp về metric |
| T5 | Google Trends — Explore link 5y Máy lọc không khí | Link ở Mục 3 | Prepared 12/11/2026; CSV chưa export | Cao về cấu hình; thấp về metric |
| T6 | Google Trends — Explore link 5y Laptop | Link ở Mục 3 | Prepared 12/11/2026; CSV chưa export | Cao về cấu hình; thấp về metric |
| S1 | Metric — màn hình monitor | https://metric.vn/ereport/man-hinh-monitor | Dữ liệu 2025; baseline v1.0; trích đoạn công khai | Trung bình |
| S2 | Metric — máy lọc không khí | https://metric.vn/ereport/may-loc-khong-khi | Dữ liệu 2025; baseline v1.0; trích đoạn công khai | Trung bình |
| S3 | Metric — tai nghe | https://metric.vn/ereport/tai-nghe | Dữ liệu 2025; baseline v1.0; trích đoạn công khai | Trung bình |
| S4 | Metric — máy tính/laptop/thiết bị văn phòng | https://metric.vn/ereport/nganh-hang-may-tinh-laptop-thiet-bi-van-phong | Dữ liệu 2025; nhóm rộng | Trung bình |
| S5 | Bộ Công Thương — báo cáo thị trường nội địa 2025 | https://dms.gov.vn/documents/d/guest/bc-ttnd-2025-pdf | Báo cáo 2025; baseline v1.0 | Cao |
| S6 | YouNet ECI — TMĐT Việt Nam H1/2026 | https://youneteci.com/vi/bao-cao-toan-canh-tmdt-viet-nam-nua-dau-nam-2026/ | H1/2026; baseline v1.0 | Trung bình–cao |
| R1 | TGDĐ — màn hình 27 inch | https://www.thegioididong.com/man-hinh-may-tinh-27-inch | Search result cache khoảng 3 tuần; kiểm tra 12/11 | Trung bình |
| R2 | TGDĐ — tai nghe Bluetooth | https://www.thegioididong.com/tai-nghe-bluetooth | Search result cache khoảng 3 tuần; kiểm tra 12/11 | Trung bình |
| R3 | TGDĐ — tai nghe chụp tai | https://www.thegioididong.com/tai-nghe-chup-tai | Search result; kiểm tra 12/11 | Trung bình |
| R4 | TGDĐ — máy lọc không khí | https://www.thegioididong.com/may-loc-khong-khi | Search result cache khoảng 3 tuần; kiểm tra 12/11 | Trung bình |
| R5 | TGDĐ — laptop | https://www.thegioididong.com/laptop | Search result cache khoảng 3 tuần; kiểm tra 12/11 | Trung bình |
| R6 | Hanoinew — laptop 20–25 triệu | https://hanoinew.vn/laptop-may-tinh-xach-tay?filter=22-969-972-984&max=25000000&min=20000000 | Search result; kiểm tra 12/11 | Trung bình |
| R7 | Sintech — laptop 20–25 triệu | https://sintech.vn/collections/laptop-20-25-trieu | Trang kết quả cập nhật 10/11/2026 hiển thị; kiểm tra 12/11 | Trung bình |
| R8 | Sogia — so sánh laptop | https://sogia.com.vn/laptop/trang-2 | Trang hiển thị cập nhật giá 11/11; kiểm tra 12/11 | Trung bình |
| R9 | Bếp Xanh — máy lọc không khí | https://bepxanh.com/may-loc-khong-khi/ | Trang sản phẩm/danh mục; kiểm tra 12/11 | Trung bình |
| M1 | Xiaomi Monitor A27i specs | https://www.mi.com/vn/product/xiaomi-monitor-a27i/specs/ | Kiểm tra 12/11; model code P27FBA-RAGL | Cao |
| M2 | ASUS TUF VG27AQE5A | https://www.asus.com/displays-desktops/monitors/tuf-gaming/tuf-gaming-vg27aqe5a/ | Kiểm tra 12/11 | Cao |
| M3 | Samsung S3 LS27D300GAEXXV | https://www.samsung.com/vn/monitors/full-hd-1080p/essential-monitor-s3-s30gd-27-inch-fhd-ips-100hz-ls27d300gaexxv/ | Kiểm tra 12/11 | Cao |
| M4 | Philips Evnia 27M2N2500NF/71 | https://www.philips.com.vn/c-p/27M2N2500NF_71/fast-ips-gaming-monitor-quad-hd-gaming-monitor | Kiểm tra 12/11 | Cao |
| M5 | Dell U2725QE | https://www.dell.com/en-us/shop/monitors/apd/dell-ultrasharp-27-4k-thunderbolt-hub-monitor-u2725qe/u2725qe_monitor/- | Kiểm tra 12/11; market PDP US, cần mapping region VN | Cao về model; trung bình về VN offer |
| A1 | Sony WH-1000XM6 specs | https://www.sony.com.vn/electronics/support/wireless-headphones-bluetooth-headphones/wh-1000xm6/specifications | Kiểm tra 12/11 | Cao |
| A2 | JBL product catalog | https://www.jbl.com/headphones.html | Kiểm tra 12/11; exact VN SKU chưa map | Trung bình |
| A3 | Apple AirPods Pro | https://www.apple.com/vn/airpods-pro/ | Kiểm tra 12/11; exact reseller configuration cần mapping | Cao về official family |
| A4 | Samsung audio catalog | https://www.samsung.com/vn/audio-sound/ | Kiểm tra 12/11; exact Buds4 Pro SKU chưa mở đúng PDP | Trung bình |
| A5 | Soundcore official catalog | https://www.soundcore.com/ | Kiểm tra 12/11; D1203 chưa map đến exact official PDP | Trung bình–thấp |
| P1 | Xiaomi Air Purifier 4 Compact specs | https://www.mi.com/vn/product/xiaomi-smart-air-purifier-4-compact/specs/ | Kiểm tra 12/11; AC-M18-SC | Cao |
| P2 | Sharp Vietnam air purifier catalog | https://vn.sharp/en/products/air-purifier | Kiểm tra 12/11; có FX-S82V-B và FP-J80EV-H | Cao |
| P3 | LG PuriCare AS60GHHG0 | https://www.lg.com/vn/cham-soc-khong-khi/may-loc-khong-khi/as60ghhg0/ | Kiểm tra 12/11; exact product code/variant | Cao |
| P4 | Philips air purifier catalog | https://www.philips.com.vn/c-m-ho/climate-care/air-purifier/latest | Kiểm tra 12/11; AC1715/20 và một số model series | Cao |
| L1 | ASUS Vivobook S14 S5406 / S3407 family | https://www.asus.com/vn/laptops/ | Kiểm tra 12/11; cần phân biệt S5406 vs S3407 và P/N | Cao về hãng; trung bình về SKU chưa nối |
| L2 | Dell Inspiron 14 5440 NDY5V1 retailer sample | https://hacom.vn/laptop-ai-dell-inspiron-14-5440-ndy5v1 | Kiểm tra 12/11 | Trung bình–cao |
| L3 | MacBook Air M4 13 16/256 retailer sample | https://www.maccenter.vn/MacBookAir-13-M4-256GB-16GB.aspx | Kiểm tra 12/11 | Trung bình–cao |
| L4 | Lenovo PSREF | https://psref.lenovo.com/ | Kiểm tra 12/11; cần exact row/machine type match | Cao về official PSREF |
| L5 | Lenovo V14 Gen 5 retailer sample | https://hanoinew.vn/laptop-may-tinh-xach-tay?filter=22-969-972-984&max=25000000&min=20000000 | Kiểm tra 12/11 | Trung bình |
| AF1 | ACCESSTRADE terms — Publisher definition | https://merchant.accesstrade.me/dieu-khoan/ | Kiểm tra 12/11 | Cao |
| AF2 | ACCESSTRADE Publisher FAQ — IDs, website, API, cookie | https://help.accesstrade.vn/faq-publisher/ | Kiểm tra 12/11 | Cao về tài liệu; campaign-specific cần xác minh |
| AF3 | ACCESSTRADE Publisher API docs | https://developers.accesstrade.vn/api-publisher-vietnamese | Tài liệu báo Last updated 6 days; kiểm tra 12/11 | Cao về API docs; chưa test runtime |
| AF4 | Shopee Affiliate T&C updated 15/09/2026 | https://help.shopee.vn/portal/10/article/206429?previousPage=other+articles | Cập nhật 15/09/2026; kiểm tra 12/11 | Cao |
| AF5 | Lazada affiliate support | https://pages.lazada.vn/wow/i/vn/corp/affiliate-support?hybrid=1 | Kiểm tra baseline; current terms/cookie 2026 chưa xác minh | Trung bình–thấp |
| AF6 | MasOffer Publisher API portal | https://publisher-api.masoffer.net/docs/ | Portal tồn tại; schema/campaign chưa xác minh | Thấp–trung bình |
| LEG1 | Luật TMĐT 122/2025/QH15 — Cổng văn bản Chính phủ | https://vanban.chinhphu.vn/?classid=1&docid=216503&pageid=27160&typegroupid=3 | Ban hành 10/12/2025; hiệu lực 01/07/2026 | Cao |
| LEG2 | Nghị định 248/2026/NĐ-CP — Cổng văn bản Chính phủ | https://vanban.chinhphu.vn/?docid=218747&orggroupid=2&pageid=27160 | Ban hành 30/06/2026; hiệu lực 01/07/2026 | Cao |
| LEG3 | Cục TMĐT — thông báo triển khai 14/10/2026 | https://www.idea.gov.vn/default.aspx?category_id=6e3f3b28-3917-4816-83c5-a331259dd181&do=detail&id=184e0d3f-daab-42a5-a33e-782c78e579c0&page=news | Ngày 14/10/2026; kiểm tra 12/11 | Cao |
| LEG4 | Luật Quảng cáo sửa đổi 75/2025/QH15 — Cổng văn bản Chính phủ | https://vanban.chinhphu.vn/?classid=1&docid=214561&pageid=27160 | Ban hành 16/06/2025; hiệu lực 01/01/2026 | Cao về văn bản/hiệu lực |
| LEG5 | Bản tra cứu Luật Quảng cáo sửa đổi — quy định nhận diện quảng cáo trực tuyến | https://thuvienphapluat.vn/van-ban/thuong-mai/law-75-2025-qh15-amendments-to-certain-articles-of-the-law-on-advertising-671036.aspx?temp=d | Kiểm tra 12/11/2026; nguồn thứ cấp để tra cứu điều khoản | Trung bình–cao |
| AF7 | TikTok Shop — Apply as Affiliate Creator (VN) | https://seller-vn.tiktok.com/university/essay?knowledge_id=6837838528808705&lang=en | Bản tài liệu creator kiểm tra baseline v1.0; không đồng nhất publisher website | Cao về chương trình creator |

---

**Kết luận bàn giao PILOT-05:** Đã xác minh được đường publisher website/API qua ACCESSTRADE, đường Short-tail có điều kiện của Shopee, ba văn bản pháp lý có liên quan và 20 mẫu model từ nguồn hãng/retailer. SERP đã được khảo sát sơ bộ theo truy vấn mua hàng. **Chưa thể kết luận search demand 5 năm vì chưa có CSV Google Trends; cũng chưa xác minh commission/cookie/campaign điện tử theo SKU, API runtime, retailer feed hay conversion data.** Không chọn ngành hàng thay CEO.
