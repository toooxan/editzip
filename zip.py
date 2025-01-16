import zipfile
import shutil

zip_path = 'feed.zip'

temp_zip_path = 'temp_archive.zip'

file_name = 'task.yaml'

with zipfile.ZipFile(zip_path, 'r') as zip_file:
    with zipfile.ZipFile(temp_zip_path, 'w') as temp_zip:
        for item in zip_file.infolist():
            if item.filename == file_name:
                content = zip_file.read(file_name).decode('utf-8')
                updated_content = content.replace('period: full', 'period: half_1')
                temp_zip.writestr(file_name, updated_content)
            else:
                temp_zip.writestr(item, zip_file.read(item.filename))

shutil.move(temp_zip_path, zip_path)

print("File updated successfully!")
