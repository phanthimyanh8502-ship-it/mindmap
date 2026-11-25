# RULE CHUNG CHO MỌI KÊNH BÁN (STG)

> Tách từ `RULE-CHINH-SACH-KENH-BAN.md` (nguồn: thông tin user cung cấp ngày 03/11/2026). Dùng kèm [`../../../RULE-XHD.md`](../../../RULE-XHD.md).
> Rule riêng từng kênh: xem [mục lục](../../../RULE-CHINH-SACH-KENH-BAN.md).

---

## 1. Tool chính sách (BP)

- **URL:** http://bp-stag.fpt.net/
- **Host:** **Cần host** (khai báo host trước khi truy cập)
- **Mục đích:** khai báo chính sách bán hàng cho các kênh FTEL.

### Chính sách quyết định gì
- **Giá bán** của SPDV.
- **Các gói bán** của dịch vụ.
- **Khu vực bán** (bán ở khu vực nào).
- **Thiết bị đi kèm** (bán kèm thiết bị gì).
- **Đối tượng khách hàng** được bán.
- **Kênh bán** (bán ở kênh nào).
- **Đơn vị bán hàng**.
- **Phương thức thanh toán**.
- **Loại khách hàng:** khách hàng mới hay khách hàng cũ.
- **Hình thức triển khai** của thiết bị (xem §2).
- **Phiếu mua hàng / voucher:** khách hàng hoặc nhân viên add vào lúc tạo đơn (nguồn: user cung cấp 04/11/2026).

### Cách tạo chính sách bán hàng
1. Tìm chính sách bán hàng có sẵn với dịch vụ muốn bán.
2. **Sao chép** chính sách đó.
3. Chọn **Sửa** → chọn/nhập thông tin muốn tạo → **Lưu**.
4. Nhấn **Trở về** → chọn **Gửi đề xuất**.
5. Vào menu **Bán hàng** → tab **Bán hàng**.
6. Tìm mã chính sách vừa gửi đề xuất → tích chọn → **Tạo quyết định**.
7. Nhập thông tin hợp lệ → **Lưu**.

---

## 2. Quy tắc hình thức triển khai thiết bị

Thiết bị có nhiều hình thức triển khai tùy theo chính sách khai báo:

| Hình thức triển khai | Đẩy qua |
|---|---|
| Không, Quầy, Sale | **Tool quầy** |
| NCC-Samsung, NCC-Casper | **M-Vendor** |
| TIN/PNC | **Giao & lắp đặt** |

### 2.1 Dịch vụ nào triển khai theo hình thức nào (theo qc-iia)

> Nguồn: `qc-iia/00_input/v2.0/Doc/AnhNQ75-List HT Triển khai.xlsx` (sheet "1. HT Triển khai") + các clarification CL-XHD-27, CL-XHD-34 (chốt 20/10/2026).
> ⚠️ File này **không có bảng liệt kê từng dịch vụ ↔ hình thức triển khai**; hình thức thực tế của mỗi thiết bị do **chính sách khai báo** trên tool BP quyết định.

| HT triển khai | Áp dụng cho dịch vụ | Chủ thể | Đầu ra / tín hiệu |
|---|---|---|---|
| **TIN/PNC** | Thiết bị cần **triển khai, kích hoạt tại địa chỉ đăng ký** của đơn (không giới hạn nhóm dịch vụ — vd Internet kèm modem, như TC của qc-iia) | TIN/PNC | Phiếu thi công theo đơn hàng, loại **Triển khai** |
| **TIN/PNC giao hàng** | **Chỉ Camera Offnet** và **Thiết bị lẻ** — giao hàng, không yêu cầu kích hoạt | TIN/PNC | Phiếu thi công theo đơn hàng, loại **Giao hàng** |
| Quầy | Chỉ Camera Offnet, Thiết bị lẻ | DVKH CN | Phiếu giao dịch bán thiết bị tại quầy |
| Sale | Chỉ Thiết bị lẻ (quản lý MAC) | Nhân viên bán hàng | Phiếu giao dịch bán thiết bị tại quầy |
| NCC Samsung / Sony / Casper | Chỉ Thiết bị lẻ mua từ NCC bán lại (TV…) | Nhà cung cấp | Đơn đặt hàng Vendor + mã vận đơn |
| FTI | SPDV đặc thù, dự án: **OnCall, Camera B2B, ListLine**… (HN, HCM, CNx) | Đối tác FTI | Phiếu thi công, loại Triển khai |
| Không / None | Dịch vụ không cần triển khai, vd **dịch vụ Code SA** (đẩy code qua SMS) | — | Không có phiếu |

