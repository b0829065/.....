from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Post


from django.http import JsonResponse
from django.shortcuts import render



def test_view(request):
    data = {
        'name':'pan',
        'age':23,
    }
    return JsonResponse(data)

def TW2330(request):
    data = {
        'name':"台積電",
        'detail':"台積電成立於1987年2月21日，是全球第一家也是全球最大的專業積體電路(IC)製造服務公司",
    }
    return JsonResponse(data)

def TW2454(request):
    data = {
        'name':"聯發科",
        'detail':"聯發科技股份有限公司(2454.TW)成立於1997年5月28日，早期為聯電集團轉投資之半導體晶片設計公司，是無線通訊及數位媒體晶片整合系統方案之主要供應商，排名全球前十大半導體晶片廠",
    }
    return JsonResponse(data)

def TW2303(request):
    data = {
        'name':"聯電",
        'detail':
            "聯電成立於1980年五月二十二日，為國內第一家上市的半導體公司，台灣僅次於台積電之晶圓專業代工公司。"
            "公司發展策略不同於台積電，以晶圓製造服務為後盾，轉投資諸多半導體晶片設計公司，以自有產能及技術扶植半導體晶片設計公司，而當半導體晶片設計公司之產品在市場中具競爭優勢取得需求量時，亦回饋公司，得以維持晶圓代工產能利用率，兩者相輔相成。",
    }
    return JsonResponse(data)

def TW2881(request):
    data = {
        'name':"富邦金",
        'detail':
            "富邦金(2881)成立於1961年，前身為富邦保險，2001年富邦金以股權讓與方式納入富邦產物保險股份有限公司，並以股權轉換方式併入富邦綜合證券股份有限公司、富邦商業銀行股份有限公司、及富邦人壽保險股份有限公司。同年年底富邦金控掛牌上市，為台灣第一家上市的金融控股公司。"
    }
    return JsonResponse(data)