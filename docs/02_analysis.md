## 2. PHÂN TÍCH

### 2.1 Giới thiệu

#### 2.1.1. Mục đích

Mục đích của tài liệu này nhằm mô tả một cách đầy đủ và toàn diện yêu cầu của ứng dụng: các yêu cầu chức năng, yêu cầu phi chức năng, các ràng buộc về mặt thiết kế.

Nhằm mô tả một cách đầy đủ và toàn diện yêu cầu của ứng dụng MVP này với các chức năng và các ràng buộc về mặt thiết kế: 
#### 2.1.2 Phạm vi

Mô tả ngắn gọn đặc điểm của ứng dụng; phạm vi, đối tượng phục vụ của ứng dụng; nhóm các hệ thống con
Chỉ ra được tài liệu này dùng cho đối tượng nào?
### Phạm vi: MVP (Minimum Viable Product) của hệ thống dịch từ giọng nói sang văn bản và dịch văn bản hướng tới các đối tượng sau:

- Người hay làm việc với khách nước ngoài nói tiếng Anh:

    Nhân viên văn phòng, chuyên viên tư vấn, giáo viên, nhà nghiên cứu, và các chuyên gia khác thường xuyên phải giao tiếp với người nước ngoài.
    Các cá nhân thường xuyên tham gia các cuộc họp, hội thảo quốc tế và cần công cụ hỗ trợ dịch thuật nhanh chóng, chính xác.
- Người yếu tiếng Anh nhưng có nhu cầu tham gia các cuộc hội thảo quốc tế:

    Sinh viên, nhà nghiên cứu, và những người có nhu cầu học tập, nghiên cứu quốc tế.
    Những người cần công cụ hỗ trợ dịch thuật để hiểu và tham gia thảo luận trong các hội thảo, khóa học trực tuyến và các sự kiện quốc tế khác.
### Đối tượng phục vụ
1. Nhân viên văn phòng và chuyên gia:

- Người làm việc trong các công ty, tổ chức có liên quan đến đối tác, khách hàng quốc tế.
- Chuyên gia cần trình bày và giao tiếp trong các hội thảo, cuộc họp quốc tế.
2. Sinh viên và nhà nghiên cứu:

- Người tham gia các khóa học, nghiên cứu quốc tế, hội thảo học thuật.
- Người có nhu cầu học tập, trao đổi kiến thức với các chuyên gia quốc tế.
### 2.2 Phân tích yêu cầu

#### 2.2.1 Đặc tả Actors

1. Người dùng cuối (End User)

- Mô tả: Các cá nhân sử dụng ứng dụng để dịch giọng nói và văn bản trong các cuộc hội họp trực tuyến.
- Vai trò và trách nhiệm:
    Sử dụng ứng dụng để chuyển đổi giọng nói thành văn bản.
    Yêu cầu dịch văn bản từ tiếng Anh sang tiếng Việt hoặc hiển thị transcript.
    Tương tác với hệ thống trong các cuộc họp và hội thảo trực tuyến như chat, tóm tắt nội dung cuộc họp.
- Quyền hạn:
    Truy cập các chức năng chuyển đổi giọng nói và dịch văn bản.
    Truy cập vào chức năng chat và tóm tắt cuộc hội thoại
    Nhận kết quả dịch thuật và lưu trữ chúng nếu cần.
2. Nhà phát triển phần mềm (Software Developer)

Mô tả: Nhóm lập trình viên và kỹ sư phát triển và bảo trì ứng dụng.
Vai trò và trách nhiệm:
Phát triển và cập nhật các tính năng của hệ thống.
Sửa lỗi và cải thiện hiệu suất của ứng dụng.
Đảm bảo tính tương thích và tích hợp của các công nghệ dịch thuật.
Quyền hạn:
Truy cập mã nguồn và tài liệu phát triển.
Thực hiện các thay đổi và cập nhật cần thiết cho hệ thống.


#### 2.2.2 Đặc tả Use-cases

- Danh sách các use-cases:
    - UC01: đăng nhập (Mô tả:...)
    - UC02: thống kê (Mô tả:...)
    - UC03: đăng bài viết (Mô tả:...)
    - UC04:  (Mô tả:...)
    - ... 
- Liệt kê các use-cases theo actor: (LƯU Ý: nếu phần này các chức năng thực hiện khác nhau ở mỗi actor thì ghi rõ các khác nhau đó)
    - Actor 1:
        - UC01: đăng nhập
        - UC03: đăng bài viết
    - Actor 2:
        - UC01: đăng nhập
        - UC02: thống kê
    - Actor 3:
        - ...
