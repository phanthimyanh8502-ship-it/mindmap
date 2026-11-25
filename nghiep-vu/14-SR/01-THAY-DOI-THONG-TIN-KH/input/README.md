# Input — SR THAY ĐỔI THÔNG TIN KHÁCH HÀNG

Tài liệu đầu vào của quy trình nghiệp vụ ở [`../quy-trinh-nghiep-vu.md`](../quy-trinh-nghiep-vu.md).

## Tool

### Tool thao tác, cập nhật
- **Tool SR** — Fox ERP › Service Request — tạo và xử lý SR.
- **Econtract – Biên bản điện tử** — hệ thống tự gen biên bản (dạng thông báo hoặc cần ký).
- **App HiFPT – Ký kết** — Tài khoản › Hợp đồng/Phụ lục — khách ký biên bản; chuyển chủ sở hữu thì cả chủ cũ và chủ mới ký (QC cung cấp 25/11/2026).
- **Chốt cước** — Quản lý hợp đồng › Chốt cước — chuyển chủ sở hữu: chốt cước tới ngày hiệu lực (QC cung cấp 25/11/2026).
- **FLI – SĐT Camera** — SR gọi FLI cập nhật SĐT dịch vụ FPT Camera.
- **Hệ thống quản lý khách hàng, hợp đồng** — nhận thông tin mới khi SR xử lý xong.

## Thao tác

### Đổi thông tin khách hàng trên hợp đồng (SR)
1. Tạo SR: chọn hợp đồng, loại thay đổi, nguyên nhân.
2. Liên hệ, tư vấn khách.
3. Xử lý giao dịch: nhập thông tin mới.
4. Khách ký biên bản điện tử trên HiFPT (hoặc biên bản dạng thông báo).
5. Hệ thống cập nhật thông tin khách hàng vào hợp đồng → SR Đã xử lý.

### Chuyển chủ sở hữu hợp đồng (SR)
1. Xử lý giao dịch: nhập chủ hợp đồng mới, ngày hiệu lực.
2. Xử lý miễn giảm, thu tiền chốt cước.
3. Chủ cũ và chủ mới cùng ký biên bản điện tử → hệ thống cập nhật hợp đồng.

## Ý chính tài liệu

### `ISC-FTEL SR Web thay đổi thông tin Khách hàng_URD V3.0.docx`
- SR đổi thông tin chủ hợp đồng, MST, người đại diện, SĐT, email, địa chỉ (lắp đặt, thanh toán, xuất hóa đơn), PTTT, SĐT dịch vụ; **chuyển chủ sở hữu** là luồng riêng.
- Điều kiện: hợp đồng chưa chấm dứt, chưa có SR đổi thông tin đang mở; đổi PTTT thì hợp đồng không còn hóa đơn chưa thanh toán.
- Có biên bản điện tử (dạng thông báo hoặc khách ký trên HiFPT); chuyển chủ sở hữu luôn ký, cả 2 bên.
- Chuyển chủ sở hữu có thu tiền chốt cước (tiền chốt cước + cước 2 tháng trước), có thể miễn giảm.
- Kết quả: hệ thống quản lý khách hàng, hợp đồng nhận thông tin mới.

## Nguồn

- `ISC-FTEL SR Web thay đổi thông tin Khách hàng_URD V3.0.docx` (file nằm ở [input của SR](../../input/))
- Thông tin QC cung cấp 25/11/2026: khách ký trên app HiFPT › Tài khoản › Hợp đồng/Phụ lục.
- Thông tin QC cung cấp 25/11/2026: menu chốt cước là Quản lý hợp đồng › Chốt cước.
