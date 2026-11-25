# Input — PHIẾU THI CÔNG

Tài liệu đầu vào của [`../quy-trinh-nghiep-vu.md`](../quy-trinh-nghiep-vu.md). 

## Tool

- **Inside new v5** — Thông tin chung › Triển khai — kiểm tra PTC theo hợp đồng, phân tuyến, chọn Đã xử lý hoàn tất (QC cung cấp 25/11/2026).
- **Partner portal** — Bypass — bypass điều kiện hoàn tất PTC (tối đa 24 giờ). http://partner-stag.fpt.net/pt-portal/bypass
- **SPF Web admin** — Chi tiết đơn hàng › PTC › Hoàn tất PTC — hoàn tất PTC của đơn hàng. http://saleplatform-stag.fpt.net/web-admin/Account/Login
- **App MobiX** — nhân sự TIN/PNC xử lý phiếu thi công.
- **Inside — Quản lý hợp đồng** — HĐ NOT OK V3 › PTC NOT OK — hủy PTC hoặc chuyển thi công lại.
- **Fox ERP** — Quản lý đối tác › Quản lý Block › Quota PTC - TUT — phân công quota PTC. https://fox-erp-stag.fpt.net/

## Thao tác

### Kiểm tra phiếu thi công
1. Vào Inside new v5 › Thông tin chung › Triển khai, nhập số hợp đồng, xem PTC và trạng thái.

### Xử lý phiếu thi công
1. Inside new v5 › Thông tin chung › Triển khai: nhập số hợp đồng, mở PTC.
2. Phân tuyến, phân công nhân sự TIN/PNC; nhân sự xử lý phiếu trên app MobiX.

### Hoàn tất phiếu thi công (để có tín hiệu giao hàng gửi INVOICE)
1. Cách 1: partner portal › Bypass (tích tất cả, nhập hợp đồng, thời hạn ≤ 24 giờ, nguyên nhân) → quay lại PTC chọn Đã xử lý hoàn tất.
2. Cách 2: SPF Web admin › Chi tiết đơn hàng › PTC › Hoàn tất PTC.

### Hủy PTC hoặc chuyển thi công lại
1. Inside › Quản lý hợp đồng › HĐ NOT OK V3 › PTC NOT OK.

## Ý chính tài liệu

### `ISC_Phat-trien-phan-he-Trien-khai_v2.0_URD-v1.0.docx`
- Mục đích: xây phân hệ Triển khai theo Microservices, làm mới giao diện PTC, rút ngắn thao tác; quy trình xử lý giữ nguyên.
- Quy trình: hợp đồng / đơn hàng cần triển khai → request tạo PTC → đạt điều kiện thì PTC triển khai, không đạt thì phiếu công trắng → phân công đối tác, nhân sự → thi công.
- Không đủ điều kiện thi công ⇒ PTC NOT OK ⇒ chuyển thi công lại hoặc đề nghị hủy PTC.
- Hoàn tất PTC khi đạt điều kiện ⇒ nghiệm thu vật tư ⇒ cập nhật vật tư, thu hồi vật tư, hoàn ứng tự động.
- Chức năng cấp 1: tạo PTC, tìm PTC theo hợp đồng, cập nhật PTC, quy trình hoàn tất PTC, xem PTC tồn, xem báo cáo triển khai.

### `validate-completed-deployment.png`
- Điều kiện hoàn tất PTC chia 5 nhóm: tiên quyết, tác vụ, hợp đồng, đơn hàng, dịch vụ.
- Tiên quyết: hợp đồng bình thường, PTC chưa Hoàn tất. Tác vụ: check-in / check-out lệch ≤ 50 m, đã phân công nhân sự chính.
- Hợp đồng, đơn hàng, dịch vụ: khoản thu trên PTC, BBĐT, biên bản nghiệm thu, vật tư hợp lệ, dịch vụ active, MAC online = MAC trên PTC.
- Điều kiện khoản thu mâu thuẫn với BR-PTK-05 (câu hỏi C1).

### QC xác nhận 19/11/2026
- PTC tạo từ đơn hàng, hoặc từ hợp đồng khi tạo SR chuyển dịch vụ / chuyển địa điểm / khôi phục dịch vụ.

### Thông tin QC cung cấp (04/11/2026, 17/11/2026)
- PTC gom thông tin hợp đồng, đơn hàng, vật tư triển khai / thu hồi, khoản thu; vật tư lấy từ Tool Quản lý vật tư.
- Luồng: phân tuyến ⇒ phân công TIN/PNC ⇒ xử lý trên MobiX ⇒ Đã xử lý hoàn tất ⇒ tín hiệu giao hàng về INVOICE.
- 17/11/2026: bỏ rule cũ "ký BBĐT + khoản thu đã thanh toán mới hoàn tất PTC" (BR-PTK-05).

### List HT triển khai
- TIN/PNC, TIN/PNC giao hàng, FTI đều đi phiếu thi công; chi tiết ở input tổng quan.

## File trong thư mục này

- `ISC_Phat-trien-phan-he-Trien-khai_v2.0_URD-v1.0.docx` (QC bổ sung 19/11/2026)
- `validate-completed-deployment.png` (QC bổ sung 19/11/2026): sơ đồ điều kiện hoàn tất PTC

## Nguồn

- `validate-completed-deployment.png`: chỉ lấy các **nhóm điều kiện** hoàn tất PTC
- QC xác nhận 19/11/2026: PTC tạo từ đơn hàng, hoặc từ hợp đồng khi tạo SR chuyển dịch vụ / chuyển địa điểm / khôi phục dịch vụ
- `ISC_Phat-trien-phan-he-Trien-khai_v2.0_URD-v1.0.docx`: chỉ dùng mục **Tổng quan › Sơ đồ tổng quan** (quy trình triển khai + chức năng cấp 1)
- Thông tin QC cung cấp: 04/11/2026 (thông tin PTC, cách hoàn tất, thao tác khác), 17/11/2026 (bỏ rule cũ hoàn tất PTC)
- List HT triển khai: xem [input tổng quan](../../input/README.md)
- Thông tin QC cung cấp 25/11/2026: kiểm tra phiếu thi công ở Inside new v5 › Thông tin chung › Triển khai.
