# Input — SR (SERVICE REQUEST)

Tài liệu đầu vào của quy trình nghiệp vụ ở [`../quy-trinh-nghiep-vu.md`](../quy-trinh-nghiep-vu.md). File gốc là tài liệu nội bộ, không đưa lên repo (`.gitignore`).

## Tool

### Tool thao tác, cập nhật
- **Tool SR** — Fox ERP › Service Request — tạo và xử lý các loại SR cập nhật hợp đồng (8 loại) và SR thanh lý trước sử dụng. URD gọi là "hệ thống SR" chạy trên Inside Nextgen.
- **Inside** — Quản lý hợp đồng › Cập nhật hợp đồng (New) — **chỉ** cập nhật thông tin khách hàng (QC cung cấp 25/11/2026).
- **App HiFPT – Ký kết** — Tài khoản › Hợp đồng/Phụ lục — khách ký biên bản / phụ lục của SR (QC cung cấp 25/11/2026).
- Hệ thống được SR gọi tự động: Inside (khoản thu, phát hành hóa đơn, ký kết, phiếu thi công), SPF (đơn hàng, hủy đơn), Econtract (biên bản điện tử), FLI (FPT Play), ePayment (hoàn tiền chuyển khoản; UAT https://uat-epay.fpt.com — Cần host).

## Thao tác

### Tạo và xử lý một SR (luồng chung mọi loại SR)
1. Tạo SR: chọn hợp đồng → loại yêu cầu → dịch vụ → Tạo SR.
2. CBQL phân công, người xử lý nhận SR.
3. Liên hệ, tư vấn khách; nhập kết quả liên lạc và kết quả tư vấn.
4. Khách đồng ý → bấm Xử lý giao dịch, nhập thông tin mới theo loại SR.
5. Xử lý các ticket được sinh ra: duyệt, miễn giảm, thu tiền, ký kết, triển khai… (tùy loại SR).
6. Hệ thống cập nhật hợp đồng → SR Đã xử lý → khách đánh giá → Đã hoàn tất.

## Ý chính tài liệu

### Bộ URD SR (9 file)
- SR là nơi ghi nhận yêu cầu của khách hàng và điều hướng các ticket để xử lý trọn luồng; mỗi SR gắn 1 hợp đồng.
- Luồng chung: tạo SR → phân công → liên hệ, tư vấn → xử lý giao dịch → các ticket → cập nhật hợp đồng → khách đánh giá.
- Ý chính của từng URD nằm ở tài liệu của từng loại SR (bấm 📄 ở loại SR đó).

## Nguồn (QC thêm vào ngày 25/11/2026)

| File | Nội dung |
|---|---|
| `ISC-FTEL SR Web thay đổi thông tin Khách hàng_URD V3.0.docx` | SR thay đổi thông tin khách hàng (gồm chuyển chủ sở hữu) |
| `ISC-FTEL SR_V1.0_URD CDD_CDV_Confirmed.docx` | SR chuyển địa điểm cùng tỉnh (CDD), chuyển dịch vụ (CDV) |
| `ISC-FTEL SR_V1.0_TL_TN_URD V1.0.docx` | SR thanh lý / tạm ngưng (TL/TN) |
| `ISC-FTEL Service Request V1.2 - KPDV_URD V1.0_02082024.docx` | SR khôi phục dịch vụ (KPDV) |
| `ISC_Service-Request-Transaction_v.1.2_URD_v1.0_22082024.docx` | Màn xử lý giao dịch của SR khôi phục dịch vụ |
| `ISC_SR TL TSD_v1.0_URD_v1.0_DonhangChuathanhtoan.docx` | SR thanh lý trước sử dụng — đơn hàng chưa thanh toán |
| `ISC-FTEL SR Web Khóa ứng dụng FPT play_URD V1.0.docx` | SR khóa ứng dụng FPT Play (thêm 25/11/2026) |
| `ISC_SR Thủ tục thanh toán_v.1.0_URD_v1.0.docx` | SR thủ tục thanh toán — luồng nằm trong hình (thêm 25/11/2026) |
| `ISC_SR_HoanTien_URD_v1.0.docx` | SR hoàn tiền (thêm 25/11/2026) |

## Thông tin QC cung cấp

- 25/11/2026: SR thanh lý trước sử dụng — SPF hủy đơn thì **có hủy phiếu thi công và khoản thu** (URD không ghi).
