file1=open('C:\\Users\\86156\\Desktop\\text\\xxx.txt','r',encoding='utf-8')
fi=file1.readlines()
file1.close()
end=[]
for i in fi:
    data=i.split()
    sum=0
    for num in data[1:]:
        sum=sum+int(num)
    result=data[0]+str(sum)+'\n'
    print(result)
    end.append(result)
file2=open('C:\\Users\\86156\\Desktop\\text\\xxy.txt','w',encoding='utf-8')
file2.writelines(end)
file2.close()