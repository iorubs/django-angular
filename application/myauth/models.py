from __future__ import unicode_literals
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class AccountManager(BaseUserManager):
	def create_user(self, email, password=None, **kwargs):
		if not email:
			raise ValueError('User must have a valid email address.')

		if not kwargs.get('username'):
			raise ValueError('Users must have a valid username.')

		account = self.model(email=self.normalize_email(email), **kwargs)

		account.set_password(password)
		account.save()

		return account

	'''re-uses the normal user account to create a simillar
	type of account with admin privileges (superuser)'''
	def create_superuser(self, email, password, **kwargs):
		account = self.create_user(email, password, **kwargs)

		account.is_admin = True
		account.is_staff = True
		account.save()

		return account

class Account(AbstractBaseUser):
	#enforce the need for unique emails and usernames
	email = models.EmailField(unique=True)
	username = models.CharField(max_length=40, unique=True)

	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)

	#implement different user levels
	is_admin = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)

	#time and date account was created/updated on.
	created_on = models.DateTimeField(auto_now_add=True)
	last_update_date = models.DateTimeField(auto_now=True)

	objects = AccountManager()

	'''Enforce the need for an username and extra methods
	for complience with django expected format.'''
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

	def __unicode__(self):
		return self.email

	def get_full_name(self):
		return ' '.join([self.first_name, self.last_name])

	def get_short_name(self):
		return self.first_name

	def has_module_perms(self, app_label):
		return self.is_admin

	def has_perm(self, app_label):
		return self.is_admin
