## 1. KẾ HOẠCH

### 1.1 Mô tả ý tưởng đề tài
#### Ý tưởng
Trong quá trình học tập thì lượng kiến thức, khóa học trực tuyến thường là những khóa học bằng tiếng Anh. Cho nên việc tiếp cận các kiến thức đang bị rào cản bởi ngoại ngữ. Để tăng cường hiệu suất học tập, làm việc thì nhóm nảy ra ý tưởng để vượt qua rào cản đó bằng việc phát triển tiện ích hỗ trợ tạo phụ đề cho video (speech to text) và dịch phụ đề (translate) cho tiếng Việt. 
#### Phạm vi dự án
-	**Trang Web**:
--	Chức năng và tải lên tệp video, âm thanh để có thể tạo ra phụ đề
--	Chức năng dịch thuật phụ đề.
--	Hỗ trợ tóm tắt nội dung văn bản của video.
--	Chatbot hỏi đáp dựa trên nội dung của video.
--	Lưu trữ và quản lý lịch sử của người dùng.
-	**Extension**:
--	Hỗ trợ ghi hình trực tiếp và hiện thị phụ đề theo thời gian thực, hỗ trợ đa nền tảng, cả ngoài trình duyệt
--	Tóm tắt, hỏi đáp nội dung sau khi kết thúc ghi hình.

#### Kế hoạch làm việc
- *Tuần 1: Khảo sát thị trường, phân tích và lên kế hoạch*
  - Thu thập và phân tích yêu cầu từ các bên liên quan.
  - Xác định các chức năng chính và phụ của hệ thống.
  - Lập kế hoạch chi tiết cho từng giai đoạn của dự án.

- *Tuần 2: Thiết kế hệ thống và giao diện*
  - Thiết kế kiến trúc hệ thống bao gồm frontend, backend và cơ sở dữ liệu.
  - Tạo prototype giao diện người dùng.
  - Xác định các API cần thiết và cách tích hợp.

- *Tuần 3-5: Phát triển hệ thống*
  - Phát triển frontend với các công nghệ như HTML, CSS, JavaScript.
  - Phát triển backend với Django, tích hợp API nhận dạng giọng nói và dịch ngôn ngữ.
  - Thiết kế và triển khai cơ sở dữ liệu với PostgreSQL.

- *Tuần 6: Kiểm thử và triển khai*
  - Thực hiện kiểm thử đơn vị (unit testing) và kiểm thử tích hợp (integration testing).
  - Kiểm thử giao diện người dùng để đảm bảo trải nghiệm mượt mà và không lỗi.

- *Tuần 7: Hoàn thiện*
  - Sửa lỗi từ kiểm thử, thu thập phản hồi từ người dùng và điều chỉnh hệ thống.
  - Đánh giá hiệu suất và độ ổn định của hệ thống.
  - Chuẩn bị báo cáo cuối cùng và tài liệu hướng dẫn sử dụng.

### 1.2 Sản phẩm MVP
#### Trang Web
- **Chuyển đổi giọng nói thành văn bản:(tạo phụ đề)**
   - Cho phép người dùng tải lên tệp âm thanh.
   - Sử dụng API OpenAI Speech-to-Text để chuyển đổi giọng nói thành văn bản.

- **Dịch phụ đề trên video**
   - Hỗ trợ dịch phụ đề bằng API của OpenAI.

- **Giao diện người dùng đơn giản:**
   - Trang chính với chức năng tải lên tệp video.
   - Hiển thị phụ đề và dịch phụ đề.

- **Quản lý phiên làm việc:**
   - Lưu trữ tạm thời các phiên làm việc hiện tại mà không cần đăng nhập.

#### Extension

1. **Ghi hình và hiển thị phụ đề**
   - Cho phép người dùng ghi âm trực tiếp từ màn hình máy tính và hiển thị popup phụ đề ngay lập tứ.

### 1.3 Sản phẩm hoàn thiện

#### Trang Web

1. **Tính Năng Cải Tiến:**
    - **Giao diện người dùng nâng cao**: Trang chính với chức năng tải lên tệp video. Hiển thị phụ đề và dịch phụ đề với giao diện thân thiện, dễ sử dụng.
    - **Bổ sung thêm tính năng:** Phát triển thêm một số tính năng như tóm tắt nội dung video, chatbot hỏi đáp dựa trên nội dung trong video.

2. **Trải Nghiệm Người Dùng:**
   - **Giao Diện Thân Thiện Hơn:** Cải thiện giao diện người dùng để tạo ra một trải nghiệm sử dụng dễ dàng và trực quan hơn. 
   - **Đăng nhập**: yêu cầu phải đăng nhập tài khoản mới sử dụng được để có thể quản lý lịch sử dụng hiệu quả.

#### Extension

1. **Nâng cấp chức năng:**
   - **Bổ sung thêm tính năng:** Phát triển thêm một số tính năng như tóm tắt nội dung video, chatbot hỏi đáp dựa trên nội dung sau khi kết thúc ghi hình.
   - **Cải thiện trải nghiệm người dùng**: Hỗ trợ người dùng có thể di chuyển tùy chọn vị trí hiển thị của popup "Streaming Caption" giúp trải nghiệm tốt hơn, không bị che mất nội dung trong một số trường hợp.
   - **Yêu cầu đăng nhập**: Yêu cầu đăng nhập để có thể sử dụng, giúp cho người dùng có thể lưu lại, quản lý lịch sử ghi hình tốt hơn. Nếu người dùng chưa đăng nhập thì click vào nút "Đăng nhập" sẽ nhảy qua trang web để đăng nhập.
   
2. **Hiệu Suất và Ổn Định:**
   - **Tối ưu hóa tốc độ:** Tối ưu hóa mã nguồn và kiến trúc để cải thiện hiệu suất và tốc độ hoạt động của extension để hỗ trợ tốt nha realtime.
   - **Kiểm Thử Tích Hợp Kỹ Lưỡng:** Thực hiện kiểm thử tích hợp đầy đủ để đảm bảo tính ổn định và tương thích với các phiên bản trình duyệt khác nhau.


