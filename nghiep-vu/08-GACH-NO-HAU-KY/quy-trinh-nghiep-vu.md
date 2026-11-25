# RULE CHỦ THỂ — GẠCH NỢ & HẬU KỲ

> Thanh toán → cọc → hóa đơn → gạch nợ; hậu kỳ đẩy hóa đơn điện tử và tiền trả trước.
> Tách từ `../../RULE-XHD.md` và `../01-DON-HANG/kenh-ban/00-CHUNG.md`; số mục (§) giữ theo file gốc.
> Bổ sung 19/11/2026 — quy trình tổng quan từ URD Xuất hóa đơn v2.2 (input của 07) — chỉ phần **Mô tả + Flow** của mục II Gạch nợ hóa đơn và III Đẩy hậu kỳ.

---

## Quy trình tổng quan

> Nguồn: URD Invoice Issuance v2.2 (nằm ở [input của Xuất hóa đơn](../07-XUAT-HOA-DON/input/README.md)) — chỉ phần **a. Mô tả** và **b. Flow** của mục **B.II Gạch nợ hóa đơn** và **B.III Đẩy hậu kỳ qua dịch vụ – tiền trả trước**. Không lấy business rule chi tiết.

### Gạch nợ hóa đơn (URD B.II)

| Mục | Nội dung |
|---|---|
| Mô tả | Đồng bộ thông tin thanh toán (**Paid**) từ kênh thanh toán, rồi gạch nợ hóa đơn bằng **Paid** hoặc bằng **Cọc**. Đơn kênh sàn TMĐT được **gạch nợ tạm**; khi sàn quyết toán thì gỡ gạch nợ tạm và gạch nợ thật |
| Tác nhân | INVOICE, kênh thanh toán, đội EVC |
| Trigger | 3 điểm chạm xét gạch nợ: đồng bộ Paid xong · sau khi xuất hóa đơn · worker quét 30 phút một lần |
| Điều kiện trước | Hóa đơn đã phát hành và còn nợ; có Paid hoặc có tồn cọc theo hợp đồng |
| Kết quả | Hóa đơn **Đã gạch nợ** khi tổng Payment = tổng tiền hóa đơn |

| # | Bước | Hệ thống | Lưu ý |
|---|---|---|---|
| 1 | Đồng bộ Paid từ kênh thanh toán | INVOICE, kênh thanh toán | Luôn ghi nhận Paid, kể cả khi hóa đơn chưa phát hành |
| 2 | Nhận điểm chạm xét gạch nợ | INVOICE | 3 điểm chạm ở trên |
| 3 | Lấy nợ, chọn **Paid** hay **Cọc** | INVOICE, kênh thanh toán | Một đơn chỉ đi 1 luồng |
| 4a | Nếu Paid: gạch tạm → gỡ tạm → gạch thật | INVOICE, đội EVC | Chỉ đơn kênh sàn mới gạch tạm; phần EVC do đội EVC gạch. Kiểm tra gạch nợ tạm: Inside › **Bảng kê TT** (QC cung cấp 25/11/2026) |
| 4b | Nếu Cọc: kiểm tra đủ rồi trừ cọc | INVOICE, đội EVC | Cọc không có gạch nợ tạm. Kiểm tra cọc: Inside › Quản lý kế toán › Tiền đặt cọc › Tra cứu (QC cung cấp 25/11/2026) |
| 5 | Cập nhật trạng thái **Đã gạch nợ** | INVOICE | Gạch từng hóa đơn, theo số tiền từ cao xuống thấp |

### Đẩy hậu kỳ — HĐĐT và tiền trả trước (URD B.III)

| Mục | Nội dung |
|---|---|
| Mô tả | Đẩy thông tin hậu kỳ (tạo hóa đơn điện tử, add tiền trả trước) khi một đơn có thể có nhiều hóa đơn. Sau khi nhận bản tin báo hóa đơn đã phát hành (**Invoice Event**): nhánh HĐĐT đẩy ngay; nhánh tiền trả trước **chờ hóa đơn gạch nợ xong** mới đẩy (QC cung cấp 25/11/2026) |
| Tác nhân | INVOICE, hệ thống HĐĐT, hệ thống Dịch vụ |
| Trigger | Hóa đơn phát hành thành công (Invoice Event). Riêng tiền trả trước: hóa đơn Đã gạch nợ |
| Kết quả | Thông tin và tiền dịch vụ đẩy đúng theo từng đơn cấu thành hóa đơn; đã add tiền trả trước cho khách |

