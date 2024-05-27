## 5. GHI CHÚ CÁC CÔNG VIỆC

### 5.1 Phân công

| Tên | Công việc |
|----------|----------|
| Nguyễn Văn Nam   | Backend API   |
| Dương Văn Tài    | Làm Chatbot  |
| Hoàng Tiến Anh    | Làm Extention   |
| Lê Thanh Di    | Backend Login/Logout   |


### 5.2 Nhật ký

- Tuần 18/03 - 25/03: 
    - Thực hiện
        - Thu thập và phân tích yêu cầu từ các bên liên quan: Tất cả thành viên
        - Xác định các chức năng chính và phụ của hệ thống: Tất cả thành viên
        - Lập kế hoạch chi tiết cho từng giai đoạn của dự án: Nam
    - Vấn đề
        - Chưa thống nhất được các chức năng của hệ thống.
        - Do đây là hệ thống còn mới nên các nguồn liên quan còn ít.
- Tuần 25/03 - 01/04: 
    - Thực hiện
        - Thiết kế kiến trúc giao diện Fontend: Tiến Di, Nam
        - Thiết kê kiến trúc hệ thống Backend, API: Di, Nam
        - Thiết kế cấu trúc cơ sở dữ liệu: Tiến Anh
        - Tạo prototype giao diện người dùng: Tài
    - Vấn đề
        - Chưa xác định được API hợp lý
        - Chưa định hình được cấu trúc cơ sở dữ liệu
- Tuần 01/04 - 08/04: 
    - Thực hiện
        - Tìm hiểu Docker: Tài, Nam
        - Tìm hiểu Flask và build thử API: Di, Nam
        - Học Javascrips: Tiến Anh
        - Tìm cách lấy audio từ Youtube, Zoom: Nam
    - Vấn đề
        - Chưa tìm được cách lấy audio hợp lý
        - Flask không phù hợp với yêu cầu của nhóm và thay thế bằng Django
- Tuần 08/04 - 15/04: 
    - Thực hiện
        - Tạo trang login, logout, đổi mật khẩu người dùng: Tiến Anh, Tài
        - Dựng API Speechtotext với Django: Di
        - Sửa lại sơ đồ database và check lại với sơ đồ usecase: Tiến Anh
        - Dựng database trên django: Nam
    - Vấn đề
        - Do vừa học vừa làm nên còn hơi khó với mọi người
- Tuần 15/04 - 22/04: 
    - Thực hiện
        - Code xử lý video dài khi đưa vào GPT API, subtitle : Tài
        - Sử dụng Postgres lưu âm thanh trên drive và data text lưu trên database: Di
        - Code một cái API trên js đẩy video đầu xuống backend: Tiến Anh
        - Tìm lỗi của front end, chỉ lấy được 1 cái video đầu, hỏi cộng đồng : Nam
        - Đóng gói ứng dụng bằng Docker: Nam
        - Hợp nhất trang đăng nhập đăng ký với control hiện tại: Di

    - Vấn đề
        - Làm subtitle cho video dài thì chưa xong, nhưng đã xử lý được video dài.
        - Hoàn thành ghép trang đăng ký và đăng nhập, chưa đẩy dữ liệu database lên drive.
- Tuần 22/04 - 29/04: 
    - Thực hiện
        - Tìm cách xử lý phần đăng nhập người dùng trên extension: Di, Nam
        - Xem websocket và ứng dụng nó vô speech to text stream: Di, Tiến Anh
        - Tìm cách chạy file .py trong extension: Tài
    - Vấn đề
        - Bị vướng chỗ làm sao để người dùng đăng nhập 1 lần và các lần sau ko càn đăng nhập nữa
        - Time xử lý của OPENAI quá lâu: 2.2 s
- Tuần 29/04 - 06/05: 
    - Thực hiện
        - Có bản demo chatbot dùng dữ liệu người dùng để chat (ví dụ: subtitle trên youtube): Di, Tài
        - Hoàn chỉnh phần login và gen text: Nam, Diện
        - Dùng websocket khi truyền dữ liệu qua API của Deepgram, và OpenAI chỉ dùng speech to text ko có translate: Tiến Anh
    - Vấn đề
        - Websocket chưa thử được trên Backend
        - Xây dựng được chatbot nhưng không có khả năng ghi nhớ đoạn hội thoại trước và trả lời đôi lúc nữa anh hoặc việt
- Tuần 06/05 - 13/05: 
    - Thực hiện
        - Tìm hiểu về langchain chatbot sử dụng dữ liệu đầu vào là text: Di, Tài
        - Integrate chatbot into MVP hiện tại: Nam, Tài
        - Research websocket cho API speech to text hiện tại của mình sao cho nó nhanh: Tiến Anh
        - Điều chỉnh lại phần translate sử dụng translate của google dịch cho nhanh: Tài
    - Vấn đề
        - Websocket khá chậm cho hệ thống và chưa tìm được giải pháp khắc phục.
- Tuần 13/05 - 20/05: 
    - Thực hiện
        - Thực hiện loại bỏ các tính năng, những công nghệ không có tác dụng trong hệ thống: Tiến Anh
        - Kết hợp tất cả chức năng hệ thống: Nam
        - Thực hiện kiểm thử hệ thống: Tất cả thành viên
    - Vấn đề
        - Do chưa đồng bộ được code nên khá khó khăn trong việc kết hợp lại.
        - Hệ thống còn một số lỗi và cần khắc phục.
- Tuần 20/05 - 27/05: 
    - Thực hiện
        - Khắc phục các lỗi và điều chỉnh lại hệ thống: Tất cả thành viên
        - Đánh giá lại hiệu suất và độ ổn định của hệ thống: Tất cả thành viên
        - Thực hiện viết báo cáo và tài liệu hướng dẫn người dùng: Tất cả thành viên