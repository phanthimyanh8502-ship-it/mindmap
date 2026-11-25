# Input — PHIẾU GIAO DỊCH THIẾT BỊ TẠI QUẦY

Tài liệu đầu vào của [`../quy-trinh-nghiep-vu.md`](../quy-trinh-nghiep-vu.md).

## Tool

- **Tool quầy (QLVT)** — Quản lý chuỗi cung ứng › Giao dịch thiết bị — nhận xử lý, đề nghị xuất vật tư, đóng hàng, hoàn tất phiếu.
- **Quản lý vật tư quầy** — Tạm ứng vật tư › Đề nghị tạm ứng — tạm ứng vật tư khi chưa có MAC.
- **SCM (FTELSCM)** — Quản lý kho › Nhập kho / Xác nhận tạm ứng từ Inside — tạo tồn kho test, xác nhận xuất vật tư theo MAC. https://ftelscm-uat.fpt.net — Cần host.
- **GHTK staging** — Thông tin tài khoản › Cấu hình API › Webhook — giả lập ĐVVC đổi trạng thái vận đơn. https://khachhang-staging.ghtklab.com/web/
- **Vendor vận chuyển** — tự động: tạo vận đơn, kết nối ĐVVC, tracking, đối soát.
- **Tool GH Quầy** (tool QC, đang thử nghiệm) — chạy nhanh luồng phiếu có shipper theo số hợp đồng.

## Thao tác

### Hoàn tất phiếu giao tại quầy có shipper
1. Giao dịch thiết bị → tìm hợp đồng → Nhận xử lý phiếu → chọn kho xuất.
2. Đề nghị xuất vật tư → trên SCM xác nhận tạm ứng từ Inside.
3. Quay lại phiếu → Lưu và đóng hàng (Vendor tạo vận đơn).
4. GHTK staging: Webhook → nhập mã vận đơn → cập nhật trạng thái 5.

### Hoàn tất phiếu giao tại quầy không có shipper
1. Chưa có MAC: tạm ứng trên Quản lý vật tư quầy, xác nhận tạm ứng và nhập MAC trên SCM.
2. Đã có MAC: Giao dịch thiết bị → tìm hợp đồng → chọn đối tác, tổ → Chỉnh sửa, chọn MAC → Lưu → kết quả Hoàn tất → Xác nhận.

## Ý chính tài liệu

### `QC-ISC_Resource-Equipment_v2.2_URD_v1.0.docx`
- Mục đích: giao thiết bị bán qua shipper bằng phiếu giao dịch thiết bị loại Giao hàng, kết nối ĐVVC (GHTK, Ahamove…) qua Vendor vận chuyển.
- Luồng chính: đơn SPF thanh toán ⇒ tạo phiếu giao (Chờ xác nhận) ⇒ thủ kho xử lý thông tin giao, tạm ứng xuất vật tư qua SCM ⇒ khai tiền bồi thường ⇒ đóng hàng ⇒ Vendor tạo vận đơn ⇒ ĐVVC giao.
- Giao thành công: hoàn ứng tự động, báo SPF ghi nhận đơn hoàn tất, gửi MAC sang SM nếu là FPT Camera Combo, đẩy hạch toán chi phí.
- BR-GH-01: phiếu chỉ tạo khi đơn đã thanh toán và có vật tư chính. BR-GH-02: 1 phiếu giao — 1 ĐVVC. BR-GH-04: chỉ đóng hàng khi đã xuất đủ, khớp MAC.
- Ngoại lệ: hủy giao hàng (BR-GH-11: chưa lấy hàng ⇒ kho tạm, đã lấy ⇒ kho tổng), cập nhật phiếu / phát lại khi đơn BÌNH THƯỜNG (BR-GH-10), hủy cả đơn hoặc 1 phần qua NOK V3 / SR.
- BR-GH-13: đối soát ĐVVC tính theo từng mã vận đơn.

### Thông tin QC cung cấp (04/11/2026)
- Phiếu có shipper: Giao dịch thiết bị → SCM xác nhận tạm ứng → đóng hàng → GHTK webhook giả lập trạng thái vận đơn.
- Phiếu không shipper: có MAC thì chọn MAC và hoàn tất; chưa có MAC thì tạm ứng trên Quản lý vật tư quầy và SCM trước.
- "Trạng thái 5" trên webhook là mã trạng thái của GHTK, không phải trạng thái phiếu (BA-7).

## File trong thư mục này

- `QC-ISC_Resource-Equipment_v2.2_URD_v1.0.docx` (QC bổ sung 19/11/2026)

## Nguồn

- `QC-ISC_Resource-Equipment_v2.2_URD_v1.0.docx`: **chỉ dùng mục "Quy trình giao hàng qua đơn vị vận chuyển"** (bảng B1–B11 + sơ đồ quy trình)
- Thông tin QC cung cấp: 04/11/2026 (thao tác STG: phiếu có shipper, không shipper, GHTK webhook)
