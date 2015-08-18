from __future__ import unicode_literals
# from python
import logging
# import from django
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
# from other apps
# import from this app
from .models import Thread, Post, SubForum
from .forms_post import PostCreateForm, PostUpdateForm
from .forms_thread import ThreadUpdateForm, ThreadCreateForm

from .views_forum import ForumMixin
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.template import Context
from apps_data.course.models import Course,CourseOwner
from django.contrib.sites.models import Site
from .helpers_subforums import calc_subforum_enriched_list
from .cache import recalc_subforum_change, recalc_thread_data
from braces.views import MessageMixin



import logging


logger = logging.getLogger(__name__)


class ThreadMixin(ForumMixin, MessageMixin):

    def get_context_data(self, **kwargs):
        context = super(ThreadMixin, self).get_context_data(**kwargs)
        logger.debug("---------- in ThreadMixin get_context_data")
        try:
            thread = Thread.objects.get(id=self.kwargs['thread'])
            author = Thread.author
            timesince_last_changed = context['threaddata'][thread.id]['last_changed']
            output_dict = {
                'thread':thread,
                'author': thread.author,
                'last_author': context['threaddata'][thread.id]['last_author'],
                'timesince_last_changed': timesince_last_changed,
                'last_author_id': context['threaddata'][thread.id]['last_author_id'],
                'postcount' : context['threaddata'][thread.id]['post_count'],
                'subforum_title': context['subforumdict'][thread.subforum_id]['title'],
            }
            context['thread'] = output_dict
        except:
            subforum = SubForum.objects.get(id=self.kwargs['subforum'])
            context['subforum'] = subforum
        int(self.kwargs['subforum'])
        ancestor_list = context['subforumdict'][int(self.kwargs['subforum'])]['ancestors']
        ancestor_enriched_list = calc_subforum_enriched_list(ancestor_list, context['subforumdict'])
        context['ancestors']= ancestor_enriched_list


        return context

    def get_success_url(self):
        logger.debug("---------- in ThreadMixin get_success_url")

        return reverse(
            'forum:thread',
            kwargs={"subforum": self.kwargs['subforum'], "slug": self.kwargs['slug'], "thread": self.kwargs['thread']
        })


class ThreadListPostCreateView(ThreadMixin, CreateView):

    template_name = 'classroom_forum/thread.html'
    form_class = PostCreateForm

    def get_context_data(self, **kwargs):
        context = super(ThreadListPostCreateView, self).get_context_data(**kwargs)
        logger.debug("---------- in ThreadListPostCreateView get_context_data")
        posts = Post.objects.filter(thread_id=self.kwargs['thread']).order_by('created')
        context['posts'] = posts
        try:
            latest_post = posts.latest('created')
            context['latest_post'] = latest_post
        except:
            pass
        return context

    def get_success_url(self):
        logger.debug("---------- in ThreadListPostCreateView get_success_url")
        recalc_thread_data(self.object.forum_id)
        recalc_subforum_change(self.object.forum_id)
        #self.messages.success("Der Post wurde gespeichert.")

        return super(ThreadListPostCreateView, self).get_success_url()

    def form_valid(self, form, **kwargs):
        logger.debug("---------- in ThreadListPostCreateView form_valid")
        context = self.get_context_data(**kwargs)
        form.instance.forum_id = context['courseevent']['forum_id']
        courseevent = context['courseevent']
        form.instance.thread_id = self.kwargs['thread']
        form.instance.author = self.request.user
        context = self.get_context_data()
        print " ------------- determine outgoing emails:"
        print "for thread %s" % form.instance.thread_id,
        people_in_thread = Post.objects.filter(thread_id=context['thread']['thread'].id).\
            values_list('author_id', flat=True)
        print "1 people in thread = %s" % people_in_thread
        people_in_thread = list(people_in_thread)
        courseowner = CourseOwner.objects.filter(course_id=courseevent['course_id']).\
            values_list('user_id', flat=True)

        for owner in courseowner:
            people_in_thread.append(owner)
        print "2 people in thread = %s" % people_in_thread
        people_in_thread.append(self.request.user.id)
        print "3 people in thread = %s" % people_in_thread
        people_in_thread.append(context['thread']['thread'].author_id)
        people_in_thread = list(set(people_in_thread))
        print "4 people in thread = %s" % people_in_thread
        users_in_thread = User.objects.filter(id__in=people_in_thread)
        print "-------- outgoing emails:"
        print users_in_thread
        course = Course.objects.get(id=courseevent['course_id'])
        # send email to requesting email

        subject = "Neuer Post zum Beitrag %s" % context['thread']['thread'].title
        to_list = []
        for user in users_in_thread:
            to_list.append(user.email)
        to = to_list
        from_mail = course.email
        site = Site.objects.get(id=1)
        context = {
                'courseevent_title': context['courseevent']['courseevent_title'],
                'title': context['thread']['thread'].title,
                'text': form.cleaned_data['text'],
                'author': form.instance.author,
                'thread': form.instance.thread_id,
                'slug': self.kwargs['slug'],
                'subforum':self.kwargs['subforum'],
                'betreff': subject,
                'site':site
        }
        message = get_template('email/newpost.html').render(Context(context))
        msg = EmailMessage(subject, message, to=to, from_email=from_mail)
        msg.content_subtype = 'html'
        msg.send()
        self.messages.success(u"Wow, vielen Dank, %s, dass Du etwas gepostet hast." % form.instance.author )
        return super(ThreadListPostCreateView, self).form_valid(form)


