# ENGINE-03 — Data Source & Offer Adapter Standard

**Bản:** v1.1 — phân tích, tái thiết kế và tiêu chí nghiệm thu pilot  
**Ngày rà soát:** 12/11/2026  
**Phạm vi:** A+ Việt Nam · màn hình · thiết bị âm thanh · máy lọc không khí · laptop  
**Chủ trì nội dung nghiệp vụ:** Trâm Anh — Market Research & Affiliate Operations  
**Trạng thái:** `REVIEW_REQUIRED` — đề xuất để Hoàng/A Long/CEO/Legal phản biện; chưa được phê duyệt production  
**Thay thế:** Bản v1.0 ngày 12/11/2026

---

## 0. Báo cáo điều hành

### 0.1 Kết luận

Bản v1.0 có đúng định hướng nền tảng: tách thông tin sản phẩm khỏi giá bán, lưu nguồn gốc dữ liệu, kiểm soát độ mới và cách ly bản ghi không đáng tin. Tuy nhiên, v1.0 mới ở mức nguyên tắc vận hành; chưa đủ chặt để chuyển trực tiếp thành schema production hoặc giao cho kỹ thuật triển khai mà không phát sinh cách hiểu khác nhau.

**Khuyến nghị:** chấp nhận v1.1 làm cơ sở review thiết kế; chưa bật tự động publish cho đến khi hoàn tất 5 cổng kiểm soát: (1) identity Model/Variant, (2) permission theo dữ liệu và mục đích, (3) freshness/price semantics, (4) affiliate eligibility/tracking, (5) quarantine và audit.

### 0.2 Các chỉnh sửa có ảnh hưởng lớn

1. Tách `ProductModel` khỏi `ProductVariant`; không để `product_id + variant_key` mơ hồ giữa model và cấu hình bán.
2. Tách `ProductFactClaim` khỏi nguồn chứng cứ; một thông số có thể có nhiều nguồn, nhiều revision và trạng thái xung đột.
3. Tách `RetailOffer` khỏi `OfferObservation`; giữ lịch sử giá/tồn kho theo thời điểm thay vì ghi đè mất lịch sử.
4. Tách `AffiliateTrackingLink` khỏi `RetailOffer`; một offer có thể có nhiều campaign/network/link và trạng thái hiệu lực khác nhau.
5. Nâng quyền sử dụng từ “approved source” thành `PermissionGrant` theo loại dữ liệu, hành động, mục đích, lãnh thổ, thời hạn và điều kiện.
6. Thay TTL chung bằng chính sách freshness theo nguồn/trường, có trạng thái phục vụ và hành động khi hết hạn.
7. Bổ sung legal gate theo Luật Thương mại điện tử 122/2025/QH15 (hiệu lực 01/07/2026), Nghị định 248/2026/NĐ-CP, Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 (hiệu lực 01/01/2026) và Luật sửa đổi Luật Quảng cáo 75/2025/QH15 (hiệu lực 01/01/2026). Đây là checklist vận hành để Legal xác minh cách áp dụng cho mô hình A+, không phải kết luận pháp lý.

### 0.3 Đánh giá v1.0

| Miền đánh giá | Đánh giá v1.0 | Vì sao chưa đủ | Mức ưu tiên |
|---|---|---|---|
| Tách Product Fact / Retail Offer | Đạt một phần | Đúng nguyên tắc nhưng thiếu lớp Model/Variant | P0 |
| Định danh model/variant | Chưa đạt | GTIN/MPN được nêu nhưng chưa có quy tắc scope, region, packaging và mapping | P0 |
| Provenance và xung đột fact | Đạt một phần | Có source cho từng fact nhưng thiếu claim history, applicability và conflict resolution | P1 |
| Giá, tồn kho và lịch sử | Chưa đạt | Có timestamp/TTL nhưng không có observation history và semantics giá đủ chi tiết | P0 |
| Affiliate tracking | Đạt một phần | Link gắn vào offer; thiếu entity link/campaign lifecycle riêng | P1 |
| Quyền sử dụng dữ liệu | Chưa đạt | “Permission status” cấp nguồn quá rộng; chưa xác minh quyền theo field/asset/action | P0 |
| Freshness | Đạt một phần | TTL đề xuất có ích nhưng dễ bị hiểu là SLA cố định | P1 |
| Quarantine / audit | Đạt một phần | Có trigger và trạng thái nhưng chưa có severity, phạm vi tác động và rule release | P0 |
| API/adapter operation | Đạt một phần | Pipeline đúng hướng nhưng thiếu contract/version/drift và rollback criteria | P1 |
| Legal readiness | Chưa đạt | Chưa phản ánh đầy đủ luật có hiệu lực năm 2026 và chưa phân biệt vai trò pháp lý | P0 |

> “Chưa đạt” ở đây nghĩa là tài liệu chưa định nghĩa đủ để nghiệm thu; không đồng nghĩa hệ thống hiện tại đã vi phạm hoặc dữ liệu thực tế đang sai.

---

## 1. Phạm vi, giả định và nguyên tắc thiết kế

### 1.1 Phạm vi

ENGINE-03 quản lý việc thu nhận, chuẩn hóa, xác minh, lưu lịch sử, cập nhật và phân phối dữ liệu cho A+:

- **Product domain:** model, biến thể/cấu hình bán, thông số, tài liệu và bằng chứng.
- **Commerce domain:** seller, listing/offer, giá, tồn kho, khuyến mãi và điều kiện bán.
- **Affiliate domain:** publisher/campaign eligibility, deeplink/tracking link, attribution metadata và đối soát.
- **Governance domain:** nguồn, quyền sử dụng, retention, audit, freshness và quarantine.

### 1.2 Không thuộc phạm vi

- Quyết định category MVP, chiến lược kinh doanh hoặc thứ tự ưu tiên sản phẩm.
- Chấm điểm chất lượng sản phẩm hoặc xếp hạng dựa trên hoa hồng.
- Tự kết luận tính hợp pháp của từng nguồn, seller hoặc chương trình affiliate.
- Tự xác nhận website A+ thuộc loại hình pháp lý nào khi chưa rà soát đầy đủ chức năng và luồng giao dịch.
- Cam kết API/feed của đối tác hoạt động hoặc có quyền dùng dữ liệu chỉ vì tài liệu API công khai tồn tại.

### 1.3 Nguyên tắc bắt buộc

1. **Một dữ kiện — một scope rõ:** dữ kiện áp dụng cho model hay variant phải được khai báo.
2. **Một giá bán — một seller, một variant, một điều kiện, một thời điểm:** không lưu giá chung cho model nếu listing bán cấu hình cụ thể.
3. **Provenance ở cấp claim/observation:** biết ai cung cấp, URL/record nào, lấy lúc nào, nguồn cập nhật khi nào và adapter version nào.
4. **Permission trước ingestion và trước publish:** quyền xem, truy xuất, lưu, biến đổi, hiển thị và phân phối là các quyền khác nhau.
5. **Không tự suy đoán dữ liệu thiếu:** thiếu ship/tax/stock không được chuyển thành 0/đã có hàng.
6. **Fail closed:** không chắc về identity, permission, tính hợp lệ hoặc freshness thì không được hiển thị như sự thật hiện tại.
7. **Commission không phải quality signal:** không dùng commission rate để xác minh thông số, chất lượng hoặc độ phù hợp sản phẩm.
8. **Có thể truy nguyên và thu hồi:** mọi dữ liệu public phải truy về nguồn; có thể unpublish nhanh theo source, product, variant, offer hoặc tracking link.

