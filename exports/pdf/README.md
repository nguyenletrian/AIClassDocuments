# PDF exports — Bản phát hành cho sinh viên

Thư mục này dành riêng cho **tài liệu PDF được xuất từ các bài Markdown đã duyệt**. Bản gốc để chỉnh sửa vẫn ở `lessons/`. Không copy ảnh, chỉnh code hay thay nội dung một cách thủ công giữa hai bản.

## Quy tắc đặt tên

Ví dụ:

```text
AIClassDocuments/
├── lessons/pilot/AI-MATH-01-pca.vi.md   # Markdown gốc (có thể tiếp tục biên tập)
├── lessons/pilot/assets/                # SVG / PNG gốc của bài
└── exports/pdf/
    ├── README.md
    └── AI-MATH-01-pca.vi.pdf            # chỉ tồn tại SAU KHI đã xuất thật
```

## Quy trình khi được yêu cầu xuất PDF

1. Đọc đúng phiên bản Markdown và tham chiếu hình tương đối từ thư mục chứa nó. Xác minh cả hai hình SVG hiện có; nếu engine PDF không đọc SVG thì chuyển thành PNG tại bước tạo PDF, **không sửa đường dẫn nguồn hay xóa hình gốc**.
2. Xuất thành PDF từ nguồn Markdown (hoặc chuyển qua DOCX/HTML trung gian nếu phù hợp) với font Unicode hỗ trợ tiếng Việt, style rõ ràng, bảng không tràn lề và khối code có thể đọc.
3. Đảm bảo giữ **20 câu song ngữ Anh–Việt, 80 lựa chọn song ngữ, 20 đáp án với giải thích Anh–Việt**, cùng hai hình và tất cả bảng dữ liệu.
4. Render PDF thành ảnh từng trang và xem lại bố cục: không mất hình, chữ có dấu, hàng/cột và code không bị cắt, các lựa chọn trắc nghiệm không bị lẫn.
5. Chỉ đưa file PDF đã kiểm tra vào `exports/pdf/` với tên tương ứng. Bản gốc trong `lessons/` không đổi.

**Hiện trạng:** Mới chuẩn bị thư mục và quy tắc. **Chưa tạo PDF.** Không ghi log `PDF_EXPORTED`/đánh dấu `SOURCE_READY` nếu chưa có file PDF thật cùng bằng chứng kiểm tra.
