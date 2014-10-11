from django.contrib.sitemaps import Sitemap
from note.models import Notes
from django.template.defaultfilters import slugify

class NoteSitemap(Sitemap):
	changefreq = 'weekly'
	priority = 0.6
	def items(self):
		return Notes.objects.filter(folder__name='public')
	def lastmod(self, obj):
		return obj.modified
	def location(self, obj):
		slug = slugify(obj.title[:59] if len(obj.title) > 60  else obj.title)
		return '/note/%d/%s' %(obj.pk,slug)