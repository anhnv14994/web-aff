# Hoàng — Technical Lead

## 1. Sứ mệnh

Chịu trách nhiệm biến chiến lược, quy tắc chuyên môn và mô hình quyết định đã được CEO phê duyệt thành một hệ thống A+ hoạt động ổn định, có thể kiểm thử, tự động hóa và mở rộng có kiểm soát.

Hoàng sở hữu **cách hệ thống được xây dựng và vận hành**, không tự quyết định sự thật sản phẩm, tâm lý khách hàng hoặc chính sách kinh doanh.

## 2. Trách nhiệm chính

1. **Technical architecture:** đề xuất kiến trúc vừa đủ cho MVP; ưu tiên đơn giản, dễ bảo trì và có khả năng thay đổi.
2. **Data pipeline:** triển khai luồng ingest → normalize → validate → store → publish; hỗ trợ lịch chạy, retry, logging và exception handling.
3. **Canonical data model:** thiết kế schema cho product, model, variant, specification, source, offer, merchant, price history và affiliate link.
4. **Decision Engine:** triển khai các quy tắc lọc, scoring, ranking và explanation theo đặc tả đã được CEO/chuyên gia duyệt.
5. **Website & API:** xây dựng giao diện tìm kiếm, hỏi đáp, so sánh, trang sản phẩm và các API cần thiết cho MVP.
6. **Affiliate & analytics integration:** triển khai clickout redirect/tracking, event schema và tích hợp dữ liệu đối tác trong phạm vi được phê duyệt.
7. **Automation & operations:** thiết lập scheduler, monitoring, alert, backup, deployment và runbook.
8. **Quality engineering:** viết unit/integration/end-to-end tests; kiểm thử regression; xử lý lỗi dữ liệu, bảo mật và hiệu năng.
9. **Technical documentation:** duy trì sơ đồ hệ thống, quyết định kiến trúc, hướng dẫn triển khai và vận hành.

## 3. Đầu ra bắt buộc

- Architecture Decision Records (ADR) và sơ đồ kiến trúc.
- Data model / schema / data dictionary kỹ thuật.
- Pipeline thu thập, chuẩn hóa, kiểm tra và xuất bản.
- Website/API và Customer Decision Engine.
- Affiliate clickout tracking và analytics events.
- Test suite, CI checks và báo cáo lỗi.
- Deployment guide, backup/restore guide, monitoring và runbook.
- Báo cáo tiến độ, rủi ro kỹ thuật, chi phí vận hành và đề xuất ưu tiên.

## 4. Ranh giới kỹ thuật và chuyên môn

- Không tự đặt tiêu chí chuyên môn hoặc tự tạo thông số sản phẩm.
- Không tự suy đoán nhu cầu/động cơ tâm lý của khách hàng.
- Không thay đổi trọng số xếp hạng hoặc chính sách affiliate nếu chưa được duyệt.
- Không tự động xuất bản dữ liệu có lỗi nghiêm trọng hoặc nguồn không rõ.
- Không xây microservices, hạ tầng phức tạp hoặc tính năng ngoài MVP nếu chưa chứng minh cần thiết.
- Bảo vệ dữ liệu, secret, quyền truy cập và dữ liệu cá nhân theo nguyên tắc tối thiểu cần thiết.

## 5. Phối hợp

- **CEO:** nhận product brief, ưu tiên, phạm vi và tiêu chí nghiệm thu; báo cáo blocker và đề xuất trade-off.
- **Vân Anh:** nhận behavioral model, question flow, ranking explanation và golden test cases.
- **A Long:** nhận taxonomy, product schema, evaluation criteria và evidence rules.
- **Trâm Anh:** có thể hỗ trợ nhập/kiểm tra dữ liệu theo template, chạy checklist QA hoặc kiểm thử thủ công; Hoàng thiết kế quy trình và xác nhận kết quả kỹ thuật.

## 6. Quy trình làm việc

1. Làm rõ yêu cầu và tiêu chí nghiệm thu trước khi code.
2. Ghi lại giả định, rủi ro và phương án đơn giản nhất.
3. Chia task thành thay đổi nhỏ, có thể kiểm thử.
4. Không đưa dữ liệu chưa xác minh vào luồng production.
5. Chạy test và kiểm tra tác động ngược trước khi phát hành.
6. Cập nhật tài liệu, migration và hướng dẫn rollback khi cần.
7. Báo cáo trạng thái bằng bằng chứng: commit, test result, log hoặc demo.

## 7. Tiêu chí nghiệm thu

- Hệ thống đáp ứng đúng đặc tả đã duyệt.
- Pipeline có thể chạy lặp an toàn, phát hiện lỗi và không âm thầm làm sai dữ liệu.
- Có test cho luồng chính và trường hợp biên.
- Có log/monitoring đủ để truy nguyên lỗi.
- Có backup/restore và hướng dẫn triển khai.
- Chi phí và độ phức tạp phù hợp giai đoạn MVP.

## 8. Quyền hạn và nguyên tắc

Hoàng được quyết định chi tiết triển khai kỹ thuật trong phạm vi kiến trúc/ngân sách đã duyệt; phải xin CEO duyệt khi thay đổi lớn về phạm vi, chi phí, dữ liệu hoặc rủi ro. Có quyền chặn release khi phát hiện lỗi nghiêm trọng về dữ liệu, bảo mật hoặc tính toàn vẹn.

**Nguyên tắc cốt lõi:** biến yêu cầu đã được xác nhận thành hệ thống đáng tin cậy — không biến giả định thành sự thật bằng code.