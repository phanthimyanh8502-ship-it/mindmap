# Input — HỦY ĐƠN HÀNG

Tài liệu đầu vào của quy trình nghiệp vụ ở [`../quy-trinh-nghiep-vu.md`](../quy-trinh-nghiep-vu.md).

## Tool

### Tool thao tác, cập nhật
- **Inside – Hợp đồng NOT OK V3** — Quản lý hợp đồng › Hợp đồng NOT OK V3 › tab Trước sử dụng — hủy đơn hàng.
- **Tool SR** — Fox ERP › Service Request — SR thanh lý trước sử dụng, **chỉ đơn chưa thanh toán**.

## Thao tác

### Hủy đơn bằng Tool Hợp đồng NOT OK V3
1. Vào Inside › Quản lý hợp đồng › Hợp đồng NOT OK V3 › tab Trước sử dụng, tìm hợp đồng.
2. Thao tác hủy đơn.
3. Đơn đã thanh toán: chờ TPKD duyệt.

### Hủy đơn chưa thanh toán bằng SR
1. Tạo SR thanh lý trước sử dụng theo mã đơn (xem tài liệu SR thanh lý trước sử dụng).

## Nghiệp vụ chính

- **Đơn chưa thanh toán:** hệ thống hủy ngay phiếu thi công, khoản thu; đơn chuyển Đã hủy.
- **Đơn đã thanh toán:** TPKD duyệt rồi mới ghi nhận hủy; PTC chưa hoàn tất thì hủy, đã hoàn tất thì giữ; có thể tạo đề nghị hoàn tiền.
- Hủy đơn là 1 trong 2 sự kiện SPF gửi về INVOICE (BR-DB-01); đơn bị hủy không xuất hóa đơn (BR-XHD-10).
- Cấp duyệt thực tế chỉ thấy TPKD; BGĐCN, CUSX chưa thấy.

## Nguồn

- Thông tin QC cung cấp (ghi ở đầu từng mục trong `quy-trinh-nghiep-vu.md`): 04/11/2026
