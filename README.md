Repo settings
=============

+ 539ba4b35004461920000107@simplenote-suhailvs.rhcloud.com
+ openshift id: suhailvs@gmail.com

wsgi.py
-------

+ os.environ['DJANGO_SETTINGS_MODULE'] = 'notes.settings'
+ sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'],'simplenotesite'))


URL Saving
==========

nothing a small change

4) the pattern of url note Http://<sitename>/+<note>/<redirect url>
The note will be saved in the database under url tag.

the regular expression syntax for the url pattern is as follows \+(.{5,500})


note = <matched str>.split('/')[0]
url=<matched str>.split('/')[1]

TO build extesions
==================

`python /home/suhail/exten/kango.py build extension/`


some good code formattings
==========================

https://bradmontgomery.net/blog/2009/01/05/add-a-context-processor-for-your-django-app-using-sites/

http://lightglitch.github.io/bootstrap-xtra/

To do
=====

edit the extenstions and make it usable with different users with option to login.
