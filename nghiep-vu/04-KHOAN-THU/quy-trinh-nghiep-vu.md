# RULE CHỦ THỂ — KHOẢN THU

> Thông tin khoản thu, thời điểm sinh theo PTTT, sau khi thanh toán, cách thanh toán (STG).
> Tách từ `../01-DON-HANG/kenh-ban/00-CHUNG.md`; số mục (§) giữ theo file gốc.

---

### 4.0a Thông tin khoản thu

> Nguồn: thông tin QC cung cấp ngày 04/11/2026.

| Trường | Ý nghĩa |
|---|---|
| Hợp đồng | Số hợp đồng của khoản thu |
| Nội dung | Nội dung khoản thu |
| Số tiền | Số tiền khoản thu |
| Trạng thái | Chưa thanh toán / Đã thanh toán |

**Rule:** khoản thu của đơn hàng ⇒ **số tiền khoản thu = số tiền đơn hàng**.

### 4.1 PTTT = Thanh toán khi triển khai (mọi kênh có khoản thu)
Ngay **sau khi tạo đơn** (không chờ thanh toán), hệ thống gen **đồng thời**:
- Khoản thu
- Phiếu thi công
- Biên bản điện tử
- Tình trạng đơn hàng = **Chưa thanh toán**

### 4.2 PTTT Online — theo kênh

| Kênh | Luồng | Chi tiết |
|---|---|---|
| DKOL | KH thanh toán xong mới tạo đơn ⇒ đơn và khoản thu **Đã thanh toán** ⇒ gen phiếu thi công, biên bản điện tử | [DKOL.md](../01-DON-HANG/kenh-ban/DKOL/DKOL.md) |
| Desktop / Mobile | Tạo báo giá (có mã đơn) ⇒ bấm **Tạo hợp đồng** ⇒ khoản thu **Chưa thanh toán** và biên bản điện tử (chưa thanh toán đã có BBĐT — QC xác nhận 19/11/2026) ⇒ KH thanh toán ⇒ gen phiếu thi công | [DESKTOP.md](../01-DON-HANG/kenh-ban/SOP/DESKTOP.md), [MOBILE.md](../01-DON-HANG/kenh-ban/SOP/MOBILE.md) |
| Shopee / TikTok | **Không có khoản thu**, dùng Order Transaction (2 lần) | [SHOPEE.md](../01-DON-HANG/kenh-ban/SHOPEE/SHOPEE.md), [TIKTOK.md](../01-DON-HANG/kenh-ban/TIKTOK/TIKTOK.md) |
| VNTT | Chỉ ghi nhận HĐ, **không tạo khoản thu** | [VNTT.md](../01-DON-HANG/kenh-ban/VNTT/VNTT.md) |

### 4.3 Sau khi thanh toán khoản thu
- Khoản thu phải chuyển sang **Đã thanh toán**.
- Tiền được **đẩy vào cọc**.

**Luồng thanh toán → cọc → hóa đơn → gạch nợ** (SOP Desktop/Mobile, DKOL, FPL) (nguồn: QC cung cấp 17/11/2026):
1. Khách thanh toán ⇒ hệ thống cập nhật khoản thu **Đã thanh toán**.
2. Hệ thống **nhập cọc**.
3. Nhận được **tín hiệu xuất hóa đơn** ⇒ hệ thống xuất hóa đơn.
4. **Có cọc** ⇒ hệ thống **gạch nợ hóa đơn** theo cọc và cập nhật hóa đơn **Đã thanh toán**.
5. Hóa đơn **dịch vụ trả trước** ⇒ hệ thống **add tiền trả trước**.

**Cách gạch nợ theo loại đơn** (nguồn: QC cung cấp 17/11/2026):
- Đơn **TMĐT** (Shopee, TikTok) ⇒ hệ thống **gạch nợ theo Paid**.
- Đơn **khác TMĐT** ⇒ hệ thống **gạch nợ bằng cọc**.
- Hóa đơn có **dịch vụ trả trước** ⇒ hệ thống **add tiền trả trước**.
- **Kiểm tra khoản thu:** Inside › menu **Foxpay › Thanh toán online › Đối soát khoản thu online**.
- **Kiểm tra tiền đặt cọc:** Inside › menu **Quản lý kế toán › Tiền đặt cọc › Tra cứu** (QC cung cấp 25/11/2026).

---

### 4.5 Cách thanh toán khoản thu (STG)

> Nguồn: thông tin QC cung cấp ngày 04/11/2026.

Có 3 cách:
1. **App HiFPT:** menu **Thanh toán › Trả hộ ngay**.
2. **Web:** https://staging.fpt.vn/pay
3. **SPF Web admin** (http://saleplatform-stag.fpt.net/web-admin/Account/Login): vào **chi tiết đơn hàng › Receipt** › nhấn **Thanh toán online**.

**Thẻ test thanh toán (STG)** — nguồn: QC cung cấp 04/11/2026:

| Loại thẻ | Thông tin |
|---|---|
| Thẻ tín dụng | VISA: `4000000000001091` · Mastercard: `5200000000001096` · Tên chủ thẻ: NGUYEN VAN A · Hiệu lực: 12/26 · CVV: 111 · Pass: 1234 |
| Thẻ nội địa | Số thẻ: `9704 0000 0000 0018` · Tên chủ thẻ: NGUYEN VAN A · Ngày phát hành: 03/07 · OTP: otp |
