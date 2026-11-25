# RULE CHỦ THỂ — ĐƠN HÀNG

> Xem đơn hàng sau khi tạo, thời điểm sinh khoản thu / giao & lắp đặt / BBĐT, các kênh tạo đơn.
> Tách từ `../01-DON-HANG/kenh-ban/00-CHUNG.md`; số mục (§) giữ theo file gốc.

Rule riêng từng kênh tạo đơn: thư mục [`kenh-ban/`](kenh-ban/) ngay trong chủ thể này (rule chung `kenh-ban/00-CHUNG.md` + 1 file / kênh), mục lục ở [`RULE-CHINH-SACH-KENH-BAN.md`](../../RULE-CHINH-SACH-KENH-BAN.md).

---

## 3. Sau khi tạo đơn hàng (mọi kênh)

- **Xem thông tin đơn hàng:** vào **SPF Web admin** — http://saleplatform-stag.fpt.net/web-admin/Account/Login (nguồn: QC cung cấp 04/11/2026).
- Tạo đơn hàng xong sẽ có **thông tin hợp đồng**. Riêng **SOP (Desktop, Mobile)**: **bán mới** tạo báo giá xong mới có đơn hàng, phải bấm **Tạo hợp đồng** mới có hợp đồng (xem mục Báo giá SOP bên dưới). **Bán thêm** không qua báo giá: chọn dịch vụ → màn Tạo đơn (có sẵn số hợp đồng) → nhấn **Tạo đơn hàng** ⇒ sang màn Chi tiết đơn hàng, cập nhật đơn nếu có → nhấn **Gen BBĐT/PLHD** ⇒ gen xong mới có **khoản thu** và **BBĐT**; giao & lắp đặt theo PTTT: **Thanh toán khi triển khai** ⇒ Gen xong **luôn có phiếu thi công**, **Online** ⇒ **ký BBĐT** ⇒ **thanh toán xong** ⇒ mới gen phiếu; phần sau giống bán mới (nguồn: QC cung cấp 20/11/2026).
- Kiểm tra thông tin hợp đồng ở **tool Tình trạng** trên **Inside** (vd: hợp đồng con có thông tin hợp đồng cha cũng xem ở đây).
- Hợp đồng được dùng khi xuất hóa đơn: thông tin khách, hiệu lực hợp đồng, chi nhánh quản lý, mã tỉnh theo địa chỉ hợp đồng; các loại hợp đồng tổ chức / con / SST / nghiệp vụ có rule riêng (xem `RULE-XHD.md` §4, §6, §7).

---

## Báo giá SOP (Desktop, Mobile) — quy trình tổng quan

> Nguồn: `kenh-ban/SOP/input/URD_BaoGia_v1.0_22 Apr 2026_KieuPTP5.docx` — B. Quy trình nghiệp vụ, mục I (Sơ đồ tổng quan) và II (Flow A–D), mục III.1 (Trạng thái báo giá); kèm thông tin QC xác nhận 19/11/2026 (áp dụng cả App và Desktop; bấm Tạo báo giá là có mã đơn hàng; SOP Online phải bấm Tạo hợp đồng mới có khoản thu).

1. **Sale tạo báo giá** (Flow A): nhập địa chỉ → chọn đối tượng KH → chọn dịch vụ → nhập họ tên, SĐT → áp voucher (nếu có) → chọn **PTTT** (chọn ở bước này, trước khi tạo báo giá — QC xác nhận 19/11/2026; đơn đi nhánh nào sau khi tạo hợp đồng là theo PTTT này) → bấm **Tạo báo giá** ⇒ có **mã đơn hàng** và **link báo giá**; sale gửi link cho KH (Zalo, SMS…).
2. **KH xem báo giá** trên fpt.vn (Flow B), chỉ xem: chọn **Thanh toán** hoặc **Gửi yêu cầu chỉnh sửa** (sale sửa ngay trên link cũ rồi tự gửi lại cho KH).
3. **Lên hợp đồng** — 2 cách:
   - **Sale bấm Tạo hợp đồng** (Flow D, "Tạo thẳng HĐ"): lúc này mới có **hợp đồng**; link báo giá bị thu hồi; đơn đi tiếp luồng bán hiện có theo PTTT. SOP Online: tạo hợp đồng xong mới có **khoản thu** (Chưa thanh toán) và BBĐT.
   - **KH tự thanh toán qua link** (Flow C, chỉ **mua mới**): hệ thống kiểm tra chính sách, voucher còn hợp lệ ⇒ tạo khoản thu ⇒ KH quét QR (hiệu lực 8 phút) ⇒ thanh toán thành công ⇒ báo giá có **mã hợp đồng**, đơn đẩy đi triển khai.
