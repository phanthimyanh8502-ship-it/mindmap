# KÊNH MOBILE (SaleChannelID 1)

> Tách từ `RULE-CHINH-SACH-KENH-BAN.md` (nguồn: user cung cấp 03/11/2026). Rule chung: [00-CHUNG.md](../00-CHUNG.md) · Rule XHD: [`../../../../RULE-XHD.md`](../../../../RULE-XHD.md).

## Thông tin chung

| Mục | Nội dung |
|---|---|
| Owner | KhiemBT |
| Nơi tạo đơn | **App SOP** |
| Loại đơn | Bán mới + bán thêm (giống Desktop) |

## Dịch vụ
Giống Desktop (19 dịch vụ) — xem [DESKTOP.md](DESKTOP.md#dịch-vụ-19).

## Cách tạo đơn
1. Chọn menu **Đơn hàng**.
2. Tại tab bán thêm / bán mới chọn dấu **+**.

### Bán mới (giống Desktop)
Chọn + ở bán mới → tìm địa chỉ → xác nhận → đối tượng KH → dịch vụ → chi tiết giỏ hàng → cập nhật thông tin KH → tạo báo giá → tạo hợp đồng → cập nhật HĐ nếu muốn.

### Bán thêm (giống Desktop)
Chọn + ở bán thêm → tìm HĐ → icon + → dịch vụ → màn hình Tạo đơn (có số hợp đồng) → nhấn **Tạo đơn hàng** ⇒ sang màn Chi tiết đơn hàng → cập nhật đơn hàng (nếu có) → nhấn **Gen BBĐT/PLHD** ⇒ gen xong mới có khoản thu và BBĐT. Giao & lắp đặt: PTTT Thanh toán khi triển khai ⇒ Gen xong luôn có phiếu thi công; PTTT Online ⇒ ký BBĐT ⇒ thanh toán xong ⇒ mới gen phiếu. Phần sau giống bán mới. Không qua báo giá (nguồn: user cung cấp 20/11/2026).

Chi tiết từng bước: [DESKTOP.md](DESKTOP.md#cách-tạo-đơn).

## Hình thức triển khai
Giống Desktop — theo chính sách khai báo, xem [00-CHUNG.md §2](../00-CHUNG.md#2-quy-tắc-hình-thức-triển-khai-thiết-bị).

## Thanh toán & khoản thu
Giống Desktop:
- **PTTT = Thanh toán khi triển khai:** gen đồng thời khoản thu, phiếu thi công, biên bản điện tử; đơn = **Chưa thanh toán**.
- **PTTT Online:** tạo báo giá (có mã đơn, **Chưa thanh toán**) ⇒ bấm **Tạo hợp đồng** mới có khoản thu **Chưa thanh toán** và **biên bản điện tử** (chưa thanh toán đã có BBĐT — user xác nhận 19/11/2026) ⇒ khách thanh toán xong ⇒ mới gen **phiếu thi công**.
- **Thanh toán → cọc → hóa đơn → gạch nợ** (nguồn: user cung cấp 17/11/2026): giống DKOL — khoản thu **Đã thanh toán** ⇒ **nhập cọc** ⇒ nhận tín hiệu thì xuất hóa đơn ⇒ có cọc thì **gạch nợ**, hóa đơn **Đã thanh toán** ⇒ dịch vụ **trả trước** thì **add tiền trả trước**. Chi tiết: [00-CHUNG.md §4.3](../00-CHUNG.md#43-sau-khi-thanh-toán-khoản-thu).

## Phạm vi test XHD
Bán mới + bán thêm, 19 nhóm (trừ nhóm 25 Prepaid 3) — `RULE-XHD.md` §1.1.

## Báo giá
PTTT chọn trước khi bấm Tạo báo giá (user xác nhận 19/11/2026). Bấm **Tạo báo giá** là có mã đơn hàng; phải bấm **Tạo hợp đồng** mới có hợp đồng (và khoản thu với PTTT Online) — user xác nhận 19/11/2026. Quy trình tổng quan: [`../quy-trinh-nghiep-vu.md`](../../quy-trinh-nghiep-vu.md) mục Báo giá SOP (nguồn URD Báo giá v1.0).
