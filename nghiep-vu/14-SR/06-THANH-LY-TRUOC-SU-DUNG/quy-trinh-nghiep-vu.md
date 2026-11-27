# RULE — SR THANH LÝ TRƯỚC SỬ DỤNG (TL TSD) — CHỈ ĐƠN CHƯA THANH TOÁN

> Một loại SR của [SR](../quy-trinh-nghiep-vu.md); luồng chung (tạo, phân công, liên hệ, đánh giá) xem ở đó.

Nguồn: URD SR TL TSD v1.0 – Đơn hàng chưa thanh toán, §B.II.

- ⚠ **Chỉ áp dụng cho đơn hàng CHƯA THANH TOÁN**, dịch vụ chưa kích hoạt: hủy toàn phần đơn. Tạo trên SR web hoặc tự động từ SPF.
- **Điều kiện tạo SR** (URD §B.II bước B1):
  - Tạo theo **mã đơn hàng**; đơn hàng tình trạng **Bình thường**, chưa thanh toán.
  - Hợp đồng không có SR thanh lý trước sử dụng của đơn hàng đó.
  - Không đủ điều kiện ⇒ hệ thống báo không đủ điều kiện tạo SR. Đủ ⇒ hiện danh sách sản phẩm, dịch vụ hủy được.
  - Đơn có ≥ 1 dịch vụ đã active: vẫn tạo được SR, nhưng khi xử lý chỉ ghi nhận và kết thúc (bước 2).
- Trên mindmap nằm ở **Hủy đơn hàng** (tab SR, cạnh tab Tool Hợp đồng NOT OK V3).

| # | Bước | Hệ thống |
|---|---|---|
| 1 | Tạo SR theo mã đơn hàng, phân công tự động | Hệ thống SR |
| 2 | Có dịch vụ đã active ⇒ SR **Hủy – KH đã active**, kết thúc | Hệ thống SR |
| 3 | Tư vấn: khách dùng tiếp ⇒ kiểm tra phiếu thi công, đề xuất hạ tầng nếu cần, **chuyển thi công** | Inside |
| 4 | Khách thanh lý ⇒ CBQL **duyệt thanh lý** → ticket **hủy đơn hàng SPF** | SPF |
| 4.1 | SR gửi yêu cầu **hủy toàn phần** sang SPF: hủy **toàn bộ dịch vụ và sản phẩm (thiết bị)** của đơn, tổng tiền hủy gồm giá trị phiếu mua hàng. SPF **hủy phiếu thi công** và **hủy khoản thu** của đơn (QC xác nhận 25/11/2026). SPF trả kết quả từng mục về SR, báo Fchat cho NV bán, NV xử lý | SPF → SR |
| 5 | SR Đã xử lý → khách đánh giá → Đã hoàn tất | Hệ thống SR |