---

## 2. Phân tích lỗ hổng và quyết định thiết kế

### 2.1 Product Model và Product Variant cần là hai thực thể

Trong v1.0, `product_id` kèm `variant_key` chưa chỉ rõ ID đại diện model hay cấu hình có thể mua. Điều này dễ gây lỗi ở laptop (cùng tên nhưng CPU/RAM/SSD/GPU khác), màn hình (kích thước/revision/region), tai nghe (màu hoặc phiên bản kết nối) và máy lọc (phiên bản/điện áp/bộ lọc đi kèm).

**Quyết định đề xuất:**
- `ProductModel`: danh tính model/series kỹ thuật theo brand + model code + market/revision.
- `ProductVariant`: cấu hình thương mại cụ thể có thể được seller niêm yết, gắn với đúng một model; chứa RAM/SSD/GPU/màu/kích thước/bundle hoặc yếu tố ảnh hưởng giá.
- `GTIN`/EAN/UPC, MPN, seller SKU là identifier có namespace và issuer; không dùng một trường chuỗi chung.
- GTIN là tín hiệu ghép mạnh nhưng không được xem là phép chứng minh duy nhất nếu packaging, region hoặc listing mâu thuẫn.

### 2.2 Không ghi đè Product Fact khi có nguồn mới

Một fact có thể có nhiều nguồn, thời điểm, phạm vi áp dụng và revision. Chỉ giữ một `source_id` ngay trên fact làm mất lịch sử nguồn, gây khó giải thích vì sao giá trị được chọn.

**Quyết định đề xuất:** tách `ProductFactClaim` (giá trị đang được xem xét/hiển thị) và `FactEvidence` (mỗi chứng cứ từ nguồn). Mỗi claim có scope (`model` hoặc `variant`), unit, applicability, observed/published time, verification status và reviewer. Khi hai nguồn xung đột, lưu cả hai evidence, không tự chọn theo thứ tự “nguồn nào mới hơn” nếu chúng đo khác điều kiện hoặc khác revision.

### 2.3 Giá và tồn kho phải có lịch sử quan sát

`RetailOffer` ở dạng bản ghi hiện tại không đủ giải thích biến động giá, lỗi feed hoặc offer đã hết hạn. Cần một danh tính offer ổn định và nhiều observation nối tiếp.

**Quyết định đề xuất:** `RetailOffer` mô tả listing/seller/variant/điều kiện; `OfferObservation` ghi từng lần thu nhận giá, ship, thuế, stock, promotion và freshness. Observation bất thường bị quarantine, không ghi đè observation đang được phục vụ.

### 2.4 Tracking link không đồng nhất với offer

Một listing có thể tham gia nhiều network/campaign, campaign có thể bị pause, publisher có thể bị rút quyền, và link có thể hết hiệu lực trong khi listing vẫn còn. Gắn `tracking_url` thẳng vào Retail Offer tạo coupling không cần thiết.

**Quyết định đề xuất:** `AffiliateTrackingLink` là thực thể riêng, liên kết với `retail_offer_id`, `network_id`, `campaign_id`, publisher/site ID, deeplink, tracking parameters được phép, trạng thái và thời gian kiểm tra gần nhất. Link chỉ active nếu cả publisher, campaign, offer và quyền tạo link đều hợp lệ.

### 2.5 “Source approved” không đồng nghĩa mọi dữ liệu của source đều được phép dùng

Một đối tác có thể cho phép lấy giá bằng feed nhưng không cho phép tái xuất bản ảnh/mô tả; có thể cho phép hiển thị trong dashboard nhưng không cho phép phân phối lại. V1.0 đang gom quyền theo source.

**Quyết định đề xuất:** quản lý `PermissionGrant` theo `source × data_class × action × purpose × territory × validity_period`. Ví dụ: cho phép fetch price và display price không tự động cấp quyền lưu raw feed, cache dài hạn, dùng ảnh, hoặc tạo nội dung phái sinh.

---

## 3. Mô hình dữ liệu chuẩn đề xuất

### 3.1 Sơ đồ thực thể

```text
Source
  ├── PermissionGrant
  ├── IngestionRun ── RawRecordRef / RawSnapshot (nếu được phép lưu)
  └── AdapterVersion

Brand ── ProductModel ── ProductVariant
                  │              │
                  └── ProductFactClaim ── FactEvidence
                                 
Seller ── RetailOffer ── OfferObservation
                    │
                    └── AffiliateTrackingLink ── AffiliateCampaign / Network
```

`ProductModel`/`ProductVariant` là danh tính sản phẩm. `RetailOffer` là listing bán. `AffiliateTrackingLink` là đường dẫn đo attribution. Ba lớp này không được gộp làm một.

### 3.2 Source Registry

Các trường tối thiểu:

| Field | Yêu cầu |
|---|---|
| `source_id` | ID nội bộ bất biến |
| `source_name`, `source_type` | OEM, independent_test, retailer, distributor, affiliate_network, other |
| `legal_entity` | Tổ chức vận hành nguồn nếu xác định được |
| `base_url`, `documentation_url`, `support_contact` | URL/contact được kiểm tra |
| `access_method` | API, XML, CSV, XLSX, manual, permitted_crawl |
| `auth_profile_ref` | Tham chiếu secret manager; không lưu token trong catalog/log |
| `terms_url`, `terms_version`, `checked_at` | Dấu vết điều khoản tại thời điểm review |
| `source_status` | `candidate`, `approved_limited`, `approved`, `suspended`, `expired`, `prohibited` |
| `data_classes_available[]` | Fact, price, stock, seller, image, description, campaign, transaction… |
| `owner`, `review_due_at` | Người phụ trách và ngày review lại |
| `adapter_id`, `adapter_version` | Phiên bản tích hợp |
| `last_success_at`, `last_error_at` | Vận hành nguồn |

`source_status=approved` chỉ cho biết nguồn được duyệt trong phạm vi đã ghi. Permission thực tế vẫn phải kiểm tra theo từng grant.

### 3.3 PermissionGrant

| Field | Quy tắc |
|---|---|
| `permission_id` | ID bất biến |
| `source_id` | Nguồn cấp dữ liệu/quyền |
| `data_class` | `product_fact`, `price`, `stock`, `promotion`, `image`, `description`, `seller_identity`, `tracking`, `click`, `conversion`… |
| `action` | `fetch`, `parse`, `store_raw`, `store_normalized`, `transform`, `display`, `cache`, `redistribute`, `create_affiliate_link`, `measure` |
| `purpose` | `internal_research`, `comparison_display`, `affiliate_referral`, `analytics`, v.v. |
| `territory` | Ví dụ `VN`; không ngầm định quyền toàn cầu |
| `valid_from`, `valid_until` | Thời hạn quyền |
| `retention_limit` | Thời gian lưu tối đa nếu có |
| `attribution_rule` | Nội dung ghi nguồn/credit bắt buộc |
| `evidence_ref` | Hợp đồng, email, approval ID hoặc terms version |
| `approval_status` | `pending`, `approved`, `rejected`, `expired`, `revoked` |
| `approved_by`, `approved_at` | Người và thời điểm duyệt |

**Rule:** trước fetch phải có grant cho `fetch`; trước lưu phải có grant `store_*`; trước public phải có `display`; ảnh phải có grant riêng cho `image`; deeplink phải có grant/approval riêng của campaign. Không kế thừa quyền ngầm giữa các `data_class`.

