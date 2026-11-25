# Input — SR THANH LÝ / TẠM NGƯNG (TL/TN)

Tài liệu đầu vào của quy trình nghiệp vụ ở [`../quy-trinh-nghiep-vu.md`](../quy-trinh-nghiep-vu.md).

## Tool

- **Tool SR** — Fox ERP › Service Request — tạo và xử lý SR.
- **Inside – Xử lý giao dịch** — người xử lý nhập thông tin thanh lý / tạm ngưng trên màn xử lý giao dịch.
- **Inside – Khoản thu** — khoản thu lớn hơn 0 thì tạo ticket thu tiền; trả xong thì Đã thanh toán.
- **Inside – Thu hồi thiết bị** — tạo ticket thu hồi nếu có chọn thu hồi.
- **Quản lý chuỗi cung ứng – Vật tư thu hồi** — Quản lý chuỗi cung ứng › Quản lý vật tư thu hồi — kiểm tra, xử lý thiết bị thu hồi (QC cung cấp 25/11/2026).
- **App HiFPT – Ký kết** — Tài khoản › Hợp đồng/Phụ lục — Inside tạo biên bản, **khách vào app HiFPT ký** (QC cung cấp 25/11/2026).
- **Owner dịch vụ** — SR gửi thông tin thanh lý / tạm ngưng khi xử lý xong.

## Thao tác

### Thanh lý hoặc tạm ngưng hợp đồng (SR)
1. Tạo SR: chọn hợp đồng, loại thanh lý hoặc tạm ngưng (tạm ngưng chọn 1–6 tháng).
2. Liên hệ, tư vấn giữ khách.
3. Khách không dùng tiếp: miễn giảm → thu tiền → thu hồi thiết bị nếu có → ký kết.
4. Hệ thống gửi thông tin sang owner dịch vụ → SR Đã xử lý.

### Giữ khách khi khách đồng ý dùng tiếp
1. Chọn phương án hỗ trợ: kỹ thuật, bồi hoàn, hủy / điều chỉnh giảm hóa đơn, hoặc sub SR chuyển địa điểm / chuyển dịch vụ.

## Ý chính tài liệu

### `ISC-FTEL SR_V1.0_TL_TN_URD V1.0.docx`
- SR **thanh lý / tạm ngưng**; hợp đồng Bình thường, Ngưng vì lý do thanh toán hoặc Chủ thuê bao đi vắng; tạm ngưng 1–6 tháng.
- Tư vấn giữ khách trước: dùng tiếp thì hỗ trợ kỹ thuật, bồi hoàn, hủy / điều chỉnh giảm hóa đơn hoặc sub SR CDD/CDV.
- Không dùng tiếp: miễn giảm → thu tiền (khoản thu lớn hơn 0) → thu hồi thiết bị nếu có → ký kết → gửi sang owner dịch vụ.

## Nguồn

- `ISC-FTEL SR_V1.0_TL_TN_URD V1.0.docx` (file nằm ở [input của SR](../../input/))
- Thông tin QC cung cấp 25/11/2026: khách ký trên app HiFPT › Tài khoản › Hợp đồng/Phụ lục.
- Thông tin QC cung cấp 25/11/2026: thu hồi thiết bị xử lý / kiểm tra ở tool Quản lý chuỗi cung ứng › Quản lý vật tư thu hồi.
