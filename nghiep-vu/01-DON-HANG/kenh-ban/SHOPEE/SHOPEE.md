# KÊNH SHOPEE (SaleChannelID 20)

> Tách từ `RULE-CHINH-SACH-KENH-BAN.md` (nguồn: QC cung cấp 03/11/2026). Rule chung: [00-CHUNG.md](../00-CHUNG.md) · Rule XHD: [`../../../../RULE-XHD.md`](../../../../RULE-XHD.md). Kênh cùng luồng: [TIKTOK.md](../TIKTOK/TIKTOK.md).

## Thông tin chung

| Mục | Nội dung |
|---|---|
| Owner | HaiPV7 |
| Nơi tạo đơn | Web admin SPF (menu Retry Order) |
| Loại đơn | Bán mới |

## Dịch vụ (bán mới)
Internet, FPT Camera Only, FPT Play Stands Alone, FPT Play, Sản phẩm khác.

## Chuẩn bị
- Nhờ owner kéo đơn từ PRO về (kèm **refcode**).
- Sao chép chính sách về staging.
- Nhờ owner **map SKU**.
- ⚠️ Đơn Shopee có **hạn key 4 giờ** — hết 4h thì nhờ owner kéo key về lại.

## Cách tạo đơn (Web admin SPF)
1. Truy cập web admin: http://saleplatform-stag.fpt.net/web-admin/Account/Login
2. Chọn menu **Retry Order**.
3. Tìm kiếm đơn hàng với **refcode** owner cung cấp.
4. Nếu có thông tin thì thao tác **ngắt kết nối đơn hàng**.
5. Chuyển qua tab **Cập nhật địa chỉ, SĐT**.
6. Tìm kiếm đơn hàng với refcode owner cung cấp.
7. Nhấn **Load**.
8. Nhập thông tin đầy đủ.
9. Nhấn **Submit**.

## Hình thức triển khai
**Quầy** (có chính sách shipper giao hàng) và **TIN/PNC**. Cách hoàn tất phiếu: [00-CHUNG.md §5.1, §5.2](../00-CHUNG.md#5-cách-hoàn-tất-phiếu-giao-hàng--triển-khai-stg).

## Thanh toán — không có khoản thu

**Lần 1 — Đơn ghi nhận khách hàng đã thanh toán cho sàn**
1. Shopee gửi đơn.
2. SPF tạo đơn với trạng thái **Chưa thanh toán**.
   - **PTC và BBĐT được gen sau khi tạo đơn hàng thành công** (nguồn: QC cung cấp 04/11/2026).
3. Tạo **Order Transaction** với trạng thái **Thanh toán tạm** (KH đã thanh toán cho sàn).
4. Cập nhật đơn SPF sang **Đã thanh toán**.
5. Phiếu thi công (PTC) hoàn tất.
6. Xuất hóa đơn theo rule quy định (xem `RULE-XHD.md`) và **gạch nợ hóa đơn tạm**.

**Lần 2 — Sàn quyết toán tiền về FTEL**
1. Shopee gửi thông tin quyết toán.
2. SPF **không cập nhật** đơn hàng.
3. Order Transaction cập nhật trạng thái **Đã thanh toán**; **Order Paid** ghi nhận phí sàn và số tiền FTEL thực lãnh.
4. IIA thực hiện **gạch nợ hóa đơn thật**.

## Phạm vi test XHD
Chỉ bán mới {1,3,5,6,7} — hồi quy Phase 1 — `RULE-XHD.md` §1.1.
