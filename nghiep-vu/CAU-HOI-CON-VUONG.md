# Câu hỏi còn vướng (cập nhật 19/11/2026)

Tổng hợp từ việc đọc các tài liệu `input/`. **Phạm vi: chỉ workflow tổng quan** (bạn chốt 19/11/2026) — câu hỏi mức chi tiết đánh ⚪ không cần. Câu có mã BA-n được ghi chi tiết trong file `quy-trinh-nghiep-vu.md` của chủ thể tương ứng.

## A. Hỏi bạn (cách dùng tài liệu)

| # | Câu hỏi |
|---|---|
| A1 | ✅ Đã trả lời: bạn thay bằng URD Business Policy 2.1 |
| A2 | ✅ Đã trả lời: không có bản mới; quy trình tổng quan SCM do BA suy luận (xem C3) |
| A3 | ✅ Đã trả lời: bạn thay bằng URD Resource Equipment V1.0 — hệ thống là Inside – Vật tư TIN/PNC + Mobinet (còn hỏi: Mobinet có phải MobiX? xem C2) |
| A4 | ✅ Đã cập nhật sơ đồ và nhánh trên mindmap |

## B. Hỏi BA / PO

### Phiếu thi công (URD Phát triển phân hệ Triển khai)
| # | Câu hỏi |
|---|---|
| B1 | ✅ Một phần: PTC tạo từ đơn hàng, hoặc từ hợp đồng khi có SR chuyển dịch vụ / chuyển địa điểm / khôi phục dịch vụ. **Còn hỏi:** "phiếu công trắng" (khi request không đạt điều kiện) là gì? |
| B2 | ✅ Một phần: điều kiện hoàn tất theo `validate-completed-deployment.png`. Điều kiện tạo PTC / thi công: ⚪ không cần (chi tiết) |
| B3 | ✅ Đúng: hoàn ứng trên Tool Quản lý vật tư |

### Phiếu giao dịch thiết bị tại quầy — giao qua ĐVVC (URD Resource Equipment)
| # | Câu hỏi |
|---|---|
| BA-1 | ✅ chuyển về **Giao hàng thành công** · (hỏi: Bước B8 giao thành công nhưng ghi chuyển phiếu sang "Giao hàng **không** thành công": lỗi soạn thảo?) |
| BA-2 | ✅ **Chờ xác nhận** · (hỏi: Trạng thái đầu là "Chờ xử lý" (B1) hay "Chờ xác nhận" (B10)?) |
| BA-3 | ✅ không có — giữ đúng URD · (hỏi: Trạng thái số 10, 14, 15 là gì?) |
| BA-4 | ✅ **là 1** trạng thái · (hỏi: "Giao hàng không thành công" và "11. Giao không thành công" là 1 hay 2 trạng thái?) |
| BA-5 | ✅ **thu hồi về FTEL**, về kho đã chọn lúc xác nhận · (hỏi: Hủy đơn khi ĐVVC đã lấy hàng: thu hồi về FTEL hay vẫn giao cho khách? Vật tư về kho nào?) |
| BA-6 | ✅ QLVT gửi tín hiệu cho **SPF ghi nhận đơn hàng đã hoàn tất** · (hỏi: Phiếu giao có gửi tín hiệu giao hàng hoàn tất cho INVOICE với mọi đơn không (bảng B8 chỉ nói SPF cho đơn TMĐT và SM)?) |
| BA-7 | ⚪ Không cần — chi tiết, ngoài phạm vi workflow tổng quan (bạn 19/11/2026) · (hỏi: Có bảng map mã trạng thái GHTK / Ahamove → trạng thái phiếu giao không?) |
| BA-8 | ✅ **sau khi tạo đơn hàng** · (hỏi: Đơn Shopee / TikTok tạo phiếu giao ở thời điểm nào (không có khoản thu)?) |
| BA-9 | ✅ **trạng thái của đơn hàng** · (hỏi: "Đơn hàng BÌNH THƯỜNG" là tình trạng của đơn hay của hợp đồng?) |
| B4 | ✅ đúng, là **phiếu bán thiết bị** · (hỏi: Retail-Counter có nhiều loại giao dịch thiết bị (bán, thuê, đổi bảo hành…). Phiếu giao tại quầy của đơn SPF ứng với loại nào, có phải "phiếu bán thiết bị" không?) |

