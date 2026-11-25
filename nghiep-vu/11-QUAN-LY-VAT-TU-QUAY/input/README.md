# Input — TOOL QUẢN LÝ VẬT TƯ QUẦY

Tài liệu đầu vào của quy trình nghiệp vụ ở [`../quy-trinh-nghiep-vu.md`](../quy-trinh-nghiep-vu.md).

## Tool

### Tool thao tác, cập nhật
- **Tool Quản lý vật tư quầy** — Inside – Vật tư quầy (trên Fox ERP) › Tạm ứng vật tư › Đề nghị tạm ứng — tạm ứng, hoàn ứng, nhập, bồi thường, đối soát vật tư quầy.
- **Tool SCM (FTELSCM)** — Quản lý kho › Nhập kho › Tạo phiếu nhập; Quản lý kho › Xác nhận tạm ứng từ Inside — tạo MAC và xác nhận tạm ứng. https://ftelscm-uat.fpt.net — **Cần host**.
- **Quản lý chuỗi cung ứng** — Quản lý chuỗi cung ứng › Giao dịch thiết bị — gắn MAC, hoàn tất phiếu giao tại quầy.
- **Quản lý chuỗi cung ứng – Vật tư thu hồi** — Quản lý chuỗi cung ứng › Quản lý vật tư thu hồi — xử lý, kiểm tra thiết bị thu hồi từ khách (QC cung cấp 25/11/2026).

## Thao tác

### Tạm ứng vật tư cho quầy
1. Vào Quản lý vật tư quầy › Tạm ứng vật tư › Đề nghị tạm ứng.
2. Chọn đối tác, tổ, vật tư ⇒ tạo phiếu ⇒ nhập số lượng ⇒ xác nhận.
3. Trên SCM: tạo phiếu nhập hàng hóa cần giao (kho KTN test MAC).
4. Trên SCM: xác nhận tạm ứng từ Inside (Bảo hành V2), nhập MAC vừa tạo ⇒ Xác nhận V2.

### Giao dịch thiết bị tại quầy (hoàn tất phiếu)
1. Vào Quản lý chuỗi cung ứng › Giao dịch thiết bị: tìm hợp đồng, chọn đối tác, tổ, MAC ⇒ hoàn tất phiếu.

### Hoàn ứng sau giao dịch
1. Đề nghị hoàn ứng ⇒ FAF xác nhận, tổng hợp phiếu xuất.

### Kiểm tra / xử lý thiết bị thu hồi
1. Vào Quản lý chuỗi cung ứng › Quản lý vật tư thu hồi, tìm theo hợp đồng hoặc phiếu thu hồi.
2. Cập nhật kết quả thu hồi → nhập kho thu hồi.

## Ý chính tài liệu

### `ISC_INSIDE_Retail-Counter-V1.0_URD_V1.0_18072024.docx`

- Quy trình giao dịch thiết bị – quản lý vật tư quầy trên Inside – Vật tư quầy (chỉ dùng mục Tổng quan › Quy trình nghiệp vụ).
- Luồng chính: khai báo vật tư, phân quyền đối tác – kho, định mức ⇒ giao dịch viên đề nghị tạm ứng ⇒ FMD xác nhận trên FTELSCM ⇒ trưởng đơn vị bàn giao vật tư ⇒ giao dịch thiết bị ⇒ hoàn ứng (FAF xác nhận, tổng hợp phiếu xuất) ⇒ xác nhận ORC ERP.
- Giao dịch thiết bị: bán, thuê có / không thu hồi, đổi bảo hành (đổi 7 ngày do BGĐ phê duyệt), đổi mới / đổi chênh lệch, xuất thiết bị HĐ khôi phục dịch vụ ⇒ cập nhật hóa đơn ⇒ hoàn tất phiếu.
- Thu hồi: phiếu thu hồi tại quầy ⇒ cập nhật kết quả thu hồi ⇒ nhập kho thu hồi.
- Nhánh phụ: hoàn ứng điều chỉnh (TP / PP), nhập vật tư (FMD), bồi thường (FAF), đối soát kho tạm, dataload Compact ⇒ ORC ERP.
- Hệ thống liên quan: Inside – QLCS (chính sách), Saleclub / AM, Inside đại lý, kênh chuỗi (đơn ⇒ phiếu bán thiết bị), FTELSCM, ORC ERP.

### Thông tin QC cung cấp

- Luồng vật tư (04/11/2026): Kho SCM ⇒ tạm ứng ⇒ Tool vật tư ⇒ load vật tư ⇒ Giao & lắp đặt.
- Phiếu giao dịch thiết bị tại quầy load vật tư từ Tool Quản lý vật tư quầy.
- Hoàn tất phiếu giao tại quầy không có shipper: đã có MAC thì hoàn tất ngay; chưa có MAC thì tạm ứng và tạo MAC trên SCM trước.
- Phiếu giao tại quầy của đơn SPF = phiếu bán thiết bị (19/11/2026).

## File trong thư mục này

- `ISC_INSIDE_Retail-Counter-V1.0_URD_V1.0_18072024.docx` (QC bổ sung 19/11/2026)

## Nguồn

- `ISC_INSIDE_Retail-Counter-V1.0_URD_V1.0_18072024.docx`: chỉ dùng mục **Tổng quan › Quy trình nghiệp vụ**
- Thông tin QC cung cấp (ghi ở đầu từng mục trong `quy-trinh-nghiep-vu.md`): 04/11/2026
- Thông tin QC cung cấp 25/11/2026: thu hồi thiết bị xử lý / kiểm tra ở tool Quản lý chuỗi cung ứng › Quản lý vật tư thu hồi.