### 3.4 ProductModel

| Field | Kiểu | Quy tắc |
|---|---|---|
| `product_model_id` | string | ID A+ bất biến |
| `brand_id` | string | Tham chiếu brand chuẩn |
| `model_name` | string | Tên hiển thị chuẩn; không phải khóa duy nhất |
| `model_code` | string | Mã model chính thức, giữ chính xác ký tự |
| `market_region` | string | Thị trường áp dụng, ví dụ `VN` |
| `revision` | string/null | Revision hoặc generation khi hãng có phân biệt |
| `category` | enum | monitor, audio, air_purifier, laptop |
| `official_url` | URI/null | Trang chính thức đúng model/region |
| `identity_status` | enum | `candidate`, `verified`, `disputed`, `retired`, `quarantined` |
| `created_at`, `updated_at` | datetime UTC | ISO 8601 |

### 3.5 ProductVariant

| Field | Kiểu | Quy tắc |
|---|---|---|
| `product_variant_id` | string | ID biến thể bất biến |
| `product_model_id` | FK | Bắt buộc |
| `variant_signature` | string/object | Cấu hình chuẩn hóa để so khớp |
| `market_region` | string | Có thể cụ thể hóa khác model nếu SKU thương mại khác vùng |
| `mpn` | string/null | Mã part của hãng nếu có |
| `gtin` | string/null | GTIN/EAN/UPC; giữ kiểu chuỗi, kiểm tra checksum khi phù hợp |
| `manufacturer_sku` | string/null | SKU hãng |
| `variant_status` | enum | `candidate`, `verified`, `disputed`, `retired`, `quarantined` |
| `created_at`, `updated_at` | datetime UTC | Bắt buộc |

Không dùng `seller_sku` làm manufacturer identifier. Seller SKU chỉ có ý nghĩa trong phạm vi seller/listing.

### 3.6 ProductFactClaim và FactEvidence

`ProductFactClaim` là giá trị A+ quyết định dùng sau review; `FactEvidence` là bằng chứng nguồn.

| Field claim | Quy tắc |
|---|---|
| `claim_id` | ID bất biến |
| `subject_type` | `model` hoặc `variant` |
| `subject_id` | ID model/variant |
| `attribute_key` | Key theo schema ngành, ví dụ `refresh_rate_hz` |
| `value`, `unit`, `value_type` | Lưu kiểu dữ liệu và đơn vị rõ ràng |
| `applicability` | Region/revision/firmware/condition nếu liên quan |
| `claim_status` | `candidate`, `verified`, `disputed`, `rejected`, `superseded` |
| `selected_evidence_id` | Chứng cứ được reviewer chọn |
| `reviewer`, `reviewed_at` | Người và thời điểm xác minh |
| `valid_from`, `valid_to` | Khoảng dữ kiện có hiệu lực nếu biết |

| Field evidence | Quy tắc |
|---|---|
| `evidence_id`, `claim_id`, `source_id` | ID và nguồn |
| `source_record_ref`, `source_url` | Đường dẫn/ID nguồn nếu được lưu |
| `source_published_at` | Thời điểm nguồn phát hành nếu có |
| `observed_at` | Thời điểm A+ quan sát |
| `source_revision` | Revision/spec version/firmware/methodology nếu có |
| `evidence_excerpt_or_hash` | Chỉ lưu nội dung/trích đoạn nếu được quyền; nếu không, lưu hash/metadata |
| `methodology` | Đặc biệt bắt buộc với dữ liệu đo thử độc lập |
| `evidence_status` | `supporting`, `contradicting`, `insufficient`, `withdrawn` |

Không coi `confidence=high` là thay thế cho review. Độ tin cậy phải gắn với loại thuộc tính, revision và điều kiện đo. Thông số hãng công bố phù hợp để xác nhận “claimed specification”; không tự động chứng minh hiệu năng thực tế.

### 3.7 RetailOffer

`RetailOffer` mô tả listing ổn định; dữ liệu biến động nằm trong `OfferObservation`.

| Field | Quy tắc |
|---|---|
| `retail_offer_id` | ID A+ bất biến |
| `product_variant_id` | FK bắt buộc tới đúng variant |
| `source_id` | Nguồn trả offer |
| `seller_id`, `seller_name`, `seller_type` | Phân biệt brand store, authorized retailer, marketplace seller, other, unknown |
| `seller_verification_status` | `verified`, `unverified`, `disputed`, `blocked` |
| `seller_listing_id`, `seller_sku` | ID/SKU trong phạm vi seller |
| `seller_product_url` | URL listing cụ thể |
| `market_region`, `condition` | Ví dụ VN; `new`, `used`, `refurbished`, `open_box`, `unknown` |
| `bundle_signature` | Gói đi kèm nếu ảnh hưởng giá/variant |
| `offer_status` | `candidate`, `active`, `paused`, `unavailable`, `quarantined`, `expired` |
| `first_seen_at`, `last_seen_at` | Lần đầu/cuối quan sát |

### 3.8 OfferObservation

Mỗi lần fetch thành công tạo observation; không sửa lịch sử đã tạo.

| Field | Quy tắc |
|---|---|
| `observation_id`, `retail_offer_id` | ID và FK |
| `observed_at` | UTC, thời điểm A+ lấy |
| `source_updated_at` | Timestamp nguồn nếu có; không có thì null |
| `currency` | ISO 4217, ví dụ `VND` |
| `base_price` | Giá niêm yết/cơ sở nếu có |
| `sale_price` | Giá nguồn đang chào; null nếu không có/không xác minh |
| `price_type` | `regular`, `sale`, `member`, `voucher`, `installment`, `personalized`, `unknown` |
| `price_conditions` | Điều kiện thành viên, thanh toán, voucher, min spend, thời hạn, vùng áp dụng |
| `shipping_fee` | Số hoặc null; không biến null thành 0 |
| `tax_status` | `included`, `excluded`, `unknown` |
| `stock_status` | `in_stock`, `limited`, `out_of_stock`, `preorder`, `backorder`, `unknown` |
| `stock_quantity` | Integer hoặc null; chỉ dùng nếu feed cho phép và có ngữ nghĩa rõ |
| `promotion_refs[]` | ID chương trình/điều kiện; không chỉ text mơ hồ |
| `freshness_status` | `fresh`, `near_stale`, `stale`, `unknown`, `invalid` |
| `source_record_ref`, `ingestion_run_id` | Traceability |
| `anomaly_flags[]` | Giá bất thường, currency mismatch, stock conflict… |

Lưu `sale_price` dưới decimal hoặc integer minor unit với quy ước currency rõ; không dùng floating point. Nếu A+ cần hiển thị “giá thấp nhất”, phải định nghĩa điều kiện so sánh (cùng variant, cùng market, cùng loại giá, có/không voucher, ship/tax) trước khi tính.

### 3.9 AffiliateTrackingLink

| Field | Quy tắc |
|---|---|
| `tracking_link_id` | ID A+ bất biến |
| `retail_offer_id` | Offer liên quan |
| `network_id`, `campaign_id`, `publisher_id` | Tham chiếu được network cấp |
| `destination_url` | URL đích/deeplink chuẩn trước tracking |
| `tracking_url` | Link do network tạo; không tự ghép nếu API yêu cầu tạo qua endpoint |
| `tracking_params` | Chỉ tham số được network cho phép; không chứa PII |
| `link_status` | `pending`, `active`, `suspended`, `expired`, `broken`, `revoked` |
| `campaign_terms_version` | Version/ngày terms xác minh |
| `created_at`, `last_checked_at`, `expires_at` | Thời gian |
| `last_test_result` | HTTP/redirect result theo cách test được network cho phép |

