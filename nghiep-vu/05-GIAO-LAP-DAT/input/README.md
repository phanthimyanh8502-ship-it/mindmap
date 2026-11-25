# Input — GIAO & LẮP ĐẶT (tổng quan)

Tài liệu đầu vào của [`../quy-trinh-nghiep-vu.md`](../quy-trinh-nghiep-vu.md). Input riêng của từng loại triển khai nằm trong `input/` của thư mục con.

## Tool

### Tool thao tác, cập nhật
- **SPF Web admin / app MobiX** — Chi tiết đơn hàng › PTC — hoàn tất phiếu thi công (TIN/PNC, TIN/PNC giao hàng, FTI). http://saleplatform-stag.fpt.net/web-admin/Account/Login
- **Tool quầy (QLVT)** — Quản lý chuỗi cung ứng › Giao dịch thiết bị — hoàn tất phiếu giao dịch thiết bị tại quầy (Quầy, Sale).
- **M-Vendor trên Fox ERP** — Quản lý NCU › Giao hàng, triển khai NCU — hoàn tất phiếu giao hàng NCC. https://fox-erp-stag.fpt.net/
- **Không / None** — không có phiếu, không dùng tool.

## Thao tác

### Hoàn tất giao & lắp đặt theo loại triển khai
1. TIN/PNC, TIN/PNC giao hàng, FTI: hoàn tất phiếu thi công trên SPF Web admin hoặc app MobiX (xem `01-PHIEU-THI-CONG`).
2. Quầy, Sale: hoàn tất phiếu giao dịch thiết bị trên Tool quầy / QLVT (xem `02-PHIEU-GIAO-DICH-THIET-BI-TAI-QUAY`).
3. NCC Samsung / Sony / Casper: cập nhật phiếu giao hàng NCC tới Đã hoàn tất trên M-Vendor (xem `03-DON-DAT-HANG-VENDOR`).
4. Không / None: không có phiếu; thiết bị chỉ xuất hóa đơn khi quầy gửi tín hiệu.

## Ý chính tài liệu

### `AnhNQ75-List HT Triển khai.xlsx`
- Liệt kê từng hình thức triển khai (DeployType) trên đơn SPF: chủ thể, trigger, đầu ra.
- TIN/PNC ⇒ phiếu thi công loại Triển khai. TIN/PNC giao hàng ⇒ phiếu thi công loại Giao hàng, chỉ Camera Offnet, thiết bị lẻ. FTI ⇒ phiếu thi công phân công đối tác FTI cho dự án, SPDV đặc thù.
- Quầy (DVKH CN), Sale (nhân viên bán hàng) ⇒ phiếu giao dịch thiết bị loại Bán thiết bị. Sale chỉ áp dụng thiết bị lẻ quản lý MAC.
- NCC Samsung / Sony / Casper ⇒ phiếu giao hàng NCC + mã vận đơn NCC gửi lại; 1 NCC = 1 Vendor Order = 1 Delivery Order.
- Đơn trộn TIN/PNC với Quầy/Sale ⇒ tự đi luồng TIN/PNC. Trộn "Không" + TIN/PNC ⇒ phiếu thi công. Chỉ có "Không" ⇒ không đẩy triển khai.

### URD Xuất hóa đơn REQ-XHD-043
- Hoàn tất phiếu sinh tín hiệu giao hàng hoàn tất, đi thẳng về INVOICE để xuất hóa đơn thiết bị.
- Nguồn tín hiệu: phiếu thi công (TIN/PNC, FTI) · Vendor (NCC) · phiếu giao tại quầy (Quầy, Sale).
- Map theo mã đơn + ServiceCode + SubserviceType + phương thức triển khai; chỉ xuất hóa đơn thiết bị có trong tín hiệu (BR-DB-02, BR-DB-07).

### Thông tin QC cung cấp (04/11/2026, 17/11/2026)
- BR-PTK-02: phiếu thi công sinh ngay khi tạo đơn nếu PTTT = Thanh toán khi triển khai; PTTT Online thì sau khi khách thanh toán.
- BR-PTK-03: phiếu giao tại quầy và phiếu giao hàng NCC chỉ sinh sau khi đơn đã thanh toán.
- BR-PTK-04: mỗi loại phiếu hoàn tất trên tool của phiếu đó.
- BR-PTK-05: hoàn tất PTC không còn điều kiện "đã ký BBĐT + khoản thu đã thanh toán".

## File trong thư mục này

- `AnhNQ75-List HT Triển khai.xlsx`

## Nguồn

- `AnhNQ75-List HT Triển khai.xlsx` (sheet "1. HT Triển khai"), bản gốc ở `qc-iia/00_input/v2.0/Doc/`
- URD Xuất hóa đơn REQ-XHD-043: xem input của [Xuất hóa đơn](../../07-XUAT-HOA-DON/input/)
- Thông tin QC cung cấp: 04/11/2026, 17/11/2026 (quy tắc sinh và hoàn tất phiếu)
