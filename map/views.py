import json
import urllib.request
import os

from django.shortcuts import render

def search(request):
    if request.method == 'GET':
        client_id = os.environ.get('MY_CLIEND_ID') # 애플리케이션 등록시 발급 받은 값 입력
        client_secret = os.environ.get('MY_CLIEND_SECRET') # 애플리케이션 등록시 발급 받은 값 입력

        q = request.GET.get('q')
        encText = urllib.parse.quote("{}".format(q))
        url = "https://openapi.naver.com/v1/search/local?query=" + encText  # json 결과
        address_api_request = urllib.request.Request(url)
        address_api_request.add_header("X-Naver-Client-Id", client_id)
        address_api_request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(address_api_request)
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            result = json.loads(response_body.decode('utf-8'))
            items = result.get('items')
            print(result)  

            context = {
                'items': items
            }
            return render(request, 'map_search.html', context=context)