4. **Trạng thái báo giá:** Đã tạo báo giá · Yêu cầu điều chỉnh · Đang thanh toán · Đã thanh toán (có mã HĐ) · Vô hiệu hóa (sale thu hồi link, hoặc cùng SĐT đã thanh toán ở link khác).

**Điểm cần hỏi BA:**
- ~~BA-1: báo giá có áp dụng cho bán thêm không?~~ Đã rõ: bán thêm SOP **không qua báo giá**, tạo đơn rồi Gen BBĐT/PLHD (nguồn: QC cung cấp 20/11/2026).
- BA-2: URD không nêu thời điểm có mã đơn hàng (chỉ nêu mã đơn ở màn Hoàn tất sau thanh toán); thực tế: bấm Tạo báo giá là có mã đơn (QC xác nhận 19/11/2026).

---

### 4.0 Khi nào sinh khoản thu, giao & lắp đặt, BBĐT (tổng hợp)

> Tổng hợp từ §4.1, §4.2, §4.4 và rule từng kênh. BBĐT là **thực thể riêng**, không phụ thuộc phiếu thi công.
>
> **Loại BBĐT** (nguồn: QC cung cấp 11/11/2026): **Không auto ký** (ký tay: trên SPF Web admin hoặc khách ký trên app HiFPT › Tài khoản › Hợp đồng/Phụ lục — QC cung cấp 25/11/2026) → Internet, FPT Camera B2B, FPT Camera Combo, Tổng đài Oncall, Ultra Fast, FPT Play · **Auto ký** → các dịch vụ còn lại: FPT Camera Only, FPT Play Stands Alone, Sản phẩm khác, FPT Smart Home, Ultra Fast Stand Alone, FPro, FSafe Go, VioEdu Stand Alone, VIP 247, SIM data, Pay Wifi, HyperFast, FPT AI Wi-Fi · Vendor → tự động ký · Shopee/TikTok → có BBĐT, gen sau khi tạo đơn thành công; loại BBĐT (auto ký / ký tay) theo dịch vụ như mọi kênh (QC xác nhận 19/11/2026).

| Trường hợp | Áp dụng | Khoản thu | Giao & lắp đặt | BBĐT |
|---|---|---|---|---|
| 1. Cả 3 cùng lúc | PTTT = Thanh toán khi triển khai (mọi kênh có khoản thu) | Sau khi tạo đơn, Chưa thanh toán | **Phiếu thi công:** sau khi tạo đơn (không chờ thanh toán) | Sau khi tạo đơn |
| 2. Khoản thu trước | Desktop / Mobile, PTTT Online | **Sau khi bấm Tạo hợp đồng** (QC xác nhận 19/11/2026), Chưa thanh toán | Sau khi KH thanh toán khoản thu | **Sau khi bấm Tạo hợp đồng**, cùng lúc khoản thu (chưa thanh toán đã có BBĐT — QC xác nhận 19/11/2026) |
| 3. PTTT Online: KH thanh toán trước, rồi mới tạo đơn, khoản thu, phiếu thi công, BBĐT | DKOL, PTTT Online | Khi tạo đơn, trạng thái **Đã thanh toán** | Sau khi tạo đơn | Sau khi tạo đơn |
| 4. Không có khoản thu | Shopee / TikTok | Không có — dùng Order Transaction | **PTC / phiếu giao tại quầy tạo sau khi tạo đơn hàng thành công** (hoàn tất trước khi xuất HĐ; phiếu giao xác nhận 19/11/2026) | **Sau khi tạo đơn hàng thành công** |
| 5. Không tạo khoản thu | VNTT | Không tạo | **Chưa rõ** | **Chưa rõ** |
| 6. Không có phiếu, BBĐT auto ký | **Kênh:** FPL (cả kênh) · **Dịch vụ:** Ultra Fast SA, FPT Play SA, HyperFast SA | Theo PTTT | Không có phiếu | **Có, auto ký** |
| 7. Phiếu tại quầy / Vendor | Mọi PTTT (kể cả Thanh toán khi triển khai), **trừ đơn sàn TMĐT** (xem dòng 4) | Theo PTTT | **Chỉ gen sau khi đơn đã thanh toán** | Quầy: **FPT Camera Combo** phải ký; **Sản phẩm khác, FPT Camera Only** **tự động ký** · Vendor: **tự động ký** |

**Cần xác nhận:**
- VNTT: có phiếu, BBĐT không?
