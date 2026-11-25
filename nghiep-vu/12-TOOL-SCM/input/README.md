# Input — TOOL SCM (KHO)

Tài liệu đầu vào của quy trình nghiệp vụ ở [`../quy-trinh-nghiep-vu.md`](../quy-trinh-nghiep-vu.md).

## Tool

- **Tool SCM (FTELSCM)** — Quản lý kho › Nhập kho › Tạo phiếu nhập — nhập hàng hóa, tạo MAC vào kho (KTN test MAC). https://ftelscm-uat.fpt.net — **Cần host**.
- **Tool SCM (FTELSCM)** — Quản lý kho › Xác nhận tạm ứng từ Inside — FMD xác nhận tạm ứng cho tool vật tư.
- **Tool vật tư (Fox ERP)** — Quản lý vật tư, Quản lý vật tư quầy — đề nghị tạm ứng, hoàn ứng, nhập, bồi thường.
- **Quản lý chuỗi cung ứng** — Quản lý chuỗi cung ứng › Giao dịch thiết bị — nhận xử lý phiếu giao tại quầy, đề nghị xuất vật tư.
- **GHTK (staging)** — Thông tin tài khoản › Cấu hình API › Webhook — giả lập trạng thái vận đơn. https://khachhang-staging.ghtklab.com/web/
- **Quản lý chuỗi cung ứng – Vật tư thu hồi** — Quản lý chuỗi cung ứng › Quản lý vật tư thu hồi — xử lý, kiểm tra thiết bị thu hồi từ khách (QC cung cấp 25/11/2026).

## Thao tác

### Tạm ứng vật tư (nhập hàng và xác nhận trên SCM)
1. Tool vật tư (Fox ERP) tạo đề nghị tạm ứng.
2. Trên SCM: tạo phiếu nhập hàng hóa cần giao (kho KTN test MAC).
3. Trên SCM: xác nhận tạm ứng từ Inside ⇒ vật tư về kho tạm của tool vật tư.
4. Phiếu giao & lắp đặt load vật tư từ tool vật tư.

### Hoàn ứng, nhập lại, đối soát
1. Sau khi dùng: đề nghị hoàn ứng ⇒ FAF xác nhận ⇒ SCM tổng hợp phiếu xuất.
2. Vật tư không dùng hoặc thu hồi: đề nghị nhập ⇒ thủ kho xác nhận nhập kho.
3. Đối soát kho tạm Fox ERP ↔ FTELSCM ⇒ FAF xác nhận Dataload ORC ERP.

### Kiểm tra / xử lý thiết bị thu hồi
1. Vào Quản lý chuỗi cung ứng › Quản lý vật tư thu hồi, tìm theo hợp đồng hoặc phiếu thu hồi.
2. Cập nhật kết quả thu hồi → nhập kho thu hồi.

## Ý chính tài liệu

### `Quy-trình-SCM.docx`

- Hướng dẫn sử dụng FTELSCM 1.5 (Hệ thống quản lý vật tư FTEL), cập nhật 25/07/2019.
- Chỉ dùng mục lục IX. Tích hợp Inside: 5 quy trình tạm ứng, hoàn ứng, trả vật tư, bồi thường vật tư, thu hồi vật tư.
- File không có nội dung mục IX; bước và vai trò lấy từ 2 URD vật tư.

### URD Resource Equipment V1.0 và URD Retail-Counter V1.0

- Tạm ứng: tool vật tư đề nghị ⇒ FMD (thủ kho) xác nhận trên FTELSCM.
- Hoàn ứng: FAF xác nhận hoàn ứng, xác nhận tổng hợp (phiếu xuất tổng hợp).
- Nhập / trả vật tư: FMD xác nhận nhập. Bồi thường: FAF xác nhận.
- Thu hồi (vật tư quầy): phiếu thu hồi ⇒ cập nhật kết quả ⇒ nhập kho thu hồi.
- Đối soát kho tạm với FTELSCM; FAF xác nhận Dataload ORC ERP.

### Thông tin QC cung cấp

- Luồng vật tư (04/11/2026): Kho SCM ⇒ tạm ứng ⇒ Tool vật tư ⇒ load vật tư ⇒ Giao & lắp đặt. SCM cần host.
- Phiếu giao tại quầy có shipper: nhận xử lý, đề nghị xuất vật tư ⇒ SCM nhập kho, xác nhận tạm ứng ⇒ lưu và đóng hàng ⇒ cập nhật trạng thái vận đơn qua GHTK.
- Tool Quản lý vật tư và Quản lý vật tư quầy nằm ở Fox ERP; quy trình tổng quan chỉ cần phần Tích hợp Inside (19/11/2026).

## File trong thư mục này

- `Quy-trình-SCM.docx` (QC bổ sung 19/11/2026)

## Nguồn

- `Quy-trình-SCM.docx`: hướng dẫn sử dụng FTELSCM 1.5 (25/07/2019). Chỉ dùng tên 5 quy trình ở mục lục **IX. Tích hợp Inside** (file không có nội dung mục này)
- URD Resource Equipment V1.0 (input của [Quản lý vật tư](../../10-QUAN-LY-VAT-TU/input/README.md)) và URD Retail-Counter V1.0 (input của [Vật tư quầy](../../11-QUAN-LY-VAT-TU-QUAY/input/README.md)): vai trò FMD / FAF trong tạm ứng, hoàn ứng, nhập, bồi thường, thu hồi, đối soát
- Thông tin QC cung cấp (ghi ở đầu từng mục trong `quy-trinh-nghiep-vu.md`): 04/11/2026
- Thông tin QC cung cấp 25/11/2026: thu hồi thiết bị xử lý / kiểm tra ở tool Quản lý chuỗi cung ứng › Quản lý vật tư thu hồi.