Thông tin hoa hồng/attribution window thuộc campaign/network terms, không gắn thành thuộc tính sản phẩm. Không đưa rate hoa hồng vào logic chất lượng hay thứ hạng tư vấn.

---

## 4. Quy tắc identity và matching

### 4.1 Luồng matching

1. Chuẩn hóa brand, model code và region, nhưng giữ nguyên chuỗi nguồn.
2. So khớp GTIN có kiểm tra định dạng/check digit khi phù hợp; xác minh loại GTIN và packaging level.
3. So khớp MPN/manufacturer SKU + brand + region + revision.
4. So khớp model code chính xác + cấu hình trọng yếu.
5. Manual mapping có reviewer, ngày duyệt và bằng chứng.
6. Fuzzy matching chỉ được tạo candidate; không có đường publish tự động.

### 4.2 Hard-stop — bắt buộc quarantine

- Cùng tên thương mại nhưng khác model code/revision.
- Cùng series nhưng CPU/GPU/RAM/SSD, kích thước panel hoặc variant ảnh hưởng giá khác nhau.
- GTIN khớp nhưng listing mô tả hàng khác region/packaging/bundle hoặc dữ kiện khác mâu thuẫn.
- Listing không có mã đủ phân biệt, seller SKU thay đổi hoặc trang đích chuyển sang biến thể khác.
- Ảnh/tên/specs không nhất quán với mã model.

### 4.3 Không dùng tên làm khóa

Tên thương mại chỉ là label/search alias. Khóa canonical nội bộ không được tái sử dụng khi sản phẩm bị retire. Alias/typo được lưu ở bảng mapping có nguồn và thời gian.

---

## 5. Chuẩn nguồn và đánh giá chứng cứ

### 5.1 Nguồn được tin cậy theo từng thuộc tính, không theo nhãn nguồn chung

| Loại dữ kiện | Nguồn ưu tiên | Điều kiện |
|---|---|---|
| Mã model, thông số hãng công bố | OEM/manual/datasheet | Đúng model code, region, revision |
| Kết quả đo/hiệu năng thực tế | Đơn vị thử nghiệm/reviewer có phương pháp | Ghi mẫu thử, điều kiện, firmware, ngày test, thiết bị đo và giới hạn |
| Giá/tồn kho | Retailer/seller feed hoặc network feed được phép | Đúng seller + listing + variant, observed time rõ |
| Seller authorization | Danh sách đại lý chính thức/hồ sơ xác thực đáng tin | Phải ghi trạng thái và ngày kiểm tra; không suy ra từ tên shop |
| Campaign/tracking/commission | Affiliate network | Publisher đã duyệt, campaign active, terms phù hợp |
| Ảnh/mô tả | OEM/retailer/network có grant rõ | Kiểm tra riêng quyền hiển thị, cache, transform và attribution |

### 5.2 Conflict resolution

- Không “lấy nguồn mới nhất thắng” nếu khác revision hoặc khác điều kiện đo.
- Ưu tiên evidence có scope trùng chính xác với model/variant và điều kiện người dùng cần.
- Fact đo thử không được ghi đè thông số hãng; hai loại phải mang nhãn khác nhau (`manufacturer_claim` vs `independent_test_result`).
- Nếu chưa thể phân xử, claim là `disputed`; không hiển thị như fact đã xác minh.
- Ghi lý do chọn evidence: `scope_match`, `source_authority_for_attribute`, `revision_match`, `measurement_method`, `recency`, `reviewer_decision`.

### 5.3 Schema thuộc tính chuyên ngành

**Màn hình:** kích thước và độ cong; độ phân giải; panel; refresh rate; response time kèm chuẩn đo; độ sáng SDR/HDR và điều kiện; gamut/coverage; HDR certification; cổng và băng thông; VRR; VESA/stand; revision.

**Âm thanh:** loại thiết bị; driver/transducer; codec và profile; ANC/transparency; microphone; kết nối; pin kèm mức âm lượng/codec/ANC/điều kiện đo; trở kháng/độ nhạy nếu công bố; fit/size nếu liên quan.

**Máy lọc không khí:** CADR kèm chuẩn/điều kiện test; phòng khuyến nghị và giả định; loại/mã filter; tuổi thọ filter và điều kiện; độ ồn theo từng mức; lưu lượng gió; công suất; cảm biến; chi phí vật tư thay thế.

**Laptop:** CPU/GPU đúng mã; RAM dung lượng/chuẩn/kênh/hàn/nâng cấp; SSD và slot; panel/màn hình; pin kèm điều kiện thử; cổng/băng thông; adapter; trọng lượng; OS; mã cấu hình thương mại; bảo hành.

Không tự điền thuộc tính chuyên ngành từ tên marketing, ảnh hoặc listing thiếu chứng cứ. Unit conversion phải lưu cả raw value và normalized value.

---

## 6. Ingestion, adapter và vận hành API/feed

### 6.1 Pipeline bắt buộc

```text
Source Registry
  → Permission Pre-check
  → Fetch (API/feed/manual authorized import)
  → Parse + Contract Validation
  → Raw Evidence Reference (only if permitted)
  → Normalize
  → Identity Match (Model/Variant)
  → Fact/Offer Validation
  → Freshness + Anomaly Check
  → Quarantine or Approve
  → Publish Projection
  → Monitoring + Reconciliation
```

### 6.2 Adapter contract

Mỗi adapter phải khai báo:

- `adapter_id`, semantic version và supported source schema versions.
- Authentication profile reference; không in token/secret vào log.
- Endpoint/method, request scope, allowed parameters, pagination/cursor và rate limit.
- Mappings source field → canonical field, transformation/unit/currency/timezone.
- Null semantics, enum mapping, fallback policy và fields ignored.
- Error map: retryable, non-retryable, authorization, rate-limited, schema drift.
- Permission grants cần có trước khi fetch/store/display.
- Test fixtures đã loại bỏ secret/PII và expected normalized output.

### 6.3 IngestionRun và idempotency

Mỗi run ghi: `run_id`, `source_id`, adapter version, start/end UTC, cursor/page, request count, response code, received/parsed/inserted/updated/unchanged/quarantined counts, retry count, `Retry-After`, error class và checksum/reference.

Idempotency key khuyến nghị:

`source_id + source_record_id + source_revision_or_updated_at`

Nếu nguồn không cấp record ID ổn định, Hoàng phải định nghĩa compound key có test collision; không dùng hash của tên hiển thị làm khóa duy nhất.

### 6.4 Quy tắc retry và bảo vệ hệ thống

- Exponential backoff có jitter và trần retry; tôn trọng `Retry-After`.
- Không retry lỗi 4xx không retryable; 401/403 phải cảnh báo permission/authentication và dừng nguồn tương ứng.
- Rate limit theo source; circuit breaker khi lỗi liên tiếp vượt ngưỡng cấu hình.
- Schema drift không được tự “đoán” mapping mới; dừng adapter hoặc đưa record vào quarantine.
- Crawl chỉ trong trường hợp có quyền/điều khoản cho phép; không vượt CAPTCHA, paywall, đăng nhập trái phép, rate limit hay biện pháp bảo vệ kỹ thuật.
- Không dùng session/cookie cá nhân ngoài phạm vi được cấp.

