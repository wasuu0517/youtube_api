from googleapiclient.discovery import build
import json
import requests
import threading

API_KEY = 'AIzaSyBHV-3MJqrlJLMkQc9hAeqwSow2Vld8bR0' # 自分のAPIキーに置き換える

notice_name=[] #名前

notice = []#空

CHANNEL_ID = [] #id

youtube = build('youtube', 'v3', developerKey=API_KEY)
send = []#空

f = open('myfile.txt', 'a+') #file
r = open('myfile.txt', 'r', encoding='UTF-8')
a = 0
name = open('name.txt',"a+",encoding="utf-8")
name1 = open('name.txt',"r",encoding="utf-8")


def wait_for_input():
    global user_input
    user_input = input("10秒か、'y' または 'n' を入力してください: ")



while True:#チャンネルid取得
    print("追加しますか。y/n")
    id = input()
    if id == "n":
        break
    elif id == "y":
        print("チャンネルidを入力")
        date = input()
        if date == "":
            continue
        dateread = r.read()
        print(dateread.count(",") == 0)
        if dateread.count(",") == 0:
            pass
            
            
        else:
            for element in dateread.split(","):
                print(element)
                
                if element == date:
                    print(element,date)
                    print(element != date)
                    #f.write(date + ",")
                    #一致アリの場合ループ抜け出し
                    a = 1
                    break
            
        if a == 1:
            print("追加済み")
        else:
            print("追加完了")
            f.write(date + ",")
        
        continue

#txtファイルから配列への受け渡し
dateread = r.read()
for element in dateread.split(","):
    if element == "":
        a = 1
        continue 
    CHANNEL_ID.append(element)
        


namenamename = name1.read()
namename = name.read()
#配列からyoutubeapiを使い取得
for i in range(len(CHANNEL_ID)):
    request = youtube.search().list(
        part='snippet',
        channelId=CHANNEL_ID[i],
        order='date',
        type='video',
        maxResults=1
    )

    response = request.execute()#youtubeapi叩く
    print(request)
    

    if 'items' in response and response['items']:
        latest_video = response['items'][0]
        video_title = response["items"][0]["snippet"]["title"]
        live_broadcast_content = latest_video.get('snippet', {}).get('liveBroadcastContent', None)

        print(response['items'][0]['snippet']['channelTitle'])
        nametest = response['items'][0]['snippet']['channelTitle']

        
        
        b = 0
        
        print(namenamename.count(",") == 0)
        if namenamename.count(",") == 0:
            name.write(nametest+",")
            
        else:
            for element in namenamename.split(","):
                print(element)
                
                if element == nametest:
                    print(element,nametest)
                    print(element != nametest)
                    #f.write(date + ",")
                    #一致アリの場合ループ抜け出し
                    b = 1
                    
                    break
            if b == 1:
                notice_name.append(element)
                pass
            else:
                name.write(nametest + ",")
                notice_name.append(element)

        

        if live_broadcast_content == 'live':
            print("最新の動画はライブ放送中です")
            print(video_title)

            
            notice.append(video_title + "\n\n")
            notice_name.append(notice_name[i])
            
            print(*notice)
            

            
        else:
            print("最新の動画はライブ放送ではありません")

    else:
        print("最新の動画が見つかりませんでした")
now = "".join(notice)
#now_name = "".join(notice_name)

#slack
url = 'https://hooks.slack.com/services/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'
for i in range(len(notice)):
    send.append(notice_name+"\n"+video_title+"\n\n")#リスト追加
payload = {'text': now}

headers = {'Content-type': 'application/json'}#触るな

response = requests.post(url, data=json.dumps(payload), headers=headers)#触るな

