# KÊNH DKOL (SaleChannelID 4)

> Tách từ `RULE-CHINH-SACH-KENH-BAN.md` (nguồn: QC cung cấp 03/11/2026). Rule chung: [00-CHUNG.md](../00-CHUNG.md) · Rule XHD: [`../../../../RULE-XHD.md`](../../../../RULE-XHD.md).

## Thông tin chung

| Mục | Nội dung |
|---|---|
| Owner | TaiTT13 |
| Nơi tạo đơn | **HiFPT** và **FPT.vn** — cả 2 đều có **SaleChannel = DKOL** |
| Loại đơn | Bán mới + bán thêm |
| Ghi chú | Kênh HiFPT cũ đã move sang DKOL |

## Sale team
- Lên đơn từ **HiFPT:** sale team *Khách hàng bình thường HiFPT*.
- Lên đơn từ **FPT.vn:** DKOL (KH vãng lai), AM (sale IBB), CTV_sale (208), ANCS (239), Đối tác (238).

## Dịch vụ

### HiFPT
- **Bán mới:** Net, combo Net–Camera, combo Net–PayTV, TripleF Net–PayTV–Cam, Ultra Fast SA, FPT Play SA, Smart Home, Smart TV, thiết bị modem, thiết bị y tế, Camera combo (lẻ).
- **Nâng cấp:** Cloud, Camera, FPT Play (billing).

### FPT.vn
- **KH vãng lai:** như bán mới HiFPT + **HyperFast SA**, **trừ thiết bị y tế**.
- **Sale team còn lại:** chủ yếu Net và combo của Net.
- Prepaid là bán mới nhưng ghi nhận cho sale.
- **Nâng cấp:** Camera ưu đãi, FPT Play sub, nâng cấp FPT Play (sub).

## Các trang vào bán mới riêng của FPT.vn

> Nguồn: `input/ISC_PRD_F-citizen_FPTvn_v1.1.docx` (§B.II Mô tả các bước) · `input/CL_BCA.xlsx` (testcase Tri ân CAND: Landing page, Combo, Triple) · `input/ISC_AM_v2.0_PRD_Standard_v1.0.docx` (§5.2) · `input/ISC_FPTVN_v2.4_PRD_Standard_Cap_nhat_don_AM_v1.0.docx` (§5.2). Cả 3 trang cuối cùng đi tiếp luồng bán mới chung ở trên.

| Trang | Luồng tổng quan |
|---|---|
| **F-citizen** (fpt.vn/fcitizen) | CBNV FPT chọn công ty, nhập email → OTP gửi email → autofill form → bổ sung địa chỉ → HĐLĐ chính thức và SĐT/email chưa có HĐ Internet ⇒ bán mới. Không phải CBNV: để lại SĐT tạo KHTN cho ECOM · HĐLĐ không chính thức: tạo KHTN · đã có HĐ Internet: tạo SR Tư vấn giải đáp |
| **Tri ân CAND** (fpt.vn/vip) | Popup nhập mã khuyến mãi → landing ưu đãi → chọn gói Combo Internet–truyền hình hoặc Triple (+ Camera) → đăng ký → thanh toán |
| **AM** (link Sale AM) | Link Sale AM (bộ gói Sales cấu hình trên AM SOP) hoặc khách vãng lai (9 gói chung) → nhập địa chỉ, kiểm tra chính sách (không có ⇒ KHTN, trang Hoàn tất) → cấu hình đơn, tự áp voucher → thanh toán COD / QR / cổng TT; khách vãng lai gửi Omnisell theo tỉnh. Đổi thông tin đơn AM chưa thanh toán: Sale hủy đơn trên SOP → HĐ cũ Pending, sinh Code + link AM mới → đơn mới thanh toán xong gắn lại HĐ cũ |

## Luồng nâng cấp (HiFPT ≠ FPT.vn)

Bán mới 2 nơi giống nhau. Nâng cấp mỗi nơi theo nguồn riêng: **HiFPT** theo URD Nâng cấp All kênh + thông tin owner cung cấp · **FPT.vn chỉ theo PRD OTP Nâng cấp/Bán thêm** (không lấy URD Nâng cấp cho FPT.vn, quyết định của user 23/11/2026).

### HiFPT

> Nguồn: `input/ISC_NangCap_ Hifpt_V1.0_URD_v1.0.xlsx` (URD Nâng cấp All kênh v1.0, sheet Nâng cấp · mục 2 Mô tả quy trình, mục 3 Thông tin SR) · thông tin QC cung cấp 23/11/2026.

