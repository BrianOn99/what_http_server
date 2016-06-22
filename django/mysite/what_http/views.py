from django.shortcuts import render
from what_http.lib import httphead
from what_http.models import AskedUrl

def index(request):
    context = {};
    context["past_url_records"] = AskedUrl.objects.all()
    asked_url = request.GET.get("url", None)

    if (asked_url):
        context["asked_url"] = asked_url
        try:
            context["result_server"] = httphead.find_server(asked_url) or "unknown"
        except (IOError, ValueError):
            context["http_error"] = True
        else:
            print("saving record");
            AskedUrl.objects.create(url=asked_url);
            print(AskedUrl.objects.all())

    return render(request, "index.html", context)
