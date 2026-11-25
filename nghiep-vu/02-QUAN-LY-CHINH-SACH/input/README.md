# Input — QUẢN LÝ CHÍNH SÁCH (TOOL BP)

Tài liệu đầu vào của quy trình nghiệp vụ ở [`../quy-trinh-nghiep-vu.md`](../quy-trinh-nghiep-vu.md).

## Tool

- **Tool BP (QLCS)** — Bán hàng › tab Bán hàng — tạo, gửi đề xuất và ra quyết định chính sách bán hàng. STG: http://bp-stag.fpt.net/ (cần host).

## Thao tác

### Tạo chính sách bán hàng mới (Tool BP)
1. Tìm chính sách bán hàng có sẵn của dịch vụ muốn bán.
2. Sao chép chính sách đó, sửa thông tin chính sách mới rồi lưu.
3. Trở về, gửi đề xuất.

### Ra quyết định để chính sách được áp dụng
1. Vào Bán hàng › tab Bán hàng, tìm mã chính sách vừa gửi đề xuất.
2. Tích chọn, tạo quyết định, nhập thông tin hợp lệ rồi lưu.

## Ý chính tài liệu

### `ISC_Business-Policy_2.1-URD-v1.1.docx`

- Tool QLCS quản lý chính sách từ lúc tạo đề xuất ⇒ xem xét ⇒ phê duyệt ⇒ quyết định ⇒ ban hành.
- Chính sách bán hàng, ưu đãi, chiết khấu tạo trên cùng hệ thống, giúp tạo combo bán hàng nhanh.
- Các tool bán hàng khác lấy giá bán từ QLCS. Phạm vi triển khai: toàn quốc.
- Nhóm Chính sách bán hàng: nhập chính sách only và combo 1 dịch vụ nhiều phí, cập nhật nhanh PHM trong cùng chính sách, rule lấy giá FPT Play giống Net cho SPF.
- Nhóm Voucher: lọc chính sách để phân phối theo quyền tài khoản HRIS (kể cả kiêm nhiệm); hạn mức khách vãng lai chỉ khai báo cấp Vùng cho từng chính sách.

### Thông tin QC cung cấp

- Chính sách quyết định giá bán, gói bán, khu vực bán, thiết bị đi kèm, đối tượng và loại khách hàng, kênh bán, đơn vị bán hàng, phương thức thanh toán, hình thức triển khai.
- Voucher: khách hàng hoặc nhân viên add vào lúc tạo đơn (04/11/2026).
- Hình thức triển khai quyết định nơi đẩy: Không, Quầy, Sale ⇒ Tool quầy; NCC-Samsung, NCC-Casper ⇒ M-Vendor; TIN/PNC ⇒ Giao & lắp đặt.
- Tool QLCS chính là Tool BP. Bán thiết bị: QLCS lấy dữ liệu từ Quản lý vật tư rồi trả ra SPF (19/11/2026).

### `AnhNQ75-List HT Triển khai.xlsx`

- Liệt kê các hình thức triển khai: TIN/PNC, TIN/PNC giao hàng, Quầy, Sale, NCC Samsung / Sony / Casper, FTI, Không.
- Đầu ra: TIN/PNC, FTI ⇒ phiếu thi công loại Triển khai; TIN/PNC giao hàng ⇒ phiếu thi công loại Giao hàng; Quầy, Sale ⇒ phiếu giao dịch bán thiết bị; NCC ⇒ phiếu giao hàng NCC và mã vận đơn; Không ⇒ không có phiếu.
- Phạm vi: TIN/PNC giao hàng và Quầy chỉ cho Camera Offnet, Thiết bị lẻ; Sale chỉ Thiết bị lẻ quản lý MAC; NCC chỉ thiết bị lẻ mua từ NCC bán lại; FTI cho dự án, SPDV đặc thù (OnCall, Camera B2B, ListLine).
- Đơn có ≥1 SPDV mix TIN/PNC với Quầy / Sale ⇒ tự xử lý theo luồng TIN/PNC. Chỉ có "Không" ⇒ không đẩy triển khai, giao hàng.
- File không có bảng từng dịch vụ ↔ hình thức triển khai; hình thức thực tế do chính sách khai báo.

### Clarification CL-XHD-27, CL-XHD-34

- Chốt 20/10/2026 trong dự án `qc-iia`.
- Thiết bị "Không" chỉ xuất hóa đơn khi quầy gửi tín hiệu; quầy không gửi ⇒ không xuất hóa đơn.
- Mix "Không" + TIN/PNC ⇒ triển khai theo phiếu thi công. Đơn có ≥1 SPDV mix TIN/PNC ⇒ cả đơn đi luồng TIN/PNC.

## File trong thư mục này

- `ISC_Business-Policy_2.1-URD-v1.1.docx` (QC bổ sung 19/11/2026)

## Nguồn

- `ISC_Business-Policy_2.1-URD-v1.1.docx`: chỉ dùng mục **Thông tin chung** và **Tổng quan** (sơ đồ tổng quan, danh sách chức năng)
- Thông tin QC cung cấp (ghi ở đầu từng mục trong `quy-trinh-nghiep-vu.md`): 03/11/2026, 04/11/2026 (voucher)
- Danh sách hình thức triển khai: [`AnhNQ75-List HT Triển khai.xlsx`](../../05-GIAO-LAP-DAT/input/) (nằm ở input của Giao & lắp đặt)
- Clarification CL-XHD-27, CL-XHD-34 (chốt 20/10/2026, dự án `qc-iia`)
