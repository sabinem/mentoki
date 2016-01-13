#app storefront
renders a list of courses and the detail page for each course

##landing pages
views.info: landing page for each course

##caching
used for template parts

##data used
* apps_productdata.mentoki_product.models.courseproduct/courseproductgroup
* apps_customerdata.customer.models.order

##logging
#views.info: 
logger = logging.getLogger('public.offerpages')
logger_sentry = logging.getLogger('sentry.offerpages')
 
 
 