**Quy tắc gộp về luồng TIN/PNC:**
- Đơn có **≥1 SPDV** mix TIN/PNC với Quầy/Sale ⇒ **cả đơn** tự xử lý theo luồng TIN/PNC (thiết bị giao tại quầy cũng chờ phiếu thi công).
- Hàng hóa mix "Không" + TIN/PNC ⇒ triển khai bởi TIN/PNC (theo phiếu thi công).
- Chỉ có "Không" ⇒ không đẩy triển khai/giao hàng; thiết bị "Không" chỉ xuất hóa đơn nếu quầy gửi tín hiệu.

**Hình thức triển khai theo kênh** (chi tiết trong file từng kênh):

| Kênh | Hình thức triển khai |
|---|---|
| Desktop, Mobile | Theo chính sách khai báo (bảng §2) |
| DKOL | TIN/PNC (phiếu thi công): dịch vụ cần triển khai, kích hoạt tại địa chỉ — **không phải Camera** · Camera: Quầy (shipper) · TV: Vendor · Ultra Fast SA, FPT Play SA, HyperFast SA: không có phiếu |
| Shopee, TikTok | Quầy (chính sách shipper giao hàng) và TIN/PNC |
| W-Sale | Chỉ TIN/PNC |
| FPL | Không có hình thức triển khai (không có phiếu, BBĐT auto ký) |

---

## 3. Sau khi tạo đơn hàng (mọi kênh)

- **Xem thông tin đơn hàng:** vào **SPF Web admin** — http://saleplatform-stag.fpt.net/web-admin/Account/Login (nguồn: user cung cấp 04/11/2026).
- Tạo đơn hàng xong sẽ có **thông tin hợp đồng**.
- Kiểm tra thông tin hợp đồng ở **tool Tình trạng** trên **Inside** (vd: hợp đồng con có thông tin hợp đồng cha cũng xem ở đây).
- Hợp đồng được dùng khi xuất hóa đơn: thông tin khách, hiệu lực hợp đồng, chi nhánh quản lý, mã tỉnh theo địa chỉ hợp đồng; các loại hợp đồng tổ chức / con / SST / nghiệp vụ có rule riêng (xem `RULE-XHD.md` §4, §6, §7).

### 3.1 Cập nhật thông tin hợp đồng

> Nguồn: thông tin user cung cấp ngày 04/11/2026.

