# RULE TOOL CHÍNH SÁCH & CÁC KÊNH BÁN HÀNG (STG) — MỤC LỤC

> Nguồn: thông tin QC cung cấp ngày 03/11/2026. Dùng kèm `RULE-XHD.md`.
> Nội dung đã tách theo từng kênh vào thư mục [`nghiep-vu/01-DON-HANG/kenh-ban/`](nghiep-vu/01-DON-HANG/kenh-ban/): mỗi kênh 1 thư mục `<KÊNH>/` gồm `<KÊNH>.md` + `input/` riêng; Desktop + Mobile gom chung thư mục `SOP/`.

## Rule chung
[nghiep-vu/01-DON-HANG/kenh-ban/00-CHUNG.md](nghiep-vu/01-DON-HANG/kenh-ban/00-CHUNG.md): tool chính sách BP, hình thức triển khai thiết bị, sau khi tạo đơn, thanh toán & khoản thu, cách hoàn tất phiếu, hủy đơn hàng, URL/host STG.

## Kênh đang tạo được đơn (11)

| Kênh | ID | Owner | Nơi tạo đơn | Loại đơn / dịch vụ | File |
|---|---|---|---|---|---|
| Desktop | 2 | KhiemBT | Web SOP | Bán mới + bán thêm, 19 dịch vụ | [DESKTOP.md](nghiep-vu/01-DON-HANG/kenh-ban/SOP/DESKTOP.md) |
| Mobile | 1 | KhiemBT | App SOP | Bán mới + bán thêm, 19 dịch vụ | [MOBILE.md](nghiep-vu/01-DON-HANG/kenh-ban/SOP/MOBILE.md) |
| DKOL | 4 | TaiTT13 | HiFPT / FPT.vn | Bán mới + bán thêm | [DKOL.md](nghiep-vu/01-DON-HANG/kenh-ban/DKOL/DKOL.md) |
| FPL | 10 | — | Web FPL (dev.fptplay.vn) | FPT Play SA | [FPL.md](nghiep-vu/01-DON-HANG/kenh-ban/FPL/FPL.md) |
| Shopee | 20 | HaiPV7 | Web admin SPF (Retry Order) | Bán mới · hạn key 4h | [SHOPEE.md](nghiep-vu/01-DON-HANG/kenh-ban/SHOPEE/SHOPEE.md) |
| TikTok | 21 | HaiPV7 | Web admin SPF (Retry Order) | Bán mới | [TIKTOK.md](nghiep-vu/01-DON-HANG/kenh-ban/TIKTOK/TIKTOK.md) |
| W-Sale | 9 | HoangVT11 | Web W-Sale | 2 luồng: lên đơn tích hợp SOP (bán mới, bán thêm qua SDK SOP) · Swap (Wifi 6, Box Only, Combo) | [W-SALE.md](nghiep-vu/01-DON-HANG/kenh-ban/W-SALE/W-SALE.md) |
| CRM | 13 | HoangPHD | Web CRM | Chỉ FPT Play SME | [CRM.md](nghiep-vu/01-DON-HANG/kenh-ban/CRM/CRM.md) |
| CRM-APP | 16 | PhuongTT3 | App FPT Life | Chỉ cloud nhóm FPT Camera Only | [CRM-APP.md](nghiep-vu/01-DON-HANG/kenh-ban/CRM-APP/CRM-APP.md) |
| Momo | 17 | HaiPV7 | Nhờ owner tạo | Play, combo Play; Camera off | [MOMO.md](nghiep-vu/01-DON-HANG/kenh-ban/MOMO/MOMO.md) |
| VNTT | 11 | HaiPV7 | — | Chỉ ghi nhận HĐ, không tạo khoản thu | [VNTT.md](nghiep-vu/01-DON-HANG/kenh-ban/VNTT/VNTT.md) |

## Kênh chưa dùng được (11)
API, F-Retail, TGDD, HiFPT (đã sang DKOL), MBBank, App Partner, Shop, SR-KPDV, Ven-vrace, WebSDK, Outside — xem [KENH-CHUA-DUNG-DUOC.md](nghiep-vu/01-DON-HANG/kenh-ban/KENH-CHUA-DUNG-DUOC.md).
