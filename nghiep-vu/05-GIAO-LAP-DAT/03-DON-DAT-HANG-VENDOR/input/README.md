# Input — PHIẾU GIAO HÀNG NCC

Tài liệu đầu vào của [`../quy-trinh-nghiep-vu.md`](../quy-trinh-nghiep-vu.md).

## Tool

- **M-Vendor trên Fox ERP** — Quản lý NCU › Giao hàng, triển khai NCU › tab Quản lý phiếu giao hàng — cập nhật tình trạng phiếu giao hàng NCC. https://fox-erp-stag.fpt.net/
- **Tool GH Vendor** (tool QC) — nhập mã đơn hàng FTEL — chạy nhanh tới Đã hoàn tất.
- BBĐT tự động ký; tín hiệu giao hàng hoàn tất về INVOICE do Vendor gửi.

## Thao tác

### Hoàn tất phiếu giao hàng NCC (M-Vendor trên Fox ERP)
1. Đăng nhập Fox ERP, mở ứng dụng Quản lý NCU.
2. Vào Giao hàng, triển khai NCU › tab Quản lý phiếu giao hàng, tìm phiếu theo mã đơn hàng FTEL.
3. Chuyển Chưa giao hàng → Đang giao hàng, nhập hóa đơn NCU và hóa đơn điện tử.
4. Chuyển Đang giao hàng → Đã hoàn tất.

### Hủy phiếu giao hàng NCC
1. Chọn Hủy đơn hàng — chỉ khi phiếu còn Chưa giao hàng.

### Chạy nhanh khi test
1. Tool GH Vendor: nhập mã đơn hàng FTEL, chạy tới Đã hoàn tất.

## Ý chính tài liệu

### `ISC_INSIDE-M-VendorCooperation_V1.1_URD_V1.0.docx`
- Mục đích: user cập nhật tình trạng giao hàng của phiếu giao hàng NCU (Iteration 2).
- Luồng: đăng nhập (URD ghi Inside, thực tế Fox ERP) → Quản lý NCU › Giao hàng, triển khai NCU › QL Giao hàng → mở phiếu → cập nhật tình trạng hoặc hủy đơn → hệ thống kiểm tra điều kiện → lưu và báo thành công, hoặc báo lỗi.
- Chỉ user được cấp quyền vào menu mới xem danh sách; chỉ user có quyền cập nhật tình trạng đơn hàng mới cập nhật được (BR-VD-01).
- BR01: danh sách phiếu giao hàng dùng chung cho FPL, SPF, SCM; bổ sung kết nối giao hàng đối tác SCM.
- BR02: bổ sung hủy đơn hàng trên chi tiết phiếu giao hàng.

### Thông tin QC cung cấp
- Loại BBĐT (11/11/2026): BBĐT của phiếu giao hàng NCC tự động ký; phiếu chỉ sinh sau khi đơn đã thanh toán (BR-VD-02).
- Tool QC GH Vendor: đăng nhập Fox ERP, tự chuyển Đang giao hàng (kèm hóa đơn NCU, hóa đơn điện tử) → Đã hoàn tất.

## File trong thư mục này

- `ISC_INSIDE-M-VendorCooperation_V1.1_URD_V1.0.docx` (QC bổ sung 19/11/2026)

## Nguồn

- `ISC_INSIDE-M-VendorCooperation_V1.1_URD_V1.0.docx`: **chỉ dùng mục "Quản lý giao hàng"** (Iteration 2: workflow, diễn giải các bước, BR01–BR02, ảnh màn hình danh sách phiếu giao hàng)
- Thông tin QC cung cấp: loại BBĐT (11/11/2026), tool QC GH Vendor
