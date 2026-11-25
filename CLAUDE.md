# CLAUDE.md — luong_ban_hang2

Repo tài liệu nghiệp vụ **luồng bán hàng → hóa đơn** (môi trường STG): rule từng chủ thể, từng kênh bán, và mindmap HTML trực quan hóa toàn luồng. Không có code ứng dụng; chỉ Markdown + HTML tĩnh + 1 script nhúng.

## 1. Thứ tự đọc (nguồn sự thật)

1. [`RULE-XHD.md`](RULE-XHD.md) — rule module Xuất hóa đơn v2.0 (kênh/dịch vụ trong scope, BR đồng bộ, CL đã chốt).
2. [`RULE-CHINH-SACH-KENH-BAN.md`](RULE-CHINH-SACH-KENH-BAN.md) — mục lục tool chính sách & các kênh bán, trỏ vào `nghiep-vu/01-DON-HANG/kenh-ban/`.
3. [`nghiep-vu/README.md`](nghiep-vu/README.md) — bảng 13 chủ thể + quy ước thư mục + file gốc nằm ở đâu.
4. `nghiep-vu/<NN-CHU-THE>/quy-trinh-nghiep-vu.md` — chi tiết từng chủ thể; câu hỏi còn mở ở [`nghiep-vu/CAU-HOI-CON-VUONG.md`](nghiep-vu/CAU-HOI-CON-VUONG.md).

Chỉ đọc file cần cho task, không đọc cả 3 file mindmap HTML (rất lớn: 60–420 KB).

## 2. Bản đồ repo

| Đường dẫn | Vai trò |
|---|---|
| `nghiep-vu/<NN-CHU-THE>/` | 1 chủ thể = `input/` (nguồn + `README.md` liệt kê nguồn) + `quy-trinh-nghiep-vu.md` |
| `nghiep-vu/01-DON-HANG/kenh-ban/` | Ngoại lệ: không có `input/` chung; `00-CHUNG.md` + 1 thư mục/kênh `<KÊNH>/<KÊNH>.md` + `input/` riêng. Desktop + Mobile chung `SOP/` |
| `nghiep-vu/05-PHIEU-TRIEN-KHAI/` | 3 thư mục con theo loại triển khai (thi công / giao tại quầy / vendor), mỗi con có `input/` + `quy-trinh-nghiep-vu.md` |
| `mindmap-don-hang-v2.html` | Mindmap bản chính (popup kênh bán, nút 📄 Tài liệu hiện `quy-trinh-nghiep-vu.md`) |
| `mindmap-don-hang.html` | Mindmap v1 (vẫn được nhúng docs) |
| `mindmap-don-hang-lite.html` | Bản rút gọn (owner, nơi thao tác) — **không** nhúng docs, sửa tay |
| `scripts/embed-docs.py` | Nhúng mọi `quy-trinh-nghiep-vu.md` vào v1 + v2 (giữa `DOCS:BEGIN`/`DOCS:END`) |
| `tools/*.zip` | Tool Node.js hỗ trợ **tạo data test nhanh** (vd `Don_SOP` lên đơn SOP, `Don_TMDT` đơn TMĐT, `Tao_DH`, `Thanh_toan`, `FPL`, `GH_quay`, `GH_Vendor`). Mindmap có link tải; chỉ thay khi user đưa bản mới |

## 3. Quy trình sửa nội dung

1. Sửa đúng file `.md` của chủ thể/kênh (rule kênh → `kenh-ban/<KÊNH>/<KÊNH>.md`; rule chung mọi kênh → `00-CHUNG.md`).
2. Thông tin mới từ user → ghi nguồn + ngày vào `input/README.md` tương ứng.
3. Sửa bất kỳ `quy-trinh-nghiep-vu.md` nào → **bắt buộc chạy** `python3 scripts/embed-docs.py` rồi commit cả HTML.
4. Thêm/đổi kênh hoặc chủ thể → cập nhật luôn mục lục (`RULE-CHINH-SACH-KENH-BAN.md`, `nghiep-vu/README.md`) và node tương ứng trong mindmap v2 (+ lite nếu liên quan).
5. Không sửa HTML giữa `DOCS:BEGIN`/`DOCS:END` bằng tay.

## 4. Ràng buộc

- **Repo công khai.** Không commit tài liệu gốc nội bộ (`.gitignore` chặn `*.docx/*.xlsx/*.pdf/*.png` trong `nghiep-vu/`); chỉ ghi tên file trong `input/README.md`.
- Không ghi secret, token, mật khẩu, tài khoản STG vào bất kỳ file nào (kể cả `.env` trong zip tool — chỉ có `.env.example`).
- Viết tiếng Việt có dấu; giữ nguyên thuật ngữ/ID hệ thống (SaleChannelID, ServiceID, SubServiceType, BR-*, REQ-*, CL-*).

## 5. Commit

Conventional Commits + tag `[AI]`, scope theo vùng sửa:
- `feat(mindmap): ...` — thay đổi HTML mindmap
- `docs(kenh-ban): ...` / `docs(nghiep-vu): ...` — thay đổi rule Markdown
