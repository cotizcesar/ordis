import re
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
def number_formatter(value, num_decimals=2):
    """
    Django template filter to convert regular numbers to a
    cool format (ie: 2K, 434.4K, 33M...)
    :param value: number
    :param num_decimals: Number of decimal digits

    Source: https://gist.github.com/dnmellen/bfc1b3005999aaff3ed4
    """

    int_value = int(value)
    formatted_number = "{{:.{}f}}".format(num_decimals)
    if int_value < 1000:
        return str(int_value)
    elif int_value < 1000000:
        return formatted_number.format(int_value / 1000.0).rstrip("0").rstrip(".") + "K"
    else:
        return (
            formatted_number.format(int_value / 1000000.0).rstrip("0").rstrip(".") + "M"
        )


@register.filter
def proper_paginate(paginator, current_page, neighbors=10):
    if paginator.num_pages > 2 * neighbors:
        start_index = max(1, current_page - neighbors)
        end_index = min(paginator.num_pages, current_page + neighbors)
        if end_index < start_index + 2 * neighbors:
            end_index = start_index + 2 * neighbors
        elif start_index > end_index - 2 * neighbors:
            start_index = end_index - 2 * neighbors
        if start_index < 1:
            end_index -= start_index
            start_index = 1
        elif end_index > paginator.num_pages:
            start_index -= end_index - paginator.num_pages
            end_index = paginator.num_pages
        page_list = [f for f in range(start_index, end_index + 1)]
        return page_list[: (2 * neighbors + 1)]
    return paginator.page_range


@register.simple_tag
def url_replace(request, field, value):
    query_string = request.GET.copy()
    query_string[field] = value

    return query_string.urlencode()


@register.filter
def youtube_embed_url(value):
    div_responsive_start = '<div class="embed-responsive embed-responsive-16by9">'
    div_responsive_end = "</div>"
    iframe1 = '<iframe class="embed-responsive-item" src="'
    iframe2 = '" allowfullscreen="allowfullscreen" mozallowfullscreen="mozallowfullscreen" msallowfullscreen="msallowfullscreen" oallowfullscreen="oallowfullscreen" webkitallowfullscreen="webkitallowfullscreen"></iframe>'
    nosupp = '<div class="jumbotron bg-black-t">'
    orted = "</div>"
    match = re.search(
        r"^(?:https?:\/\/)?(?:www\.|m\.)?youtu\.?be(?:\.com)?\/?.*(?:watch|embed)?(?:.*v=|v\/|\/)([\w\-_]+)?(\?t=\d+s)?(&feature=related)?$",
        value,
    )
    match2 = re.search(
        r"^(http|https)?:\/\/(www\.)?vimeo.com\/(?:channels\/(?:\w+\/)?|groups\/([^\/]*)\/videos\/|)(\d+)(?:|\/\?)$",
        value,
    )
    match3 = re.search(
        r"^(^http(s)?://)?((www|en-es|en-gb|secure|beta|ro|www-origin|en-ca|fr-ca|lt|zh-tw|he|id|ca|mk|lv|ma|tl|hi|ar|bg|vi|th)\.)?twitch.tv/(?!directory|p|user/legal|admin|login|signup|jobs)(?P<channel>\w+)$",
        value,
    )
    match4 = re.search(r"^(http|https)?:\/\/(www|clips)?.twitch.tv\/(\w+)$", value)
    match5 = re.search(
        r"^(http|https):\/\/(media|giphy).(com|giphy.com)\/(media|gifs)\/([a-zA-Z0-9_.-]*)\/([a-zA-Z0-9_.-]*)$",
        value,
    )
    if match:
        embed_url = "https://www.youtube.com/embed/%s?rel=0" % (match.group(1))
        res = div_responsive_start + iframe1 + embed_url + iframe2 + div_responsive_end
        return res
    elif match2:
        embed_url = "https://player.vimeo.com/video/%s" % (match2.group(4))
        res = div_responsive_start + iframe1 + embed_url + iframe2 + div_responsive_end
        return res
    elif match3:
        embed_url = "https://player.twitch.tv/?channel=%s&autoplay=false" % (
            match3.group("channel")
        )
        res = div_responsive_start + iframe1 + embed_url + iframe2 + div_responsive_end
        return res
    elif match4:
        embed_url = "https://clips.twitch.tv/embed?clip=%s&autoplay=false" % (
            match4.group(3)
        )
        res = div_responsive_start + iframe1 + embed_url + iframe2 + div_responsive_end
        return res
    elif match5:
        embed_url = "https://media.giphy.com/media/%s/giphy.mp4" % (match5.group(5))
        res = (
            div_responsive_start
            + '<video class="embed-responsive-item" autoplay loop><source src="'
            + embed_url
            + '" type="video/mp4"></video>'
            + div_responsive_end
        )
        return res
    else:
        embed_url = '<h2 class="lead text-center">Link format not supported.</h2> <p class="text-center text-info">The developers have been notified of this error.</p>'
        res = nosupp + embed_url + orted
        return res
    return ""


youtube_embed_url.is_safe = True