# Input — SR CHUYỂN DỊCH VỤ (CDV)

Tài liệu đầu vào của quy trình nghiệp vụ ở [`../quy-trinh-nghiep-vu.md`](../quy-trinh-nghiep-vu.md).

## Tool

### Tool thao tác, cập nhật
- **Tool SR** — Fox ERP › Service Request — tạo và xử lý SR.
- **Inside – Khoản thu** — SR đẩy thông tin sang để tạo khoản thu; khách trả tiền xong thì khoản thu Đã thanh toán.
- **Inside – Hóa đơn** — khoản thu Đã thanh toán thì Inside tự phát hành hóa đơn.
- **App HiFPT – Ký kết** — Tài khoản › Hợp đồng/Phụ lục — Inside tạo biên bản, **khách vào app HiFPT ký** (QC cung cấp 25/11/2026).
- **Inside – Phiếu thi công** — chỉ khi đổi thiết bị: ticket Triển khai chuyển sang Inside xử lý phiếu thi công.

## Thao tác

### Đổi gói, câu lệnh giá của dịch vụ đang dùng (SR)
1. Tạo SR: chọn dịch vụ cũ, gói mới, gói tính cước, câu lệnh giá.
2. Liên hệ, tư vấn → Xử lý giao dịch trên Inside.
3. Câu lệnh giá mới rẻ hơn: duyệt 2 cấp.
4. Thu tiền (có thể kèm miễn giảm) → Inside tự phát hành hóa đơn.
5. Ký kết; đổi thiết bị thì triển khai (phiếu thi công).
6. Hệ thống cập nhật dịch vụ trên hợp đồng → SR Đã xử lý.

## Ý chính tài liệu

### `ISC-FTEL SR_V1.0_URD CDD_CDV_Confirmed.docx`
- 2 loại: **chuyển địa điểm cùng tỉnh (CDD)** cho cả hợp đồng, **chuyển dịch vụ (CDV)** đổi gói, gói tính cước, câu lệnh giá.
- CDD: hợp đồng chuyển chủ sở hữu dưới 6 tháng thì TP DVKH chi nhánh phải duyệt.
- CDV: câu lệnh giá mới rẻ hơn thì duyệt 2 cấp; chỉ đổi thiết bị mới có triển khai.
- Ticket chung: miễn giảm → thu tiền (Inside tạo khoản thu) → Đã thanh toán thì Inside tự phát hành hóa đơn → ký kết → triển khai (phiếu thi công). COD: ký kết, triển khai cùng lúc thu tiền.

## Nguồn

- `ISC-FTEL SR_V1.0_URD CDD_CDV_Confirmed.docx` (file nằm ở [input của SR](../../input/))
- Thông tin QC cung cấp 25/11/2026: khách ký trên app HiFPT › Tài khoản › Hợp đồng/Phụ lục.
