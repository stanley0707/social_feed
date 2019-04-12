"""
Не успел:
    
    1. Довести до ума исключения
Протестировать разнообразные варинты запросов
к api при часто меняющихся данных из вк
    
    2. Асинхронность
Данные, поступающие на клиент, берутся из db сразу
после того, как произойдет update некоторых постов,
число которых очень разнится. Асинхронность позволит
совершать эти процессы паралльельно облегчив отклик API
на клиенте.
    
    3. Вёрстка
Вёрстка и стилизация. Хотел успеть приятный горизонатлый
скролл фотографий и видео (если таковых больше одной в
записи). Столкнулся с запретом на отображение фотографий и
роликов на ютубе.


Проблемы в процессе:

    1. Сложность с API Twitter
Изменение в политике конфиденциальности повстречалось
и у facebook. На разбор полётов с тем, какие же использовать
api ушло больше всего времени.

    2. Вёрстка
    3. mongodb
Моё устройство и Cloud9 настойчиво отказывались запускать Mongo.
Проект запущен на Postgresql из сообажений скорости.
"""

import vk_api
import json
from django.http import JsonResponse
from django.views import View
from .models import VkUser, Post, Media # LoadSession
from django.shortcuts import render


class ApiView(View):
    """ Объект десериализации даннных из вк.
    """
    model = Post
    
    def get_video(self, _id, owner_id, access_key, session):
        """
        access_key хронится в получаемом из api
        массиве
        """
        _id = str(owner_id)+'_'+str(_id)
        
        for i in session.video.get(videos=(_id, access_key)).get('items'):
            player = i.get('player')
            return player

    
    def save_media(self, p_id, photo_url=None, video_url=None):
        """ save_media принимаем аргументами инстанс
        модели публикации и именнованные аргументы медиа ссылок.
        
        
        проверяем наличие или потребность
        обновления медиа данных поубликации
        Реализуем требуемую связь один ко многим
        пост : медиа**
        """
       
        post_instance  = Post.objects.get(postid=p_id)
        content_type = 'video'
        url = video_url
        
        if photo_url:
            content_type = 'photo'
            url = photo_url
        
        if Media.objects.filter(url=url).exists() == False:
            # !!!! внимание !!!!
            # получаемые данные довольно часто обновляются
            # чем больше подписок, тем больше новых данных,
            # поэтому методы get_or_create или update_or_create
            # вызывали слишком частые обращения к базе.
            Media.objects.create(
                        post=post_instance,
                        url=url,
                        content_type=content_type
                        )
            print('false')
        
        pass
        

    def save_post(self, post_id, date, likes, title):
        # проверяем наличие или потребность
        # обновления публикации
        
        if Post.objects.filter(postid=post_id).exists() == False:
            
            Post.objects.create(postid=post_id,
                    date=date,
                    likes=likes,
                    title=title
                    )
            print('false')
        
        pass
    
    
    
    def from_vk_save(self, data, session):
        """
        Метод принимает общий массив полученных данных и 
        сессию пользователя. Собираем записи включающие в
        себя от одной фотографии или видео.
        
        "attachments" - обеъект json включаюший в себя медиа 
        файлы, имеет обеъект "type", содержащий тип контента
        док. vk. api
        """
        for i in data.get('items'):
            
            if "attachments" in i and i.get('attachments')[0]['type'] == "photo":
                # отбираем объекты фото.
                # отделяем медеиконтент в модель Media, 
                # остальные(общие и строковые данные в 
                # модель публикации Post
                
                
                # сохраняем пост
                self.save_post(post_id=i.get('post_id'),
                                       date=i.get('date'),
                                       likes=i.get('likes').get('count'),
                                       title=i.get('text')
                                   )
                
                # сохраняем медиаданные
                self.save_media(
                    p_id=i.get('post_id'),
                    photo_url=i.get('attachments')[0].get('photo').get('sizes')[-1].get('url')
                    )
                
            if "attachments" in i and i.get('attachments')[0]['type'] == "video":
                # для получения ссылки видео необходимо
                # обратитьтся к video.get api vk.
                
                
                # вызывает метод класса get_video
                # и получаем ссылку на видео данной
                # итерации цыкла
                video_player_url = self.get_video(
                     i.get('attachments')[0].get('video').get('id'),
                     i.get('attachments')[0].get('video').get('owner_id'),
                     i.get('attachments')[0].get('video').get('access_key'),
                     session
                )    
                
                self.save_post(post_id=i.get('post_id'),
                                       date=i.get('date'),
                                       likes=i.get('likes').get('count'),
                                       title=i.get('text')
                                   )
        
                self.save_media(
                    p_id=i.get('post_id'),
                    video_url=video_player_url
                    )
                
    
    def get_vk_api(self, login, password):
        """ 
        Метод get_vk_api принимает в аргументами
        логин и пароль
        
        вызывает метод аторизации класса auth()
        передается в сессию искомые параметры
        отбора для метода vk_api newsfeed.
        
        возвращает метод класса from_vk_save
        """
        session = self.auth(login, password)
        data = session.newsfeed.get(filters='post', count=100)
        
        return self.from_vk_save(data, session)
        
    
    def auth(self, login, password):
        """ создаем экземпляр класса
        VkApi и возвращаем сессию
        """
        vk_session = vk_api.VkApi(login, password)
        vk_session.auth()
        
        return vk_session.get_api()

    def post_pagination(self, page, part, data):
        """ Если запрашиваемая страница не первая, то каждый элемент массива равен
        сумме итерируемой единицы множетсва страниц с разностью произведения суммы
        запрашиваемых объектов и номера страницы.
        
        """
        out_post = []
        composition = part * page
        
        for i in range(part):
             
            if page == 1:
                out_post.append(data[i])
            
            else:
                out_post.append(data[(composition-part)+i])
            out_post[i]['index'] = (composition-part)+i
       
        return out_post

    
    def post_serializer(self):
        """ Сериализация данных моделей
        для json в респонс на клиент.
        
        Получаем все посты и вложенные
        медиа объекты из базы и возвращаем
        список.
        """
        data = []
        
        for post in self.model.objects.all():
            media = Media.objects.filter(post=post)
            
            items = {
                    "index": 0, 
                    "id": post.id,
                    "vk_id": post.postid,
                    "type": "".join([i.get_content_type() for i in media]),
                    "media": {"url": [i.get_url() for i in media]},
                    "text": post.title,
                    "likes": post.likes,
                    "date": post.date
                }
            
            data.append(items)
            
        return data
        


