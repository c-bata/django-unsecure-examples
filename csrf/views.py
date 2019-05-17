from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import Template, Context
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from csrf.models import Comment

_comment_list_template = """<html>
<body>
    <ul>
        {% for c in comments %}
        <li>{{ c.posted_by }} {{ c.content }}</li>
        {% endfor %}
    </ul>
    
    <form method="post">
        <input type="text" name="content" value="">
        <button type="submit">投稿</button>
    </form>
</body>
</html>
"""


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class CsrfView(View):
    def get(self, request):
        comments = Comment.objects.all()
        html = Template(_comment_list_template).render(Context({"comments": comments}))
        return HttpResponse(html)

    def post(self, request):
        comment = Comment(content=request.POST['content'], posted_by=request.user)
        comment.save()
        return redirect(reverse('csrf'))
