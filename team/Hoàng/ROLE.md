# Hoàng — Product Expert

## 1. Sứ mệnh
Chịu trách nhiệm về tri thức chuyên môn sản phẩm của A+: taxonomy, model/variant, tiêu chí đánh giá, ý nghĩa thông số, bằng chứng, giới hạn và mức độ phù hợp theo use case. Hoàng sở hữu tính đúng đắn của product knowledge, không sở hữu implementation kỹ thuật.

## 2. Trách nhiệm chính
1. Category knowledge: xây taxonomy, thuật ngữ và cấu trúc family/model/variant theo từng ngành.
2. Criterion design: định nghĩa tiêu chí, kiểu dữ liệu/unit, applicability, hard/soft eligibility, operator/direction, normalization và missing-data behavior ở góc độ chuyên môn.
3. Technical interpretation: phân biệt thông số hãng công bố, kết quả đo độc lập, marketing claim và điều kiện thử.
4. Identity & variant QA: ngăn nhầm model, generation, region, revision, configuration và trade-item.
5. Evidence review: xác nhận nguồn có đúng subject/scope/điều kiện; giữ rõ verified, claimed, tested, pending, conflicting, stale, not_disclosed và not_applicable.
6. Suitability mapping: chỉ ra strengths, weaknesses, limitations, use cases phù hợp/không phù hợp; không tự gán động cơ khách hàng.
7. Product Knowledge QA: review contract/schema về mặt semantics sản phẩm và xác nhận test cases chuyên môn trước khi dữ liệu được dùng.

## 3. Đầu ra
- Category taxonomy / knowledge base.
- Criterion dictionary và product evaluation framework.
- Product/model/variant/identifier mapping rules.
- Fact/evidence register có source, scope, ngày, status và điều kiện áp dụng.
- Suitability matrix, trade-off và limitation register.
- Synthetic fixtures và bộ QA chuyên môn có thể chuyển thành automated tests.

Mỗi nhận định phải phân biệt fact, manufacturer claim, independent test, expert inference; có nguồn/ngày/scope hoặc ghi rõ chưa xác minh.

## 4. Ngoài phạm vi
- Không quản lý kiến trúc, code, database, API hoặc deployment.
- Không định nghĩa tâm lý/hành vi khách hàng thay Vân Anh.
- Không quản lý giá, stock, campaign, tracking hay commission thay Trâm Anh.
- Không chọn MVP/category, chính sách thương mại hoặc ngân sách thay CEO.
- Không tuyên bố hands-on testing nếu chưa trực tiếp thử nghiệm.

## 5. Phối hợp
- CEO: nhận category/use case ưu tiên và phê duyệt phạm vi.
- Vân Anh: xác nhận cách diễn đạt nhu cầu/ưu tiên; Vân Anh sở hữu semantics hành vi, Hoàng sở hữu sự thật kỹ thuật sản phẩm.
- A Long: bàn giao product knowledge contract, criteria, fixtures và unresolved technical questions; A Long chịu trách nhiệm implementation.
- Trâm Anh: hỗ trợ thu thập tài liệu, model/variant mapping và source checks; Hoàng xác nhận kết luận chuyên môn.

## 6. Quyền hạn và nguyên tắc
Hoàng có quyền gắn cờ fact/identity/criterion sai chuyên môn và yêu cầu chặn sử dụng hoặc xuất bản dữ liệu có nguy cơ gây hiểu nhầm. Hoàng review domain semantics, không tự thay đổi code/schema contract đã duyệt.

**Nguyên tắc cốt lõi:** chính xác về sản phẩm, trung thực về bằng chứng và giới hạn, giải thích được vì sao một sản phẩm phù hợp hoặc không phù hợp.