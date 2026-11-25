# Chủ thể

Mỗi thư mục là 1 chủ thể của mindmap, gồm 2 thành phần:

| Thành phần | Nội dung |
|---|---|
| `input/` | Tài liệu đầu vào: file gốc (URD, PRD, Excel) nếu có, và `README.md` liệt kê mọi nguồn (gồm cả thông tin QC cung cấp theo ngày) |
| `quy-trinh-nghiep-vu.md` | Quy trình nghiệp vụ / rule của chủ thể. Mindmap v2 hiện file này ở nút **📄 Tài liệu** trong popup chủ thể |

Riêng **Đơn hàng** (`01-DON-HANG`): `input/README.md` chỉ chứa nội dung nút 📄 Tài liệu (tool, thao tác, nghiệp vụ chính), không chứa file gốc (nguồn chung ghi ngay trong `quy-trinh-nghiep-vu.md`), thay bằng thư mục `kenh-ban/`: rule chung mọi kênh (`00-CHUNG.md`) và 1 thư mục / kênh bán (`kenh-ban/<KÊNH>/` gồm `<KÊNH>.md` + `input/` riêng, không dùng chung; Desktop + Mobile chung thư mục `SOP/`), vì kênh bán là nơi tạo đơn. **Giao & lắp đặt** (`05`) tách 3 thư mục con theo loại triển khai, mỗi thư mục cũng có `input/` + `quy-trinh-nghiep-vu.md`.

| Thư mục | Chủ thể | File gốc trong `input/` |
|---|---|---|
| `01-DON-HANG` | Đơn hàng (+ `kenh-ban/`) | — · `kenh-ban/SOP/input/`: `URD_BaoGia_v1.0_22 Apr 2026_KieuPTP5.docx` |
| `02-QUAN-LY-CHINH-SACH` | Quản lý chính sách (Tool BP) | — (dùng file Excel ở `05`) |
| `03-HOP-DONG` | Hợp đồng | — (dùng URD ở `07`) |
| `04-KHOAN-THU` | Khoản thu | — |
| `05-GIAO-LAP-DAT` | Giao & lắp đặt (tổng quan) + 3 thư mục con, mỗi thư mục 1 loại triển khai: `01-PHIEU-THI-CONG`, `02-PHIEU-GIAO-DICH-THIET-BI-TAI-QUAY`, `03-DON-DAT-HANG-VENDOR` | `AnhNQ75-List HT Triển khai.xlsx` · 02: `QC-ISC_Resource-Equipment_v2.2_URD_v1.0.docx` · 03: `ISC_INSIDE-M-VendorCooperation_V1.1_URD_V1.0.docx` |
| `06-BIEN-BAN-DIEN-TU` | Biên bản điện tử | — |
| `07-XUAT-HOA-DON` | Xuất hóa đơn | `Invoice_Issuance_Architecture_v2_2_URD_v2_0.docx` |
| `08-GACH-NO-HAU-KY` | Gạch nợ & hậu kỳ | — (dùng URD ở `07`) |
| `09-HUY-DON-HANG` | Hủy đơn hàng | — |
| `10-QUAN-LY-VAT-TU` | Tool Quản lý vật tư | — |
| `11-QUAN-LY-VAT-TU-QUAY` | Tool Quản lý vật tư quầy | — |
| `12-TOOL-SCM` | Tool SCM | — |
| `13-PHAN-BO-DOANH-THU` | Phân bổ doanh thu | `Phan_bo_doanh_thu_v1_0_PRD_v1_1.docx` |
| `14-SR` | SR (Service Request) — luồng chung ở thư mục cha; 9 thư mục con `01`…`09`, mỗi loại SR 1 tài liệu (`quy-trinh-nghiep-vu.md` + `input/README.md`). Trên mindmap: Hợp đồng › Cập nhật hợp đồng › Tool SR; SR thanh lý trước sử dụng ở Hủy đơn hàng | 9 URD SR, để chung ở `14-SR/input/` |

Mỗi file gốc chỉ để ở 1 chủ thể; chủ thể khác dùng chung thì `input/README.md` trỏ tới. Riêng kênh bán: mỗi kênh giữ bản riêng trong `input/` của kênh; Desktop + Mobile gom chung thư mục `kenh-ban/SOP/` (1 `input/`).

> ⚠️ File gốc là tài liệu nội bộ, repo GitHub đang công khai: `.gitignore` chặn `*.docx`, `*.xlsx`, `*.pdf` trong `nghiep-vu/**/input/`.

Sửa `quy-trinh-nghiep-vu.md` xong thì chạy `python3 scripts/embed-docs.py` để cập nhật mindmap, rồi đăng lại artifact.
