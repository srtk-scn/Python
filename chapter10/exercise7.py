#find the links in the html file and extract the link in some another text file if only one link in one line

# with open('link_with_exercise7.html','r') as rf:
#     with open('htmltextexercise7.txt','a') as wf:
#         for line in rf.readlines():
#             if '<a href=' in line:
#                 pos=line.find('<a href=')
#                 first_quote=line.find('\"',prfos)
#                 second_quote=line.find('\"',first_quote+1)
#                 url=line[first_quote+1:second_quote]
#                 wf.write(url + '\n')



#find the links in the html file and extract the link in some another text file if more than one link in one line


with open('link_with_exercise7.html','r') as rf:
    with open('execise7.txt','a') as wf:
        page=rf.read()
        link_exist=True
        while link_exist:
            pos=page.find('<a href=')
            if pos==-1:
                link_exist=False
            else:
                first_quote=page.find('\"',pos)
                second_quote=page.find('\"',first_quote+1)
                url=page[first_quote+1:second_quote]
                wf.write(url+'\n')
                page=page[second_quote:]

