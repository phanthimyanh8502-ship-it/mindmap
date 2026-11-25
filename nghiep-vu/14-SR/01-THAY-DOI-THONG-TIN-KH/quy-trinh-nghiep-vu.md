# RULE — SR THAY ĐỔI THÔNG TIN KHÁCH HÀNG

> Một loại SR của [SR](../quy-trinh-nghiep-vu.md); luồng chung (tạo, phân công, liên hệ, đánh giá) xem ở đó.

Nguồn: URD SR Web thay đổi thông tin Khách hàng v3.0, §C.II.

- Đổi: thông tin chủ hợp đồng, MST, loại hình KH, người đại diện, SĐT, email, địa chỉ (lắp đặt, thanh toán, xuất hóa đơn), PTTT, SĐT dịch vụ, **chuyển chủ sở hữu** (chọn riêng).
- Điều kiện: hợp đồng chưa chấm dứt, chưa có SR đổi thông tin đang mở. Đổi PTTT: hợp đồng không còn hóa đơn chưa thanh toán.

| # | Bước | Hệ thống |
|---|---|---|
| 1 | Tạo SR, liên hệ tư vấn khách | Hệ thống SR |
| 2 | Nhập thông tin mới. Chuyển chủ sở hữu: nhập chủ mới, ngày hiệu lực, có **miễn giảm / thu tiền** chốt cước | Hệ thống SR, Inside |
| 3 | **Biên bản điện tử**: dạng thông báo hoặc khách ký trên HiFPT. Chuyển chủ sở hữu: luôn ký, cả 2 bên | Econtract, HiFPT |
| 4 | Đổi SĐT Camera: cập nhật sang FLI | FLI |
| 5 | Cập nhật thông tin khách hàng vào hợp đồng → SR Đã xử lý | Hệ thống quản lý khách hàng, hợp đồng |

Lần phát hành hóa đơn sau dùng thông tin mới nhất; cập nhật không kích hoạt phát hành (BR-DB-03).
