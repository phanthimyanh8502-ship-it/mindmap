# RULE CHỦ THỂ — HỢP ĐỒNG

> Sinh ra khi tạo đơn; cập nhật hợp đồng, SR; điều kiện hợp đồng khi xuất hóa đơn.
> Tách từ `../../RULE-XHD.md` và `../01-DON-HANG/kenh-ban/00-CHUNG.md`; số mục (§) giữ theo file gốc.

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
| **SR chuyển địa điểm** | Chuyển địa điểm sử dụng dịch vụ (bạn cung cấp 19/11/2026) |

**SR sinh phiếu thi công** (bạn xác nhận 19/11/2026): **SR chuyển dịch vụ**, **SR chuyển địa điểm**, **SR khôi phục dịch vụ** tạo PTC từ hợp đồng (xem [Phiếu thi công](../05-GIAO-LAP-DAT/01-PHIEU-THI-CONG/quy-trinh-nghiep-vu.md)).

Liên quan xuất hóa đơn (`RULE-XHD.md`): hợp đồng tạm ngưng / đã chấm dứt ⇒ không xuất hóa đơn (BR-XHD-10); cập nhật thông tin khách không kích hoạt phát hành, lần phát hành sau dùng thông tin mới nhất (BR-DB-03).

---

## 4. Điều kiện phát hành (BR-XHD-03)

| Đối tượng | Điều kiện |
|---|---|
| **Dịch vụ (DV)** | Có tín hiệu **"đã thanh toán"** từ SPF |
| **Thiết bị (TB)** | Có tín hiệu **giao hàng hoàn tất** của phương thức triển khai tương ứng; chỉ phát hành TB có trong tín hiệu |
| DV và TB | Xét **độc lập**, dùng chung mọi kênh |
| **Đơn TMĐT** | DV khi SPF đánh dấu "đã thanh toán"; TB khi giao hàng thành công |
| **Kênh FPL** | Delay **2 giờ** tính từ thời gian tạo đơn — áp cả DV và TB |
| **Hợp đồng tổ chức** (KH cấp 1 = Tổ chức) | Chỉ phát hành khi **đã duyệt PĐK** (lấy từ SPF); **2 ngày lịch cuối tháng** không xét. Chưa duyệt ⇒ chặn, ghi log, phải xuất tay (đợt sau không tự phát hành). Đơn bán thêm phải duyệt PĐK mới của đơn đó. |
| **Hợp đồng con** (có gắn hợp đồng cha/dự án) | **Không phát hành** cả DV và TB |
| **Hợp đồng SST / hợp đồng nghiệp vụ** | **Không tự động xuất hóa đơn** (yêu cầu BA 23/10/2026, ngoài URD) |

---

## 6. Điều kiện hợp lệ của đơn (BR-XHD-10)

Đơn chỉ được xuất hóa đơn khi:
- **Đơn hợp lệ:** không bị hủy, không đang cập nhật.
- **Hợp đồng hợp lệ:** hợp đồng còn hiệu lực.
- **Đủ thông tin chung:** sale team, kênh bán, tên khách hàng, loại hình khách hàng, địa chỉ xuất hóa đơn, địa bàn (LocationID).
- **Đủ thông tin dịch vụ:** dịch vụ, nhóm dịch vụ, gói dịch vụ, chính sách, câu lệnh giá, CTKM đều phải có giá trị hợp lệ (> 0).

Không hợp lệ ⇒ **không xuất hóa đơn** và ghi log; hệ thống không giữ lại để xuất sau.