### 6.5 Raw retention

Không có mặc định “luôn lưu raw”. `RawSnapshot` chỉ lưu khi `PermissionGrant` cho phép `store_raw` và retention. Nếu không được lưu raw, chỉ lưu metadata được phép: source record ID, URL, timestamp, adapter version, checksum/hash và kết quả parse. Không được giữ bản sao trái điều khoản chỉ để phục vụ audit.

---

## 7. Freshness và cách hiển thị

### 7.1 Phân biệt thời điểm

- `source_updated_at`: timestamp do nguồn cung cấp, có thể thiếu hoặc sai.
- `observed_at`: thời điểm A+ nhận được dữ liệu.
- `validated_at`: thời điểm kiểm tra/duyệt.
- `published_at`: thời điểm projection được đưa ra public.
- `expires_at`: thời điểm hết freshness theo policy.

Không thay `observed_at` bằng timestamp nguồn; không coi nguồn không đổi dữ liệu là dữ liệu vừa được xác minh lại nếu fetch thất bại.

### 7.2 Freshness state

| State | Định nghĩa | Hành vi public |
|---|---|---|
| `fresh` | Trong SLA nguồn/trường và validation pass | Có thể hiển thị như thông tin hiện tại |
| `near_stale` | Gần hết SLA | Có thể hiển thị kèm timestamp, không khẳng định còn hàng nếu SLA stock ngắn |
| `stale` | Quá SLA | Không hiển thị giá/tồn như hiện tại; có thể giữ fact tĩnh nếu fact còn hiệu lực |
| `unknown` | Thiếu timestamp hoặc không xác định được SLA | Không khẳng định giá/tồn hiện tại |
| `invalid` | Dữ liệu lỗi/xung đột | Quarantine |

### 7.3 TTL khởi điểm để pilot — không phải cam kết đối tác

| Dữ liệu | Giá trị đề xuất | Điều kiện và hành vi |
|---|---:|---|
| Giá | 60 phút | Dùng làm ngưỡng pilot; nếu campaign/retailer có SLA ngắn hơn thì theo SLA ngắn hơn |
| Tồn kho | 30 phút | Hết hạn chuyển unknown/stale; không khẳng định còn hàng |
| Voucher/promotion | 60 phút hoặc expiry nguồn | Chặn khi hết hạn hoặc thiếu điều kiện áp dụng |
| Tracking link/campaign | Check theo lịch + khi campaign update; tối đa 24h không kiểm tra lại trong pilot | Không tạo link mới nếu campaign không active/Publisher không eligible |
| Fact OEM | 180 ngày hoặc ngay khi có revision mới | Recheck; không tự xóa dữ liệu lịch sử |
| Review/test | Theo sample/revision/firmware/method | Không áp cho revision mới nếu chưa xác minh tương đương |
| Permission/terms | Khi onboarding, khi nguồn báo đổi, và tối thiểu mỗi 90 ngày trong pilot | Quá hạn review chuyển `pending_review`, chặn hành động chưa còn được xác nhận |

TTL này chỉ là cấu hình khởi điểm nội bộ. Hoàng cần đo latency/feed behavior; Trâm Anh cần xác minh điều khoản/nguồn; CEO/Legal duyệt rủi ro trước khi chốt SLA public.

### 7.4 Tách giá khỏi khả năng bấm link

- Offer giá cũ không được hiển thị như giá hiện tại.
- Một tracking link còn hợp lệ không chứng minh giá/stock còn mới.
- Một offer stale không nhất thiết làm fact sản phẩm stale.
- Có thể giữ nút “Xem tại cửa hàng” chỉ khi destination/link còn hợp lệ và copy không ngụ ý còn hàng/giá cố định; nếu chưa xác thực link hoặc campaign thì ẩn CTA affiliate.
- Giá cá nhân hóa, voucher thành viên và giá trả góp phải gắn nhãn điều kiện; không so sánh trực tiếp với giá phổ thông.

---

## 8. Affiliate link, campaign và attribution

### 8.1 Eligibility gate

Trước khi tạo/hiển thị tracking link, kiểm tra:

1. Publisher/site A+ đã được network chấp thuận cho campaign tương ứng.
2. Campaign đang active và áp dụng cho đúng seller/product/category/traffic channel.
3. Destination URL nằm trong phạm vi được chấp thuận.
4. Tracking params/sub IDs được phép và không chứa dữ liệu cá nhân.
5. Terms/campaign version hiện tại đã được lưu.
6. Link được tạo bằng API/dashboard/công cụ được network cho phép và vượt qua kiểm tra hợp lệ.

### 8.2 Theo dõi

Lưu link creation request ID, campaign ID, destination, returned tracking URL, error/suspended URL, created_at, last_checked_at, link status và source/terms reference. Không giả lập conversion, không tự đặt đơn thử khi network không cho phép, không tự tuyên bố attribution window/commission khi terms không xác nhận.

### 8.3 Đối soát

Bảng giao dịch phải tách click, order, conversion, approved, rejected, reversed/cancelled và commission. Lưu kỳ báo cáo, currency, timezone, trạng thái cuối cùng và `transaction_id` của network. Đơn hàng không phải bằng chứng cho phép lưu PII người mua; chỉ nhận các trường network cho phép và cần cho đối soát.

### 8.4 Disclosure

Giao diện A+ phải thể hiện rõ quan hệ affiliate ở vị trí người dùng dễ nhận biết trước khi click; câu chữ cần do CEO/Legal duyệt, không dùng thông báo ẩn trong footer làm cơ chế duy nhất. Lưu phiên bản disclosure và ngày áp dụng.

---

## 9. Quyền dữ liệu và tuân thủ

### 9.1 Ma trận quyền tối thiểu

| Data class | Fetch | Store raw | Normalize | Display | Cache | Redistribute | Điều kiện bắt buộc |
|---|---:|---:|---:|---:|---:|---:|---|
| Model code/spec | Theo grant | Theo grant | Theo grant | Theo grant | Theo grant | Theo grant | Nguồn, accuracy, scope, attribution |
| Giá/stock | Theo grant | Theo grant | Theo grant | Theo grant | Theo grant | Theo grant | Freshness, seller/listing, cache TTL |
| Hình ảnh | Theo grant | Theo grant | Crop/resize chỉ khi cho phép | Theo grant | Theo grant | Không mặc định | Giấy phép ảnh cụ thể, attribution, duration |
| Mô tả/review | Theo grant | Theo grant | Trích tóm tắt chỉ khi cho phép | Theo grant | Theo grant | Không mặc định | Bản quyền, quote limits, license |
| Feed/raw payload | Theo grant | Theo grant | Theo grant | Không mặc định | Theo grant | Không mặc định | Terms, retention, security |
| Tracking link | Theo campaign | Theo network | Không tự rewrite | Theo campaign | Theo terms | Không tự phân phối | Publisher/campaign approval |
| Click/conversion | Theo API/terms | Theo grant | Theo grant | Không public | Theo grant | Không mặc định | Purpose limitation, privacy, retention |

### 9.2 Cập nhật pháp lý Việt Nam cần đưa vào checklist

**Tình trạng kiểm tra: 12/11/2026. Đây là rà soát sơ bộ tài liệu pháp luật, không phải ý kiến pháp lý.**

