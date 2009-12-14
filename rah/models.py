import hashlib
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from base64 import b64encode

class User(User):
    class Meta:
        proxy = True

    def get_name(self):
        return self.get_full_name() if self.get_full_name() else self.email

    def get_welcome(self):
        return 'Welcome, %s' % (self.get_full_name()) if self.get_full_name() else 'Logged in as, %s' % (self.email)
        
    def set_email(self, email):
        if User.objects.filter(email=email):
            return False
        self.username = b64encode(email)
        return True

class DefaultModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
    
    def __unicode__(self):
        return u'%s' % (self.name)

class Action(DefaultModel):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    teaser = models.TextField()
    content = models.TextField()
    category = models.ForeignKey('ActionCat')
    
    @staticmethod
    def get_recommended_actions_for_user(user, quantity=5):
        """
        return a list of actions that are recommended for this user
        """
        return Action.objects.all()[:quantity]
        
    @staticmethod
    def get_actions_with_tasks_and_user_completes_for_user(user):
        """
        return a list of actions with 2 extra attributes, tasks will contain the number
        of assocaited tasks and user_completes will contain the number of tasks completed
        by the specified user
        """
        if not user:
            raise Exception("User must be defined.")
        return Action.objects.all().extra(
            select = { 'tasks': 'SELECT COUNT(at.id) \
                                 FROM rah_actiontask at \
                                 WHERE at.action_id = rah_action.id' }).extra(
            select_params = (user.id,),
            select = { 'user_completes': 'SELECT COUNT(uat.id) \
                                          FROM rah_useractiontask uat \
                                          JOIN rah_actiontask at ON uat.action_task_id = at.id \
                                          WHERE uat.user_id = %s AND at.action_id = rah_action.id'})

class ActionCat(DefaultModel):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    teaser = models.TextField()
    content = models.TextField()

class ActionTask(DefaultModel):
    """
    class representing the individual tasks (or steps) a user must complete
    in order to gain successful completion of the associated action
    """
    action = models.ForeignKey(Action)
    name = models.CharField(max_length=255)
    content = models.TextField()
    points = models.IntegerField()
    sequence = models.PositiveIntegerField()
    
    class Meta:
        ordering = ['action', 'sequence']
        unique_together = ('action', 'sequence',)

    @staticmethod
    def get_action_tasks_by_action_optional_user(action, user):
        return ActionTask.objects.filter(action=action.id).extra(
            select_params = (user.id,), 
            select = { 'completed': 'SELECT rah_useractiontask.completed \
                                     FROM rah_useractiontask \
                                     WHERE rah_useractiontask.user_id = %s AND \
                                     rah_useractiontask.action_task_id = rah_actiontask.id' })

class UserActionTask(models.Model):
    """
    class representing the ActionTasks a specific user has completed
    """
    action_task = models.ForeignKey(ActionTask)
    user = models.ForeignKey(User)
    completed = models.DateTimeField(auto_now=True)
    
    class Meta:
        get_latest_by = 'complete'

    def __unicode__(self):
        return u'%s completed at %s' % (self.action_task, self.completed)

class Location(models.Model):
    name = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=5)
    county = models.CharField(max_length=100)
    st = models.CharField(max_length=2)
    state = models.CharField(max_length=50)
    lon = models.CharField(max_length=50)
    lat = models.CharField(max_length=50)
    pop = models.PositiveIntegerField()
    timezone = models.CharField(max_length=100)
    
    def __unicode__(self):
        return u'%s, %s (%s)' % (self.name, self.st, self.zipcode)

class Points(DefaultModel):
    """
    Points can be associated with a given action task or a given arbitrarily.
    To assign the points arbitrarily, you should provide a value for `reason`
    
    
    ex: Points(user=request.user, points=10, task=task).save()
    ex: Points(user=request.user, points=10, reason=1).save()
    """
    
    REASONS = (
        (1, "Because we like you"),
        (2, "Because we don't like you"),
    )
    
    class Meta:
        verbose_name_plural = 'points'
    
    user = models.ForeignKey(User)
    points = models.IntegerField()
    task = models.ForeignKey(ActionTask, related_name="task", null=True)
    reason = models.IntegerField(choices=REASONS, default='')

    def __unicode__(self):
        return u'%s points' % (self.points)

class Signup(models.Model):
    email = models.EmailField(max_length=255)
    zipcode = models.CharField(max_length=5)

    def __unicode__(self):
        return u'%s' % (self.email)

class Profile(models.Model):
    """Profile"""
    # OPTIMIZE these choices can be tied to an IntegerField if the value is an integer: (1, 'Apartment'),
    BUILDING_CHOICES = (
        ('A', 'Apartment'),
        ('S', 'Single Family Home'),
    )
    user = models.ForeignKey(User, unique=True)
    location = models.ForeignKey(Location, null=True)
    building_type = models.CharField(null=True, max_length=1, choices=BUILDING_CHOICES, blank=True)
    
    def __unicode__(self):
        return u'%s' % (self.user.username)

    def get_gravatar_url(self, size=200, default_icon='identicon'):
        return 'http://www.gravatar.com/avatar/%s?r=g&s=%s&d=%s' % (self._email_hash(), size, default_icon)

    def _email_hash(self):
        return (hashlib.md5(self.user.email.lower()).hexdigest())
