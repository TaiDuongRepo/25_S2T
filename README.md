# Tên ứng dụng

- Mô tả vắn tắt tên ứng dụng ở đây (Gợi ý: ứng dụng giải quyết vấn đề gì, có các đối tượng người dùng như thế nào, có các chức năng gì...)

- Bạn có thể trải nghiệm ứng dụng ở đây [LINK](https://update-this-link)
- Một số sceenshot của ứng dụng
# Nhóm 2: Xây dựng trang web và extension cho text to speech transcript và translation

- Mô tả vắn tắt tên ứng dụng ở đây (Gợi ý: ứng dụng giải quyết vấn đề gì, có các đối tượng người dùng như thế nào, có các chức năng gì...)

- Bạn có thể trải nghiệm ứng dụng ở đây [LINK](https://update-this-link)
- Một số sceenshot của ứng dụng

Trong quá trình học tập thì lượng kiến thức, khóa học trực tuyến thường là những khóa học bằng tiếng Anh. Cho nên việc tiếp cận các kiến thức đang bị rào cản bởi ngoại ngữ. Để tăng cường hiệu suất học tập, làm việc thì nhóm nảy ra ý tưởng để vượt qua rào cản đó bằng việc phát triển tiện ích hỗ trợ tạo phụ đề cho video (speech to text) và dịch phụ đề (translate) cho tiếng Việt.

**Phạm vi dự án**

Trang Web: 
- Chức năng và tải lên tệp video, âm thanh để có thể tạo ra phụ đề
- Chức năng đăng nhập, đăng ký tài khoản
- Xác thực token accept ở cho extension
  
Extension:
- Hỗ trợ ghi hình trực tiếp và hiện thị phụ đề theo thời gian thực, hỗ trợ đa nền tảng, cả ngoài trình duyệt
- Chức năng phụ đề từ giọng nói và dịch thành tiếng việt theo thời gian thực.
- Tóm tắt cuộc hội thoại.
- Chatbot trực tiếp trong quá trình tham gia cuộc hội thoại với khả năng đưa ra kết quả tốt hơn so với việc chat riêng lẻ do sử dụng dữ liệu từ cuộc hội thoại.

## CÀI ĐẶT

### Hướng dẫn cài đặt và chạy Backend

Dưới đây là các bước cài đặt và chạy dự án Backend. Hãy chắc chắn rằng bạn đã cài đặt Python và `ffmpeg` trên máy của bạn trước khi bắt đầu. Nếu không hãy làm theo hướng dẫn sau để cài đặt https://phoenixnap.com/kb/ffmpeg-windows
Hãy kiểm tra version của ffmpeg: 
![image](https://github.com/TaiDuongRepo/25_S2T/assets/97231719/84cac1b4-ffa5-4fcd-b000-5f39ad22a068)
**Nếu không hiện giống format đó thì nghĩa là bạn chưa cài ffmpeg

**Bước 1: Clone dự án**

Mở terminal hoặc command prompt và chạy lệnh sau để clone dự án:

```
git clone https://github.com/TaiDuongRepo/25_S2T/tree/main
```

**Bước 2: Tạo môi trường ảo**

Chuyển đến thư mục `Backend` vừa clone:

```
cd ./25_S2T/src/Backend
```

Tạo một môi trường ảo bằng cách sử dụng Python:

```
python -m venv .venv
```

**Bước 3: Kích hoạt môi trường ảo và cài đặt các thư viện cần thiết**

Đối với Windows, kích hoạt môi trường ảo:

```
.venv\Scripts\activate
```

Sau đó, cài đặt các thư viện cần thiết từ `requirements.txt`:

```
pip install -r requirements.txt
```

**Bước 4: Cài đặt thư viện bổ sung**

Chạy các lệnh sau để cài đặt các thư viện bổ sung:

```
pip install openai==1.13.3
pip install djangorestframework-simplejwt==5.3.1
pip install pydub==0.25.1
pip install psycopg2==2.9.9
pip install djangorestframework==3.14.0
pip install django-cors-headers==4.3.1
pip install google-auth==2.28.1
pip install private-django-googledrive-storage==1.6.0
pip install google-auth-oauthlib==1.2.0
pip install google-auth-httplib2==0.2.0
pip install google-api-python-client==2.120.0
pip install google-api-core==2.10.2
```

**Bước 5: Chạy máy chủ**

Trước khi chạy máy chủ, hãy đảm bảo rằng bạn đã cài đặt `ffmpeg` và thêm nó vào biến môi trường (path environment variable) của hệ thống. Khởi động lại máy của bạn nếu chưa có `ffmpeg`.

Chạy máy chủ bằng cách sử dụng lệnh:

```
python manage.py runserver
```

Bây giờ, bạn có thể truy cập máy chủ thông qua địa chỉ mặc định: `http://127.0.0.1:8000/`.

**Sử dụng dùng Postman để test API**

Login tài khoản: 
- Tên: test1
- MK: 123
- Sử dụng audio.webm trên folder ./Data/
F12 vào phần Application phía dưới có Local storage click vào `http://127.0.0.1:8000/` và copy đoạn token
  i
![image](https://github.com/Research-Product-Lab/Backend/assets/97231719/c844aa03-cb25-4c25-aefe-61b7c2d108c5)

Và dữ liệu được chuyền dưới dạng .webm 
![image](https://github.com/Research-Product-Lab/Backend/assets/97231719/ac69a57e-4413-4ca0-90b4-bfa24edfba99)
### Hướng dẫn cài đặt extension PASO

Truy cập vào link: chrome://extensions/

Bật chế độ developer: 

![image](https://github.com/TaiDuongRepo/25_S2T/assets/97231719/20028ca6-81d3-4a09-ab15-1d2ad9e578b5)

Chọn Upload unpacked:

![image](https://github.com/TaiDuongRepo/25_S2T/assets/97231719/7b958eaf-9461-403d-b9a0-019fe24dd761)

Chọn folder extension:

![image](https://github.com/TaiDuongRepo/25_S2T/assets/97231719/c4c05cd4-252d-4545-9eeb-6a0ed5c3f73d)

Load lại trang web và sử dụng ứng dụng MVP
## THÔNG TIN THÀNH VIÊN

- Nguyễn Văn Nam - 21017711
- Hoàng Tiến Anh - 21068521
- Lê Thanh Di - 21018401
- Dương Văn Tài - msv

## TRÁCH NHIỆM

- Nguyễn Văn Nam:
    - Nhóm trưởng
    - Phân công nhiệm vụ
    - Phụ trách hỗ trợ phát triển extension và backend
- Dương Văn Tài
    - Thiết kế database 
    - Nghiên cứu phát triển chatbot RAG 
- Hoàng Tiến Anh
    - Nghiên cứu sử dụng websocket vào dự án
    - Nghiên cứu các giải pháp lấy audio trên trình duyệt và code extension
    - Tìm các nguồn API speech to text theo yêu cầu của dự án
        - Deepgrame
        - OpenAi
          
        Nhóm đã chọn OpenAI vì độ chính xác cao, thành vì tốc độ.
      
- Lê Thanh Di
    - Code chính Backend theo thiết kế.
    - Nghiên cứu phát triển chatbot RAG.
    

  


---

## CÀI ĐẶT

Hướng dẫn cài đặt và chạy sau khi pull project từ github về (Lưu ý: hướng dẫn phải chạy được). Bao gồm:
- Các phần mềm cần cài đặt
- Các gói thư viện python cần dùng (có thể sử dụng pip freeze để tạo)
- Script tạo database (Để script trong thư mục installation)
- Script tạo dữ liệu (Để script trong thư mục installation)

## THÔNG TIN THÀNH VIÊN

- Nguyễn Văn Nam - msv
- Họ tên sv 2 - msv
- Họ tên sv 3 - msv
- Họ tên sv 4 - msv

## TRÁCH NHIỆM

- Thành viên 1:
    - trách nhiệm 1
    - trách nhiệm 2
- Thành viên 2
    - trách nhiệm 1
    - trách nhiệm 2
- ...


---