1. **Luật Thương mại điện tử 122/2025/QH15** được ban hành ngày 10/12/2025 và có hiệu lực 01/07/2026. Luật định nghĩa affiliate marketing trong thương mại điện tử là hoạt động quảng cáo thông qua link/mã giới thiệu liên kết với sàn; Điều 25 quy định trách nhiệm của tổ chức/cá nhân cung cấp dịch vụ affiliate; Điều 26 quy định trách nhiệm của affiliate, bao gồm nghĩa vụ từ chối một số nền tảng/nội dung và gỡ link liên quan hàng hóa/dịch vụ vi phạm hoặc theo yêu cầu cơ quan có thẩm quyền. A+ cần xác định vai trò vận hành thực tế: là affiliate/publisher, hay còn cung cấp dịch vụ tạo link/mã giới thiệu cho bên khác. Không mặc định hai vai trò này giống nhau.
2. **Nghị định 248/2026/NĐ-CP** được ban hành 30/06/2026 và có hiệu lực 01/07/2026, quy định chi tiết một số điều của Luật Thương mại điện tử. Nghị định có quy trình thông báo cho nền tảng bán hàng trực tiếp có chức năng đặt hàng và đăng ký cho nền tảng trung gian/mạng xã hội/tích hợp theo mô hình tương ứng. Luật định nghĩa chức năng đặt hàng là chức năng cho phép thực hiện hợp đồng điện tử trên nền tảng. Vì vậy, Legal phải đánh giá chức năng thực tế của A+ (chỉ so sánh và chuyển link ra ngoài hay có luồng đặt hàng/hợp đồng, trung gian seller hoặc dịch vụ nền tảng khác); không kết luận chỉ từ tên gọi “affiliate website”.
3. **Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15** có hiệu lực 01/01/2026. Click ID, sub ID, analytics, cookie/device identifiers và dữ liệu giao dịch phải được thiết kế theo nguyên tắc tối thiểu hóa, giới hạn mục đích, kiểm soát truy cập, retention và quy trình xử lý yêu cầu của chủ thể dữ liệu theo phạm vi luật áp dụng. Không đưa email, số điện thoại, tên, địa chỉ hoặc mã định danh cá nhân vào `sub_id`/tracking params.
4. **Luật sửa đổi Luật Quảng cáo 75/2025/QH15** có hiệu lực 01/01/2026. Nội dung quảng cáo và người chuyển tải quảng cáo có nghĩa vụ tương ứng theo luật; nếu A+ đăng nội dung mang tính giới thiệu/quảng cáo hoặc có người có ảnh hưởng tham gia, Legal cần review quy trình kiểm chứng nội dung, disclosure và bằng chứng. Không nên suy diễn rằng mọi quy định về người có ảnh hưởng áp dụng đồng nhất cho mọi publisher.
5. Cục Thương mại điện tử đăng thông báo ngày 14/10/2026 về việc triển khai Luật 122/2025 và Nghị định 248/2026; ngày 26/10/2026 có thông báo mời các chủ quản nền tảng làm việc về định danh, xác thực tài khoản của người bán, người livestream và người tiếp thị liên kết với VNeID. Đây là dấu hiệu cần theo dõi về thực thi; thông báo mời họp không tự nó thay thế văn bản quy phạm hoặc đặc tả kỹ thuật cuối cùng. A+ cần xác minh quy trình định danh hiện hành với network/đơn vị dịch vụ affiliate và Legal, không tự kết luận phải tích hợp VNeID theo một API chưa được công bố.
6. **Luật Bảo vệ quyền lợi người tiêu dùng 2023 và pháp luật sở hữu trí tuệ** tiếp tục nằm trong review checklist về tính chính xác, thông tin gây nhầm lẫn, nội dung/ảnh và xử lý khiếu nại. Cần Legal kiểm tra văn bản hợp nhất, nghị định/thông tư hướng dẫn và điều khoản network/retailer đang có hiệu lực tại thời điểm ký kết.

### 9.3 Legal go-live checklist

- [ ] Có legal memo ngắn phân loại mô hình A+ theo chức năng thực tế, phạm vi affiliate và nghĩa vụ tương ứng.
- [ ] Xác định nghĩa vụ notification/registration (nếu có) theo Luật 122/2025 và Nghị định 248/2026; không tự suy ra từ việc website chỉ có hoặc không có nút mua.
- [ ] Có Terms of Use, Privacy Notice, Affiliate Disclosure, Contact/Complaint route được duyệt.
- [ ] Hợp đồng/terms mỗi network và campaign được lưu version; xác minh publisher/site approval và traffic restrictions.
- [ ] Quyền ảnh, mô tả, giá, feed, dữ liệu click/conversion được duyệt riêng.
- [ ] Quy trình gỡ link/sản phẩm bị cảnh báo, khiếu nại và lưu evidence có owner/SLA.
- [ ] Kiểm tra consent/analytics, retention và truy cập dữ liệu cá nhân theo Luật 91/2025.
- [ ] Kiểm tra nội dung quảng cáo/disclosure theo Luật 75/2025.

---

## 10. Quarantine, incident và release control

### 10.1 Severity

| Mức | Ví dụ | Hành động ngay |
|---|---|---|
| `Q0_CRITICAL` | Nguồn/campaign bị cấm hoặc permission bị thu hồi; link dẫn tới hàng hóa/dịch vụ vi phạm theo thông báo đáng tin; rò rỉ secret/PII | Kill switch source/campaign; unpublish link/offer liên quan; báo CEO/Legal/Hoàng |
| `Q1_IDENTITY` | Sai model/variant; GTIN/MPN/region mâu thuẫn; seller/listing không xác định | Chặn offer; không ảnh hưởng fact model khác nếu không liên quan |
| `Q2_COMMERCE` | Giá/stock bất thường; currency, promotion, ship/tax không rõ; feed stale | Ẩn trường giá/stock/CTA có liên quan; giữ fact độc lập nếu hợp lệ |
| `Q3_TECHNICAL` | Schema drift, parse lỗi, pagination thiếu, link lỗi | Tạm dừng adapter/source projection; không phát hành record mới chưa validate |
| `Q4_METADATA` | Thiếu alias, mô tả hoặc trường không trọng yếu | Cảnh báo và đưa review queue; không chặn trường đã được chứng minh nếu risk không lan rộng |

### 10.2 State machine

```text
received → parsed → normalized → validated → approved → published
    └────────────── any blocking rule ─────────────→ quarantined
quarantined → under_review → approved → published
                         └→ rejected / source_suspended
published → stale / paused / withdrawn / retired
```

Không tự chuyển `quarantined` sang `published`. Release phải có reviewer, evidence reference, resolution reason và audit timestamp.

### 10.3 Phạm vi cách ly

Quarantine ở mức nhỏ nhất đủ an toàn: `field/claim`, `variant`, `offer`, `tracking_link`, `campaign` hoặc `source`. Chỉ quarantine toàn source nếu rủi ro là source-wide (permission revoke, credential compromise, schema mapping sai diện rộng). Tránh làm mất dữ liệu đúng không liên quan.

### 10.4 Audit fields

`quarantine_id`, `severity`, `reason_code`, `detected_at`, `detected_by` (system/user), `affected_entity_type/id`, `evidence_refs[]`, `review_owner`, `review_started_at`, `resolution`, `released_by`, `released_at`, `change_log_ref`.

### 10.5 Mục tiêu xử lý pilot đề xuất

