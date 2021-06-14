from django.http import HttpResponse
from django.views.generic import TemplateView

# ・function based view
# 自分で設定することが多い。
# 細かく機能を設定できる。
def helloworldfunction(request):
    returnedobject = HttpResponse('<h1>hello world</h1>')
    return returnedobject


# ・class based view
# 自動である程度の機能が備わっている
# 身を変更しにくい
# システムキッチン
class HelloworldClass(TemplateView):
    # ・template_name
    # 設定必須項目
    # 呼び出したときにとってくるHTMLファイル。
    # settings.pyのTEMPLATESのDIRSにHTMLファイルを入れるディレクトリのパスを記載しておく。
    # DIRSは[BASE_DIR / 'templates']とするのが一般的。
    template_name = 'hello.html'