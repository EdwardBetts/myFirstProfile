# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'AutoReplyResumeLog'
        db.delete_table(u'weixin_autoreplyresumelog')

        # Adding field 'MsgSendLog.errcode'
        db.add_column(u'weixin_msgsendlog', 'errcode',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'MsgSendLog.errmsg'
        db.add_column(u'weixin_msgsendlog', 'errmsg',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'AutoReplyResumeLog'
        db.create_table(u'weixin_autoreplyresumelog', (
            ('weixin_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='auto_reply_weixin_user', to=orm['weixin.WeixinUser'])),
            ('reply_content', self.gf('django.db.models.fields.CharField')(max_length=200)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('add_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'weixin', ['AutoReplyResumeLog'])

        # Deleting field 'MsgSendLog.errcode'
        db.delete_column(u'weixin_msgsendlog', 'errcode')

        # Deleting field 'MsgSendLog.errmsg'
        db.delete_column(u'weixin_msgsendlog', 'errmsg')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'weixin.msgsendlog': {
            'Meta': {'object_name': 'MsgSendLog'},
            'add_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'display_time': ('django.db.models.fields.DateTimeField', [], {}),
            'errcode': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'errmsg': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'msg_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'reco_num': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'weixin_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'weixin_user'", 'to': u"orm['weixin.WeixinUser']"})
        },
        u'weixin.weixinuser': {
            'Meta': {'object_name': 'WeixinUser'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'groupid': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'headimgurl': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_bind': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_subscribe': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'openid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'privilege': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'remark': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sex': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'blank': 'True'}),
            'subscribe': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'subscribe_time': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'unionid': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'weixin_user'", 'unique': 'True', 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['weixin']