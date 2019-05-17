from django.http import HttpResponse
from django.template import Template, Context

from sqlinjection.models import Snippet

_snippet_list_template = """<html>
<body>
    <ul>
        {% for s in snippet %}
        <li>{{ s.title }}</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

_form_html = """<form method="get">
   <input type="text" name="snippet" placeholder="Snippet id" value="">
   <button type="submit">Go</button>
</form>
"""


def sql_injection(request):
    if 'snippet' not in request.GET:
        html = Template(_form_html).render(Context())
    else:
        snippet_id = request.GET['snippet']
        sql = "SELECT id, title FROM snippets WHERE id = '{}';".format(snippet_id)
        snippet = Snippet.objects.raw(sql)
        html = Template(_snippet_list_template).render(Context({'snippet': snippet}))
    return HttpResponse(html)
