# Input — MOBIX

Tài liệu đầu vào của [`../quy-trinh-nghiep-vu.md`](../quy-trinh-nghiep-vu.md). File gốc để theo thư mục phiên bản app (`V1.0`, `V1.2`, `V2.0`, `v2.3`, `v2.4`, `v2.9`).

## Tool

### Tool thao tác, cập nhật
- **App MobiX** — Ca tồn › tab Triển khai — nhận ca, check-in, xử lý và hoàn tất PTC; Thanh toán; Vật tư.
- **Inside new v5** — Thông tin chung › Triển khai — phân tuyến, phân công PTC.

### Tool kiểm tra
- **Partner portal** — Tồn giám sát — xem trạng thái ticket tồn và nhân sự đang xử lý. http://partner.fpt.net/pt-portal/monitor

## Thao tác

### Xử lý phiếu thi công trên MobiX
1. MobiX › Ca tồn › tab Triển khai: chọn phiếu, nhận ca.
2. Gọi khách chốt lịch (đổi lịch thì tích hẹn lại); xác nhận di chuyển (không bắt buộc).
3. Tới nhà khách: check-in; thu tiền, ký BBĐT, cập nhật CCCD (đơn bán mới ĐKOL / TLS / CS).
4. Chọn MAC bàn giao (từ kho tạm) và MAC thu hồi (nếu có).
5. Chụp ảnh thi công, nghiệm thu dịch vụ, chọn Đã xử lý hoàn tất. Không triển khai được thì chọn kết quả Không thành công + nguyên nhân trả về.

### Hoàn tất bảo trì
1. MobiX › Ca tồn › tab Bảo trì: chọn phiếu, nhận ca, check-in (ca xử lý từ xa không cần).
2. Xử lý checklist bảo trì; đổi thiết bị thì chọn MAC thu hồi từ danh sách thiết bị đã hoàn ứng cho hợp đồng.
3. Chọn Đã xử lý hoàn tất; không xử lý được thì Chờ xác minh.

### Tạo SR
1. MobiX › Quản lý SR › Tạo SR (hoặc từ ca có hướng xử lý cần SR); xem lại ở danh sách SR đã tạo.

### Thanh toán hóa đơn, khoản thu
1. MobiX › chi tiết hợp đồng › Thanh toán: chọn hóa đơn / khoản thu (bắt buộc khoản thu PTC).
2. Chọn hình thức: Tiền mặt tạm · Ví FPT Pay · QR Pay – VNPay; với QR bấm Kiểm tra thanh toán.

### Nhả tuyến
1. Chi tiết phiếu › Nhả tuyến › chọn nguyên nhân › Cập nhật.

## Ý chính tài liệu

### `MBX - V2.3 - FTQ - Mô tả thay đổi tình trạng ticket TKBT` (v2.4)
- Quy trình ticket triển khai / bảo trì: Chưa phân công → Đã phân công → Đã nhận ca → Đang di chuyển → Đang xử lý → Đã xử lý và đang theo dõi / Chờ xác minh / Đã xử lý hoàn tất.
- Thêm 2 trạng thái Đã nhận tuyến, Đang di chuyển; người dùng không tự chọn tay; truyền sang SR, SPF, HiFPT.

### `MBN_NEXTGEN_v1.0_URD_Phiếu Triển Khai` (V1.0)
- Chức năng trên phiếu triển khai: nhả tuyến, lịch sử nhả tuyến, định danh khách hàng, nguyên nhân trả về, nâng cấp gói, up ảnh CCCD.
- Đơn bán mới của ĐKOL, TLS, CS phải cập nhật CCCD mới hoàn tất phiếu.

### `FTP_MobinetNextgen_v1.0_URD_Caton` (V1.0)
- Danh sách ca tồn; trên ca triển khai / bảo trì: nhận ca, check-in, ghép cặp, tích hẹn lại, liên hệ, lịch sử phiếu.

### `ĐTYC Check trùng HĐ MBX` (v2.4)
- PTC triển khai mới: check trùng khách hàng / địa chỉ với hợp đồng cũ ⇒ tiếp tục triển khai (thu hồi thiết bị cũ nếu chưa thu) hoặc ngưng (khách trả trước / đóng nợ, hoặc tạo SR khôi phục dịch vụ).

### `ĐTYC_Gông vật tư bàn giao, thu hồi` (v2.4)
- MAC bàn giao lấy từ kho tạm KTV; MAC thu hồi lấy từ thiết bị đã hoàn ứng cho hợp đồng.

### `MobiX_v2.1_URD_QuanlySR` (v2.3)
- Tạo và xem SR ngay trên MobiX; ca cần SR phải tạo SR thành công mới hoàn tất phiếu.

### `ISC_Thanh toan v2.0_URD` (V2.0)
- SDK thanh toán dùng chung cho Sale, TIN/PNC, thu cước: tiền mặt tạm, Ví FPT Pay, QR VNPay.
- TIN/PNC bắt buộc thanh toán khoản thu của PTC; hợp đồng còn HĐĐT / PLHĐ / BBĐT chưa ký thì không thu được.

### `Rule tồn tạm New` (v2.9)
- Tiền mặt tạm nộp về công ty trước 10 giờ ngày làm việc kế tiếp; quá hạn ⇒ khóa thu tiền tạm và online; tồn quá 48 giờ ⇒ không cho xuất vật tư.

### `ISC_MBX_v2.9_PRD` (v2.9)
- Thanh toán tạm, gạch nợ online, gạch nợ tạm chuyển sang Billing Hub; DVKH HO gạch nợ trên Fox ERP.
- Phân loại tập hợp đồng trả trước có / không có khoản thu cho KTV đi thu.

### `FTP_MobinetNextgen_v1.0_URD_Quanlyvattu` (V1.0), `ĐTYC_Quản lý mac theo ngày xuất` (v2.4)
- Kho tạm KTV: tạm ứng, nhập trả, chuyển, nhận vật tư.
- MAC giữ quá 15 ngày ⇒ cảnh báo; từ 30 ngày ⇒ khóa, chỉ nhập trả.

### `FTP_MobiX_v1.3_URD_Tool Đội trưởng` (V1.2)
- Đội trưởng: báo cáo ca vụ, quản lý ca tồn của KTV, phân tuyến lại, cập nhật port, xem tọa độ nhân sự.

## Nguồn

- QC cung cấp 26/11/2026: MobiX có nhiều chức năng (hoàn tất PTC, hoàn tất bảo trì, tạo SR, thanh toán hóa đơn), tách luồng riêng, không gộp vào Phiếu thi công.
- QC cung cấp 26/11/2026: bộ tài liệu MobiX theo phiên bản app (V1.0 → v2.9). Chỉ lấy quy trình tổng quan và các rule gông liên quan PTC, thanh toán, vật tư.
- QC xác nhận 19/11/2026: Mobinet và MobiX là 1 app, thống nhất gọi MobiX.