| Cách | Dùng để |
|---|---|
| Inside › **Quản lý hợp đồng › Cập nhật hợp đồng (New)** | Cập nhật thông tin hợp đồng |
| Tạo SR: **Fox ERP** (https://fox-erp-stag.fpt.net/) › menu **Service Request** | Nơi tạo 4 loại SR bên dưới |
| **SR thay đổi thông tin khách hàng** | Thay đổi các thông tin của khách hàng |
| **SR chuyển dịch vụ** | Chuyển các gói dịch vụ **trong cùng 1 nhóm** |
| **SR thanh lý / tạm ngưng** | Cập nhật hợp đồng sang trạng thái **Đã chấm dứt / Tạm ngưng** |
| **SR khôi phục dịch vụ** | Đưa hợp đồng từ **Đã chấm dứt / Tạm ngưng** về **Bình thường** |

Liên quan xuất hóa đơn (`RULE-XHD.md`): hợp đồng tạm ngưng / đã chấm dứt ⇒ không xuất hóa đơn (BR-XHD-10); cập nhật thông tin khách không kích hoạt phát hành, lần phát hành sau dùng thông tin mới nhất (BR-DB-03).

---

## 4. Thanh toán & khoản thu (chung)

### 4.0 Khi nào sinh khoản thu, giao & lắp đặt, BBĐT (tổng hợp)

> Tổng hợp từ §4.1, §4.2, §4.4 và rule từng kênh. BBĐT là **thực thể riêng**, không phụ thuộc phiếu thi công.
>
> **Loại BBĐT** (nguồn: user cung cấp 11/11/2026): **Không auto ký** (phải ký trên SPF Web admin) → Internet, FPT Camera B2B, FPT Camera Combo, Tổng đài Oncall, Ultra Fast, FPT Play · **Auto ký** → các dịch vụ còn lại: FPT Camera Only, FPT Play Stands Alone, Sản phẩm khác, FPT Smart Home, Ultra Fast Stand Alone, FPro, FSafe Go, VioEdu Stand Alone, VIP 247, SIM data, Pay Wifi, HyperFast, FPT AI Wi-Fi · Vendor → tự động ký · Shopee/TikTok → có BBĐT, gen sau khi tạo đơn thành công; loại BBĐT (auto ký / ký tay) theo dịch vụ như mọi kênh (user xác nhận 19/11/2026).

| Trường hợp | Áp dụng | Khoản thu | Giao & lắp đặt | BBĐT |
|---|---|---|---|---|
| 1. Cả 3 cùng lúc | PTTT = Thanh toán khi triển khai (mọi kênh có khoản thu) | Sau khi tạo đơn, Chưa thanh toán | **Phiếu thi công:** sau khi tạo đơn (không chờ thanh toán) | Sau khi tạo đơn |
| 2. Khoản thu trước | Desktop / Mobile, PTTT Online | **Sau khi bấm Tạo hợp đồng** (user xác nhận 19/11/2026), Chưa thanh toán | Sau khi KH thanh toán khoản thu | **Sau khi bấm Tạo hợp đồng**, cùng lúc khoản thu (chưa thanh toán đã có BBĐT — user xác nhận 19/11/2026) |
| 3. PTTT Online: KH thanh toán trước, rồi mới tạo đơn, khoản thu, phiếu thi công, BBĐT | DKOL, PTTT Online | Khi tạo đơn, trạng thái **Đã thanh toán** | Sau khi tạo đơn | Sau khi tạo đơn |
| 4. Không có khoản thu | Shopee / TikTok | Không có — dùng Order Transaction | **PTC / phiếu giao tại quầy tạo sau khi tạo đơn hàng thành công** (hoàn tất trước khi xuất HĐ; phiếu giao xác nhận 19/11/2026) | **Sau khi tạo đơn hàng thành công** |
| 5. Không tạo khoản thu | VNTT | Không tạo | **Chưa rõ** | **Chưa rõ** |
| 6. Không có phiếu, BBĐT auto ký | **Kênh:** FPL (cả kênh) · **Dịch vụ:** Ultra Fast SA, FPT Play SA, HyperFast SA | Theo PTTT | Không có phiếu | **Có, auto ký** |
| 7. Phiếu tại quầy / Vendor | Mọi PTTT (kể cả Thanh toán khi triển khai), **trừ đơn sàn TMĐT** (xem dòng 4) | Theo PTTT | **Chỉ gen sau khi đơn đã thanh toán** | Quầy: **FPT Camera Combo** phải ký; **Sản phẩm khác, FPT Camera Only** **tự động ký** · Vendor: **tự động ký** |

**Cần xác nhận:**
- VNTT: có phiếu, BBĐT không?

### 4.0a Thông tin khoản thu

> Nguồn: thông tin user cung cấp ngày 04/11/2026.

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
| DKOL | KH thanh toán xong mới tạo đơn ⇒ đơn và khoản thu **Đã thanh toán** ⇒ gen phiếu thi công, biên bản điện tử | [DKOL.md](DKOL/DKOL.md) |
| Desktop / Mobile | Tạo báo giá (có mã đơn) ⇒ bấm **Tạo hợp đồng** ⇒ khoản thu **Chưa thanh toán** và biên bản điện tử (chưa thanh toán đã có BBĐT — user xác nhận 19/11/2026) ⇒ KH thanh toán ⇒ gen phiếu thi công | [DESKTOP.md](SOP/DESKTOP.md), [MOBILE.md](SOP/MOBILE.md) |
| Shopee / TikTok | **Không có khoản thu**, dùng Order Transaction (2 lần) | [SHOPEE.md](SHOPEE/SHOPEE.md), [TIKTOK.md](TIKTOK/TIKTOK.md) |
| VNTT | Chỉ ghi nhận HĐ, **không tạo khoản thu** | [VNTT.md](VNTT/VNTT.md) |

### 4.3 Sau khi thanh toán khoản thu
- Khoản thu phải chuyển sang **Đã thanh toán**.
- Tiền được **đẩy vào cọc**.

**Luồng thanh toán → cọc → hóa đơn → gạch nợ** (SOP Desktop/Mobile, DKOL, FPL) (nguồn: user cung cấp 17/11/2026):
1. Khách thanh toán ⇒ hệ thống cập nhật khoản thu **Đã thanh toán**.
2. Hệ thống **nhập cọc**.
3. Nhận được **tín hiệu xuất hóa đơn** ⇒ hệ thống xuất hóa đơn.
4. **Có cọc** ⇒ hệ thống **gạch nợ hóa đơn** theo cọc và cập nhật hóa đơn **Đã thanh toán**.
5. Hóa đơn **dịch vụ trả trước** ⇒ hệ thống **add tiền trả trước**.

**Cách gạch nợ theo loại đơn** (nguồn: user cung cấp 17/11/2026):
- Đơn **TMĐT** (Shopee, TikTok) ⇒ hệ thống **gạch nợ theo Paid**.
- Đơn **khác TMĐT** ⇒ hệ thống **gạch nợ bằng cọc**.
- Hóa đơn có **dịch vụ trả trước** ⇒ hệ thống **add tiền trả trước**.
- **Kiểm tra khoản thu:** Inside › menu **Foxpay › Thanh toán online › Đối soát khoản thu online**.

### 4.4 Kích hoạt dịch vụ sau thanh toán

> Nguồn: thông tin user cung cấp ngày 04/11/2026.

- Sau khi thanh toán xong, hệ thống **active dịch vụ** của đơn hàng trong **hợp đồng**.
- Riêng **tài khoản FPT Play**: được kích hoạt **sau khi ký biên bản (điện tử)** xong.
- **FPT Play SA** (BBĐT auto ký) có 2 hình thức kích hoạt: **gửi code qua SMS** để khách hàng nhập kích hoạt, hoặc **auto kích hoạt**.
- **Cách ký biên bản điện tử (BBĐT):** SPF Web admin › **chi tiết đơn hàng › Thông tin khác › Ký BBĐT**.

### 4.5 Cách thanh toán khoản thu (STG)

> Nguồn: thông tin user cung cấp ngày 04/11/2026.

Có 3 cách:
1. **App HiFPT:** menu **Thanh toán › Trả hộ ngay**.
2. **Web:** https://staging.fpt.vn/pay
3. **SPF Web admin** (http://saleplatform-stag.fpt.net/web-admin/Account/Login): vào **chi tiết đơn hàng › Receipt** › nhấn **Thanh toán online**.

**Thẻ test thanh toán (STG)** — nguồn: user cung cấp 04/11/2026:

| Loại thẻ | Thông tin |
|---|---|
| Thẻ tín dụng | VISA: `4000000000001091` · Mastercard: `5200000000001096` · Tên chủ thẻ: NGUYEN VAN A · Hiệu lực: 12/26 · CVV: 111 · Pass: 1234 |
| Thẻ nội địa | Số thẻ: `9704 0000 0000 0018` · Tên chủ thẻ: NGUYEN VAN A · Ngày phát hành: 03/07 · OTP: otp |

---

## 5. Cách hoàn tất phiếu giao hàng / triển khai (STG)

> Hoàn tất phiếu = sinh **tín hiệu giao hàng hoàn tất** để xuất hóa đơn thiết bị (xem `RULE-XHD.md` §2, §4).

### 5.0 Thông tin và xử lý phiếu thi công (PTC)

> Nguồn: thông tin user cung cấp ngày 04/11/2026.

**Thông tin trên PTC:**
- **Phân tuyến:** lấy từ tool **Quản lý đối tác**, dùng để phân công nhân sự TIN/PNC đi thi công.
- Thông tin **hợp đồng**.
- Thông tin **đơn hàng**.
- **Vật tư triển khai** (thiết bị khách hàng mua).
- **Vật tư thu hồi**.
- **Khoản thu**.

**Xử lý:** phân tuyến ⇒ phân công nhân sự TIN/PNC ⇒ nhân sự TIN/PNC vào **app MobiX** thao tác xử lý phiếu thi công.

### 5.1 Hoàn tất phiếu thi công (PTC) — hình thức TIN/PNC

> **Bỏ rule cũ** "phải ký BBĐT + khoản thu đã thanh toán mới được hoàn tất PTC" (nguồn: user cung cấp 17/11/2026).
> **Mỗi loại phiếu hoàn tất trên tool của phiếu đó:** chỉ **phiếu thi công** hoàn tất trên **SPF Web admin / app MobiX**; phiếu giao hàng tại quầy hoàn tất trên **Tool quầy** (§5.2, §5.3), **không** hoàn tất PTC; đơn đặt hàng Vendor trên **M-Vendor**.

**Cách 1 — Inside + partner portal:**
1. Vào **Inside new v5 › Thông tin chung › Triển khai**.
2. Nhập số hợp đồng.
3. **Phân tuyến**.
4. Truy cập http://partner-stag.fpt.net/pt-portal/bypass
5. Chọn **Bypass** → tích **tất cả** → nhập hợp đồng → nhập **Thời gian hết hạn bypass** (tối đa 24 giờ) → nhập **Nguyên nhân bypass** → nhấn **Cập nhật**.
6. Quay lại phiếu thi công → chọn trạng thái **Đã xử lý hoàn tất**.

**Cách 2 — SPF Web admin** (PTC của đơn hàng): http://saleplatform-stag.fpt.net/web-admin/Account/Login › **chi tiết đơn hàng** › chọn **PTC** › nhấn **Hoàn tất PTC**.

### 5.2 Hoàn tất phiếu giao hàng tại quầy có shipper giao hàng
1. Vào tool **Quản lý chuỗi cung ứng › Giao dịch thiết bị** → tìm hợp đồng.
2. **Nhận xử lý** phiếu.
3. Chọn kho xuất **KTN test**.
4. **Đề nghị xuất vật tư**.
5. Trên tool **SCM** (https://ftelscm-uat.fpt.net — **cần host**): **Quản lý kho › Nhập kho › Tạo phiếu nhập** với hàng hóa đang cần giao, chọn kho **KTN test MAC**.
6. **Quản lý kho › Xác nhận tạm ứng từ Inside**.
7. Quay lại phiếu giao dịch thiết bị → chọn **Lưu và đóng hàng**.
8. Trên tool GHTK (https://khachhang-staging.ghtklab.com/web/): **Thông tin tài khoản › Cấu hình API**.
9. **Webhook** → chọn **Test** → nhập **mã vận đơn** vào ô Mã đơn hàng.
10. Chọn **cập nhật trạng thái 5**.

### 5.3 Hoàn tất phiếu giao hàng tại quầy không có shipper giao hàng

**Trường hợp đã có MAC:**
1. Vào tool **Quản lý chuỗi cung ứng › Giao dịch thiết bị** → tìm hợp đồng.
2. Chọn đối tác **Bến Thành**, **Tổ 300**.
3. Chọn **Chỉnh sửa** → chọn **danh sách MAC** → nhấn **Lưu**.
4. Chọn kết quả xử lý **Hoàn tất**.
5. Nhấn **Xác nhận**.

**Trường hợp chưa có MAC** (tạo MAC trước, rồi làm lại các bước trên):
1. Vào tool **Quản lý vật tư quầy**.
2. Chọn **Tạm ứng vật tư**.
3. Chọn **Đề nghị tạm ứng**.
4. Chọn đối tác, tổ, vật tư muốn tạm ứng.
5. Nhấn **Tạo phiếu**.
6. Nhập số lượng → **Xác nhận**.
7. Trên tool **SCM** (https://ftelscm-uat.fpt.net — **cần host**): **Quản lý kho › Nhập kho › Tạo phiếu nhập** với hàng hóa đang cần giao, chọn kho **KTN test MAC**.
8. **Quản lý kho › Xác nhận tạm ứng từ Inside**.
9. Chọn kho **KTN test MAC**, tích **Bảo hành V2**.
10. Chọn **phiếu tạm ứng** → nhập **MAC vừa tạo ở phiếu nhập**.
11. Nhấn **Xác nhận V2**.

### 5.4 Thao tác khác với phiếu thi công
- **Hủy PTC / Chuyển thi công (thi công lại):** Inside › **Quản lý hợp đồng › HĐ NOT OK V3 › PTC NOT OK**.
- **Phân công quota phiếu thi công:** Fox ERP (https://fox-erp-stag.fpt.net/) › **Quản lý đối tác › Quản lý Block › Quota PTC - TUT**.

### 5.5 Vật tư cho phiếu & kho SCM

> Nguồn: thông tin user cung cấp ngày 04/11/2026.

**Luồng vật tư:** Kho SCM ⇒ (tạm ứng) ⇒ Tool vật tư ⇒ (load vật tư) ⇒ Giao & lắp đặt.

1. Tool vật tư **đề nghị tạm ứng**.
2. Tool **kho SCM** (https://ftelscm-uat.fpt.net — **cần host**):
   - **Quản lý kho › Nhập kho › Tạo phiếu nhập** hàng hóa (kho **KTN test MAC**).
   - **Quản lý kho › Xác nhận tạm ứng từ Inside**.
3. Vật tư được tạm ứng về tool vật tư.
4. Giao & lắp đặt **load vật tư** từ tool vật tư.

| Tool vật tư | Phiếu load vật tư từ tool này |
|---|---|
| **Quản lý vật tư quầy** | Phiếu giao dịch thiết bị tại quầy (bước đề nghị tạm ứng: xem §5.3, trường hợp chưa có MAC) |
| **Quản lý vật tư** | Phiếu thi công TIN/PNC (chưa có các bước chi tiết) |

---|---|
| **Quản lý vật tư quầy** | Vật tư ở quầy — phiếu giao dịch thiết bị tại quầy (bước tạm ứng: xem §5.3, trường hợp chưa có MAC) |
| **Quản lý vật tư** | Vật tư trong **phiếu thi công TIN/PNC** (chưa có các bước chi tiết) |

Cả 2 tool, sau khi **đề nghị tạm ứng**, đều sang **tool kho SCM** (https://ftelscm-uat.fpt.net — **cần host**):
1. **Quản lý kho › Nhập kho › Tạo phiếu nhập** hàng hóa (kho **KTN test MAC**).
2. **Quản lý kho › Xác nhận tạm ứng từ Inside**.

---

## 6. Hủy đơn hàng

> Nguồn: thông tin user cung cấp ngày 04/11/2026.

- **Tool hủy đơn hàng:** Inside › tool **Quản lý hợp đồng › Hợp đồng NOT OK V3 › tab Trước sử dụng**.

| Trường hợp | Hệ thống xử lý |
|---|---|
| **Đơn chưa thanh toán** | Hủy **phiếu thi công (PTC)**, hủy **khoản thu**, đơn hàng cập nhật trạng thái **Đã hủy**. |
| **Đơn đã thanh toán** | Sau khi hủy phải được **TPKD duyệt** ⇒ đơn hàng **ghi nhận hủy**. **PTC chưa hoàn tất** ⇒ hủy PTC; **PTC đã hoàn tất** ⇒ không chuyển trạng thái hủy. Có thể tạo **đề nghị hoàn tiền**. |

- Liên quan xuất hóa đơn: hủy đơn là 1 trong 2 sự kiện SPF gửi về INVOICE (`RULE-XHD.md` BR-DB-01); đơn bị hủy không được xuất hóa đơn (BR-XHD-10).
- **Cấp duyệt:** hiện thực tế chỉ thấy **TPKD** duyệt; các cấp BGĐCN, CUSX (thông tin ban đầu) chưa thấy xuất hiện.

---

## 7. Danh sách URL / host STG

| Hệ thống | URL | Host |
|---|---|---|
| Tool chính sách (BP) | http://bp-stag.fpt.net/ | **Cần host** |
| CRM | https://crm-stag.fpt.net/ | **Cần host** |
| SOP (Desktop) | https://portal-sop-stg.fpt.vn/user/login/basic-auth | — |
| SPF Web admin | http://saleplatform-stag.fpt.net/web-admin/Account/Login | — |
| Thanh toán FPT.vn | https://staging.fpt.vn/pay | — |
| W-Sale | http://wsale-stag.fpt.net/ | **Cần host** |
| Partner portal (bypass PTC) | http://partner-stag.fpt.net/pt-portal/bypass | — |
| Fox ERP (Service Request, quota PTC) | https://fox-erp-stag.fpt.net/ | — |
| SCM (quản lý kho) | https://ftelscm-uat.fpt.net | **Cần host** |
| GHTK staging (webhook shipper) | https://khachhang-staging.ghtklab.com/web/ | — |
| FPL | dev.fptplay.vn | Không cần host |
