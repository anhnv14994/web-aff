# A+ — Affiliate Decision Platform

A+ là dự án xây dựng một nền tảng affiliate tự động, lấy **chất lượng quyết định mua hàng của khách hàng** làm trung tâm.

Website không chỉ liệt kê sản phẩm hoặc so sánh giá. A+ giúp khách hàng làm rõ nhu cầu, hiểu khác biệt giữa các lựa chọn, nhận biết đánh đổi và tìm được sản phẩm phù hợp; sau đó kết nối tới nhà bán thông qua liên kết affiliate.

## Mục tiêu

1. Giúp khách hàng hiểu rõ mình cần gì và chọn sản phẩm phù hợp hơn.
2. Tạo trải nghiệm tìm hiểu, so sánh và ra quyết định đáng tin cậy.
3. Xây dựng hệ thống tự động thu thập, chuẩn hóa, đánh giá, xuất bản và cập nhật dữ liệu/nội dung.
4. Tạo doanh thu affiliate có thể đo lường, đối soát và tối ưu bền vững.
5. Xây dựng nội dung có ích, có bằng chứng, dễ được công cụ tìm kiếm và hệ thống AI truy xuất/trích dẫn.

**AI visibility là kênh phân phối, không phải mục tiêu kinh doanh cuối cùng.** Thành công phải đồng thời gắn với giá trị khách hàng, hành vi clickout và doanh thu affiliate.

## Nguyên tắc không được vi phạm

- Mức độ phù hợp với khách hàng phải độc lập với hoa hồng affiliate. Không nâng hạng sản phẩm chỉ vì hoa hồng cao.
- Không bịa thông số, giá, tình trạng hàng, trải nghiệm, đánh giá hoặc bằng chứng.
- Phân biệt rõ dữ kiện đã xác minh, dữ kiện do nguồn cung cấp và giả thuyết/chưa xác minh.
- Khi dữ liệu thiếu, mâu thuẫn hoặc rủi ro cao: đánh dấu, hạn chế hiển thị hoặc chờ xác minh; không tự suy diễn.
- Nội dung affiliate phải tạo giá trị thực, không chỉ là trang mỏng chứa liên kết.
- Tự động hóa quy trình thường ngày; con người đặt quy tắc, duyệt thay đổi quan trọng và kiểm tra chất lượng định kỳ.
- Giữ phạm vi gọn: chưa mở rộng đa ngành, app di động, API B2B, huấn luyện model riêng hay kiến trúc microservices khi chưa có bằng chứng cần thiết.

## Ba động cơ cốt lõi

1. **Product & Offer Engine:** dữ liệu sản phẩm chuẩn, định danh model/variant, giá, nhà bán, affiliate URL, lịch sử và độ tin cậy dữ liệu.
2. **Customer Decision Engine:** hiểu nhu cầu, hỏi tối thiểu, lọc/xếp hạng theo độ phù hợp, giải thích ưu nhược điểm và đánh đổi.
3. **Affiliate & Growth Engine:** trang sản phẩm/so sánh, SEO và AI retrievability, clickout tracking, đối soát hoa hồng và đo hiệu quả.

## Nhóm năng lực

- Customer Psychology & Decision Science — Vân Anh.
- Product Expertise — chuyên gia ngành hàng.
- Product & Market Intelligence — dữ liệu sản phẩm, thị trường, nguồn bán.
- Affiliate Business — đối tác, tracking, điều kiện ghi nhận và đối soát.
- SEO/GEO & Growth — phân phối, khả năng truy xuất, đo lường.
- Product Engineering & Analytics — hệ thống, tự động hóa, kiểm thử và phân tích.

Một người có thể kiêm nhiều nhóm ở giai đoạn đầu. Đây là các **năng lực cần có**, không phải yêu cầu tuyển đủ sáu nhân sự.

## Trạng thái quyết định

- Thị trường khởi đầu: Việt Nam.
- Phạm vi: chọn một ngành hàng tập trung để thử nghiệm.
- Ngành hàng MVP: **chưa chốt**; phải đánh giá dữ liệu, affiliate economics, mức độ cần tư vấn và khả năng tạo khác biệt trước khi quyết định.
- Quy mô thử nghiệm tham khảo: khoảng 100–300 model chuẩn, 1–2 nguồn affiliate khả thi; điều chỉnh sau khi khảo sát thực tế.
- Audio là ứng viên có lợi thế kiến thức chuyên môn, nhưng chưa được mặc định là ngành hàng MVP.

## Tài liệu điều hành

- [Project Charter & Operating Process](docs/PROJECT-CHARTER.md) — mục tiêu, phạm vi, vai trò, quy trình, lộ trình và tiêu chí quyết định.

## Cách ra quyết định

Mọi đề xuất mở rộng hoặc thay đổi lớn cần trả lời:
1. Vấn đề khách hàng/kinh doanh cụ thể là gì?
2. Bằng chứng nào cho thấy vấn đề có thật?
3. Tác động dự kiến đến trải nghiệm, vận hành hoặc doanh thu?
4. Chi phí và rủi ro triển khai?
5. Có thể kiểm thử nhỏ trước khi đầu tư lớn không?

Không thêm tính năng chỉ vì công nghệ cho phép.