class PostUpdateView(ThreadMixin, UpdateView):

    template_name = 'forum/threadCRUD/postupdate.html'
    form_class = PostUpdateForm

    def get_success_url(self):
        logger.debug("---------- in PostUpdateView get_success_url")
        recalc_thread_data(self.object.forum_id)
        recalc_subforum_change(self.object.forum_id)
        self.messages.success("Der Post wurde geaendert.")
        return super(PostUpdateView, self).get_success_url()

    def get_object(self, queryset=None):
        logger.debug("---------- in PostUpdateView get_object")
        post = Post.objects.get(id=self.kwargs['post'])
        return post


class PostDeleteView(ThreadMixin, DeleteView):

    template_name = 'forum/threadCRUD/postdelete.html'
    model = Post

    def get_success_url(self):
        logger.debug("---------- in PostDeleteView get_success_url")
        self.messages.success("Der Post wurde geloescht.")
        recalc_thread_data(self.object.forum_id)
        recalc_subforum_change(self.object.forum_id)
        return super(PostDeleteView, self).get_success_url()

    def get_object(self, queryset=None):
        logger.debug("---------- in PostDeleteView get_object")
        post = Post.objects.get(id=self.kwargs['post'])
        return post


class ThreadUpdateView(ThreadMixin, UpdateView):

    template_name = 'forum/threadCRUD/threadupdate.html'
    form_class = ThreadUpdateForm

    def get_success_url(self):
        logger.debug("---------- in ThreadUpdateView get_success_url")
        recalc_subforum_change(self.object.forum_id)
        self.messages.success("Der Beitrag wurde geaendert.")
        return super(ThreadUpdateView, self).get_success_url()

    def get_object(self, queryset=None):
        logger.debug("---------- in PostUpdateView get_object")
        thread = Thread.objects.get(id=self.kwargs['thread'])
        return thread

    def get_context_data(self, **kwargs):
        context = super(ThreadUpdateView, self).get_context_data(**kwargs)
        logger.debug("---------- in ThreadUpdateView get_context_data")
        posts = Post.objects.filter(thread_id=self.kwargs['thread']).order_by('created')
        context['posts'] = posts
        return context

    def form_valid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        return super(ThreadUpdateView, self).form_valid(form)


class ThreadDeleteView(ThreadMixin, DeleteView):

    template_name = 'forum/threadCRUD/threaddelete.html'
    model = Thread

    def get_success_url(self):
        logger.debug("---------- in ThreadDeleteView get_success_url")
        self.messages.success("Der Beitrag wurde geloescht.")
        recalc_subforum_change(self.object.forum_id)
        return reverse('forum:subforum', kwargs={"subforum":self.kwargs['subforum'],
                                                   "slug": self.kwargs['slug']})

    def get_object(self, queryset=None):
        logger.debug("---------- in ThreadDeleteView get_object")
        thread = Thread.objects.get(id=self.kwargs['thread'])
        return thread


class ThreadCreateView(ThreadMixin, CreateView):

    template_name = 'classroom_forum/threadcreate.html'
    form_class = ThreadCreateForm

    def get_success_url(self):
        logger.debug("---------- in ThreadCreateView get_success_url")

        recalc_subforum_change(self.object.forum_id)
        recalc_thread_data(self.object.forum_id)
        return reverse(
            'forum:thread',
            kwargs={"subforum": self.kwargs['subforum'], "slug": self.kwargs['slug'], "thread": self.object.id
        })

    def form_valid(self, form, **kwargs):
        logger.debug("---------- in ThreadCreateView form_valid")
        context = self.get_context_data(**kwargs)

        form.instance.forum_id = context['courseevent']['forum_id']
        form.instance.author = self.request.user
        form.instance.subforum = context['subforum']
        self.messages.success(u"Hey, vielen Dank, %s, dass Du etwas zur Diskussion beigetragen hast." % form.instance.author )

        return super(ThreadCreateView, self).form_valid(form)

    def get_initial(self, **kwargs):
        initial_data = super(ThreadCreateView, self).get_initial()
        logger.debug("---------- in ThreadCreateView get_initial")
        return initial_data




