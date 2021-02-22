import os,glob
print(os.getcwd())
#print(os.listdir(r'data\traffic_images'))

dataset_path=r'data\traffic_images'
percentage_split=15
length=len(os.listdir(dataset_path))
# Create and/or truncate train.txt and test.txt
file_train = open('traffic_train.txt', 'w')
file_test = open('traffic_test.txt', 'w')
counter=1
index_test = round(length*(1/percentage_split))
for image in glob.glob(os.path.join(dataset_path,'*.jpg')):
    title, ext = os.path.splitext(os.path.basename(image))
    if counter >= index_test:
        file_train.write(dataset_path + "\\" + title + '.jpg' + "\n")
        counter = counter + 1
    else:
        file_test.write(dataset_path + "\\" + title + '.jpg' + "\n")
        counter = counter + 1
    
