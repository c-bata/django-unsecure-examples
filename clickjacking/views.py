from django.http import HttpResponse
from django.template import Template, Context

_delete_account_template = """<html>
<head>
    <title>アカウントを削除しますか？</title>
</head>
<body style="margin: 0; padding: 0;">
    <button style="width: 200px; height: 50px;" onClick="deleteAccount()">アカウントを削除する</button>

    <script>
    function deleteAccount() {
        alert("アカウントの削除が完了しました。");
    }
    </script>
</body>
</html>
"""


def click_jacking_view(request):
    html = Template(_delete_account_template).render(Context())
    return HttpResponse(html)
