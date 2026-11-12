# A+ — Catalog Evidence QA v1

> **DRI:** A Long — Product Expert  
> **Issue:** [PILOT-04 / #8](https://github.com/anhnv14994/web-aff/issues/8)  
> **Ngày kiểm tra nguồn:** 12/11/2026 (Asia/Ho_Chi_Minh)  
> **Phạm vi:** 5 màn hình + 5 tai nghe chụp tai trong shortlist PILOT-02  
> **Trạng thái:** Evidence QA v1 — tài liệu chuyên môn đã lập; dữ liệu retail/local còn các trường pending  
> **Quyết định MVP:** Không thuộc phạm vi; tài liệu này không chọn ngành hàng thương mại.

---

## 1. Tóm tắt và kết quả kiểm tra

Đã rà soát 10 model theo nguồn nhà sản xuất/đơn vị hỗ trợ chính hãng và nguồn thử nghiệm độc lập có thể gắn đúng model. Các thay đổi quan trọng so với shortlist trước:

1. **ASUS TUF Gaming VG27AQ3A:** đã tìm được trang thông số chính hãng ASUS Việt Nam. Trang ghi 180Hz tối đa qua DisplayPort và giới hạn tín hiệu dọc HDMI đến 144Hz; không được gắn 180Hz cho mọi cổng.
2. **Sennheiser MOMENTUM 4 Wireless:** đã tìm được trang chính hãng Việt Nam và danh sách SKU màu: Black 509266, White 509267, Graphite 700383. Trang Support còn liệt kê các SKU màu khác.
3. **Bose QuietComfort Ultra Headphones:** nguồn Bose phân biệt phiên bản đầu tiên (sản phẩm bán từ 2023) với 2nd Gen (bán từ 2025). Pilot giữ **đời 1 / 2023**, không gộp thông số đời 2.
4. **JBL Tour One M2:** trang JBL chính thức xác nhận Item# JBLTOURONEM2BAM cho biến thể đen; thông số Bluetooth 5.3, thời lượng pin tối đa 50h ANC off / 30h ANC on. Có điểm cần QA về cách diễn đạt số microphone: mô tả sản phẩm nói “4-mic technology”, bảng thông số ghi “Number of Microphones: 7”; không được gộp hai trường này.
5. **Apple AirPods Max USB-C:** Apple xác định model number **A3184**, đời AirPods Max 1 USB-C ra mắt 2024. Không phải AirPods Max 2 (A3454, 2026) và không phải AirPods Max 1 Lightning (A2096, 2020).
6. Đã tìm được test độc lập khớp chính xác cho ASUS PA279CRV, Sony WH-1000XM5, Sennheiser MOMENTUM 4 và Bose QuietComfort Ultra đời đầu. Với AirPods Max USB-C, bài test RTINGS công khai hiện dùng bản Lightning; chính RTINGS ghi chưa test bản USB-C. Không chuyển kết quả Lightning sang A3184. Với các màn hình/tai nghe còn lại, không tìm thấy bài thử độc lập khớp chính xác trong lượt tra cứu này; trạng thái giữ pending thay vì mượn kết quả model gần tên.

**Không xác nhận:** giá, hàng tồn, SKU của nhà bán Việt Nam, đơn vị bảo hành, affiliate eligibility hay điều kiện thương mại. Đây là những lớp dữ liệu riêng thuộc Retail Offer/Operations.

## 2. Quy ước trạng thái evidence

| Trạng thái | Ý nghĩa | Được phép dùng thế nào |
|---|---|---|
| **verified** | Nhận diện model/generation/mã SKU được nguồn trực tiếp xác nhận; hoặc một dữ kiện định danh rõ ràng đã được đối chiếu chéo | Dùng cho identity trong phạm vi được chứng minh; không suy ra retail offer |
| **manufacturer-claimed** | Thông số hoặc tính năng do chính hãng công bố | Hiển thị như “theo thông số hãng”; không gọi là phép đo độc lập |
| **independent-tested** | Có kết quả thử nghiệm độc lập khớp đúng model/variant và phương pháp/phiên bản test được ghi lại | Chỉ áp dụng đúng mẫu test, điều kiện và phiên bản phương pháp |
| **pending** | Thiếu nguồn, thiếu đúng variant, chưa có P/N/region, hoặc chưa tìm thấy test độc lập khớp | Giữ null/unknown; không điền theo model tương tự |
| **conflicting** | Hai nguồn/claim có vẻ mâu thuẫn hoặc cùng nhãn nhưng khác phạm vi/điều kiện | Chặn kết luận cho đến khi phân giải; lưu nguyên văn hai claim |

Một field có thể có đồng thời hai dòng evidence: ví dụ “manufacturer-claimed” và “independent-tested”. Không ghi đè kết quả đo độc lập bằng thông số quảng cáo, cũng không coi thông số hãng là vô giá trị; phải giữ riêng nguồn và điều kiện.

### Confidence

- **High:** nguồn chính hãng/chuẩn hoặc test độc lập gắn đúng model, đúng trường, có phạm vi rõ.
- **Medium:** nguồn có thẩm quyền nhưng giới hạn theo vùng, màu/SKU, điều kiện đo hoặc scope.
- **Low:** nguồn gián tiếp, không rõ model/variant hoặc có nhiều bước suy luận.
- **Pending:** chưa đủ căn cứ để gán confidence.

## 3. Identity register — 10 model

### 3.1. Màn hình

| ID | Canonical model / tên chính hãng | Generation / suffix / variant đã xác định | Mã nhà sản xuất / SKU được nguồn xác nhận | Identity status | Retail SKU / Vietnam P/N |
|---|---|---|---|---|---|
| MON-01 | **LG 27GS85Q-B** | Model code đầy đủ gồm suffix “-B”; trang LG Việt Nam dùng đúng chuỗi này. Không tự diễn giải suffix thành một biến thể panel khác. | Manufacturer model name: 27GS85Q-B | verified | pending — trang thông số không xác nhận mã retailer/offer cụ thể |
| MON-02 | **ASUS ProArt Display PA279CRV** | Model 27-inch 4K; không gộp PA329CRV 32-inch hoặc PA279CV. | Manufacturer model: PA279CRV | verified | pending — cần mã P/N theo lô/nhà bán |
| MON-03 | **BenQ GW2790Q** | Model 27-inch QHD; không gộp GW2790 hoặc model GW khác. | Manufacturer model: GW2790Q | verified | pending — trang spec không đưa mã retail SKU cụ thể |
| MON-04 | **BenQ MA270U** | Model Mac/productivity 27-inch 4K; phân biệt MA270U với MA270S (5K/70Hz) và MA270UP (4K nhưng lớp phủ khác theo bảng so sánh RTINGS). | Manufacturer model: MA270U | verified | pending — không dùng P/N của MA270S/MA270UP |
| MON-05 | **ASUS TUF Gaming VG27AQ3A** | Model code là VG27AQ3A; không gộp VG27AQ, VG27AQ1A hoặc VG27AQL1A. | Manufacturer model: TUF Gaming VG27AQ3A | verified | pending — ASUS ghi thông số có thể khác theo mã sản phẩm/vùng |

### 3.2. Tai nghe chụp tai

| ID | Canonical model / tên chính hãng | Generation / suffix / variant đã xác định | Mã nhà sản xuất / SKU được nguồn xác nhận | Identity status | Retail SKU / Vietnam P/N |
|---|---|---|---|---|---|
| AUD-01 | **Sony WH-1000XM5** | Dòng XM5, ra mắt giữa năm 2022 theo hồ sơ test độc lập; không gộp WH-1000XM4 hoặc XM6. | Manufacturer model: WH-1000XM5 | verified | pending — màu/retail package code chưa được chốt trong pilot |
| AUD-02 | **Sennheiser MOMENTUM 4 Wireless** | Generation M4; trang Việt Nam ghi các SKU màu: Black 509266, White 509267, Graphite 700383. Trang Support còn liệt kê Brown 800074, Teal 800073, Copper 800108, Denim 800109. | SKU color-specific do Sennheiser công bố | verified | verified đối với các SKU màu trên trang hãng; vẫn pending đối với P/N/offer của từng retailer Việt Nam |
| AUD-03 | **Bose QuietComfort Ultra Headphones (1st Gen / đời 2023)** | Bose Support ghi sản phẩm bán từ 2023; Bose phân biệt rõ đời 1 với QuietComfort Ultra Headphones (2nd Gen) bán từ 2025. Trong catalog phải giữ tên đời 1 rõ ràng. | Product family/support identifier QCUH-HEADPHONEARN xuất hiện trong Bose product assets; không coi mã family này là retail P/N | verified cho generation; pending cho P/N màu/thị trường | pending |
| AUD-04 | **JBL Tour One M2** | Dòng Tour One, model M2; không gộp Tour One M3 hoặc Tour Pro earbuds. | JBL Item# **JBLTOURONEM2BAM** được xác nhận cho biến thể đen trên JBL.com | verified cho model + Item# biến thể đen | pending đối với màu/retailer SKU khác và Vietnam warranty P/N |
| AUD-05 | **Apple AirPods Max 1 (USB-C)** | Đời 1 USB-C ra mắt 2024; model number **A3184**. Phân biệt AirPods Max 1 Lightning **A2096** (2020) và AirPods Max 2 **A3454** (2026). | Manufacturer model number A3184 | verified | pending — cần nhà bán xác nhận part/region SKU; không lấy mã Lightning |

### Identity gate

- Nếu chỉ biết “PA279CRV”/“WH-1000XM5” nhưng offer ghi tên chung, không được tự điền suffix, màu hoặc region.
- SKU màu Sennheiser và Item# JBL là mã product/variant chính hãng, không phải bằng chứng SKU đang được một retailer Việt Nam bán.
- Apple A3184 là model number của tai nghe, không phải số serial và không phải mã offer.
- Bose product family identifier không thay thế serial/model/retail part number. Nếu không đọc được nhãn trên tai nghe/hộp hoặc part number chính hãng, giữ retail P/N pending.
- Canonical model và Retail Offer phải là hai record khác nhau.

## 4. Evidence register theo thuộc tính

Ngày truy cập các trang dưới đây: **12/11/2026**. “Manufacturer-claimed” luôn chỉ claim được hãng công bố, không phải kết quả đo do A Long thực hiện.

### 4.1. Màn hình

#### MON-01 — LG 27GS85Q-B

| Field | Giá trị được nguồn công bố | Evidence / status | Giới hạn |
|---|---|---|---|
| Model identity | 27GS85Q-B | E-M01 / verified | Retail P/N vẫn pending |
| Panel / resolution | 27-inch Nano IPS, QHD 2560×1440 | E-M01 / manufacturer-claimed | Không tự suy ra panel lot/revision |
| Refresh rate | 180Hz; 200Hz chỉ ở chế độ O/C | E-M01 / manufacturer-claimed | 200Hz cần GPU hỗ trợ DP 1.4 và cáp DP 1.4; không ghi “200Hz native” |
| Response | 1ms GtG | E-M01 / manufacturer-claimed | LG ghi cần chọn Faster response mode; chưa phải kết quả đo độc lập |
| Color/HDR | DCI-P3 98% typical (minimum 90% được ghi chú); DisplayHDR 400 claim | E-M01 / manufacturer-claimed | Gamut coverage không phải color accuracy; đối chiếu VESA certification registry trước khi dùng logo/claim trong nội dung |
| Independent test | Chưa tìm thấy review độc lập trùng chính xác 27GS85Q-B trong lượt tra cứu này | pending | Không dùng test của 27GS95QE/27GP850 hoặc model UltraGear gần tên |

#### MON-02 — ASUS ProArt Display PA279CRV

| Field | Giá trị được nguồn công bố | Evidence / status | Giới hạn |
|---|---|---|---|
| Model identity | ProArt Display PA279CRV, 27-inch | E-M02 / verified | Không gộp PA329CRV hoặc PA279CV |
| Display | 4K 3840×2160 IPS/WLED, 60Hz, 5ms GtG | E-M02 / manufacturer-claimed | Không suy ra 5ms tương đương các method khác |
| Color | 100% sRGB, 99% Adobe RGB, 99% DCI-P3; factory-calibrated claim ΔE<2; Calman Verified | E-M02 / manufacturer-claimed | Gamut và color accuracy là hai field riêng; cần báo cáo calibration nếu xuất bản độ chính xác theo điều kiện cụ thể |
| Brightness/HDR | 350 cd/m² typical; 400 cd/m² HDR peak; HDR10 input support và VESA DisplayHDR 400 được liệt kê | E-M02 / manufacturer-claimed | HDR10 signal support không thay thế VESA DisplayHDR tier hoặc phép đo HDR thực tế |
| USB-C / ports | USB-C DP Alt Mode; PD 96W; DP 1.4 daisy-chain; HDMI 2.0 | E-M02 / manufacturer-claimed | 96W PD là công suất cấp nguồn hãng công bố; kiểm tra host/cáp và mode hoạt động trước khi cam kết tương thích |
| Independent test | RTINGS review khớp PA279CRV; test bench v2.1.2 cập nhật 17/03/2026 | E-M03 / independent-tested | RTINGS nêu unit 27-inch PA279CRV; kết quả không áp dụng cho PA329CRV/PA279CV. Kết quả HDR và contrast được review đánh giá hạn chế; xem review gốc trước khi dùng số đo |

#### MON-03 — BenQ GW2790Q

| Field | Giá trị được nguồn công bố | Evidence / status | Giới hạn |
|---|---|---|---|
| Model identity | GW2790Q, 27-inch | E-M04 / verified | Không gộp GW2790 hoặc model cùng series |
| Display | IPS, QHD 2560×1440, 350 nits typical, 100Hz | E-M04 / manufacturer-claimed | Các giá trị là thông số hãng công bố |
| Response | 5ms GtG và 1ms MPRT được liệt kê thành hai trường | E-M04 / manufacturer-claimed | Không chuẩn hóa về một trường “response_time=1ms”; MPRT không thay thế GtG |
| Color | 99% sRGB | E-M04 / manufacturer-claimed | Coverage không chứng minh Delta E hoặc đồng đều màu |
| Independent test | Chưa tìm thấy review độc lập khớp đúng GW2790Q | pending | Không dùng review GW2790/GW2790T hoặc model QHD 100Hz khác |

#### MON-04 — BenQ MA270U

| Field | Giá trị được nguồn công bố | Evidence / status | Giới hạn |
|---|---|---|---|
| Model identity | MA270U, 27-inch | E-M05 / verified | Phân biệt MA270S và MA270UP; không dùng test/field của các model đó |
| Display | IPS, 4K 3840×2160, 60Hz, 5ms GtG, contrast 1200:1 | E-M05 / manufacturer-claimed | Không diễn giải 5ms như independent response test |
| Color/HDR | 99% sRGB, 95% P3; 400 nits typical / HDR peak; HDR10 và VESA DisplayHDR 400 được liệt kê | E-M05 / manufacturer-claimed | Cần phân biệt gamut, accuracy, signal compatibility và chứng nhận |
| USB-C | USB-C upstream hỗ trợ DP Alt Mode, dữ liệu và PD 90W; 2 USB-A downstream, 1 USB-C downstream | E-M06 / manufacturer-claimed | Không suy PD 90W từ việc có cổng USB-C; đây là thông số được hãng nêu riêng |
| Independent test | RTINGS đã review MA270S, không phải MA270U | E-M07 / pending for MA270U | MA270S là 5K/70Hz trong bảng model comparison; không sao chép kết quả sang MA270U 4K/60Hz |

#### MON-05 — ASUS TUF Gaming VG27AQ3A

| Field | Giá trị được nguồn công bố | Evidence / status | Giới hạn |
|---|---|---|---|
| Model identity | TUF Gaming VG27AQ3A, 27-inch | E-M08 / verified | Không gộp VG27AQ, VG27AQ1A hoặc VG27AQL1A |
| Display | Fast IPS, QHD 2560×1440, 250 cd/m² typical, contrast 1000:1 | E-M08 / manufacturer-claimed | sRGB “130%” là raw field hãng gọi Color Space; không diễn giải thành 130% coverage chuẩn hoặc color accuracy |
| Refresh / port | 180Hz max; DP 1.4 HBR2 signal 48–180Hz; HDMI 2.0 signal 48–144Hz | E-M08 / manufacturer-claimed | Ghi riêng maximum refresh theo input; không ghi 180Hz cho HDMI |
| Response/HDR | 1ms GtG claim; HDR10 support | E-M08 / manufacturer-claimed | Không có method/setting tương đương độc lập; HDR10 support không phải VESA DisplayHDR certification |
| Independent test | Không dùng review RTINGS của ASUS TUF VG27AQ; đó là model khác, đời cũ 144Hz native/165Hz OC | E-M09 / pending for VG27AQ3A | Tên rất gần nhưng khác model; tuyệt đối không ghép test result |

### 4.2. Tai nghe chụp tai

#### AUD-01 — Sony WH-1000XM5

| Field | Giá trị được nguồn công bố | Evidence / status | Giới hạn |
|---|---|---|---|
| Model / generation | WH-1000XM5; model thuộc đời XM5, ra mắt giữa 2022 theo review độc lập | E-A01 / verified | Không gộp WH-1000XM4 hoặc WH-1000XM6 |
| Weight / driver | Khoảng 250g; dynamic closed, driver 30mm | E-A01 / manufacturer-claimed | Không suy từ trọng lượng ra “đeo thoải mái với mọi người” |
| Wireless | Bluetooth 5.2; A2DP/AVRCP/HFP/HSP; SBC/AAC/LDAC | E-A01 / manufacturer-claimed | Hỗ trợ codec của tai nghe không đồng nghĩa điện thoại/PC đang dùng codec đó |
| Battery | Tối đa 30h ANC on, 40h ANC off (continuous music playback theo hãng) | E-A01 / manufacturer-claimed | Điều kiện âm lượng/codec không được đồng nhất mặc định với hãng khác |
| Independent test | RTINGS review/retest đúng WH-1000XM5, Methodology v2.3; retest 02/07/2026; nêu khoảng 27h continuous playback trong bài review | E-A02 / independent-tested | Không so trực tiếp 27h với claim 30h nếu chưa đồng nhất setting/test protocol |

#### AUD-02 — Sennheiser MOMENTUM 4 Wireless

| Field | Giá trị được nguồn công bố | Evidence / status | Giới hạn |
|---|---|---|---|
| Model/generation | MOMENTUM 4 Wireless / M4; đời tiếp sau MOMENTUM 3 Wireless | E-A03 / verified | MOMENTUM 5 đã xuất hiện; không nhầm M4 với M5 |
| SKU color | Black 509266; White 509267; Graphite 700383; trang Support liệt kê thêm Brown 800074, Teal 800073, Copper 800108, Denim 800109 | E-A03 / verified | SKU là mã màu/product của hãng, không phải mã retailer Việt Nam |
| Wireless/codecs | Bluetooth 5.2; A2DP/AVRCP/HFP; SBC, AAC, aptX, aptX Adaptive | E-A03 / manufacturer-claimed | aptX/aptX Adaptive chỉ có tác dụng khi thiết bị nguồn tương thích |
| Acoustic/ANC | Dynamic 42mm; Hybrid Adaptive ANC; THD <0.3% tại 1kHz/100dBSPL theo hãng | E-A03 / manufacturer-claimed | Không biến thông số hãng thành kết quả nghe/đo độc lập |
| Battery | Up to 60h Bluetooth + ANC; hãng nêu điều kiện thử iPhone, âm lượng trung bình | E-A03 / manufacturer-claimed | Ghi điều kiện thử cùng field |
| Independent test | RTINGS review khớp MOMENTUM 4 Wireless, Methodology v2.3; mẫu màu Black được test; bài nêu kết quả pin hơn 60h và đánh giá ANC/mic/sound | E-A04 / independent-tested | Kết quả lab của mẫu Black; không dùng cho MOMENTUM 5 hoặc sản phẩm mang tên gần |

#### AUD-03 — Bose QuietComfort Ultra Headphones (1st Gen / 2023)

| Field | Giá trị được nguồn công bố | Evidence / status | Giới hạn |
|---|---|---|---|
| Generation | Product support Bose ghi QuietComfort Ultra Headphones bán từ 2023; Bose phân biệt đời 1 với 2nd Gen bán từ 2025 | E-A05 / verified | Catalog phải ghi “1st Gen / 2023”; không rút gọn thành QuietComfort Ultra nếu có cả đời 2 |
| Product name / SKU | Product name chính hãng: QuietComfort Ultra Headphones; support family ID QCUH-HEADPHONEARN | E-A05 / verified for family only | Không coi family ID là retail P/N; SKU màu/region vẫn pending |
| Wireless | Bluetooth 5.3; profiles A2DP/HFP/AVRCP/BLE; Snapdragon Sound listed | E-A06 / manufacturer-claimed | Giữ riêng aptX Adaptive/codec claims theo tài liệu hỗ trợ cụ thể; không suy codec từ Snapdragon Sound |
| Battery | Tối đa 24h Immersive Audio off; tối đa 18h Immersive Audio on; charge time đến 3h | E-A07 / manufacturer-claimed | Đây là claim đời 1; không thay bằng thông số đời 2 (30h, BT 5.4) |
| Wired audio / port | Gen 1: USB-C charging; Bose product support ghi không hỗ trợ USB audio | E-A06 / manufacturer-claimed | Đời 2 có USB-C wired lossless audio; không gán tính năng này cho Gen 1 |
| Independent test | RTINGS review 07/11/2023; bài đánh giá đúng original QuietComfort Ultra, test bench cập nhật Methodology v2.3 vào 2026 | E-A08 / independent-tested | Không dùng review QuietComfort Ultra 2nd Gen cho đời 1 |

#### AUD-04 — JBL Tour One M2

| Field | Giá trị được nguồn công bố | Evidence / status | Giới hạn |
|---|---|---|---|
| Model / Item# | JBL Tour One M2; Item# JBLTOURONEM2BAM cho trang sản phẩm đen | E-A09 / verified | Không gộp Tour One M3 hoặc Tour Pro |
| Driver / fit | Over-ear; dynamic driver 40mm; weight 278g | E-A09 / manufacturer-claimed | Weight/model source scope đúng M2 |
| Wireless | Bluetooth 5.3; profiles A2DP 1.3.2, AVRCP 1.6.2, HFP 1.7.2 | E-A09 / manufacturer-claimed | Bluetooth LE Audio/LC3 cần firmware/thiết bị tương ứng |
| Battery | Tối đa 50h ANC off và 30h ANC on; sạc đầy khoảng 2h | E-A09 / manufacturer-claimed | Điều kiện test hãng không mặc định bằng test của Bose/Sony/Sennheiser |
| ANC / mics | True Adaptive Noise Cancelling; product description nói “4-mic technology”; bảng specs ghi Number of Microphones = 7 | E-A09 / conflicting-scope | Có thể “4-mic” nói đến call/beamforming array còn 7 là tổng số mic; chưa có định nghĩa field cùng scope. Lưu riêng hai claim, chưa kết luận một con số duy nhất |
| Codec | JBL Support FAQ: AAC/SBC; LC3 được bật qua OTA update cho Bluetooth LE Audio từ 2025 | E-A10 / manufacturer-claimed, conditional | Chỉ set LC3 supported nếu firmware hiện tại và source device xác nhận; AAC/SBC là base codec claim |
| Independent test | Chưa tìm thấy bài test độc lập khớp chính xác Tour One M2 trong lượt tra cứu | pending | Không lấy test JBL Tour One M3 hoặc Tour Pro để điền |

#### AUD-05 — Apple AirPods Max 1 (USB-C)

| Field | Giá trị được nguồn công bố | Evidence / status | Giới hạn |
|---|---|---|---|
| Generation / identity | AirPods Max 1 (USB-C), năm ra mắt 2024; model number A3184 | E-A11 / verified | Đây là đời 1 USB-C, không phải AirPods Max 2 |
| Generation separation | AirPods Max 1 Lightning: A2096, 2020; AirPods Max 2: A3454, 2026 | E-A12 / verified | Không ghép variant theo tên chung “AirPods Max” |
| Audio features | Apple-designed dynamic driver; ANC/Transparency; Personalized Spatial Audio; Adaptive EQ; H1 chip mỗi bên | E-A11 / manufacturer-claimed | Tính năng một phần phụ thuộc OS, thiết bị nguồn và nội dung tương thích |
| Microphones | Apple mô tả tổng cộng 9 microphones: 8 ANC + 3 voice use (2 dùng chung ANC và 1 bổ sung) | E-A11 / manufacturer-claimed | Không cộng 8+3 thành 11 mic; Apple nêu 9 tổng cộng với hai mic dùng chung |
| Battery/weight | Up to 20h ANC; 386.2g (with cushions) | E-A11 / manufacturer-claimed | Runtime là claim hãng theo điều kiện ghi chú của Apple |
| Connectivity | Bluetooth 5.0; USB-C wired lossless audio cần kết nối USB-C có dây và nội dung/dịch vụ tương thích | E-A11 / manufacturer-claimed | Lossless over USB-C là wired mode, không phải codec Bluetooth |
| Independent test | RTINGS review có mẫu AirPods Max Lightning; review ghi rõ chưa có mẫu USB-C để test và USB-C-dependent metrics may differ | E-A13 / pending for A3184 | Không gắn independent-tested cho model A3184 từ kết quả A2096; có thể lưu review cũ dưới related evidence only |

## 5. Danh mục nguồn — evidence IDs

| Evidence ID | Nguồn | Loại | Phạm vi sử dụng |
|---|---|---|---|
| E-M01 | LG Việt Nam — 27GS85Q-B: https://www.lg.com/vn/man-hinh-may-tinh/man-hinh-gaming-ultragear/27gs85q-b/ | Manufacturer Vietnam | Exact model, QHD, 180Hz native / 200Hz O/C, Faster mode, DCI-P3 |
| E-M02 | ASUS Việt Nam — PA279CRV Tech Specs: https://www.asus.com/vn/displays-desktops/monitors/proart/proart-display-pa279crv/techspec/ | Manufacturer Vietnam | Exact model, display/color/refresh/HDR/USB-C/PD/ports |
| E-M03 | RTINGS — PA279CRV review: https://www.rtings.com/monitor/reviews/asus/proart-display-pa279crv | Independent testing | Exact 27-inch model; Methodology v2.1.2; color, HDR, response, contrast and connectivity review |
| E-M04 | BenQ Việt Nam — GW2790Q specs: https://www.benq.com/vi-vn/monitor/home/gw2790q/spec.html | Manufacturer Vietnam | 27-inch QHD, IPS, 100Hz, GtG/MPRT, sRGB |
| E-M05 | BenQ Việt Nam — MA270U specs: https://www.benq.com/vi-vn/monitor/home/ma270u/spec.html | Manufacturer Vietnam | Exact 27-inch 4K MA270U, refresh, color, response, HDR |
| E-M06 | BenQ MA270U port/PD fields (same official spec page): https://www.benq.com/vi-vn/monitor/home/ma270u/spec.html | Manufacturer Vietnam | USB-C DP Alt Mode/Data/PD 90W and downstream hub |
| E-M07 | RTINGS — BenQ MA270S review/variant table: https://www.rtings.com/monitor/reviews/benq/ma270s | Independent testing of a different model | Used only to demonstrate MA270S != MA270U; not evidence for MA270U performance |
| E-M08 | ASUS Việt Nam — VG27AQ3A Tech Specs: https://www.asus.com/vn/displays-desktops/monitors/tuf-gaming/tuf-gaming-vg27aq3a/techspec/ | Manufacturer Vietnam | Exact model, QHD/Fast IPS, 180Hz max, port timing, HDR10 |
| E-M09 | RTINGS — ASUS TUF VG27AQ review: https://www.rtings.com/monitor/reviews/asus/tuf-vg27aq | Independent testing of a different model | Explicitly excluded from VG27AQ3A evidence; older VG27AQ is not VG27AQ3A |
| E-A01 | Sony Việt Nam — WH-1000XM5 specs: https://www.sony.com.vn/electronics/tai-nghe-choang-dau-tai-nghe/wh-1000xm5/specifications | Manufacturer Vietnam | Exact model, weight, Bluetooth, codec, battery |
| E-A02 | RTINGS — Sony WH-1000XM5 review: https://www.rtings.com/headphones/reviews/sony/wh-1000xm5-wireless | Independent testing | Exact model; test bench v2.3; retest 02/07/2026 |
| E-A03 | Sennheiser Việt Nam — MOMENTUM 4 Wireless: https://vn.sennheiser-hearing.com/vi/products/momentum-4-wireless | Manufacturer Vietnam | Exact product name, SKU color variants, BT/codecs/driver/THD/ANC/battery |
| E-A04 | RTINGS — MOMENTUM 4 Wireless review: https://www.rtings.com/headphones/reviews/sennheiser/momentum-4-wireless | Independent testing | Exact model; Black test sample; test bench v2.3 |
| E-A05 | Bose Support — QC Ultra product support (sold from 2023): https://support.bose.ca/product/bose-quietcomfort-ultra-headphones/01t8c00000QEpaxAAD | Manufacturer Support | First-generation/2023 family identity |
| E-A06 | Bose Support — QC Ultra product specifications: https://support.bose.ca/article/quietcomfort-ultra-headphones-specifications | Manufacturer Support | Gen 1 Bluetooth, profiles, ports and product specs |
| E-A07 | Bose Support — Gen 1 charging/battery: https://support.bose.com/article/quietcomfort-ultra-headphones-charging-your-headphones | Manufacturer Support | Gen 1 24h/18h immersive condition and charging time |
| E-A08 | RTINGS — original Bose QuietComfort Ultra review: https://www.rtings.com/headphones/reviews/bose/quietcomfort-ultra-headphones-wireless | Independent testing | Original 2023 model; not 2nd Gen |
| E-A09 | JBL — Tour One M2: https://www.jbl.com/TOUR-ONE-M2.html | Manufacturer | Exact Item#, BT5.3, driver/weight, battery, microphone field |
| E-A10 | JBL Vietnam Support — codecs: https://support.jbl.com/vn/en/howto/?dir=desc&sort=rating&start=281&sz=60 | Manufacturer Support | AAC/SBC base; LC3 OTA/LE Audio conditional |
| E-A11 | Apple Việt Nam — AirPods Max 1 USB-C specs: https://support.apple.com/vi-vn/121205 | Manufacturer Support | 2024 model family, features, mic, weight, runtime, Bluetooth, wired USB-C audio |
| E-A12 | Apple Việt Nam — Identify AirPods: https://support.apple.com/vi-vn/109525 | Manufacturer Support | A3184 vs A2096 vs A3454 generation/model identity |
| E-A13 | RTINGS — AirPods Max review: https://www.rtings.com/headphones/reviews/apple/airpods-max-wireless | Independent testing (Lightning variant only) | Exclusion note: RTINGS tested Lightning; explicitly says USB-C sample not tested |

## 6. Cross-review thuật ngữ và câu hỏi của Vân Anh

Tài liệu đối chiếu: [Category Decision Hypotheses v1 — Vân Anh](https://github.com/anhnv14994/web-aff/blob/main/team/V%C3%A2n%20Anh/category-decision-hypotheses-v1.md), lập ngày 12/11/2026. Đây là review tài liệu/cross-check chuyên môn trên câu hỏi v1; **chưa có phản hồi trực tiếp mới của Vân Anh trong Issue #8**, vì vậy không ghi nhận đây là Vân Anh đã approve.

### 6.1. Màn hình — giữ nguyên 8 câu hỏi, chỉnh cách diễn đạt kỹ thuật

| Câu hỏi Vân Anh | Kiểm tra thuật ngữ bởi A Long | Cách hỏi/diễn giải nên dùng | Không nên hỏi người dùng phổ thông |
|---|---|---|---|
| Q1. Dùng văn phòng/lập trình, gaming, xem phim hay thiết kế? | Đúng; use case là đầu vào trước thông số | Giữ nguyên; hỏi thêm phần mềm/game chỉ khi cần phân biệt | Không hỏi “cần IPS, VA hay OLED?” ngay đầu |
| Q2. Khoảng cách nhìn và giới hạn bàn? | Đúng; cần thêm độ sâu bàn/arm nếu ảnh hưởng kích thước | Hỏi khoảng cách ngồi và chiều ngang/sâu bàn; có thể yêu cầu ảnh/kích thước nếu khách tự nguyện | Không yêu cầu người dùng tính PPI |
| Q3. Máy tính/laptop nào, cần HDMI/DP/USB-C? | Đúng; chính xác hơn là hỏi model máy/đời máy nếu cần kiểm tra output | “Bạn dùng máy nào? Muốn cắm bằng dây gì hoặc cần một dây vừa xuất hình vừa sạc laptop?” | Không hỏi DP Alt Mode, HBR2, DSC hay USB-C PD wattage trước khi biết máy |
| Q4. Có tác vụ đòi hỏi mượt hoặc màu chính xác? | Đúng; cần định nghĩa “chuyên nghiệp” theo workflow | Hỏi tên game/phần mềm và mức độ công việc màu có phải deliverable chuyên nghiệp không | Không hỏi “99% DCI-P3 hay Delta E<2?” khi khách chưa biết ý nghĩa |
| Q5. Một màn hay nhiều màn; cần sạc/hub/KVM qua một dây? | Đúng; KVM là thuật ngữ khó | “Bạn có cần dùng chung một bộ bàn phím/chuột cho hai máy hoặc sạc laptop qua màn hình không?” | Không hỏi KVM/PD/DP daisy-chain nếu không cần |
| Q6. Chọn không gian hiển thị, độ mượt, màu, kết nối hay giá? | Đúng; đây là soft preference/trade-off | Giữ dạng chọn ưu tiên; chỉ chấm tiêu chí liên quan use case | Không tự nâng refresh/gamut thành hard constraint |
| Q7. Ngân sách? | Đúng; budget là constraint do khách nói, không mặc định | Hỏi tối đa và độ linh hoạt, không ép phải nêu đầu phiên | Không suy ra ngân sách từ nghề nghiệp/thiết bị cũ |
| Q8. Chân đế/arm, loa, bảo hành/đổi điểm ảnh? | Đúng; pixel policy là điều kiện mua/offer, không chỉ thuộc tính panel | Hỏi có cần arm/VESA/điều chỉnh độ cao và có yêu cầu đổi điểm ảnh không | Không hứa chính sách đổi điểm ảnh từ spec sheet |

**Điều kiện kỹ thuật cần hỏi chỉ khi liên quan:** model máy nguồn; cổng xuất hình; độ phân giải/refresh mục tiêu; chiều sâu bàn/khoảng cách; phần mềm màu chuyên nghiệp; nhu cầu sạc laptop, hub/KVM.  
**Không cần hỏi trực tiếp:** GtG/MPRT, overdrive, DSC, HBR2, gamut percentage, Delta E, HDR tier. Product Expert/engine sẽ kiểm tra từ model và workload đã cung cấp.

### 6.2. Audio — giữ 8 câu hỏi, làm rõ nguồn phát/fit/âm thanh gọi

| Câu hỏi Vân Anh | Kiểm tra thuật ngữ bởi A Long | Cách hỏi/diễn giải nên dùng | Không nên hỏi người dùng phổ thông |
|---|---|---|---|
| Q1. Chủ yếu nghe nhạc, họp/gọi, gaming, xem phim hay thu âm? | Đúng; cần xác định use case chính/phụ | Giữ nguyên; cho phép chọn nhiều use case và thứ tự ưu tiên | Không mặc định audio = nghe nhạc |
| Q2. Dùng với thiết bị nào; có cần nhiều thiết bị cùng lúc? | Đúng; nền tảng/OS có ý nghĩa với codec, multipoint và call stack | Hỏi model điện thoại, laptop/console, hệ điều hành và chuyển thiết bị có thường xuyên không | Không hỏi codec aptX/LDAC/AAC nếu chưa rõ thiết bị nguồn |
| Q3. Môi trường yên tĩnh, văn phòng mở, đường phố hay phương tiện công cộng? | Đúng; ANC và mic phụ thuộc môi trường | Giữ nguyên; tách tiếng ồn khi nghe và tiếng ồn khi gọi | Không hỏi con số “ANC bao nhiêu dB” |
| Q4. Đeo liên tục bao lâu; có nhạy cảm với áp lực/trọng lượng/nóng bí? | Đúng; fit là cá nhân, không có spec phổ quát | Giữ nguyên; hỏi thời lượng và kiểu đeo từng thấy thoải mái/khó chịu | Không dùng khối lượng để kết luận ai cũng thoải mái |
| Q5. Ưu tiên chất âm, ANC, mic, latency, comfort, pin hay nghe môi trường? | Đúng; latency chỉ quan trọng khi gaming/video/tác vụ thời gian thực | Hỏi hệ quả thực tế: “Bạn có bị tiếng/hình lệch khi xem/chơi game không?” | Không hỏi Bluetooth latency theo ms trước khi biết use case |
| Q6. Thể loại nhạc và âm thanh thích/không thích? | Đúng; giúp diễn đạt preference mà không giả vờ đoán gu | Hỏi ví dụ bài hát/giọng/nhạc cụ hoặc tai nghe cũ khách thích | Không nói một tuning “chuẩn” phù hợp tất cả |
| Q7. Mic/độ trễ quan trọng đến mức nào; nền tảng họp/game? | Đúng; cần phân biệt mic call với mic dùng trên dây/USB/Bluetooth | Hỏi app họp, console/game, môi trường gọi, có cần dongle không | Không tự suy mic Bluetooth hoạt động tương tự trên mọi app/OS |
| Q8. Có thể nghe/đeo thử hoặc cần đổi trả rõ? | Đúng; giảm bất định về sound/fit | Giữ nguyên; offer/return policy cần nguồn retailer xác minh | Không khẳng định thử nghiệm của reviewer thay thế trải nghiệm cá nhân |

**Điều kiện kỹ thuật cần hỏi chỉ khi liên quan:** model nguồn phát và OS; app họp/game; nhu cầu multipoint; môi trường/độ ồn; thời lượng đeo; yêu cầu mic; khả năng nghe/đeo thử.  
**Không cần hỏi trực tiếp:** driver mm, impedance, sensitivity, frequency response range, codec, ANC dB. Các trường này do Product Expert xác minh theo đúng model/thiết bị.

### 6.3. Kết luận cross-review

- Bộ câu hỏi của Vân Anh đi đúng thứ tự: bối cảnh/tác vụ → ưu tiên/constraint → tương thích/rủi ro → trade-off. Không cần thay bằng bảng câu hỏi thông số.
- A Long bổ sung technical slots phía sau: exact source device/model, output port, workload/software, refresh/port limit, wireless codec compatibility, call environment và fit condition.
- Không hỏi mọi slot ở mọi phiên tư vấn. Chỉ hỏi khi câu trả lời có thể loại phương án, đổi shortlist hoặc xác định blocker.
- Nên phân biệt **hard constraint** do khách nói (ví dụ bắt buộc laptop xuất 4K/144Hz, cần đổi hai thiết bị) với **technical fact** do A Long xác minh (cổng HDMI/DP thực sự hỗ trợ mode nào).
- Cross-review này là desk review theo tài liệu Vân Anh; chờ Vân Anh phản hồi trực tiếp nếu CEO yêu cầu xác nhận thêm.

## 7. QA rules và test cases

### 7.1. Rules bắt buộc

1. **Identity-first:** model/generation/variant chưa được xác minh thì không dùng thông số để so sánh.
2. **Scope per field:** mỗi claim ghi rõ family/model/retail variant, region và điều kiện.
3. **Manufacturer ≠ independent:** mọi thông số hãng giữ trạng thái manufacturer-claimed cho tới khi có test độc lập khớp exact model.
4. **No inherited test:** không lấy kết quả MA270S cho MA270U; VG27AQ cho VG27AQ3A; AirPods Max Lightning cho A3184.
5. **Measurement semantics:** giữ GtG, MPRT, input lag, native refresh, O/C refresh, color gamut, color accuracy, HDR10 signal, VESA DisplayHDR, USB-C data, DP Alt Mode và PD wattage là các field riêng.
6. **Conditional features:** LC3 OTA, 200Hz O/C, codec/source-device compatibility và USB-C wired lossless cần điều kiện đi kèm.
7. **Conflict preservation:** không chọn một trong hai claim “4-mic” và “7 microphones” của JBL khi scope field chưa rõ; lưu cả hai + câu hỏi unresolved.
8. **Generation guard:** Bose Gen 1 / Gen 2, AirPods Max 1 USB-C / Lightning / Max 2, Momentum 4 / Momentum 5, Sony XM5 / XM6 không được gộp.
9. **Unknown stays null:** không điền P/N, warranty, price, stock, region hoặc retail offer từ tên model.
10. **Evidence freshness:** lưu retrieved_at và source version; kiểm tra lại trang hãng trước khi publish hoặc khi có firmware/model revision mới.

### 7.2. 16 test cases

| ID | Input / tình huống lỗi | Expected result | Severity |
|---|---|---|---|
| CEQ-01 | Offer ghi “LG UltraGear 27 inch 200Hz” nhưng thiếu model code | Không tự map thành 27GS85Q-B; yêu cầu exact model/P/N hoặc quarantine | Critical |
| CEQ-02 | LG 27GS85Q-B có 180Hz native và 200Hz O/C | Lưu riêng native=180Hz, overclocked=200Hz; ghi điều kiện DP 1.4 GPU + cable | Critical |
| CEQ-03 | LG 27GS85Q-B claim 1ms | Ghi manufacturer-claimed GtG; lưu Faster response mode; không gọi independent-tested | High |
| CEQ-04 | BenQ GW2790Q ghi 5ms GtG và 1ms MPRT | Không overwrite một trường bằng trường kia; UI không được hiển thị đơn lẻ “1ms response” | Critical |
| CEQ-05 | BenQ MA270U bị map sang review MA270S | Fail identity gate; MA270S là model khác (5K/70Hz); MA270U giữ pending independent test | Critical |
| CEQ-06 | MA270U có USB-C connector | Chỉ ghi PD90W/DP Alt Mode/Data nếu field source chỉ rõ; không suy tất cả từ connector presence | High |
| CEQ-07 | ASUS VG27AQ3A xuất qua HDMI | Max timing phải theo trang ASUS: HDMI tới 144Hz, DP tới 180Hz; không claim HDMI 180Hz | Critical |
| CEQ-08 | ASUS VG27AQ review được gắn vào VG27AQ3A | Reject; model code khác nhau dù tên gần giống | Critical |
| CEQ-09 | ASUS VG27AQ3A field “sRGB 130%” | Giữ raw manufacturer field; không đổi thành color accuracy hoặc “130% sRGB coverage” nếu chưa định nghĩa measurement | High |
| CEQ-10 | ASUS PA279CRV “99% DCI-P3” và ΔE<2 | Lưu gamut và accuracy riêng; giữ manufacturer calibration claim riêng với RTINGS measurement | High |
| CEQ-11 | Sony WH-1000XM5 bị gộp với XM4 hoặc XM6 | Quarantine/identity conflict; exact model required | Critical |
| CEQ-12 | MOMENTUM 4 Black SKU 509266 nhưng offer có White/Graphite | Không copy color SKU; map đúng 509267/700383 hoặc pending nếu mã không khớp | Critical |
| CEQ-13 | Bose QuietComfort Ultra đời 1 bị lấy battery/Bluetooth của 2nd Gen | Fail; Gen 1 2023 vs Gen 2 2025; BT5.3 và 24h/18h immersive conditions cho đời 1 | Critical |
| CEQ-14 | JBL M2 mô tả 4-mic tech, spec field 7 microphones | Trạng thái conflicting-scope; không gộp thành một số trước khi xác định field definition | High |
| CEQ-15 | AirPods Max USB-C A3184 dùng kết quả test Lightning A2096 | Không gán independent-tested; chỉ link related test và ghi explicit limitation | Critical |
| CEQ-16 | Headphone codec/battery/latency được so sánh | Gắn source device, codec/OS, ANC state, volume/test method và firmware; thiếu thì not directly comparable | High |

## 8. Catalog record template đề xuất

Mỗi canonical model nên có record riêng, mỗi attribute có evidence riêng. Ví dụ:

| Field | Example value | Scope | Source ID | Status | Confidence |
|---|---|---|---|---|---|
| canonical_model_id | MON-01 | model | E-M01 | verified | high |
| manufacturer_model | LG 27GS85Q-B | model | E-M01 | verified | high |
| native_refresh_hz | 180 | model / O/C off | E-M01 | manufacturer-claimed | high |
| overclock_refresh_hz | 200 | model / O/C on | E-M01 | manufacturer-claimed | high |
| overclock_condition | DP 1.4 GPU + DP 1.4 cable | condition | E-M01 | manufacturer-claimed | high |
| response_gtg_ms | 1 | Faster mode | E-M01 | manufacturer-claimed | medium |
| independent_response_test | null | exact model | none found | pending | pending |
| retailer_sku | null | offer | none | pending | pending |
| price / stock / warranty | null | offer | none | pending | pending |

**Field model đề xuất:** attribute_id, raw_value, normalized_value, unit, scope, method, condition, source_id, status, confidence, retrieved_at, valid_from, notes, reviewer. Giữ raw value để không mất wording/đơn vị gốc của hãng.

## 9. Unresolved risks / việc chưa thể nghiệm thu tuyệt đối

1. **Vietnam retailer P/N:** chưa có retailer listing/offer được Operations xác nhận cho 10 mẫu; không tự điền.
2. **Bảo hành và nguồn hàng tại Việt Nam:** không nằm trong Product Expert evidence, chờ Operations.
3. **Local/regional panel & part number:** đặc biệt màn hình ASUS/LG và nhiều màu headphone; cần đối chiếu nhãn hộp/thiết bị hoặc P/N chính hãng khi ingest offer.
4. **Independent test coverage:** hiện xác nhận test exact cho PA279CRV, XM5, MOMENTUM 4, Bose Ultra đời 1. Các mẫu còn lại để pending; AirPods Max USB-C không kế thừa test Lightning.
5. **JBL microphones:** 4-mic technology vs 7 microphones cần làm rõ scope field.
6. **AirPods Max USB-C:** các trường về lossless phải ghi rõ kết nối USB-C có dây, không gán cho Bluetooth.
7. **Refresh rate/response time:** cần test bench exact để xác định performance thực; headline claim của hãng không phải thực nghiệm độc lập.
8. **Vân Anh cross-review:** đã đối chiếu tài liệu v1; chưa có xác nhận trực tiếp trong Issue #8.
9. **Source changes:** trang hãng có thể cập nhật specs/firmware mà không thông báo; phải lưu snapshot/retrieval date trong pipeline khi triển khai thật.

## 10. Kết luận chuyên môn của A Long

- **10/10 canonical model** hiện đã có định danh chính hãng đủ để tránh gộp nhầm model/generation ở tầng model name. Riêng retail P/N/SKU và local market mapping còn pending đúng phạm vi.
- **7/10 model** có nguồn hãng trực tiếp với các thuộc tính chính đã ghi trong evidence register; Sennheiser, Bose và Apple đã bổ sung những khoảng trống identity/generation quan trọng. Các field phụ không có nguồn vẫn là pending.
- Independent evidence hiện có cho **4 model**: PA279CRV, WH-1000XM5, MOMENTUM 4 Wireless và Bose QuietComfort Ultra đời 1. Các kết quả test chỉ áp dụng đúng model/sample/test bench nêu ở trên.
- Có **1 nhóm field cần giữ conflicting-scope**: JBL Tour One M2 microphone count/“4-mic technology”. Không tự chọn một giá trị.
- Các thông số marketing dễ gây sai nhất đã được chuyển thành test: O/C refresh, GtG/MPRT, port-specific refresh, gamut vs accuracy, USB-C PD vs video/data, generation naming, codec compatibility và test inheritance.
- Câu hỏi Vân Anh có nền tảng tốt; người mua nên trả lời bằng tác vụ, thiết bị, môi trường và đánh đổi. Product Expert sẽ kiểm tra thuật ngữ/thông số phía sau; không hỏi khách phổ thông về GtG, MPRT, DCI-P3, codec hoặc DP Alt Mode nếu không cần.

**Release recommendation:** có thể dùng file này làm catalog QA seed/internal reference. Chưa xuất bản bảng xếp hạng hoặc so sánh thương mại cho đến khi các trường pending có nguồn đúng SKU và Operations xác nhận retail offer. A Long có quyền yêu cầu quarantine record nếu exact identity/source không khớp.

---

## 11. Checklist nghiệm thu

- [x] 5 màn hình có exact manufacturer model identity.
- [x] 5 tai nghe có exact model/generation; Senn SKU màu, JBL Item# và Apple A3184 đã được xác định; Bose Gen 1 được tách khỏi Gen 2.
- [x] Nguồn hãng còn thiếu được bổ sung: ASUS VG27AQ3A, MOMENTUM 4, Bose QC Ultra Gen 1, JBL Tour One M2, AirPods Max USB-C.
- [x] Evidence register theo từng field, có URL, checked date, scope, status và confidence.
- [x] Đã kiểm tra test độc lập đúng model; không kế thừa test của variant khác.
- [x] 16 test cases cho model/generation/variant/claim/provenance.
- [x] Cross-review thuật ngữ và câu hỏi màn hình/audio của Vân Anh.
- [x] Không tự tạo giá, stock, warranty Việt Nam hoặc affiliate eligibility.
- [ ] Vân Anh phản hồi trực tiếp (nếu CEO yêu cầu).
- [ ] CEO nghiệm thu.
- [ ] Operations xác minh retail SKU/P/N, warranty và offer trước public catalog.
