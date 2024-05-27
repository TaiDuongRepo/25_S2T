## 2. PHÂN TÍCH

### 2.1 Giới thiệu

#### 2.1.1. Mục đích

Mục đích của ứng dụng là cung cấp cho người dùng một công cụ đa chức năng và tiện ích để hiển thị phụ đề bằng việc chuyển đổi giọng nói thành văn bản và dịch văn bản giữa tiếng Việt và các ngôn ngữ khác. Cụ thể, ứng dụng sẽ đáp ứng các yêu cầu sau:

##### Yêu cầu chức năng:
1. **Nhận dạng giọng nói**: Hệ thống cần có khả năng nhận dạng và chuyển đổi giọng nói từ người dùng thành văn bản với độ chính xác cao.
2. **Giao diện người dùng thân thiện**: Giao diện người dùng cần được thiết kế để dễ sử dụng và trực quan, giúp người dùng tương tác một cách dễ dàng.
3. **Quản lý dữ liệu**: Hệ thống cần có khả năng lưu trữ và quản lý các bản ghi văn bản đã chuyển đổi và dịch, cũng như thông tin người dùng.

##### Yêu cầu phi chức năng:
1. **Hiệu suất**: Hệ thống cần hoạt động mượt mà và đáp ứng nhanh với các yêu cầu từ người dùng với tốc độ nhanh.
2. **Bảo mật**: Dữ liệu người dùng cần được bảo vệ một cách an toàn và không được tiết lộ cho bất kỳ bên thứ ba nào.
3. **Tương thích**: Ứng dụng cần tương thích trên nhiều nền tảng và trình duyệt khác nhau.
4. **Khả năng mở rộng:** Hệ thống phải có khả năng mở rộng để hỗ trợ thêm nhiều ngôn ngữ và tính năng trong tương lai.

##### Ràng Buộc Thiết Kế:
1. **Tích hợp API**: Sử dụng API của OpenAI để cung cấp các tính năng nhận dạng giọng nói và chuyển thành văn bản.
2. **Giao diện thân thiện**: Thiết kế giao diện người dùng để phản ánh sự thân thiện và dễ tiếp cận, đảm bảo trải nghiệm người dùng tốt nhất có thể.
3. **Dữ Liệu an toàn**: Đảm bảo rằng dữ liệu người dùng được lưu trữ và truy cập một cách an toàn và bảo mật.

#### 2.1.2 Phạm vi

Mô tả ngắn gọn đặc điểm của ứng dụng; phạm vi, đối tượng phục vụ của ứng dụng; nhóm các hệ thống con
Chỉ ra được tài liệu này dùng cho đối tượng nào?

**Đặc điểm:**
- Hiển thị phụ đề của video, record.
- Hỗ trợ nhiều ngôn ngữ phổ biến.
- Giao diện đơn giản, tương thích người dùng, dễ sử dụng.

**Phạm vi, đối tượng sử dụng:** 
MVP (Minimum Viable Product) của hệ thống dịch từ giọng nói sang văn bản (hiển thị phụ đề ) và dịch phụ đề hướng tới các đối tượng sau:
- Người hay làm việc với khách nước ngoài nói tiếng Anh:
  - Nhân viên văn phòng, chuyên viên tư vấn, giáo viên, nhà nghiên cứu, và các chuyên gia khác thường xuyên phải giao tiếp với người nước ngoài.
  - Các cá nhân thường xuyên tham gia các cuộc họp, hội thảo quốc tế và cần công cụ hỗ trợ dịch thuật nhanh chóng, chính xác.
- Người yếu tiếng Anh nhưng có nhu cầu tham gia các cuộc hội thảo quốc tế:
  - Sinh viên, nhà nghiên cứu, và những người có nhu cầu học tập, nghiên cứu quốc tế.
  - Những người cần công cụ hỗ trợ dịch thuật để hiểu và tham gia thảo luận trong các hội thảo, khóa học trực tuyến và các sự kiện quốc tế khác.
