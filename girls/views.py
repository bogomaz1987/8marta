from django.db.utils import IntegrityError
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from girls.models import Girls, Gifts, Wishes

WISH_COUNT = 3

def get_girl(request):
    girl = Girls.objects.filter(code=request.session.get('girl')).first()
    if girl:
        return girl
    return False


class Login(TemplateView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        if get_girl(request):
            return redirect('/main/')
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        girl = Girls.objects.filter(code=request.POST.get('code')).first()
        if girl:
            request.session['girl'] = girl.code
            return redirect('/main/')
        return render(request, self.template_name, {'message': 'Неверный уникальный код'})


class Spisok(TemplateView):
    template_name = 'main.html'

    def get(self, request, *args, **kwargs):
        girl = get_girl(request)
        if girl:
            return render(
                request,
                self.template_name,
                {
                    'gifts': Gifts.objects.all(),
                    'girl': girl.fio
                }
            )
        else:
            return redirect('/')

    def post(self, request, *args, **kwargs):
        girl = get_girl(request)
        if girl:
            message = 'Заявка подана. Ждите.. скоро Ваше желание осуществится'

            if Wishes.objects.filter(girl=girl).count() >= WISH_COUNT:
                message = 'К сожалению, лимит желаний исчерпан...'
            else:
                try:
                    Wishes.objects.create(girl=girl, gift_id=request.POST.get('gifts'))
                except IntegrityError:
                    message = 'К сожалению, это желание уже было... Пожалуйста, выбери другое'

            return render(
                request,
                self.template_name,
                {
                    'gifts': Gifts.objects.all(),
                    'girl': girl.fio,
                    'message': message
                }
            )
        else:
            return redirect('/')


class Logout(TemplateView):
    def get(self, request, *args, **kwargs):
        request.session.flush()
        return redirect('/')
