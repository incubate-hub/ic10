from django.shortcuts import render
from . import ml_predict

def home(request):
    return render(request, 'index.html')

def result(request):
    loc = request.GET["loc"]
    v = request.GET["v"]
    ev = request.GET["ev"]
    iv = request.GET["iv"]
    n = request.GET["n"]
    v1 = request.GET["v1"]
    l = request.GET["l"]
    d = request.GET["d"]
    i = request.GET["i"]
    e = request.GET["e"]
    b = request.GET["b"]
    t = request.GET["t"]
    loCode_numeric = request.GET["loCode_numeric"]
    loComment_numeric = request.GET["loComment_numeric"]
    loBlank_numeric = request.GET["loBlank_numeric"]
    locCodeAndComment_numeric = request.GET["locCodeAndComment_numeric"]
    prediction = ml_predict.prediction_model(
        loc, v, ev, iv, n, v1, l, d, i, e, b, t, loCode_numeric, loComment_numeric, loBlank_numeric, locCodeAndComment_numeric)
    return render(request, 'result.html',{'prediction': prediction})