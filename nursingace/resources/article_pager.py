
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
def pager(request, all_posts, per_page):
    paginator = Paginator(all_posts, per_page)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(page.num_pages)

    return posts