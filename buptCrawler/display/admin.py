# -*- coding: utf-8 -*-

from models import RateScore,Player,CurrentPlayer
from django.contrib import admin

class RateScoreAdmin(admin.ModelAdmin):
    list_display = ('judgerID', 'playerID','playerName','score','addtime')
    
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('playerID', 'playerName')
    
    
class CurrentPlayerAdmin(admin.ModelAdmin):  
    list_display = ('get_playerName', 'get_playerID','extra')

    def get_playerName(self, obj):  
        return obj.current_player.playerName 
    def get_playerID(self, obj):  
        return obj.current_player.playerID  
    
    get_playerName.short_description = u'当前选手名字'
    get_playerID.short_description = u'当前选手编号'
        
admin.site.register(Player,PlayerAdmin)
admin.site.register(CurrentPlayer,CurrentPlayerAdmin)
admin.site.register(RateScore, RateScoreAdmin)
