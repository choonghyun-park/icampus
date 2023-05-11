import webbrowser

while(True):
    url = input("ICAMPUS URL : ")

    url_split = url.split('"')

    src_idx = url_split.index(" src=")
    https_idx = src_idx+1
    https = url_split[https_idx]
    https_split = https.split('/')

    result = "https://lcms.skku.edu"
    for i in range(3, len(https_split)):
        result += "/"
        result += https_split[i]
    print()
    print(result)
    print()

    webbrowser.open(result)