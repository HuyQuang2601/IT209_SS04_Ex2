# Báo cáo Bài 2: Quản lý nhánh và giải quyết Merge Conflict

## Các bước thực hiện

1. Khởi tạo repository và tạo commit nền trên nhánh `main`.
2. Chạy `git switch -c feature-update` để tạo nhánh tính năng.
3. Trên `feature-update`, sửa dòng phiên bản trong `README.md` và commit thay đổi.
4. Chạy `git switch main`, sửa chính dòng đó theo nội dung vá bảo mật rồi commit.
5. Chạy `git merge --no-ff feature-update`. Git phát hiện hai nhánh đã thay đổi cùng một dòng nên dừng với trạng thái `CONFLICT (content)`.
6. Mở `README.md`, đọc hai phần nằm giữa `<<<<<<< HEAD`, `=======` và `>>>>>>> feature-update`.
7. Kết hợp thủ công nội dung của cả hai nhánh thành một câu hoàn chỉnh, sau đó xóa toàn bộ các ký hiệu đánh dấu xung đột.
8. Chạy `git add README.md BAO_CAO.md` và `git commit` để hoàn tất merge commit.
9. Kiểm tra kết quả bằng `git log --graph --oneline --decorate --all`.

## Nội dung sau khi giải quyết

> Phiên bản hiện tại: 2.0 - Đã bổ sung tính năng cập nhật hồ sơ người dùng, sửa lỗi bảo mật và cải thiện độ ổn định.

Kết quả này giữ lại nội dung quan trọng từ cả nhánh `main` và `feature-update`; trong file không còn các dấu `<<<<<<<`, `=======`, `>>>>>>>`.

## Cơ chế 3-Way Merge

Git so sánh ba phiên bản: commit tổ tiên chung, đầu nhánh `main`, và đầu nhánh `feature-update`. Vì cả hai nhánh đều thay đổi cùng một dòng so với tổ tiên chung nhưng có nội dung khác nhau, Git không thể tự quyết định nên giữ phiên bản nào và tạo merge conflict. Sau khi người dùng xử lý thủ công, merge commit mới có hai parent, mỗi parent trỏ về một đầu nhánh trước khi gộp.

## Minh chứng

Ảnh `images/git-log-graph.png` ghi lại kết quả lệnh kiểm tra lịch sử nhánh.
