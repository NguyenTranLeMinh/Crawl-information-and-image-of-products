import PIL
import requests

def download_image(url, file_name):
    download_path="D:\\Funix\\DEP302x_GioiThieu_Kythuat_DuLieu\\Phan_4_Web_scrapping\\shopee_crawl\\downloaded_imgs\\"
    try:
        image_content = requests.get(url).content
        # image_file = io.BytesIO(image_content)
        # image = Image.open(image_file)
        path = download_path + file_name
        with open(path + '.png', 'wb') as f:
            f.write(image_content)
    except Exception as e:
        print(f'Download_image {url} FAILED -', e)