#-*-coding:utf-8-*-
import requests
import re
import time
# def get1(pn):#now52872
#     url1="http://news.meishujia.cn/?act=app&appid=4096&mid=%d&p=view" %pn
#     html = requests.get(url1)
#     html.encoding = 'gbk'
#     h1=html.text
#     #print(h1)
#     reg = r'<li class="nw_liebi"><span>(.*?)</span><em>■</em><A HREF="(.*?)" target=_blank>(.*?)</A></li>'#取出内页
#     time,url,title= re.findall(reg,h1)
#     return time,url,title

# def get_start():
#     url1="http://news.meishujia.cn/index.php?page=1&act=app&appid=4096&fenlei=57"
#     html = requests.get(url1)
#
#     #html.encoding = 'gbk'
#     h1=html.text
#     reg = r'<li class="nw_liebi"><span>.*?</span><em>■</em><A HREF="(.*?)" target=_blank>.*?</A></li>'  # 取出内页
#     url = re.findall(reg, h1)
#     return  url
    #print(h1)
    #reg = r'<dd><strong><a href="(.*?)">'#取出内页
    #rstart= re.findall(reg,h1)



#s=requests.session()

payload = {
    '__EVENTTARGET': '',
    '__EVENTARGUMENT': '',
    '__VIEWSTATE': ' / wEPDwUKMjA0B1Lb25tb3VzZW92ZXIFGHRoaXMuc3R5bGUuY3Vyc29yPSdoYW5kJ2Rk9DkYht + mJC9S1QWFSb7blw + VyAU =',
    #VIEWSTATE是asp.net网站的验证
    '__VIEWSTATEGENERATOR': '82312306',
    'UserName': '***',#用户名
    'UserPass': '***',#密码
    'ImageButton1': '登录'
}

pp = {
    '__EVENTTARGET': '',
    '__EVENTARGUMENT': '',
    '__VIEWSTATE': '/ lTGltaXQoKWRkZAItD2QWAmYPD2QWAh8TBRNyZXR1cm4oQ2hlY2tGb3JtKCkpZGRYYL1NKmWiBj9FxQ7eanRNTDBmGg ==',
    #上传时服务器需要一串非常长的参数，这里经过大部分的裁剪
    '__VIEWSTATEGENERATOR': 'EC691A77',
    'PreTitle': '',
    'Title': 'hahah',
    'TitleFontColor': '',
    'RefreshTF': '1',
    'ShowOn3G': '1',
    'Attribute7': '1',
    'm0': '1128',
    'm1128': '1151',
    'm1151': '1153',
    'ClassID': '1152',
    'Author': ',',
    'SelAuthor': '',
    'AddDate': '2017/4/18 22:01:16',
    'autointro': '1',
    'Intro': '',
    'AttachmentCharge': '0',
    'AttachmentChargeOnce': '1',
    'Content': '',
    'PageTitle': '',
    'DefaultPic': '',
    '首页缩略图1380x460': '',
    'Hits': '0',
    'Inputer': '',
    'leibie': '',
    'xuezhi': '',
    'beizhu': '',
    'ctl00$KSContent$TxtInputer': 'sxfu_ysgc',
    'ctl00$KSContent$Verify': '1',
    'templateflag': '2',
    'ctl00$KSContent$TemplateFile': '',
    'ctl00$KSContent$Template3GFile': '',
    'filetype': '0',
    'ctl00$KSContent$FileName': '',
    'ctl00$KSContent$HidFileName': '',
    'ctl00$KSContent$TxtSeoTitle': '',
    'ctl00$KSContent$TxtSeoKeyWords': '',
    'ctl00$KSContent$TxtSeoDescription': '',
    'ctl00$KSContent$InfoPurview': '0',
    'ctl00$KSContent$ReadPoint': '0',
    'ctl00$KSContent$ChargeType': '0',
    'PitchTime': '12',
    'ReadTimes': '10',
    'ctl00$KSContent$DividePercent': '0',
    'ctl00$KSContent$Subject': '',
    'ctl00$KSContent$VoteType': '1',
    'vote_num': '1',
    'editnum': '8',
    'itemid': '0',
    'item': '',
    'votenum': '0',
    'itemid': '0',
    'item': '',
    'votenum': '0',
    'itemid': '0',
    'item': '',
    'votenum': '0',
    'itemid': '0',
    'item': '',
    'votenum': '0',
    'itemid': '0',
    'item': '',
    'votenum': '0',
    'itemid': '0',
    'item': '',
    'votenum': '0',
    'itemid': '0',
    'item': '',
    'votenum': '0',
    'itemid': '0',
    'item': '',
    'votenum': '0',
    'ctl00$KSContent$BeginDate': '2017/4/18 22:01:16',
    'ctl00$KSContent$ExpireDate': '2017/4/18 22:01:16',
    'ctl00$KSContent$UserTF': '1',
    'ctl00$KSContent$LimitIP': '1',
    'ctl00$KSContent$hidVoteID': '0',
    'ctl00$KSContent$hidPKID': '0',
    'ctl00$KSContent$TxtPkTitle': '',
    'ctl00$KSContent$TxtPKZFGD': '',
    'ctl00$KSContent$TxtPKFFGD': '',
    'ctl00$KSContent$TxtPKZFVotes': '0',
    'ctl00$KSContent$TxtPKFFVotes': '0',
    'ctl00$KSContent$TxtPKSFVotes': '0',
    'ctl00$KSContent$RdbPKUserTF': '1',
    'ctl00$KSContent$RdbPKOnceTF': '0',
    'ctl00$KSContent$RdbPKVerifyTF': '0',
    'ctl00$KSContent$RdbPKStatus': '1',
    'ctl00$KSContent$RdbPKTimeLimit': '0',
    'ctl00$KSContent$TxtPKTBeginDate': '2017/4/18 22:01:15',
    'ctl00$KSContent$TxtPKTEndDate': '2017/5/18 22:01:15',
    'ctl00$KSContent$Foot1$submitbutton': '确定保存(O)',
    'ctl00$KSContent$Foot1$ID': '0'

}

