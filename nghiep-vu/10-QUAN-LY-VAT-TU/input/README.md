# Input — TOOL QUẢN LÝ VẬT TƯ

Tài liệu đầu vào của quy trình nghiệp vụ ở [`../quy-trinh-nghiep-vu.md`](../quy-trinh-nghiep-vu.md).

## Tool

### Tool thao tác, cập nhật
- **Tool Quản lý vật tư** — Inside – Vật tư TIN/PNC (trên Fox ERP) — khai báo, phân quyền, định mức, xác nhận hoàn ứng, nhập, bồi thường, Dataload ORC ERP, báo cáo.
- **App MobiX** — app của NVKT / KTV — đề nghị tạm ứng, chuyển vật tư, đề nghị hoàn ứng, đề nghị nhập vật tư.
- **Tool SCM (FTELSCM)** — Quản lý kho › Nhập kho › Tạo phiếu nhập; Quản lý kho › Xác nhận tạm ứng từ Inside — FMD xác nhận tạm ứng. https://ftelscm-uat.fpt.net — **Cần host**.
- **Quản lý chuỗi cung ứng – Vật tư thu hồi** — Quản lý chuỗi cung ứng › Quản lý vật tư thu hồi — xử lý, kiểm tra thiết bị thu hồi từ khách (QC cung cấp 25/11/2026).

## Thao tác

### Chuẩn bị kho vật tư TIN/PNC
1. Khai báo vật tư, phân quyền kho – đối tác, định mức vật tư trên Inside.

### Tạm ứng vật tư cho kỹ thuật
1. Đội trưởng / NVKT đề nghị tạm ứng (MobiX, Inside).
2. Trên SCM: tạo phiếu nhập hàng hóa (kho KTN test MAC), rồi xác nhận tạm ứng từ Inside.
3. NVKT / KTV chuyển vật tư; phiếu thi công load vật tư khi triển khai hoặc bảo trì.

### Hoàn ứng, quyết toán vật tư
1. Đề nghị hoàn ứng ⇒ FAF xác nhận hoàn ứng, xác nhận tổng hợp.
2. Khi cần: hoàn ứng điều chỉnh, nhập vật tư (FMD xác nhận), bồi thường (FAF xác nhận).
3. FAF xác nhận Dataload ORC ERP; đối soát kho tạm với FTELSCM, báo cáo.

### Kiểm tra / xử lý thiết bị thu hồi
1. Vào Quản lý chuỗi cung ứng › Quản lý vật tư thu hồi, tìm theo hợp đồng hoặc phiếu thu hồi.
2. Cập nhật kết quả thu hồi → nhập kho thu hồi.

## Ý chính tài liệu

### `ISC_INSIDE-Resource-Equipment V1.0_URD_V1.0.docx`

- Dự án Resource Equipment: yêu cầu bổ sung (CUS, TIN/PNC, CS, FAF) cho vật tư kho tạm TIN/PNC — điều chỉnh thiết bị sử dụng, tool đề nghị bàn giao thiết bị BGĐ TIN/PNC, điều chỉnh báo cáo FAF, microservices (DDD).
- Lý do: hệ thống cũ, cần nâng cấp để đáp ứng giao dịch thiết bị, thu hồi thiết bị. Mục tiêu: chuẩn hóa theo nghiệp vụ, dễ mở rộng, tăng giám sát lỗi.
- Phạm vi triển khai: FTEL; domain Resource equipment.
- Luồng chính: khai báo vật tư, phân quyền, định mức, khóa chuyển vật tư ⇒ tạm ứng (FMD xác nhận) ⇒ chuyển vật tư, dùng khi triển khai / bảo trì ⇒ hoàn ứng (FAF xác nhận) ⇒ Dataload ORC ERP.
- Nhánh phụ: hoàn ứng điều chỉnh (TP / PP kỹ thuật), yêu cầu BGĐ CN xác nhận sử dụng vật tư, nhập vật tư, bồi thường, lịch sử – điều chỉnh vật tư (CUS HO, CS, TIN/PNC), đối soát vật tư.
- Vai trò: FAF = kế toán, FMD = thủ kho, FTQ = quản lý quy trình, INF = quản lý hạ tầng, QLĐV = quản lý đơn vị.

### Thông tin QC cung cấp

- Luồng vật tư (04/11/2026): Kho SCM ⇒ tạm ứng ⇒ Tool vật tư ⇒ load vật tư ⇒ Giao & lắp đặt.
- Phiếu thi công TIN/PNC load vật tư từ Tool Quản lý vật tư; chưa có các bước chi tiết.
- Mobinet và MobiX là 1 app, thống nhất gọi MobiX (QC xác nhận 19/11/2026).
- Loại hình bán thiết bị: QLCS lấy dữ liệu từ Quản lý vật tư rồi trả ra cho SPF (19/11/2026).

## File trong thư mục này

- `ISC_INSIDE-Resource-Equipment V1.0_URD_V1.0.docx` (bạn cập nhật 19/11/2026, thay URD Quản lý vật tư V2.0)

## Nguồn

- `ISC_INSIDE-Resource-Equipment V1.0_URD_V1.0.docx`: chỉ dùng mục **Thông tin chung** và **Tổng quan › Quy trình nghiệp vụ**
- Thông tin QC cung cấp (ghi ở đầu từng mục trong `quy-trinh-nghiep-vu.md`): 04/11/2026
- Thông tin QC cung cấp 25/11/2026: thu hồi thiết bị xử lý / kiểm tra ở tool Quản lý chuỗi cung ứng › Quản lý vật tư thu hồi.
