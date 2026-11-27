# RULE — SR KHÔI PHỤC DỊCH VỤ (KPDV)

> Một loại SR của [SR](../quy-trinh-nghiep-vu.md); luồng chung (tạo, phân công, liên hệ, đánh giá) xem ở đó.

Nguồn: URD Service Request V1.2 – KPDV, §C.I–C.II; URD Service-Request-Transaction v1.2 (màn xử lý giao dịch).

- **Điều kiện tạo SR:**
  - Hợp đồng **Bình thường** có dịch vụ đang **Chủ thuê bao đi vắng (CTBĐV)** hoặc **Đã chấm dứt**, hoặc hợp đồng **Đã chấm dứt hợp đồng**.
  - Chỉ chọn được dịch vụ CTBĐV / Đã chấm dứt (hệ thống tự chọn sẵn, cho bỏ chọn).
  - Hợp đồng Đã chấm dứt: không chọn được Oncall, Fpro, Fsafe go.

| # | Bước | Hệ thống |
|---|---|---|
| 1 | Tạo SR, liên hệ tư vấn | Hệ thống SR |
| 2 | Xử lý giao dịch: chọn gói, CLG (lấy CLG cũ nếu còn hiệu lực), cước tháng cũ | Hệ thống SR |
| 3 | Ticket duyệt nếu cần: thiết bị, thay đổi CLG, miễn giảm | Hệ thống SR |
| 4 | Ticket **Đơn hàng SPF**: sinh đơn hàng và thu tiền | SPF |
| 5 | Thanh toán xong: **cấu hình từ xa** (bật lại dịch vụ) và **phát hành hóa đơn** | SR, Inside |
| 6 | Đơn OK → SR Đã xử lý; đơn NOT OK → Xử lý không thành công, hủy phiếu mua hàng nếu có | Hệ thống SR |
