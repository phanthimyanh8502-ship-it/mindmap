# Input — PHÂN BỔ DOANH THU

Tài liệu đầu vào của quy trình nghiệp vụ ở [`../quy-trinh-nghiep-vu.md`](../quy-trinh-nghiep-vu.md).

## Tool

### Tool thao tác, cập nhật
- **Phân bổ doanh thu** — tự động — hệ thống tự treo, phân bổ dương, phân bổ âm sau khi phát hành hóa đơn.

### Tool kiểm tra
- **Báo cáo treo** — Inside › Quản lý kế toán › Master doanh thu › Báo cáo treo — theo dõi tiền đã xuất hóa đơn nhưng chưa phân bổ.
- **Báo cáo doanh thu phân bổ** — Inside › Quản lý kế toán › Master doanh thu › Báo cáo doanh thu phân bổ — báo cáo kế toán, thay menu cũ Báo cáo doanh thu › BC kế toán › PB Doanh thu.

## Thao tác

### Phân bổ doanh thu (hệ thống tự chạy)
1. Hóa đơn được phát hành khi giao hàng hoặc thanh toán hoàn tất.
2. Hệ thống xét danh mục, kỳ hạn, active ⇒ chia ngay hoặc treo.
3. Dịch vụ active ⇒ hệ thống phân bổ dương từ ngày active.
4. Có hóa đơn điều chỉnh giảm ⇒ hệ thống phân bổ âm.

### Kiểm tra kết quả phân bổ (người dùng)
1. Inside › Quản lý kế toán › Master doanh thu › Báo cáo treo: xem tiền treo theo chi nhánh và danh sách chi tiết.
2. Inside › Quản lý kế toán › Master doanh thu › Báo cáo doanh thu phân bổ: đối chiếu tiền treo với báo cáo treo.

## Ý chính tài liệu

### `Phan_bo_doanh_thu_v1_0_PRD_v1_1.docx`

- Mục đích: hóa đơn chưa có kỳ hạn lúc xuất thì chia doanh thu từ ngày active, chưa active thì treo. Lý do: xuất hóa đơn ngay khi giao hàng / thanh toán hoàn tất nhưng dịch vụ thường chưa active.
- Phạm vi: pilot cùng dự án quy hoạch xuất hóa đơn; B2B, B2C chung cơ chế. Ngoài phạm vi: điều chỉnh 0đ đổi kỳ hạn (BR-12), nâng / hạ gói, hóa đơn treo lâu, hợp đồng FTI (chi nhánh 90).
- Phân bổ dương (BR-01 → BR-07): xét danh mục ⇒ kỳ hạn (đã có thì chia như cũ, BR-03) ⇒ active (chưa thì treo, BR-04); chia từ ngày active theo số ngày, trên tiền trước VAT (BR-06, BR-07).
- Khóa sổ (BR-05): chốt tháng T ngày 02/T+1; dữ liệu active về từ 02/T+1 thì cảnh báo, phân bổ thủ công vào tháng đang mở.
- Phân bổ âm (BR-08 → BR-11): trừ từ tháng xa nhất; gốc treo thì giảm treo; tối đa 3 lần; hóa đơn bị thay thế ghi âm toàn bộ.
- Báo cáo: báo cáo treo (BR-13 → BR-17) và báo cáo doanh thu phân bổ (BR-18 → BR-20); hai báo cáo phải khớp tiền treo (BR-20).

### Phân tích `phan-bo-doanh-thu/02_analyze-requirements/v1.0/`

- Chia 4 module: PBD (phân bổ dương), PBA (phân bổ âm), BCT (báo cáo treo), BCPB (báo cáo doanh thu phân bổ).
- PBD, PBA chạy tự động; BCT, BCPB là báo cáo trên menu Master doanh thu.
- CL-PBD-01, CL-PBA-01 đã chốt 13/11/2026 (CL-PBA-01 chốt tạm theo PO); CL-BCT-02 (hóa đơn thay thế trên báo cáo treo) còn chờ BA.

## File trong thư mục này

- `Phan_bo_doanh_thu_v1_0_PRD_v1_1.docx`

## Nguồn

- `Phan_bo_doanh_thu_v1_0_PRD_v1_1.docx` (PRD v1.1, chốt 12/11/2026), bản gốc ở `phan-bo-doanh-thu/00_input/v1.0/Doc/`
- Phân tích `phan-bo-doanh-thu/02_analyze-requirements/v1.0/` (PBD, PBA, BCT, BCPB)
- Thông tin QC cung cấp 25/11/2026: kiểm tra phân bổ doanh thu ở Inside › Quản lý kế toán › Master doanh thu.
