# A Long — Task Inbox

**Vai trò:** Technical Lead  
**Nguồn công việc chính thức:** GitHub Issues được assign cho tài khoản GitHub của bạn.

## Bắt đầu mỗi phiên làm việc
1. Mở [Issues được giao](https://github.com/anhnv14994/web-aff/issues?q=is%3Aopen+assignee%3A%40me).
2. Kiểm tra Issue/comment/PR mới; chỉ bắt đầu khi task có status:ready.
3. Xác nhận CLAIMED; ghi blocker và giả định trước khi code.
4. Với task implementation, đọc contract đã duyệt và không tự quyết định semantics nghiệp vụ.
5. Tạo PR nhỏ, chạy test, ghi commit/test result và cập nhật Issue.

## Bộ lọc
- [Issues đang mở được giao cho tôi](https://github.com/anhnv14994/web-aff/issues?q=is%3Aopen+assignee%3A%40me)
- [Việc READY](https://github.com/anhnv14994/web-aff/issues?q=is%3Aopen+label%3Astatus%3Aready)
- [PR đang mở](https://github.com/anhnv14994/web-aff/pulls)

## Quy tắc
- Tuân thủ ROLE.md và WORKFLOW.
- Không code trên giả định chưa được duyệt; ghi decision request khi contract xung đột.
- Không tích hợp nguồn thật, dùng credentials, crawl, publish hoặc deploy nếu chưa có approval.
- Không tự đóng Issue; chờ CEO nghiệm thu.