### Đơn đặt hàng Vendor (URD M-Vendor)
| # | Câu hỏi |
|---|---|
| BA-10 | 🟡 Bạn: **là 1 hệ thống** nhưng chưa chắc chắn — cần xác nhận lại với BA |
| BA-11 | ✅ Chưa giao hàng · Đang giao hàng · Đã hoàn tất · Đã hủy · (hỏi: Danh sách tình trạng giao hàng đầy đủ và luồng chuyển tình trạng?) |
| BA-12 | ✅ Mục Quản lý giao hàng không mô tả điều kiện ⇒ không cần (theo bạn) · (hỏi: Điều kiện kiểm tra khi cập nhật tình trạng / hủy đơn là gì? "Chắc chắn" chuyển sang tình trạng nào?) |
| BA-13 | ⚪ Không cần — chi tiết, ngoài phạm vi workflow tổng quan (bạn 19/11/2026) · (hỏi: Khi Đã hoàn tất / Hủy đơn hàng, Vendor báo về INVOICE / SPF thế nào?) |
| BA-14 | ✅ Ở **Fox ERP** · (hỏi: Màn hình QL Giao hàng ở Inside (URD) hay Fox ERP (tool STG)?) |
| BA-15 | ✅ Hóa đơn **NCU** và **hóa đơn điện tử**, bắt buộc user nhập, không kiểm tra tồn tại · (hỏi: "Đang giao hàng (kèm hóa đơn)": hóa đơn nào, có bắt buộc không?) |

### Vật tư quầy (URD Retail-Counter)
| # | Câu hỏi |
|---|---|
| B5 | ⚪ Không cần — chi tiết, ngoài phạm vi workflow tổng quan (bạn 19/11/2026) · (hỏi: Bước "Xác nhận ORC ERP" và "Dataload Compact" làm gì ở mức nghiệp vụ, có ảnh hưởng tới đơn hàng không?) |

### Phân bổ doanh thu (PRD v1.1)
| # | Câu hỏi |
|---|---|
| B6 | ✅ Theo workflow (Hình 1): xét dịch vụ → kỳ hạn → active; không áp điều kiện vắt tháng · (hỏi: BR-03: thứ tự xét kỳ hạn / dịch vụ, kỳ hạn phải vắt sang tháng sau mới phân bổ (PRD ghi chờ chốt)) |
| B7 | ⚪ Không cần — chi tiết, ngoài phạm vi workflow tổng quan (bạn 19/11/2026) · (hỏi: BR-11: phần hóa đơn bị thay thế ở tháng đã qua ghi âm 1 lần tại tháng hiện tại hay giữ rule cũ (PRD ghi chờ chốt)) |

### Khác (từ rule hiện có)
| # | Câu hỏi |
|---|---|
| B8 | 🟡 Bạn: **chưa có thông tin** (19/11/2026) — mindmap giữ "Chưa rõ" · (hỏi: VNTT có giao & lắp đặt và BBĐT không?) |

### Mới sau khi đọc input cập nhật
| # | Câu hỏi |
|---|---|
| C1 | ⚪ Không cần — chi tiết, ngoài phạm vi workflow tổng quan (bạn 19/11/2026) · (hỏi: Sơ đồ điều kiện hoàn tất PTC có "hoàn tất tất cả khoản thu hiển thị trên PTC", nhưng bạn cung cấp 17/11/2026 là đã **bỏ** rule khoản thu đã thanh toán mới hoàn tất PTC. Điều kiện nào đang đúng (hay chỉ bỏ trên STG)?) |
| C2 | ✅ **Là 1**: Mobinet = MobiX · (hỏi: URD Resource Equipment V1.0 ghi Mobinet (MBN) cho NVKT/KTV. Mobinet có phải app MobiX dùng để hoàn tất PTC không?) |
| C3 | ✅ Bạn chốt: quy trình tổng quan SCM chỉ cần phần **Tích hợp Inside** (5 quy trình + đối soát kho tạm). Còn chưa rõ: bồi thường được ghi thế nào trên SCM |
| C4 | ✅ **Là 1**: Tool BP = Tool QLCS · (hỏi: URD Business Policy 2.1 ghi domain bp.fpt.net; mindmap đang dùng bp-stag (STG, cần host). Tool BP và Tool QLCS là một phải không?) |
