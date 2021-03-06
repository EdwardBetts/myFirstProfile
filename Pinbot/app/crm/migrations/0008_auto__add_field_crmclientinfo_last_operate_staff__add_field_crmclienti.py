# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CRMClientInfo.last_operate_staff'
        db.add_column(u'crm_crmclientinfo', 'last_operate_staff',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CRMClientInfo.last_operate_admin'
        db.add_column(u'crm_crmclientinfo', 'last_operate_admin',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='last_operate_clients', null=True, to=orm['auth.User']),
                      keep_default=False)


        # Changing field 'CandidateRemark.desc'
        db.alter_column(u'crm_candidateremark', 'desc', self.gf('django.db.models.fields.CharField')(max_length=500))

    def backwards(self, orm):
        # Deleting field 'CRMClientInfo.last_operate_staff'
        db.delete_column(u'crm_crmclientinfo', 'last_operate_staff')

        # Deleting field 'CRMClientInfo.last_operate_admin'
        db.delete_column(u'crm_crmclientinfo', 'last_operate_admin_id')


        # Changing field 'CandidateRemark.desc'
        db.alter_column(u'crm_candidateremark', 'desc', self.gf('django.db.models.fields.CharField')(max_length=150))

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
        u'crm.candidate': {
            'Meta': {'object_name': 'Candidate'},
            'admin': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'candidates'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'contact_info': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'candidate'", 'unique': 'True', 'to': u"orm['resumes.ContactInfoData']"}),
            'has_contact': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['crm.CandidateTag']", 'null': 'True', 'blank': 'True'}),
            'update_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'crm.candidateremark': {
            'Meta': {'object_name': 'CandidateRemark'},
            'admin': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'candidate_remark'", 'to': u"orm['auth.User']"}),
            'candidate': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'candidate_remarks'", 'to': u"orm['crm.Candidate']"}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'remark_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'remark_type': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'crm.candidatetag': {
            'Meta': {'object_name': 'CandidateTag'},
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'crm.companycardsendrecord': {
            'Meta': {'ordering': "['-send_time']", 'object_name': 'CompanyCardSendRecord'},
            'candidate': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'send_records'", 'to': u"orm['crm.Candidate']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['feed.Feed']"}),
            'operator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'send_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'crm.crmclientinfo': {
            'Meta': {'object_name': 'CRMClientInfo'},
            'admin': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'crm_clients'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'client': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'crm_client_info'", 'unique': 'True', 'to': u"orm['auth.User']"}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_operate_admin': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'last_operate_clients'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'last_operate_staff': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'last_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'crm.crmdownloadresume': {
            'Meta': {'object_name': 'CRMDownloadResume'},
            'admin': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'crm_download_resumes'", 'to': u"orm['auth.User']"}),
            'buy_resume': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'crm_resume_info'", 'unique': 'True', 'to': u"orm['transaction.ResumeBuyRecord']"}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'update_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'crm.crmfeedremark': {
            'Meta': {'object_name': 'CRMFeedRemark'},
            'admin': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'crm_feed_remarks'", 'to': u"orm['auth.User']"}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'crm_remarks'", 'to': "orm['feed.Feed']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'remark': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'remark_type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'update_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'feed.feed': {
            'Meta': {'object_name': 'Feed'},
            'add_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'analyze_titles': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '350', 'blank': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['jobs.Company']", 'null': 'True', 'blank': 'True'}),
            'company_prefer': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['system.CompanyCategoryPrefer']", 'null': 'True', 'blank': 'True'}),
            'degree': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'delete_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'department_to': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'expect_area': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'expire_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'feed_expire_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 1, 27, 0, 0)', 'db_index': 'True'}),
            'feed_obj_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'db_index': 'True'}),
            'feed_type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ignored': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_related': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'job_desc': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '5000'}),
            'job_domain': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['jobs.CompanyCategory']", 'null': 'True', 'blank': 'True'}),
            'job_tag': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'job_type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'job_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'job_welfare': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'key_points': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000'}),
            'keywords': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '350'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'last_click_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'major': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'recruit_num': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'report_to': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'salary_max': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'salary_min': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'skill_required': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000'}),
            'talent_level': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'update_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'username': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'work_years_max': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'work_years_min': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'jobs.company': {
            'Meta': {'object_name': 'Company'},
            'add_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 1, 19, 0, 0)'}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['jobs.CompanyCategory']", 'null': 'True', 'blank': 'True'}),
            'company_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'company_stage': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000'}),
            'core_team': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000', 'blank': 'True'}),
            'desc': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000'}),
            'favour_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_points': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000'}),
            'need_recommend': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'pinbot_recommend': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'blank': 'True'}),
            'product_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'jobs.companycategory': {
            'Meta': {'object_name': 'CompanyCategory'},
            'brick_display': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'code_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'jobs.job': {
            'Meta': {'object_name': 'Job'},
            'add_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 1, 19, 0, 0)'}),
            'address': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['jobs.Company']"}),
            'degree': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'desc': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_points': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'salary_high': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'salary_low': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'skill_desc': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'work_years': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'jobs.sendcompanycard': {
            'Meta': {'unique_together': "(('send_user', 'resume_id'),)", 'object_name': 'SendCompanyCard'},
            'download_status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'feed_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'feedback_status': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'feedback_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 1, 19, 0, 0)'}),
            'has_download': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['jobs.Job']", 'null': 'True', 'blank': 'True'}),
            'points_used': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'resume_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'send_msg': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'send_status': ('django.db.models.fields.IntegerField', [], {'default': '2', 'null': 'True', 'blank': 'True'}),
            'send_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 1, 19, 0, 0)'}),
            'send_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'to_email': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'resumes.contactinfodata': {
            'Meta': {'object_name': 'ContactInfoData', 'db_table': "'resumes_contactinfo'"},
            'add_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 1, 19, 0, 0)', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identity_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'db_column': "'identityID'", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'qq': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'reported_num': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'resume_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100', 'db_column': "'resumeID'"}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'source_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'db_column': "'sourceID'", 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'public'", 'max_length': '100'}),
            'weibo': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'system.companycategoryprefer': {
            'Meta': {'object_name': 'CompanyCategoryPrefer'},
            'code_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'})
        },
        u'transaction.feedbackinfo': {
            'Meta': {'object_name': 'FeedBackInfo'},
            'feedback_desc': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'feedback_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['transaction.FeedBackType']"})
        },
        u'transaction.feedbacktype': {
            'Meta': {'object_name': 'FeedBackType'},
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            're_points': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'transaction.resumebuyrecord': {
            'Meta': {'unique_together': "(('user', 'resume_id'),)", 'object_name': 'ResumeBuyRecord'},
            'feed_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'feedback_info': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['transaction.FeedBackInfo']", 'null': 'True', 'blank': 'True'}),
            'finished_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 1, 1, 0, 0)', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'op_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'resume_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'resume_url': ('django.db.models.fields.URLField', [], {'max_length': '1000'}),
            'send_card': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['jobs.SendCompanyCard']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['crm']