- Người tham gia các khóa học trực tuyến .

**Hệ thống con**:
- Chatbot hỏi đáp dựa trên văn bản trong video
- Tóm tắt văn bản trong video.

### 2.2 Phân tích yêu cầu

#### 2.2.1 Đặc tả Actors

**Actor 1. Người dùng cuối (End User)**
- Mô tả: Các cá nhân sử dụng ứng dụng để dịch giọng nói và văn bản trong các cuộc hội họp trực tuyến.
- Vai trò và trách nhiệm:
 - Sử dụng ứng dụng để chuyển đổi giọng nói thành văn bản.
 - Yêu cầu dịch văn bản từ tiếng Anh sang tiếng Việt hoặc hiển thị transcript.
 - Tương tác với hệ thống trong các cuộc họp và hội thảo trực tuyến như chat, tóm tắt nội dung cuộc họp.
- Quyền hạn:
   - Truy cập các chức năng chuyển đổi giọng nói và dịch văn bản.
   -  Truy cập vào chức năng chat và tóm tắt cuộc hội thoại.
   -  Nhận kết quả dịch thuật và lưu trữ chúng nếu cần. 
   
**Actor 2. Nhà phát triển phần mềm (Software Developer)**
- Mô tả: Nhóm lập trình viên và kỹ sư phát triển và bảo trì ứng dụng.
- Vai trò và trách nhiệm:
 - Phát triển và cập nhật các tính năng của hệ thống.
 -  Sửa lỗi và cải thiện hiệu suất của ứng dụng.
 - Đảm bảo tính tương thích và tích hợp của các công nghệ dịch thuật.
- Quyền hạn:
 - Truy cập mã nguồn và tài liệu phát triển.
 - Thực hiện các thay đổi và cập nhật cần thiết cho hệ thống.

#### 2.2.2 Đặc tả Use-cases

- **Danh sách các use-cases:**
    - UC01: Đăng nhập 
		- Mô tả: Người dùng nhập tên tài khoản và mật khẩu để truy cập vào ứng dụng. Hệ thống sẽ xác minh thông tin đăng nhập của người dùng và cấp quyền truy cập cho người dùng đã đăng nhập hợp lệ. Hiển thị thông báo lỗi nếu thông tin đăng nhập không hợp lệ.
    - UC02: Hiển thị phụ đề (Speech to text)
		 - Người dùng tải video lên hoặc quay màn hình. Hệ thống sẽ nhận dạng giọng nói và chuyển đổi thành văn bản sau đó hiển thị văn bản đã chuyển đổi trên giao diện người dùng.
	- UC03: Dịch phụ đề
		- Người dùng chọn tính ngôn ngữ muốn dịch, hệ thống sẽ dịch và hiển thị phụ đề theo ngôn ngữ người dùng mong muốn.
    - UC04: Tóm tắt hội thoại
		- Người dùng sử dụng tính năng tóm tắt.  Hệ thống sẽ phản hồi lại tóm tắt của đoạn hội thoại
	- UC05: Hỏi đáp dựa trên đoạn hội thoại
		- Người dùng sử dụng tính năng chatbot hỏi đáp.  Hệ thống sẽ sử dụng nội dung từ đoạn hội thoại để trả lời.
	- UC06: Quản lý người dùng
		- Quản trị viên tạo, sửa, xóa tài khoản người dùng. Quản trị viên phân quyền cho người dùng.

- **Use-cases theo actor:**
	- *Actor 1:*
        - UC01: đăng nhập
		- UC02: Hiển thị phụ đề 
		- UC03: Dịch phụ đề
		- UC04: Tóm tắt hội thoại
		- UC05: Hỏi đáp dựa trên đoạn hội thoại
    - *Actor 2:*
        - UC01: đăng nhập
		- UC02: Hiển thị phụ đề 
		- UC03: Dịch phụ đề
		- UC04: Tóm tắt hội thoại
		- UC05: Hỏi đáp dựa trên đoạn hội thoại
		- UC06: Quản lý người dùng