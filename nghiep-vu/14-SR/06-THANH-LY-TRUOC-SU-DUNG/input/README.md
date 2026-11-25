# Input — SR THANH LÝ TRƯỚC SỬ DỤNG (TL TSD) — CHỈ ĐƠN CHƯA THANH TOÁN

Tài liệu đầu vào của quy trình nghiệp vụ ở [`../quy-trinh-nghiep-vu.md`](../quy-trinh-nghiep-vu.md).

## Tool

### Tool thao tác, cập nhật
- **Tool SR** — Fox ERP › Service Request — tạo và xử lý SR.
- Hệ thống liên quan: SPF (hủy đơn), Inside (phiếu thi công, đề xuất hạ tầng).

## Thao tác

### Hủy toàn phần đơn hàng chưa thanh toán (SR)
1. Tạo SR theo mã đơn hàng chưa thanh toán (hoặc tự động từ SPF); hệ thống phân công tự động.
2. Tư vấn khách.
3. Khách thanh lý: CBQL duyệt thanh lý.
4. SPF hủy dịch vụ, sản phẩm, phiếu thi công, khoản thu → SR Đã xử lý.

### Giữ đơn khi khách đồng ý dùng tiếp
1. Kiểm tra phiếu thi công, đề xuất hạ tầng nếu cần, chuyển thi công.

## Ý chính tài liệu

### `ISC_SR TL TSD_v1.0_URD_v1.0_DonhangChuathanhtoan.docx`
- SR **thanh lý trước sử dụng**: chỉ đơn hàng **chưa thanh toán**, dịch vụ chưa active; hủy toàn phần.
- Có dịch vụ đã active ⇒ SR Hủy – KH đã active.
- KH thanh lý ⇒ CBQL duyệt ⇒ SPF hủy toàn bộ dịch vụ, sản phẩm, phiếu thi công, khoản thu (phiếu thi công, khoản thu: QC xác nhận 25/11/2026).

## Nguồn

- `ISC_SR TL TSD_v1.0_URD_v1.0_DonhangChuathanhtoan.docx` (file nằm ở [input của SR](../../input/))
- Thông tin QC cung cấp 25/11/2026: SPF hủy đơn thì có hủy phiếu thi công và khoản thu (URD không ghi).
