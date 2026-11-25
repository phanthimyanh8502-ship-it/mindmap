# RULE CHỦ THỂ — QUẢN LÝ CHÍNH SÁCH (TOOL BP)

> Chính sách bán hàng quyết định giá, gói, PTTT, voucher, hình thức triển khai.
> Tách từ `../01-DON-HANG/kenh-ban/00-CHUNG.md`; số mục (§) giữ theo file gốc.
> Bổ sung 19/11/2026 — quy trình tổng quan từ URD Business Policy 2.1 (`ISC_Business-Policy_2.1-URD-v1.1.docx`) — chỉ mục **Thông tin chung** và **Tổng quan › Sơ đồ tổng quan, Danh sách chức năng**.

---

## Quy trình tổng quan

> Nguồn: URD Business Policy 2.1, mục "Thông tin chung" và "Tổng quan" (sơ đồ tổng quan + danh sách chức năng). Không lấy đặc tả, business rule chi tiết từng chức năng.

**Tool QLCS** — cũng chính là **Tool BP** (bạn xác nhận 19/11/2026) — (Quản lý chính sách, http://bp.fpt.net/ — STG: bp-stag, cần host) quản lý chính sách từ lúc **tạo đề xuất ⇒ xem xét ⇒ phê duyệt ⇒ quyết định ⇒ ban hành**. Chính sách bán hàng, ưu đãi, chiết khấu tạo trên cùng hệ thống, tạo combo nhanh; các tool bán hàng lấy giá từ QLCS. Phạm vi: toàn quốc.

| # | Bước | Ghi chú |
|---|---|---|
| 1 | **Phân quyền sử dụng** | Quyết định ai được tạo chính sách và tra cứu |
| 2 | **Tạo chính sách bán hàng** (song song: **tạo chính sách EVC**) | Chính sách only 1 dịch vụ nhiều phí, combo 1 dịch vụ nhiều phí |
| 3 | **Phê duyệt / ban hành nhiều cấp** | Đề xuất ⇒ xem xét ⇒ phê duyệt ⇒ quyết định ⇒ ban hành |
| 4 | **Chính sách hiệu lực** | Từ đây: tra cứu chính sách · gia hạn chính sách bán hàng · package view · phân phối hạn mức chính sách EVC |
| 5 | **Phân phối hạn mức**: hạn mức tổng ⇒ hạn mức bán hàng ⇒ hạn mức chính sách EVC | Hạn mức khách vãng lai: chỉ khai báo cấp Vùng cho từng chính sách |
| 6 | **Áp dụng chính sách giá cho các tool bán hàng** | SPF và các kênh lấy giá, PTTT, hình thức triển khai, DV/TB từ chính sách. **Loại hình bán thiết bị:** QLCS lấy dữ liệu từ Quản lý vật tư rồi trả ra cho SPF (bạn xác nhận 19/11/2026) |
| 7 | **Báo cáo sử dụng voucher / chính sách** | — |

**Nhóm chức năng trong URD 2.1:** *Chính sách bán hàng* — nhập chính sách only / combo 1 dịch vụ nhiều phí, cập nhật nhanh PHM trong cùng chính sách, rule lấy giá FPT Play giống Net cho SPF · *Voucher* — lọc chính sách để phân phối theo quyền tài khoản HRIS (kể cả kiêm nhiệm), hạn mức khách vãng lai.

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
