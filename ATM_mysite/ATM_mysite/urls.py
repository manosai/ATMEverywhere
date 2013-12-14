from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ATM_mysite.views.home', name='home'),
    # url(r'^ATM_mysite/', include('ATM_mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^login$', 'ATM_mysite.ATM_myapp.views.login', name='login'),
    url(r'^submit_request$', 'ATM_mysite.ATM_myapp.views.submit_request', name='submit_request'),

)
