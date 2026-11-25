# RULE CHỦ THỂ — HỦY ĐƠN HÀNG

> Tool hủy đơn và cách hệ thống xử lý theo đơn đã / chưa thanh toán.
> Tách từ `../01-DON-HANG/kenh-ban/00-CHUNG.md`; số mục (§) giữ theo file gốc.

---

## 6. Hủy đơn hàng

> Nguồn: thông tin QC cung cấp ngày 04/11/2026.

- **Tool hủy đơn hàng:** Inside › tool **Quản lý hợp đồng › Hợp đồng NOT OK V3 › tab Trước sử dụng**.

| Trường hợp | Hệ thống xử lý |
|---|---|
| **Đơn chưa thanh toán** | Hủy **phiếu thi công (PTC)**, hủy **khoản thu**, đơn hàng cập nhật trạng thái **Đã hủy**. |
| **Đơn đã thanh toán** | Sau khi hủy phải được **TPKD duyệt** ⇒ đơn hàng **ghi nhận hủy**. **PTC chưa hoàn tất** ⇒ hủy PTC; **PTC đã hoàn tất** ⇒ không chuyển trạng thái hủy. Có thể tạo **đề nghị hoàn tiền**. |

- Liên quan xuất hóa đơn: hủy đơn là 1 trong 2 sự kiện SPF gửi về INVOICE (`RULE-XHD.md` BR-DB-01); đơn bị hủy không được xuất hóa đơn (BR-XHD-10).
- **Cấp duyệt:** hiện thực tế chỉ thấy **TPKD** duyệt; các cấp BGĐCN, CUSX (thông tin ban đầu) chưa thấy xuất hiện.

---

### 5.4 Thao tác khác với phiếu thi công
- **Hủy PTC / Chuyển thi công (thi công lại):** Inside › **Quản lý hợp đồng › HĐ NOT OK V3 › PTC NOT OK**.
- **Phân công quota phiếu thi công:** Fox ERP (https://fox-erp-stag.fpt.net/) › **Quản lý đối tác › Quản lý Block › Quota PTC - TUT**.
