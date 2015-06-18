def foto_location(instance, filename):
        return '/'.join([instance.course.slug, filename])