- Q0: chặn public ngay bằng kill switch; báo người có trách nhiệm ngay trong ca trực.
- Q1/Q2: chặn dữ liệu sai khỏi public ngay khi phát hiện; review trong 1 ngày làm việc.
- Q3: dừng adapter bị ảnh hưởng và review trong 1 ngày làm việc.
- Q4: review trong 3 ngày làm việc.

Đây là mục tiêu vận hành nội bộ đề xuất, cần Hoàng/CEO xác nhận nguồn lực; không phải thời hạn pháp luật.

---

## 11. Test plan và tiêu chí nghiệm thu

### 11.1 Bộ test bắt buộc cho từng adapter

**Contract & ingestion**
- Parse đúng UTF-8, encoding, decimal, currency, locale, timezone, null, boolean và enum.
- Pagination không bỏ sót hoặc lặp record; cursor hết hạn được xử lý đúng.
- Idempotent: chạy lại không tạo record/observation sai hoặc duplicate.
- Retry, `Retry-After`, circuit breaker và lỗi 401/403/429/5xx có hành vi riêng.
- Schema drift làm fail/quarantine, không tự map đoán.

**Identity & facts**
- GTIN/MPN/model code/region/revision match đúng; fuzzy-only không thể publish.
- Variant laptop khác RAM/SSD/GPU không bị merge.
- Fact hãng và kết quả đo thử không ghi đè lẫn nhau.
- Conflict có trạng thái disputed và lưu cả evidence.

**Offer & price**
- Thiếu price/stock/ship/tax không bị mặc định thành 0, in-stock hoặc included.
- Giá voucher/member/installment được gắn điều kiện.
- Giá âm, 0 hoặc biến động bất thường phát hiện được theo rule.
- Offer observation cũ vẫn giữ nguyên; observation mới không xóa lịch sử.

**Rights, tracking & security**
- Source chưa có grant tương ứng không thể fetch/store/display.
- Ảnh không được publish chỉ dựa trên grant cho giá.
- Campaign inactive, publisher ineligible hoặc permission expired không tạo/hiển thị affiliate link.
- Token/secret/PII không xuất hiện trong logs hoặc `sub_id`.

**Quarantine & rollback**
- Mỗi severity có rule và action tương ứng.
- Q0 kill switch thu hồi ngay link/offer liên quan.
- Release cần reviewer và audit trail.
- Rollback adapter/version không xóa Product Fact hợp lệ không liên quan.

### 11.2 Acceptance criteria pilot

| Chỉ tiêu | Ngưỡng tối thiểu |
|---|---:|
| Offer public có variant, seller, source, URL, currency, observed_at và freshness | 100% |
| Giá public có price type và điều kiện cần thiết | 100% |
| Product Fact public có scope, unit, evidence/provenance và status | 100% |
| Nguồn có owner + terms + permission grants phù hợp | 100% |
| Public variant match bằng fuzzy-only | 0 |
| Public image thiếu image grant | 0 |
| Tracking link thiếu campaign/publisher approval | 0 |
| Null stock/ship/tax bị chuyển thành trạng thái tích cực | 0 |
| Các test Q0–Q3 và rollback | 100% pass |
| Offer stale vẫn hiển thị như current | 0 |

### 11.3 Monitoring tối thiểu

- `fetch_success_rate` và `records_parsed_rate` theo source/adapter.
- `schema_drift_count`, `auth_error_count`, `rate_limit_count`.
- `public_offer_freshness_pct` và số offer stale theo tuổi.
- `identity_match_conflict_rate`, `manual_review_backlog`, `quarantine_age`.
- `price_anomaly_rate`, `broken_tracking_link_rate`, `campaign_suspended_count`.
- `permission_expiry_due` và số record public phụ thuộc grant sắp hết hạn.
- `affiliate_click/order/reversal reconciliation` theo kỳ network; không dùng click/conversion làm chỉ số chất lượng sản phẩm.

Hoàng cần chốt dashboard, ngưỡng alert, owner và đường xử lý sự cố. Không được chỉ đo số record ingest thành công; phải đo tỷ lệ record đủ điều kiện public.

---

## 12. RACI và quyết định cần phê duyệt

| Công việc | Trâm Anh | Hoàng | A Long | Vân Anh | CEO | Legal |
|---|---|---|---|---|---|---|
| Nghiên cứu nguồn, terms, publisher/campaign evidence | R | C | C | I | A | C |
| Thiết kế adapter, storage, monitoring, security | C | R/A | C | I | I | C |
| Schema fact và định nghĩa chuyên môn ngành | C | C | R/A | C | I | I |
| Cách diễn giải offer/disclosure trong UX | C | C | C | R | A | C |
| Permission và pháp lý | R (thu thập bằng chứng) | C | I | I | A | R/A chuyên môn |
| Quyết định production/release policy | C | R (technical sign-off) | C | C | A | C |

R = Responsible; A = Accountable; C = Consulted; I = Informed. Bảng này là đề xuất; CEO xác nhận phân quyền cuối cùng.

### 12.1 Quyết định cần CEO/Hoàng/A Long/Legal chốt

1. Canonical identity: chọn `ProductModel` + `ProductVariant` như đề xuất hay điều chỉnh theo data model hiện có?
2. Danh sách category fields và đơn vị/enum chuẩn do A Long xác nhận.
3. Database/event store và retention của `OfferObservation`/`FactEvidence` theo giới hạn quyền.
4. TTL/SLA theo nguồn và hành vi khi stale; xác nhận ngân sách fetch và alert.
5. Ai được approve/release claim, offer, image và tracking link?
6. Legal classification của A+ theo chức năng thực tế; nghĩa vụ liên quan Luật 122/2025/QH15 và Nghị định 248/2026/NĐ-CP.
7. Disclosure, Privacy Notice, analytics/cookie policy và quy trình yêu cầu dữ liệu cá nhân.
8. Source/campaign cụ thể nào đủ điều kiện pilot, có bằng chứng permission tương ứng.

---

## 13. Kế hoạch triển khai đề xuất theo cổng

### Gate 0 — Design sign-off

Đầu ra: schema đã thống nhất; identity contract; PermissionGrant; lifecycle state machine; legal classification memo. Không ingest production data.

### Gate 1 — One-source sandbox

Chọn **một** nguồn có API/feed và grant rõ, lấy sample nhỏ cho một category. Hoàng chạy adapter ở sandbox; Trâm Anh xác minh terms/mapping; A Long kiểm tra model/variant/fact. Tắt public publish.

### Gate 2 — Shadow mode

Chạy đồng thời với nguồn gốc, so sánh price/stock, duplicate, variant mismatch, freshness, schema drift và quarantine. Không dùng dữ liệu shadow để hiển thị public.

### Gate 3 — Limited publish

Chỉ bật nguồn/campaign đã pass rights, identity, freshness, tracking, legal disclosure và rollback test. Giới hạn record/traffic; giám sát thủ công.

### Gate 4 — Expand

Mở rộng thêm nguồn/category chỉ khi adapter, permission và KPI của Gate 3 ổn định. Không nhân rộng bằng copy-paste adapter mà không có contract tests.

---

## 14. Checklist onboarding nguồn — bản dùng thực tế

### A. Nguồn và quyền
- [ ] Source Registry có source owner và legal entity.
- [ ] Terms URL/version, ngày kiểm tra và bằng chứng approval đã lưu.
- [ ] Có PermissionGrant cho từng data class × action × purpose.
- [ ] Đã xác minh quyền ảnh riêng; không suy diễn từ quyền feed/giá.
- [ ] Retention/raw payload/cache/attribution đã được xác định.