| # | Bước | Hệ thống | Lưu ý |
|---|---|---|---|
| 1 | Nhận bản tin báo hóa đơn đã phát hành (**Invoice Event**) | INVOICE | Chỉ đẩy phần vừa xuất, tách theo đơn |
| A1 | Nhánh HĐĐT: chuẩn bị thông tin | INVOICE | Ký hiệu, ID, nội dung, tổng tiền theo thuế suất |
| A2 | Nhánh HĐĐT: đẩy sang hệ thống HĐĐT | INVOICE, HĐĐT | Đủ thông tin mới đẩy |
| B1 | Nhánh tiền trả trước: đẩy dịch vụ | INVOICE, hệ thống Dịch vụ | Chỉ khi hóa đơn Đã gạch nợ; tách theo đơn |
| B2 | Nhánh tiền trả trước: đánh dấu đã đẩy hậu kỳ | INVOICE | Mỗi đơn chỉ add tiền trả trước 1 lần |

---

### 4.3 Sau khi thanh toán khoản thu
- Khoản thu phải chuyển sang **Đã thanh toán**.
- Tiền được **đẩy vào cọc**.

**Luồng thanh toán → cọc → hóa đơn → gạch nợ** (SOP Desktop/Mobile, DKOL, FPL) (nguồn: QC cung cấp 17/11/2026):
1. Khách thanh toán ⇒ hệ thống cập nhật khoản thu **Đã thanh toán**.
2. Hệ thống **nhập cọc**.
3. Nhận được **tín hiệu xuất hóa đơn** ⇒ hệ thống xuất hóa đơn.
4. **Có cọc** ⇒ hệ thống **gạch nợ hóa đơn** theo cọc và cập nhật hóa đơn **Đã thanh toán**.
5. Gạch nợ xong, hóa đơn **dịch vụ trả trước** ⇒ hệ thống **add tiền trả trước** (chưa gạch nợ thì chưa add).

**Cách gạch nợ theo loại đơn** (nguồn: QC cung cấp 17/11/2026):
- Đơn **TMĐT** (Shopee, TikTok) ⇒ hệ thống **gạch nợ theo Paid**.
- Đơn **khác TMĐT** ⇒ hệ thống **gạch nợ bằng cọc**.
- Hóa đơn có **dịch vụ trả trước** ⇒ hệ thống **add tiền trả trước**.
- **Kiểm tra khoản thu:** Inside › menu **Foxpay › Thanh toán online › Đối soát khoản thu online**.

---

## 8. Hậu kỳ — đẩy hóa đơn điện tử & tiền trả trước (BR-HK)

Hóa đơn phát hành xong, INVOICE gửi bản tin báo hóa đơn đã phát hành (**Invoice Event**), rồi đẩy 2 nhánh hậu kỳ. Nhánh hóa đơn điện tử đẩy ngay. Nhánh tiền trả trước **chỉ đẩy khi hóa đơn đã gạch nợ xong** (nguồn: QC cung cấp 25/11/2026):

### 8.1 Nguyên tắc chung (BR-HK-01)
- Phần nào trên đơn **đã xuất hóa đơn** thì đẩy hậu kỳ đúng phần đó (dịch vụ hay thiết bị đều đẩy).
- Mỗi lần phát hành **chỉ đẩy phần vừa xuất**, không đẩy lại phần cũ; tách theo từng đơn hàng.

### 8.2 Nhánh 1 — Hóa đơn điện tử (BR-HK-02, 03, 05, 07)
- INVOICE chuẩn bị **đủ thông tin** rồi mới đẩy sang hệ thống hóa đơn điện tử; **chưa đủ thì chưa đẩy**.
- Thông tin gồm:
  - **Ký hiệu hóa đơn:** theo quy định thuế (theo vùng miền) — sai ký hiệu là sai kê khai thuế.
  - **ID hóa đơn:** loại đầu + năm + mã tỉnh + số hóa đơn.
  - **Nội dung hiển thị:** tên dịch vụ + số tháng sử dụng, không ghi từ ngày – đến ngày.
  - **Tổng tiền theo thuế suất:** gom theo từng mức (không chịu thuế, 0%, 5%, 8%, 10%) + dòng tổng cộng.
  - Dòng EVC và các thông tin khác theo mẫu hóa đơn.

### 8.3 Nhánh 2 — Tiền trả trước (BR-HK-09)
- **Kiểm tra:** tool **Tra cứu new** (QC cung cấp 25/11/2026).
- **Chỉ đẩy khi hóa đơn đã gạch nợ xong** (trạng thái Đã gạch nợ). Chưa gạch nợ ⇒ chưa add tiền trả trước (nguồn: QC cung cấp 25/11/2026).
- Add tiền gói dịch vụ trả trước vào hợp đồng của khách.
- **Mỗi đơn chỉ add 1 lần**, kể cả khi đơn được xuất nhiều hóa đơn.
- Hóa đơn chỉ có thiết bị ⇒ **không add** tiền trả trước.
- Áp dụng cho cả đơn bán mới và bán thêm.
