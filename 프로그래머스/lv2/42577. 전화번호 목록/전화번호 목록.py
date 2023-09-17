def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(1,len(phone_book)):
        j=i-1
        arr=phone_book[i].split(phone_book[j])
        if(arr[0]==''):
            answer=False
    return answer