from .views import Category


def menuCategoy(request):
    menuCategoy = Category.objects.all()

    return {'menuCategoy':menuCategoy }
