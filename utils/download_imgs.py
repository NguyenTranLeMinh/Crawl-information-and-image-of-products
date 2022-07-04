import PIL
import requests

def download_image(url, file_name):
    download_path="D:\Funix\DEP302x_GioiThieu_Kythuat_DuLieu\Phan_4_Web_scrapping\websosanh\downloaded_imgs"
    try:
        image_content = requests.get(url).content
        path = download_path + '\\' + file_name.translate(str.maketrans('', '', '/\:*?|"<>'))
        with open(path + '.png', 'wb') as f:
            f.write(image_content)
    except Exception as e:
        print(f'Download_image {url} FAILED -', e)