class NewsLineView(ApiView):
    """ Оюъект отображения api.
    Наседуется от класса ApiView.
    
    серверную пагинация:
    Возвращает заявленное кол-во
    постов при GET <.../api/?page=<num>&part=<num>
    запросе с параметрамии page, part.
    
    page – принимает натуральные числа от единицы 
    и задает итерацию запроса – момент сессии, в
    соответствии с которой клиент соверишит выгрузку
    с n по n + part позиций списка.
    
    part – принимает натуральные числа от единцы
    и задает интервал отображения, сколько именно
    требуется вернуть записей в response
    
    """
    
    
    def get(self, request):
        """ Принимаем параметры:
        page – номер страницы
        part – сумма запращиваемх постов
            
        .../api/?page=<num>&part=<num>
        """
        
        page = request.GET.get('page')
        part = request.GET.get('part')
        
        try:
            # vk_api не требует токена юзера или приложения
            # для получения сессии пользователя требуется
            # логин и пароль вк модель VkUser. Токен сохраняется
            # в json файле в  корневом каталоге вместе с остальными
            # автиризационными данными. vk_config.v2.json
            
            # метод get_vk_api(логин, пароль) 
            
            user = VkUser.get_singl()
            data = self.get_vk_api(user.login, user.password)
            
            
            data = self.post_pagination(page=int(page), part=int(part), data=self.post_serializer())
            resp_status = {'ret': 200, 'status': 'true', "total": len(self.post_serializer())}
        
        except Exception as e:
        # ловим исключение, изменияем статусы
        # запроса и отправляем результат на клиент
            
            data = {}
            resp_status = {'msg': str(e), 'status': 'false'}
        
        return JsonResponse({
            'data': data,
            'msg' : resp_status,
        }, safe=False, json_dumps_params={'ensure_ascii':False})

