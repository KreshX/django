from django.contrib import admin
from django.contrib.auth.models import User
from .models import Movie, Director, Actor
from django.db.models import QuerySet

class RatingFilter(admin.SimpleListFilter):
	title = 'Фильтр по рейтингу'
	parameter_name = 'rating'

	def lookups(self, request, model_admin):
		return [
			('<40', 'Низкий'),
			('от 40 до 59', 'Средний'),
			('от 60 до 79', 'Высокий'),
			('>=80', 'Высочайший'),
		]

	def queryset(self, request, queryset:QuerySet):
		if self.value()=='<40':
			return queryset.filter(rating__lt=40)
		if self.value()=='от 40 до 59':
			return queryset.filter(rating__gte=40).filter(rating__lt=60)
		if self.value()=='от 60 до 79':
			return queryset.filter(rating__gte=60).filter(rating__lt=80)
		if self.value()=='>=80':
			return queryset.filter(rating__gte=80)
		return queryset

# admin.site.register(Director)
# admin.site.register(Actor)

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug' : ('first_name', 'last_name',)}
	list_display = ['first_name', 'last_name', 'slug']

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug' : ('first_name', 'last_name',)}
	list_display = ['first_name', 'last_name', 'slug']

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
	list_display = ['name','rating','currency','budget','director', 'rating_status']
	list_editable = [ 'rating','currency','budget','director']
	ordering = ['-rating']
	list_per_page = 10
	actions = ['set_dollars']
	search_fields = ['name']
	list_filter= ['name', RatingFilter]
	prepopulated_fields = {'slug' : ('name', )}
	filter_horizontal = ['actors']


	@admin.display(description='Оценка')  #ordering='rating'
	def rating_status(self, mov: Movie):
		if mov.rating < 50:
			return 'Зачем это смотреть'
		if mov.rating < 75:
			return 'Разок можно глянуть'
		if mov.rating <= 85:
			return 'Зачёт'
		return 'Топчик'

	@admin.action(description = 'Установить валюту в доллар')
	def set_dollars(self, request, qs:QuerySet):
		count_updated = qs.update(currency=Movie.USD)
		self.message_user(request,f'Было обновлено {count_updated} записей')

admin.site.site_header = 'Админка тур-компании'
admin.site.index_title = 'Тур-компания: Вокруг света'









#@admin.site.register(Movie)

