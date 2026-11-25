# Input — SR HOÀN TIỀN

Tài liệu đầu vào của quy trình nghiệp vụ ở [`../quy-trinh-nghiep-vu.md`](../quy-trinh-nghiep-vu.md).

## Tool

### Tool thao tác, cập nhật
- **Tool SR** — Fox ERP › Service Request — tạo và xử lý SR.
- **ePayment** — https://uat-epay.fpt.com — **Cần host** — nhận đề nghị hoàn tiền chuyển khoản từ SR, trả kết quả các bước duyệt (QC cung cấp 25/11/2026).
- **DVKH HO** — duyệt đề nghị hoàn tiền online, cập nhật kết quả hoàn từ đối tác.

### Tool kiểm tra
- **Inside – Tiền đặt cọc** — Quản lý kế toán › Tiền đặt cọc › Tra cứu — kiểm tra tồn cọc trước và sau khi trừ cọc (QC cung cấp 25/11/2026).

## Thao tác

### Hoàn tiền cho khách (SR)
1. Tạo SR hoàn tiền theo mã SR cha (thanh lý trước / sau sử dụng, khiếu nại).
2. Xử lý giao dịch: chọn giao dịch cần hoàn, số tiền trừ cọc, phương thức hoàn.
3. Chuyển khoản: GĐCN duyệt (khi chủ tài khoản khác chủ hợp đồng) → đề nghị qua ePayment.
4. Online: HO duyệt → cập nhật kết quả hoàn từ đối tác.

## Ý chính tài liệu

### `ISC_SR_HoanTien_URD_v1.0.docx`
- Tạo từ SR cha (thanh lý trước / sau sử dụng, khiếu nại); tồn cọc phải đủ, trừ cọc theo số tiền hoàn.
- Chuyển khoản: chủ tài khoản khác chủ hợp đồng thì GĐCN duyệt; đề nghị qua ePayment, NOT OK quá 3 lần thì hoàn cọc.
- Online: HO duyệt, đối tác hoàn, cập nhật kết quả bằng import.

## Nguồn

- `ISC_SR_HoanTien_URD_v1.0.docx` (file nằm ở [input của SR](../../input/))
- Thông tin QC cung cấp 25/11/2026: ePayment UAT là uat-epay.fpt.com, cần host.
- Thông tin QC cung cấp 25/11/2026: kiểm tra tiền đặt cọc ở Inside › Quản lý kế toán › Tiền đặt cọc › Tra cứu.