- **Vào:** đăng nhập App HiFPT, lấy HĐ billing Bình thường theo SĐT đăng nhập.
- **Lõi Billing Hub:** chọn HĐ + dịch vụ (Internet / combo, FPT Play, Cloud, thiết bị) → Billing Hub lấy chính sách (mua thêm: CS bán thêm · nâng cấp: CS chuyển DV) → chọn gói, PTTT → tạo đơn (phân loại mua thêm / nâng cấp) → COD (chỉ khi chính sách có PTC, khoản thu COD đẩy vào PTC, TIN/PNC thu tại nhà) hoặc thanh toán online → hậu kỳ: mua thêm theo luồng bán thêm Selfservice; nâng cấp tạo SR chuyển DV.
- **SR chuyển DV (đơn đã chốt PTTT):** SR tự xử lý theo flow: phát hành hóa đơn → ký PLHĐ → active gói nâng cấp, **không có ticket triển khai**. SR xử lý xong gửi kết quả lại HiFPT, HiFPT cập nhật trạng thái đơn hàng (user 23/11/2026).
- **Ký PLHĐ:** SĐT chính chủ: auto ký (SMS) · không chính chủ: SMS OTP / shortlink.
- **Đứt gãy:** không có HĐ billing, không có chính sách, thanh toán online thất bại, KH bỏ dở / quá 1 giờ ⇒ mua thêm đẩy KHTN (Omnisell), nâng cấp tạo **SR đứt gãy**. Trạng thái theo rule phân công SR (kiểm tra tồn, kiểm tra nhân sự AU): phân công được nhân sự ⇒ **Chưa xử lý** · HĐ không có AU ⇒ **Chưa phân công** (user 23/11/2026).

### FPT.vn

> Nguồn: `input/ISC_FPTvn_v2.2_PRD_OTP_NangCap_BanThem_Standard_v1.0.docx` (PRD v1.2 §5.2 Luồng 1, Luồng 2 · FR01–FR03).

- **Luồng 1 · fpt.vn/nang-cap:** nhập SĐT → **OTP ngay sau SĐT** (6 số qua SMS, hiệu lực 5 phút; sai 3 lần liên tiếp hoặc quá hạn ⇒ OTP vô hiệu, gửi lại mã mới; tối đa 5 lần gửi/ngày) → danh sách HĐ hiện đủ họ tên, SĐT, địa chỉ lắp đặt, số HĐ (không che *). Phiên 30 phút từ lúc xác thực OTP; hết phiên / vào thẳng URL ⇒ quay về fpt.vn/nang-cap.
- **Luồng 2 · link ZNS ưu đãi mua thêm Camera** (`fpt.vn/uu-dai-dac-quyen?contract=…`): bấm Lựa chọn ưu đãi → vào thẳng Checkout, không OTP, thông tin HĐ che *, PTTT COD.
- **Checkout** (phiên 20 phút): không hiện popup OTP — COD / gói trả sau bỏ qua OTP; PTTT online (VNPAY, MoMo, thẻ quốc tế…) cũng không hiện popup OTP → kiểm tra chính sách, điều kiện thanh toán → tạo đơn theo luồng lên đơn hiện hữu → màn Hoàn tất đơn hàng khi thanh toán thành công.
- **Sau khi tạo đơn:** PRD giữ nguyên logic tạo đơn và thanh toán hiện hữu (Out of Scope), không mô tả SR, ký PLHĐ hay xử lý hậu kỳ.

## Hình thức triển khai
- **TIN/PNC (phiếu thi công):** dịch vụ cần triển khai, kích hoạt tại địa chỉ đăng ký. Phiếu thi công **không phải** dịch vụ Camera (nguồn: QC cung cấp 17/11/2026).
- **Camera:** **Quầy** (có chính sách shipper giao hàng).
- **TV:** đang đẩy qua **Vendor**.
- **Ultra Fast SA, FPT Play SA, HyperFast SA:** **không cần giao & lắp đặt**, **BBĐT auto ký**.

Cách hoàn tất phiếu: [00-CHUNG.md §5](../00-CHUNG.md#5-cách-hoàn-tất-phiếu-giao-hàng--triển-khai-stg).

## Thanh toán & khoản thu
- **PTTT = Thanh toán khi triển khai:** gen đồng thời khoản thu, phiếu thi công, biên bản điện tử; đơn = **Chưa thanh toán**.
- **PTTT Online:** khách hàng **phải thanh toán xong** mới tạo đơn ⇒ đơn tạo ra với tình trạng **Đã thanh toán**, khoản thu **Đã thanh toán** ⇒ sau đó mới gen **phiếu thi công** và **biên bản điện tử**.
- Sau khi thanh toán: tiền **đẩy vào cọc**. Kiểm tra: Inside › Foxpay › Thanh toán online › Đối soát khoản thu online.
- **Thanh toán → cọc → hóa đơn → gạch nợ** (nguồn: QC cung cấp 17/11/2026): khách thanh toán ⇒ khoản thu **Đã thanh toán** ⇒ **nhập cọc** ⇒ nhận tín hiệu xuất hóa đơn thì xuất hóa đơn ⇒ có cọc thì **gạch nợ hóa đơn**, cập nhật hóa đơn **Đã thanh toán** ⇒ hóa đơn dịch vụ **trả trước** thì **add tiền trả trước**. Chi tiết: [00-CHUNG.md §4.3](../00-CHUNG.md#43-sau-khi-thanh-toán-khoản-thu).

## Phạm vi test XHD
Bán mới 8 nhóm {1,4,5,6,7,9,10,21} · bán thêm 3 nhóm {1,4,7} — `RULE-XHD.md` §1.1.
