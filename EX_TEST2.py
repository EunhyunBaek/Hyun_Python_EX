def BOOKSTORE():
    BookList = []

    BookList.append({"제목":"python",            "출판사":"비트","책페이지":510,"추천도서":"T"})
    BookList.append({"제목":"MachineLearing",   "출판사":"한국","책페이지":380,"추천도서":"T"})
    BookList.append({"제목":"java",               "출판사":"비트","책페이지":400,"추천도서":"T"})
    BookList.append({"제목":"DeepLearning",      "출판사":"한국","책페이지":600,"추천도서":"T"})
    BookList.append({"제목":"IOT",                "출판사":"한국","책페이지":550,"추천도서":"T"})

    for b in BookList:
        print(b)

    UpperPage=list()
    Recommend=list()
    WriteCompList=set()
    TotalPage=int()
    for(b) in BookList:
       WriteCompList.add(b["출판사"])
       TotalPage+=b['책페이지']
       if b['책페이지']>500:
           UpperPage.append(b["제목"])
       if b['추천도서']=="T":
            Recommend.append(b["제목"])

    print("페이지 500 이상:%s"%UpperPage)
    print("내가 추천하는 책:%s"%Recommend)
    print("총 페이지:%s"%TotalPage)
    print("출판사 목록:%s"%WriteCompList)


