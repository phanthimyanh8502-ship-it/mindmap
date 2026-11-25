# Input — XUẤT HÓA ĐƠN

Tài liệu đầu vào của quy trình nghiệp vụ ở [`../quy-trinh-nghiep-vu.md`](../quy-trinh-nghiep-vu.md).

## Tool

- **INVOICE + Billing System** — hệ thống tự chạy — tự đồng bộ đơn từ SPF và phát hành hóa đơn, người dùng không thao tác.
- **SPF Web admin** — xem thời gian tạo đơn của đơn hàng (BR-DB-01).
- **Inside – Liệt kê cước** — Quản lý kế toán › Liệt kê cước — kiểm tra hóa đơn đã xuất của hợp đồng (QC cung cấp 25/11/2026).

## Thao tác

### Xuất hóa đơn tự động (hệ thống tự chạy, người dùng không thao tác)
1. SPF đẩy sự kiện thanh toán, hủy đơn về INVOICE; tín hiệu giao hàng hoàn tất đi thẳng từ phiếu thi công, Vendor, phiếu giao tại quầy.
2. INVOICE ghi nhận đơn theo lần đẩy cuối, map tín hiệu giao hàng vào thiết bị chưa xuất.
3. Phân luồng: tín hiệu trước giờ chốt vào worker, sau giờ chốt cuối vào realtime.
4. Xét điều kiện phát hành và điều kiện đơn hợp lệ.
5. Worker gộp DV/TB đủ điều kiện của cùng đơn vào 1 hóa đơn; realtime không gộp.
6. Phát hành qua Billing System, ghi BillNumber, BillDate.
7. Báo hóa đơn đã phát hành (Invoice Event) để chuyển sang gạch nợ và hậu kỳ.

### Kiểm tra hóa đơn đã xuất (người dùng)
1. Vào Inside › Quản lý kế toán › Liệt kê cước.
2. Tìm theo hợp đồng, xem hóa đơn đã xuất.

## Ý chính tài liệu

### `Invoice_Issuance_Architecture_v2_2_URD_v2_0.docx`

- Phase 2 mở rộng xuất hóa đơn tự động cho mọi kênh bán trong danh sách có đơn hàng SPF, không chỉ TMĐT; chưa gồm xuất hóa đơn tay.
- Dịch vụ phát hành khi hoàn tất thanh toán, thiết bị khi giao hàng hoàn tất, xét độc lập (BR-XHD-03); một đơn có 1..n hóa đơn (BR-XHD-14).
- Lịch chung là tham số cấu hình: 2 đợt chốt 12:00 và 18:00, FPL 2 giờ/lần và mốc 22:05 (BR-XHD-01); tín hiệu sau giờ chốt cuối xử lý realtime (BR-XHD-02).
- Worker gộp DV/TB đủ điều kiện của cùng đơn; realtime không gộp (BR-XHD-05, BR-XHD-06); mỗi dòng chỉ xuất 1 lần (BR-XHD-08).
- Đơn không hợp lệ hoặc thiếu dữ liệu thì không phát hành, ghi log, không giữ lại (BR-XHD-10). Hợp đồng tổ chức phải duyệt PĐK; hợp đồng con không phát hành (BR-XHD-03).
- Phát hành qua Billing System; chi nhánh xuất là chi nhánh quản lý hợp đồng; nội dung là tên dịch vụ + số tháng; sau đó gửi bản tin báo đã phát hành (Invoice Event) (BR-XHD-12, BR-XHD-13).

### Phân tích `qc-iia/02_analyze-requirements/v2.0/XHD/` và các clarification chốt đến 23/10/2026

- Kênh trong phạm vi test (REQ-XHD-001): Mobile, Desktop, DKOL, W-Sale, FPL, CMR-App, Momo, Shopee, Tiktok. API, VNTT, MBBank, CRM, TGDD, F-Retail, HiFPT ngoài scope; SR-KPDV không test.
- Dịch vụ (REQ-XHD-002): 20 nhóm / 55 dịch vụ, loại trừ ServiceID 2 (SubServiceType 5–9) và ServiceID 22 (GSafe); Thiết bị Oncall và Thiết bị IP phone là 1 dịch vụ.
- Áp dụng cả bán mới và bán thêm (REQ-XHD-040).
- Hình thức triển khai ⇒ nguồn tín hiệu (REQ-XHD-043): TIN/PNC, FTI ⇒ phiếu thi công; NCC ⇒ Vendor; Quầy, Sale ⇒ phiếu giao tại quầy; "Không" ⇒ qua phiếu quầy, quầy không gửi thì không xuất hóa đơn.

### Yêu cầu BA 23/10/2026 về hợp đồng SST / nghiệp vụ không tự xuất

- Hợp đồng SST và hợp đồng nghiệp vụ không tự động xuất hóa đơn, ngoài URD.

## File trong thư mục này

- `Invoice_Issuance_Architecture_v2_2_URD_v2_0.docx`

## Nguồn

- `Invoice_Issuance_Architecture_v2_2_URD_v2_0.docx` (URD rev 2.2, §B.I.c), bản gốc ở `qc-iia/00_input/v2.0/Doc/`
- Phân tích `qc-iia/02_analyze-requirements/v2.0/XHD/` và các clarification chốt đến 23/10/2026
- Yêu cầu BA 23/10/2026 về hợp đồng SST / nghiệp vụ không tự xuất: bản gốc ở `qc-iia/00_input/v2.0/Doc/`
- Thông tin QC cung cấp 25/11/2026: kiểm tra hóa đơn trên Inside › Quản lý kế toán › Liệt kê cước.