cookies1={
    'Cookie':''#登陆时的cookies
}

def get2(pn):#内页爬取
    url1='http://news.meishujia.cn/?act=app&appid=4115&mid=%d&p=view'%pn#原创新闻
    #url1 = "http://news.meishujia.cn/?act=app&appid=4096&mid=%d&p=view" % pn#综合类
    html1=requests.get(url1)
    html1.encoding = 'gbk'      #网页编码定义
    h2=html1.text


    reg2=r'<h1>(.*?)</h1>'       #取出标题
    title = re.findall(reg2, h2)


    reg2 = r'src="(.*?).jpg"'  # 取出标题
    photourl = re.findall(reg2, h2)



    reg2=r'''<ul class="nw_r_b nw_r_bt">
(.*?)<ul class="nw_r_ed">'''
    reg2 = re.compile(reg2, re.S)#re.S可匹配多行#编译正则表达式
    body = re.findall(reg2, h2)
    return url1,title,body,photourl

def login(payload):
    url1='http://www.***.org/guanli/login.aspx'
    html1 = requests.post(url1,data=payload)

    headers1=html1.headers
    cookies=html1.cookies
    return  headers1

def fabu(pp,cookies1):
    #url1 = 'http://www.***.org/guanli/Content/ks.content.aspx?Action=Add&Channelid=1'
    url1 = 'http://www.***.org/guanli/Content/KS.Content.aspx?ChannelID=1&Action=Add&ClassID=1153'
    response = requests.post(url1,cookies=cookies1,data=pp,)
    returen_page=response.text
    return returen_page


if __name__=='__main__':
    #loginpage=login(payload)#登陆首页，本来想爬取cookies但是爬不到


    for i in range(3326, 3329):
        print('正在爬取编号%d文章'%i)
        url1, title, body,photostart = get2(i)
        # photourl=photostart[1]+'.jpg'
        # print(type(body))   #list
        # print(url1)
        # print(title)
        # print(body)
        # print(photourl)
        # # 'DefaultPic': '',  #缩略图
        # print('正在发布编号%d文章' % i)
        # pp['Title'] = title         #标题
        # pp['Content'] = body        #正文
        # pp['AddDate'] = '2017/4/18 22:01:16'
        # pp['DefaultPic']=photourl
        # #fabu(pp, cookies1)
        # print('发布完毕')
        # time.sleep(1)
        # break

        if len(title)!=0:
            if len(body)!=0:
                #print(type(body))   #list
                print(url1)
                print(title)
                print(body)
                #'DefaultPic': '',  #缩略图
                print('正在发布编号%d文章'%i)
                pp['Title']=title
                pp['Content']=body
                pp['AddDate']='2017/4/18 22:01:16'
                fabu(pp, cookies1)
                print('发布完毕')
                time.sleep(1)

            else:
                print('文章内容抓取失败')
                print(url1)
                print(title)
                continue
            #break
        else:
            print('标题抓取失败')
            print(url1)
            continue






