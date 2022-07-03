Sử dụng Scrapy để cào thông tin về sản phẩm tại [trang](https://websosanh.vn/dan-organ/cat-2022.htm) và tải ảnh xuống. Kết hợp Splash để nhảy sang trang mới.

Thông tin cào về được lưu trong tệp output.json.

Splash được chạy trên docker với cổng 8050.

Lưu ý: Nếu dùng Window như mình và thiếu chỗ trống trong ổ C, làm theo [link](https://blog.codetitans.pl/post/howto-docker-over-wsl2-location/) để chuyển nơi chứa các Images trong Docker Desktop sang ổ đĩa khác.

Cú pháp:

Tại thư mục chứa scrapy.cfg, chạy lệnh sau:

scrapy crawl shopee -o output.json


Note: $(<css selector>), $x(<xpath selector>) có thể test selector trên Thẻ console của web.
