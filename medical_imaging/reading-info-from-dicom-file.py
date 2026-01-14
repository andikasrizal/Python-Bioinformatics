import pydicom
file_path="image-00000.dcm"
file2="image-00001.dcm"
medical_image=pydicom.read_file(file_path)
mi2=pydicom.read_file(file2)
print(medical_image)
print("\n \n")
print(mi2)
