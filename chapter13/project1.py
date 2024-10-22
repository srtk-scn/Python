import os, shutil


#note: you have to write single extentions inside tuples
# dict_extentions={
# "audio_extentions":('.mp3','.m4a','.wav','.flac'),
# "video_extentions":('.mp4','.mkv','.MKV','.flv','.mpeg'),
# "document_extentions":('.doc','.pdf','.txt')
# }
#
# folder_path=input('enter folder path :')
#
# def file_finder(folder_path,file_extentions):
#     files=[]
#     for file in os.listdir(folder_path):
#         for extention in file_extentions:
#             if file.endswith(extention):
#                 files.append(file)
#     return files
# # print(file_finder(folder_path,document_extentions))
# for extention_type,extention_tuple in dict_extentions.items():
#     print(f'calling file finder function for { extention_type}')
#     print(file_finder(folder_path,extention_tuple))


#-------------------------------------------------------------------------------------------------------------------
# dict_extentions={
# "audio_extentions":('.mp3','.m4a','.wav','.flac'),
# "video_extentions":('.mp4','.mkv','.MKV','.flv','.mpeg'),
# "document_extentions":('.doc','.pdf','.txt')
# }

# folderpath=input('enter folder path :')
#
#
# def file_finder(folderpath,file_extentions):
#     # files=[]
#     # for file in os.listdir(folderpath):
#     #     for extention in file_extentions:
#     #         if file.endswith(extention):
#     #             files.append(file)
#     # return files
#     return [file for file in os.listdir(folderpath) for extentions in file_extentions if file.endswith(extentions)]
# for extention_type,extention_tuple in dict_extentions.items():
#     folder_name=extention_type.split('_')[0] + "file"
#     folder_path=os.path.join(folderpath,folder_name)
#     os.mkdir(folder_path)
#     for item in (file_finder(folderpath,extention_tuple)):
#         item_old_path=os.path.join(folderpath,item)
#         item_new_path=os.path.join(folder_path,item)
#         shutil.move(item_old_path,item_new_path)
#         print(item)
#---------------------------------------------------------------------------------------------------------------------



dict_extentions={
"audio_extentions":('.mp3','.m4a','.wav','.flac'),
"video_extentions":('.mp4','.mkv','.MKV','.flv','.mpeg'),
"document_extentions":('.doc','.pdf','.txt')
}
folderpath=input('enter folder path :')


def file_finder(folderpath,file_extentions):
    files=[]
    for file in os.listdir(folderpath):
        for extention in file_extentions:
            if file.endswith(extention):
                files.append(file)
    return files
    # return [file for file in os.listdir(folderpath) for extentions in file_extentions if file.endswith(extentions)]
for extention_type,extention_tuple in dict_extentions.items():
    folder_name=extention_type.split('_')[0] + "file"
    folder_path=os.path.join(folderpath,folder_name)
    os.mkdir(folder_path)
    for item in (file_finder(folderpath,extention_tuple)):
        item_old_path=os.path.join(folderpath,item)
        item_new_path=os.path.join(folder_path,item)
        shutil.move(item_old_path,item_new_path)
