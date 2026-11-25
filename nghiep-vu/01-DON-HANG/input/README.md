# Input — ĐƠN HÀNG

Tài liệu đầu vào của quy trình nghiệp vụ ở [`../quy-trinh-nghiep-vu.md`](../quy-trinh-nghiep-vu.md). Rule từng kênh tạo đơn có `input/` riêng trong [`../kenh-ban/`](../kenh-ban/).

## Tool

- **Kênh bán** — Web/App SOP, HiFPT, FPT.vn, W-Sale, sàn TMĐT… — nơi tạo đơn (xem từng kênh trên mindmap).
- **SPF Web admin** — http://saleplatform-stag.fpt.net/web-admin/Account/Login — xem thông tin đơn hàng sau khi tạo.
- **Inside – Tình trạng** — kiểm tra hợp đồng của đơn (kể cả hợp đồng cha của hợp đồng con).

## Thao tác

### Kiểm tra đơn hàng sau khi tạo
1. Vào SPF Web admin, tìm đơn theo mã đơn, xem thông tin đơn hàng.
2. Vào Inside › Tình trạng, kiểm tra hợp đồng của đơn.

### Tạo đơn SOP bán mới qua báo giá (Desktop, Mobile)
1. Sale tạo báo giá: chọn dịch vụ, PTTT → Tạo báo giá (có mã đơn hàng).
2. Khách xem báo giá trên fpt.vn: thanh toán hoặc gửi yêu cầu chỉnh sửa.
3. Sale bấm Tạo hợp đồng (hoặc khách tự thanh toán qua link) → có hợp đồng, đơn đi tiếp theo PTTT.

## Nghiệp vụ chính

- Tạo đơn xong sẽ có **thông tin hợp đồng**. SOP bán mới: bấm Tạo hợp đồng mới có hợp đồng; bán thêm không qua báo giá.
- Thời điểm sinh khoản thu, phiếu, BBĐT tùy **PTTT** và **kênh** (Thanh toán khi triển khai: cả 3 sinh ngay sau tạo đơn; Online: theo từng kênh).
- Đơn sàn TMĐT (Shopee, TikTok) không có khoản thu, dùng Order Transaction; VNTT chỉ ghi nhận hợp đồng.
- Hợp đồng của đơn quyết định thông tin khách, chi nhánh khi xuất hóa đơn.

## Nguồn

- Thông tin QC cung cấp (ghi ở từng mục trong `quy-trinh-nghiep-vu.md`): 04/11/2026, 19/11/2026, 20/11/2026
- `URD_BaoGia_v1.0_22 Apr 2026_KieuPTP5.docx` (file nằm ở [input của SOP](../kenh-ban/SOP/input/))
