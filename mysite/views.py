from django.views.generic.base import TemplateView
from django.apps import apps

class HomeView(TemplateView):

    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['app_list'] = ['polls', 'books']
        dictVerbose = {}
        # apps.get_app_configs[] 메소드를 호출하면, 
        # settings.py 파일의 INSTALLED_APPS에 등록된 각 앱의 설정 클래스들을 담은 리스트를 반환
        for app in apps.get_app_configs():
            # site-packages 문자열이 들어있으면 외부 라이브러리 앱을 의미하므로 제외
            if 'site-packages' not in app.path:
                print('lavel: ' + app.label)
                print('verbose_name: ' + app.verbose_name)
                dictVerbose[app.label] = app.verbose_name
                
        context['verbose_dict'] = dictVerbose
        return context