# Input — KHOẢN THU

Tài liệu đầu vào của quy trình nghiệp vụ ở [`../quy-trinh-nghiep-vu.md`](../quy-trinh-nghiep-vu.md).

## Tool

### Tool thao tác, cập nhật
- **SPF Web admin** — Chi tiết đơn hàng › Receipt › Thanh toán online — thanh toán khoản thu (STG).
- **App HiFPT** — Thanh toán › Trả hộ ngay — thanh toán khoản thu (STG).
- **Web thanh toán** — https://staging.fpt.vn/pay — thanh toán khoản thu (STG).

### Tool kiểm tra
- **Inside – Đối soát khoản thu online** — Foxpay › Thanh toán online › Đối soát khoản thu online — kiểm tra khoản thu.
- **Inside – Tiền đặt cọc** — Quản lý kế toán › Tiền đặt cọc › Tra cứu — kiểm tra tiền đã đẩy vào cọc.

## Thao tác

### Thanh toán khoản thu khi test (STG) — chọn 1 trong 3 cách
1. App HiFPT › Thanh toán › Trả hộ ngay.
2. Web https://staging.fpt.vn/pay.
3. SPF Web admin › Chi tiết đơn hàng › Receipt › Thanh toán online.

### Kiểm tra sau khi thanh toán
1. Inside › Foxpay › Thanh toán online › Đối soát khoản thu online: khoản thu Đã thanh toán.
2. Inside › Quản lý kế toán › Tiền đặt cọc › Tra cứu: tiền đã vào cọc.

## Nghiệp vụ chính

- Khoản thu của đơn hàng: **số tiền khoản thu = số tiền đơn hàng**; trạng thái Chưa thanh toán / Đã thanh toán.
- PTTT Thanh toán khi triển khai: tạo đơn xong có ngay khoản thu (Chưa thanh toán), phiếu thi công, BBĐT.
- PTTT Online: DKOL thanh toán trước rồi mới tạo đơn (khoản thu Đã thanh toán); SOP Desktop/Mobile bấm Tạo hợp đồng mới có khoản thu.
- Shopee, TikTok không có khoản thu (dùng Order Transaction); VNTT không tạo khoản thu.
- Thanh toán xong: khoản thu Đã thanh toán ⇒ tiền đẩy vào cọc ⇒ có tín hiệu thì xuất hóa đơn ⇒ gạch nợ bằng cọc.

## Nguồn

- Thông tin QC cung cấp (ghi ở đầu từng mục trong `quy-trinh-nghiep-vu.md`): 04/11/2026 (thông tin, cách thanh toán, thẻ test), 17/11/2026 (luồng cọc, gạch nợ)
- Thông tin QC cung cấp 25/11/2026: kiểm tra tiền đặt cọc ở Inside › Quản lý kế toán › Tiền đặt cọc › Tra cứu.
