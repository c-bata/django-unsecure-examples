from django.http import HttpResponse


_form_html = """<form method="get">
   <input type="text" name="q" placeholder="Search" value="">
   <button type="submit">Go</button>
</form>
"""


def xss_view(request):
    if 'q' in request.GET:
        return HttpResponse(f"Searched for: {request.GET['q']}")
    else:
        return HttpResponse(_form_html)
