## 4. HIỆN THỰC

### 4.1. Công Nghệ Sử Dụng

#### Front-End
- **HTML, CSS, JavaScript:** Các công nghệ cơ bản để tạo cấu trúc và phong cách cho trang web.
- **Bootstrap:** Sử dụng để tạo giao diện đẹp mắt và phản hồi tốt trên các thiết bị khác nhau.

#### Back-End
- **Django:** Framework Python mạnh mẽ để phát triển server backend.
- **Django REST Framework:** Sử dụng để xây dựng các API RESTful.
- **PostgreSQL:** Cơ sở dữ liệu quan hệ để lưu trữ thông tin người dùng và lịch sử chuyển đổi/dịch thuật.

#### API và Dịch Vụ Bên Thứ Ba
- **OpenAI Speech-to-Text API:** Để chuyển đổi giọng nói thành văn bản.

#### Extension
- **JavaScript, HTML, CSS:** Sử dụng để phát triển Extension.
- **Chrome Extension API:** Để tương tác với trình duyệt và thực hiện các chức năng của extension.

### 4.2. Giao Diện Ứng Dụng

Dưới đây là một số hình ảnh chụp màn hình của ứng dụng:

#### Trang Chính
![Trang Chính](images\trangchu.jpg)
*Hình ảnh của trang chính với chức năng tải lên tệp video và hiển thị phụ đề.*

#### Trang Kết Quả
![Trang Kết Quả](path/to/result_page_screenshot.png)
*Hình ảnh của trang kết quả hiển thị phụ đề đã chuyển đổi và dịch thuật.*

#### Extension Popup
![Extension Popup](path/to/extension_popup_screenshot.png)
*Hình ảnh của popup extension với chức năng ghi âm và hiển thị phụ đề trực tiếp.*

### 4.3. Kết Quả

#### Làm Được
- **Ghi hình và hiển thị phụ đề trên extension:** Cho phép người dùng quay màn hình máy tính và hiển thị popup phụ đề ngay lập tức.
- **Tích hợp được một số tính năng đề xuất** : đã tích hợp một số tính năng như tóm tắt nội dung trong video, hỏi đáp dựa trên nội dung đó.
- **Giao diện người dùng đơn giản:** Đã phát triển trang chính với chức năng tải lên tệp video, hiển thị phụ đề và dịch phụ đề.
- **Quản lý phiên làm việc:** Lưu trữ phiên làm việc
- **Quản lý người dùng:** Đã tích hợp chức năng đăng ký và đăng nhập.

#### Chưa Làm Được
- **Chỉnh sửa văn bản:** Chưa hỗ trợ chỉnh sửa văn bản đã chuyển đổi và dịch thuật trực tiếp trong video
- **Hiển thị phụ đề của video trên trang web:** Cho phép người dùng tải lên tệp video và sử dụng API OpenAI Speech-to-Text để hiển thị phụ đề.
- **Dịch phụ đề trên trang web:** Hỗ trợ dịch phụ đề sử dụng API của OpenAI.

#### Hướng Phát Triển
- **Nâng cao chất lượng chuyển đổi và dịch thuật:** Huấn luyện các mô hình AI/ML để tiết kiệm chi phí cũng như cải thiện độ chính xác.
- **Cải tiến giao diện:** Cải thiện giao diện người dùng để thân thiện hơn và dễ sử dụng hơn.
- **Cải tiến tốc độ:** Sử dụng các công nghệ như WebSocket, Kafka, .... để giúp cải thiện tốc độ của extension, giúp cải thiện khả năng realtime.
