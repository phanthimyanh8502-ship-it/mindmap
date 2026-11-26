# Input — GẠCH NỢ & HẬU KỲ

Tài liệu đầu vào của quy trình nghiệp vụ ở [`../quy-trinh-nghiep-vu.md`](../quy-trinh-nghiep-vu.md).

## Tool

### Tool thao tác, cập nhật
- **INVOICE** — hệ thống tự chạy — tự gạch nợ hóa đơn và đẩy hậu kỳ (hóa đơn điện tử, tiền trả trước).
- **Fox ERP – Quản lý công nợ** — Quản lý công nợ › Quản lý gạch nợ — DVKH HO gạch nợ online / gạch nợ tạm (QC cung cấp 26/11/2026).
- **Inside – Quản lý thu cước** — Quản lý thu cước › Gạch nợ bổ sung — DVKH HO gạch nợ bổ sung cho giao dịch tiền mặt tạm sau khi KTV nộp tiền (QC xác nhận 26/11/2026).

### Tool kiểm tra
- **Inside** — Foxpay › Thanh toán online › Đối soát khoản thu online — kiểm tra khoản thu.
- **Inside – Tiền đặt cọc** — Quản lý kế toán › Tiền đặt cọc › Tra cứu — kiểm tra tồn cọc dùng gạch nợ (QC cung cấp 25/11/2026).
- **Inside – Bảng kê TT** — Quản lý kế toán › Bảng kê TT — kiểm tra gạch nợ tạm (đơn sàn TMĐT) (QC cung cấp 25/11/2026).
- **Inside – Tra cứu new** — Quản lý kế toán › Cước trả trước › Tra cứu new — kiểm tra tiền trả trước đã add vào hợp đồng (QC cung cấp 25/11/2026).

## Thao tác

### Gạch nợ hóa đơn (hệ thống tự chạy)
1. Đồng bộ Paid từ kênh thanh toán, luôn ghi nhận kể cả khi hóa đơn chưa phát hành.
2. Xét gạch nợ ở 3 điểm chạm: đồng bộ Paid xong, sau khi xuất hóa đơn, worker 30 phút một lần.
3. Lấy nợ, chọn luồng Paid hoặc Cọc; một đơn chỉ đi 1 luồng.
4. Đơn sàn TMĐT gạch nợ tạm, sàn quyết toán thì gỡ tạm rồi gạch thật; nhánh Cọc đủ cọc mới trừ.
5. Tổng Payment bằng tổng tiền hóa đơn ⇒ hóa đơn Đã gạch nợ.

### Đẩy hậu kỳ (hệ thống tự chạy)
1. Hóa đơn phát hành xong ⇒ đủ thông tin thì đẩy ngay sang hệ thống hóa đơn điện tử.
2. Hóa đơn Đã gạch nợ ⇒ add tiền trả trước, mỗi đơn 1 lần.

### Kiểm tra khoản thu (người dùng)
1. Inside › Foxpay › Thanh toán online › Đối soát khoản thu online.

### Kiểm tra tiền đặt cọc (người dùng)
1. Vào Inside › Quản lý kế toán › Tiền đặt cọc › Tra cứu, tìm theo hợp đồng, xem tồn cọc.

### Kiểm tra gạch nợ tạm (người dùng)
1. Vào tool Inside › Quản lý kế toán › Bảng kê TT, xem hóa đơn đơn sàn TMĐT đã gạch nợ tạm.

### Kiểm tra tiền trả trước (người dùng)
1. Vào Inside › Quản lý kế toán › Cước trả trước › Tra cứu new, tìm theo hợp đồng, xem tiền trả trước đã được add sau khi hóa đơn gạch nợ xong.

## Ý chính tài liệu

### Thông tin QC cung cấp

- Luồng SOP Desktop / Mobile, DKOL, FPL: khách thanh toán ⇒ khoản thu Đã thanh toán ⇒ nhập cọc ⇒ có tín hiệu thì xuất hóa đơn ⇒ có cọc thì gạch nợ theo cọc (17/11/2026).
- Đơn TMĐT (Shopee, TikTok) gạch nợ theo Paid; đơn khác TMĐT gạch nợ bằng cọc (17/11/2026).
- Hóa đơn có dịch vụ trả trước ⇒ hệ thống add tiền trả trước.
- Tiền trả trước chỉ đẩy sau khi hóa đơn gạch nợ xong; chưa gạch nợ thì chưa add (25/11/2026).

### URD Xuất hóa đơn v2.2 (`Invoice_Issuance_Architecture_v2_2_URD_v2_0.docx`)

- B.II Gạch nợ: đồng bộ Paid từ kênh thanh toán rồi gạch nợ hóa đơn bằng Paid hoặc bằng Cọc. Tác nhân: INVOICE, kênh thanh toán, đội EVC.
- Trigger là 3 điểm chạm xét gạch nợ (BR-XL-01). Điều kiện trước: hóa đơn đã phát hành, còn nợ, có Paid hoặc tồn cọc theo hợp đồng.
- Đơn kênh sàn TMĐT gạch nợ tạm; sàn quyết toán thì gỡ tạm và gạch nợ thật. Hóa đơn Đã gạch nợ khi tổng Payment bằng tổng tiền hóa đơn.
- B.III Hậu kỳ: điều chỉnh cách đẩy hậu kỳ (tạo hóa đơn điện tử, add tiền trả trước) khi một đơn có nhiều hóa đơn. Trigger: bản tin báo hóa đơn đã phát hành (Invoice Event). Tác nhân: INVOICE, hệ thống HĐĐT, hệ thống Dịch vụ.
- Chỉ đẩy phần vừa xuất, tách theo đơn (BR-HK-01); đủ thông tin mới đẩy hóa đơn điện tử (BR-HK-02); mỗi đơn chỉ add tiền trả trước 1 lần (BR-HK-09).

## Nguồn

- QC cung cấp 26/11/2026: DVKH HO gạch nợ trên Fox ERP › Quản lý công nợ › Quản lý gạch nợ; tool Quản lý thu cước / Gạch nợ bổ sung nằm trên Inside.
- Thông tin QC cung cấp (ghi ở đầu từng mục trong `quy-trinh-nghiep-vu.md`): 17/11/2026 (luồng cọc, gạch nợ); 25/11/2026 (tiền trả trước chỉ đẩy sau khi hóa đơn gạch nợ xong)
- URD Xuất hóa đơn v2.2 (file ở [input của Xuất hóa đơn](../../07-XUAT-HOA-DON/input/)): quy trình tổng quan lấy từ phần **Mô tả + Flow** của mục B.II Gạch nợ hóa đơn và B.III Đẩy hậu kỳ
- Thông tin QC cung cấp 25/11/2026: kiểm tra gạch nợ tạm trên Inside › Quản lý kế toán › Bảng kê TT.
- Thông tin QC cung cấp 25/11/2026: kiểm tra tiền trả trước trên Inside › Quản lý kế toán › Cước trả trước › Tra cứu new.
- Thông tin QC cung cấp 25/11/2026: kiểm tra tiền đặt cọc ở Inside › Quản lý kế toán › Tiền đặt cọc › Tra cứu.
