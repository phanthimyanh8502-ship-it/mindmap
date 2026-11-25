# Input — HỢP ĐỒNG

Tài liệu đầu vào của quy trình nghiệp vụ ở [`../quy-trinh-nghiep-vu.md`](../quy-trinh-nghiep-vu.md).

## Tool

- **SPF Web admin** — xem thông tin đơn hàng sau khi tạo đơn. STG: http://saleplatform-stag.fpt.net/web-admin/Account/Login
- **Inside** — Tình trạng — kiểm tra thông tin hợp đồng (kể cả hợp đồng cha của hợp đồng con).
- **Inside** — Quản lý hợp đồng › Cập nhật hợp đồng (New) — chỉ cập nhật thông tin khách hàng.
- **Fox ERP** — Service Request — tạo các loại SR cập nhật hợp đồng. STG: https://fox-erp-stag.fpt.net/
- **Chốt cước** — Quản lý hợp đồng › Chốt cước — chốt cước dịch vụ của hợp đồng tới một ngày (vd ngày hiệu lực khi chuyển chủ sở hữu) (QC cung cấp 25/11/2026).

## Thao tác

### Xem, kiểm tra hợp đồng sau khi tạo đơn
1. Tạo đơn ở kênh bán; đơn tạo xong sẽ có thông tin hợp đồng.
2. Xem thông tin đơn hàng trên SPF Web admin.
3. Kiểm tra hợp đồng ở tool Tình trạng trên Inside.

### Cập nhật hợp đồng
1. Chỉ đổi thông tin khách hàng: Inside › Quản lý hợp đồng › Cập nhật hợp đồng (New).
2. Đổi dịch vụ, địa điểm hoặc trạng thái hợp đồng: tạo SR tương ứng trên Fox ERP › Service Request.
3. SR chuyển dịch vụ, chuyển địa điểm, khôi phục dịch vụ: theo dõi phiếu thi công sinh từ hợp đồng.

## Ý chính tài liệu

### Thông tin QC cung cấp

- Tạo đơn xong sẽ có thông tin hợp đồng; xem đơn trên SPF Web admin, kiểm tra hợp đồng ở tool Tình trạng trên Inside (04/11/2026).
- Có 2 tool cập nhật hợp đồng: Inside chỉ cập nhật thông tin khách hàng; SR cập nhật được nhiều hơn (25/11/2026).
- Các loại SR: thay đổi thông tin khách hàng; chuyển dịch vụ trong cùng 1 nhóm; thanh lý / tạm ngưng (sang Đã chấm dứt / Tạm ngưng); khôi phục dịch vụ (về Bình thường); chuyển địa điểm.
- SR chuyển dịch vụ, chuyển địa điểm, khôi phục dịch vụ sinh phiếu thi công từ hợp đồng (19/11/2026).

### URD Xuất hóa đơn rev 2.2 (`Invoice_Issuance_Architecture_v2_2_URD_v2_0.docx`)

- Thông tin khách trên hóa đơn mặc định lấy theo hợp đồng; cập nhật thông tin khách không kích hoạt phát hành, lần sau dùng thông tin mới nhất (BR-DB-03).
- Hợp đồng phải còn hiệu lực mới xuất hóa đơn; không hợp lệ thì không phát hành và ghi log (BR-XHD-10).
- Hợp đồng tổ chức chỉ phát hành khi đã duyệt PĐK, 2 ngày cuối tháng không xét điều kiện này (BR-XHD-03).
- Hợp đồng con (gắn hợp đồng cha / hợp đồng dự án) không phát hành hóa đơn, cả dịch vụ và thiết bị (BR-XHD-03).
- Chi nhánh xuất hóa đơn là chi nhánh quản lý hợp đồng, xác định lúc phát hành (BR-XHD-12).

### Yêu cầu BA 23/10/2026 về hợp đồng SST / nghiệp vụ không tự xuất

- Hợp đồng SST và hợp đồng nghiệp vụ không tự động xuất hóa đơn.
- Đây là yêu cầu bổ sung, ngoài URD.

## Nguồn

- Thông tin QC cung cấp (ghi ở đầu từng mục trong `quy-trinh-nghiep-vu.md`): 04/11/2026 (cập nhật hợp đồng, SR); 25/11/2026 (2 tool cập nhật hợp đồng: Inside chỉ thông tin KH, SR nhiều loại)
- URD Xuất hóa đơn rev 2.2: [`Invoice_Issuance_Architecture_v2_2_URD_v2_0.docx`](../../07-XUAT-HOA-DON/input/) (nằm ở input của Xuất hóa đơn)
- Yêu cầu BA 23/10/2026 về hợp đồng SST / nghiệp vụ không tự xuất: bản gốc ở `qc-iia/00_input/v2.0/Doc/`
- Thông tin QC cung cấp 25/11/2026: menu chốt cước là Quản lý hợp đồng › Chốt cước.
