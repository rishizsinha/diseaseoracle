from django.db import models
from datetime import date
from django.utils import timezone

# Create your models here.

class Tweet(models.Model):
	def within(self):
		return self.tid >= timezone.now() - datetime.timedelta(weeks=w)
	tid = models.CharField(max_length=20)
	time = models.DateTimeField()
	text = models.CharField(max_length=150)
	geo = models.CharField(max_length=150)
	coordinates = models.CommaSeparatedIntegerField(max_length=100)
	place = models.CharField(max_length=100)
	user_tz = models.CharField(max_length=100)
	lang = models.CharField(max_length=10)
	within1mo = models.BooleanField()
	within2wk = models.BooleanField()
	within1wk = models.BooleanField()

	def __str__(self):
		return "{time: "+self.tid+ \
				",\ntext: "+self.text+ \
				",\ngeo: "+self.geo+ \
				",\ntimezone: "+self.user_tz+"}"





# {"created_at":"Sat Oct 10 10:27:50 +0000 2015",
# "id":652792649393418241,"id_str":"652792649393418241",
# "text":"RT @aldubmaiden: GOOD LUCK, MS. RUBY @rodriguezruby! FIGHTING! :)\n#EBDabarkadsPaMore",
# "source":"\u003ca href=\"http:\/\/twitter.com\/#!\/download\/ipad\" rel=\"nofollow\"\u003eTwitter for iPad\u003c\/a\u003e",
# "truncated":false,
# "in_reply_to_status_id":null,
# "in_reply_to_status_id_str":null,
# "in_reply_to_user_id":null,
# "in_reply_to_user_id_str":null,
# "in_reply_to_screen_name":null,

# "user":{"id":1682730505,
# 	"id_str":"1682730505",
# 	"name":"AFBCDC",
# 	"screen_name":"AFBCDC",
# 	"location":"Ulat, Silang, Cavite",
# 	"url":null,
# 	"description":"Nurturing and developing young minds.",
# 	"protected":false,
# 	"verified":false,
# 	"followers_count":32,
# 	"friends_count":46,
# 	"listed_count":3,
# 	"favourites_count":604,
# 	"statuses_count":7455,
# 	"created_at":"Mon Aug 19 08:20:57 +0000 2013",
# 	"utc_offset":10800,
# 	"time_zone":"Athens",
# 	"geo_enabled":false,
# 	"lang":"en",
# 	"contributors_enabled":false,
# 	"is_translator":false,
# 	"profile_background_color":"C0DEED",
# 	"profile_background_image_url":"http:\/\/pbs.twimg.com\/profile_background_images\/378800000054836685\/d86a9e07e82e8697f613f16ba0ff150d.jpeg","profile_background_image_url_https":"https:\/\/pbs.twimg.com\/profile_background_images\/378800000054836685\/d86a9e07e82e8697f613f16ba0ff150d.jpeg","profile_background_tile":true,
# 	"profile_link_color":"058767",
# 	"profile_sidebar_border_color":"FFFFFF",
# 	"profile_sidebar_fill_color":"DDEEF6",
# 	"profile_text_color":"333333",
# 	"profile_use_background_image":true,
# 	"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/647414187019206656\/OHeTRn1__normal.jpg",
# 	"profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/647414187019206656\/OHeTRn1__normal.jpg",
# 	"profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/1682730505\/1444425268",
# 	"default_profile":false,
# 	"default_profile_image":false,
# 	"following":null,
# 	"follow_request_sent":null,
# 	"notifications":null},

# "geo":null,
# "coordinates":null,
# "place":null,
# "contributors":null,

# "retweeted_status":{"created_at":"Sat Oct 10 05:12:25 +0000 2015",
# 	"id":652713270730579968,"id_str":"652713270730579968",
# 	"text":"GOOD LUCK, MS. RUBY @rodriguezruby! FIGHTING! :)\n#EBDabarkadsPaMore",
# 	"source":"\u003ca href=\"http:\/\/twitter.com\" rel=\"nofollow\"\u003eTwitter Web Client\u003c\/a\u003e",
# 	"truncated":false,
# 	"in_reply_to_status_id":null,
# 	"in_reply_to_status_id_str":null,
# 	"in_reply_to_user_id":null,
# 	"in_reply_to_user_id_str":null,
# 	"in_reply_to_screen_name":null,
# 	"user":{"id":3288465684,"id_str":"3288465684","name":"AlDub\u2764\ufe0fMaiDen Org",
# 		"screen_name":"aldubmaiden","location":"Worldwide",
# 			"url":"http:\/\/ask.fm\/maidenaldub16",
# 			"description":"ORGANIZATION OF THE ALDUB|MAIDEN LOVETEAM! | OFFICIAL | TRUSTED | ONE OF THE OFFICIAL ALDUB TRENDSETTER. FOLLOW US FOR MORE ALDUB UPDATES.",
# 			"protected":false,"verified":false,"followers_count":229302,"friends_count":1735,
# 			"listed_count":58,"favourites_count":2971,"statuses_count":18509,"created_at":"Thu Jul 23 06:52:28 +0000 2015",
# 			"utc_offset":null,"time_zone":null,"geo_enabled":false,"lang":"en","contributors_enabled":false,
# 			"is_translator":false,"profile_background_color":"000000","profile_background_image_url":"http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_image_url_https":"https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_tile":false,
# 			"profile_link_color":"DD2E44","profile_sidebar_border_color":"000000","profile_sidebar_fill_color":"000000","profile_text_color":"000000","profile_use_background_image":false,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/648038443910496257\/e1zsf_th_normal.jpg",
# 			"profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/648038443910496257\/e1zsf_th_normal.jpg",
# 			"profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/3288465684\/1443004500",
# 			"default_profile":false,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":null,"contributors":null,
# 			"is_quote_status":false,"retweet_count":248,"favorite_count":68,"entities":{"hashtags":[{"text":"EBDabarkadsPaMore","indices":[49,67]}],"urls":[],"user_mentions":[{"screen_name":"rodriguezruby","name":"ruby rodriguez","id":145514541,"id_str":"145514541","indices":[20,34]}],"symbols":[]},
# 			"favorited":false,"retweeted":false,"filter_level":"low","lang":"en"},"is_quote_status":false,"retweet_count":0,"favorite_count":0,
# 			"entities":{"hashtags":[{"text":"EBDabarkadsPaMore","indices":[66,84]}],"urls":[],"user_mentions":[{"screen_name":"aldubmaiden",
# 			"name":"AlDub\u2764\ufe0fMaiDen Org","id":3288465684,"id_str":"3288465684","indices":[3,15]},
# 			{"screen_name":"rodriguezruby","name":"ruby rodriguez","id":145514541,"id_str":"145514541","indices":[37,51]}],
# 			"symbols":[]},"favorited":false,"retweeted":false,"filter_level":"low","lang":"en",
# "timestamp_ms":"1444472870573"}