### B. Tích hợp
- [ ] API/feed schema, authentication, rate limit, pagination được ghi nhận.
- [ ] Secret nằm trong secret manager; log đã kiểm tra không chứa token/PII.
- [ ] Có sample fixture hợp lệ và lỗi; mapping/version có reviewer.
- [ ] Idempotency, retry, circuit breaker và schema drift đã test.

### C. Identity và dữ liệu
- [ ] Model/Variant mapping có model code/MPN/GTIN/region/variant signature.
- [ ] Fact claims có evidence ở đúng scope.
- [ ] Offer có seller/listing/variant/condition/currency và observation timestamp.
- [ ] Giá, stock, promotion, ship và tax có null semantics rõ.

### D. Affiliate và public
- [ ] Publisher/site và campaign được duyệt.
- [ ] Tracking link được tạo theo đúng network flow; link health được kiểm tra.
- [ ] Disclosure và destination page đã được Legal duyệt.
- [ ] Freshness, quarantine, kill switch, rollback và monitoring pass.
- [ ] Có người approve cuối và audit trail.

---

## 15. Ví dụ dữ liệu tham chiếu

Các ví dụ sau chỉ minh họa cấu trúc, không phải record hoặc API response có thật.

### 15.1 ProductVariant

```json
{
  "product_variant_id": "A-VAR-EXAMPLE-001",
  "product_model_id": "A-MOD-EXAMPLE-001",
  "market_region": "VN",
  "variant_signature": {
    "cpu": "Example CPU 7",
    "gpu": "Integrated",
    "ram_gb": 16,
    "storage_gb": 512,
    "color": "silver"
  },
  "mpn": "MPN-EXAMPLE-001",
  "gtin": null,
  "variant_status": "candidate"
}
```

### 15.2 ProductFactClaim + Evidence

```json
{
  "claim_id": "CLM-EXAMPLE-001",
  "subject_type": "variant",
  "subject_id": "A-VAR-EXAMPLE-001",
  "attribute_key": "ram_gb",
  "value": 16,
  "unit": "GB",
  "claim_status": "verified",
  "selected_evidence_id": "EVD-EXAMPLE-001",
  "reviewed_at": "2026-11-12T05:00:00Z"
}
```

```json
{
  "evidence_id": "EVD-EXAMPLE-001",
  "claim_id": "CLM-EXAMPLE-001",
  "source_id": "SRC-OEM-001",
  "source_url": "https://manufacturer.example/spec",
  "observed_at": "2026-11-12T04:30:00Z",
  "evidence_status": "supporting",
  "source_revision": "spec-rev-A"
}
```

### 15.3 OfferObservation

```json
{
  "observation_id": "OBS-EXAMPLE-001",
  "retail_offer_id": "OFF-EXAMPLE-001",
  "observed_at": "2026-11-12T05:00:00Z",
  "currency": "VND",
  "sale_price": 24990000,
  "price_type": "regular",
  "shipping_fee": null,
  "tax_status": "unknown",
  "stock_status": "unknown",
  "freshness_status": "fresh",
  "source_record_ref": "record-123"
}
```

---

## 16. Nguồn tham chiếu và giới hạn xác minh

**Nguồn được kiểm tra ngày 12/11/2026:**

1. Chính phủ — Luật Thương mại điện tử 122/2025/QH15, gồm định nghĩa affiliate marketing, Điều 14 về quản lý nền tảng và Điều 25–26 về trách nhiệm của nhà cung cấp dịch vụ affiliate và affiliate: https://en.baochinhphu.vn/viet-nams-law-on-e-commerce-111260825143234285.htm
2. Cổng văn bản Chính phủ — Luật số 122/2025/QH15, ban hành 10/12/2025, hiệu lực 01/07/2026: https://vanban.chinhphu.vn/?classid=1&docid=216503&pageid=27160&typegroupid=3
3. Cổng văn bản Chính phủ — Nghị định 248/2026/NĐ-CP, ban hành 30/06/2026, hiệu lực 01/07/2026: https://vanban.chinhphu.vn/?docid=218747&orggroupid=2&pageid=27160
4. Bộ Công an — Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15, hiệu lực 01/01/2026: https://mps.gov.vn/chinh-sach-phap-luat/co-so-du-lieu-van-ban/luat-bao-ve-du-lieu-ca-nhan-1753688803
5. Cổng văn bản Chính phủ — Luật sửa đổi Luật Quảng cáo 75/2025/QH15, hiệu lực 01/01/2026: https://vanban.chinhphu.vn/?classid=1&docid=214561&pageid=27160
6. AccessTrade Developer Docs — API Publisher mô tả các chức năng campaign, tạo tracking link, giao dịch, sản phẩm và datafeed: https://developers.accesstrade.vn/api-publisher-vietnamese
7. AccessTrade Developer Docs — tạo tracking link bằng campaign ID, URL đích và tham số tracking: https://developers.accesstrade.vn/api-publisher-vietnamese/tao-tracking-link.md
8. Schema.org — Offer: các thuộc tính chuẩn hóa `price`, `priceCurrency`, `availability`, `seller` và quan hệ với Product: https://schema.org/Offer
9. Cục Thương mại điện tử/Bộ Công Thương — thông tin cập nhật về triển khai Luật TMĐT và trao đổi về định danh điện tử cho người tiếp thị liên kết, thông báo 26/10/2026: https://online.gov.vn/Home/WebDetails/132595
10. Cục Thương mại điện tử/Bộ Công Thương — hệ thống văn bản pháp luật, liệt kê Luật 122/2025/QH15 và Nghị định 248/2026/NĐ-CP cùng ngày hiệu lực: https://online.gov.vn/SCT_DN/van-ban-phap-luat

**Giới hạn:** việc tài liệu API tồn tại không chứng minh A+ đã được cấp quyền, có Publisher approval, có campaign cụ thể, có quyền lưu/hiển thị feed hoặc được phép dùng mọi tham số. Từng network/retailer phải được onboarding và kiểm tra bằng tài khoản/terms thực tế. Tài liệu pháp luật cần Legal rà soát văn bản tiếng Việt chính thức, văn bản hướng dẫn và cách áp dụng cho mô hình kinh doanh thực tế của A+ trước go-live.

---

## 17. Kết luận và trạng thái khuyến nghị

**Trạng thái đề xuất:** `READY_FOR_CROSS_FUNCTIONAL_REVIEW`, không phải `PRODUCTION_APPROVED`.

V1.1 làm rõ các phần mà v1.0 còn mơ hồ: identity Model/Variant, evidence/provenance ở cấp fact, lịch sử offer observation, tracking link độc lập, permission theo data class/action/purpose, freshness state, quarantine severity và legal gates. Mô hình này giảm rủi ro ghép nhầm cấu hình, hiển thị sai giá/tồn kho, dùng ảnh/feed vượt quyền và mất khả năng truy nguyên khi xảy ra sự cố.

**Điều kiện trước khi triển khai:** Hoàng xác nhận khả năng kỹ thuật và storage/monitoring; A Long chốt field chuyên môn và scope fact; Trâm Anh cung cấp bằng chứng source/terms/campaign; Legal xác nhận phân loại và nghĩa vụ; CEO phê duyệt các policy/risk acceptance. Cho đến khi các sign-off này hoàn tất, dữ liệu mới nên chạy sandbox/shadow mode và chưa tự động publish.
