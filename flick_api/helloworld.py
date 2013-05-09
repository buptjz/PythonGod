import flickrapi

api_key = '556fe985c9177856175eb239d44a40cb'
api_secrect = '54d0540425091ba4'

flickr = flickrapi.FlickrAPI(api_key)
photos = flickr.photos_search(user_id='73509078@N00', per_page='10')
sets = flickr.photosets_getList(user_id='73509078@N00')
for photo in flickr.walk(tag_mode='all',
        tags='sybren,365,threesixtyfive',
        min_taken_date='2008-08-20',
        max_taken_date='2008-08-30'):
    print photo.get('title')
    
print sets