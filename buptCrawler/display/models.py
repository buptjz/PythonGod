# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class RateScore(models.Model):
    '''Record of the every rate item'''
    judgerID = models.CharField(u"评委编号", max_length=100, null=True)
    playerID = models.CharField(u"选手编号",max_length=100,null = True)
    playerName = models.CharField(u"选手名字",max_length=300,null = True)
    score = models.CharField(u"得分",max_length=100,null = True)
    addtime = models.DateTimeField(u"时间",null = True, auto_now_add=True)
    extra = models.CharField(u"附加信息",max_length=500,null=True)

    def __unicode__(self):
        return self.judgerID
    def _repr(self):
        return self.judgerID
    
class Player(models.Model):
    '''Player for this competition'''
    playerID = models.CharField(u"选手编号", max_length=100, null=True)
    playerName = models.CharField(u"选手名字",max_length=300,null = True)

    def __unicode__(self):
        return self.playerName+"\t"+self.playerID
    def _repr(self):
        return self.playerName+"\t"+self.playerID
    
class CurrentPlayer(models.Model):
    current_player = models.ForeignKey(Player)
    extra = models.CharField(u"附加信息",max_length=500,null=True)
    
    def __unicode__(self):
        return self.extra
    def _repr(self):
        return self.extra
    
