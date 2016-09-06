    import  requests
    
    lst = []
    url = "http://movie.douban.com/top250"
    res = requests.get(url)
    #requests.get(url) ...refer to client2.py
    print('log response object\n',res)
    
    data = res.content
    lst = data.split(',')
    print('log lst\n',lst)
