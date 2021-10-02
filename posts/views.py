"""Post Views"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import datetime

posts = [
    {
        'title': 'Rust tutorial',
        'user': {
            'name': 'Hector Pulido',
            'picture': 'https://d1fdloi71mui9q.cloudfront.net/5GIpX9AKTqGK0313X4Ws_b44rwE97v1FauXh9'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://media.discordapp.net/attachments/508946744579457034/886405897746792448/aXov40V_460s.png',
    },
    {
        'title': 'Rust tutorial plus',
        'user': {
            'name': 'Hector Pulido',
            'picture': 'https://d1fdloi71mui9q.cloudfront.net/5GIpX9AKTqGK0313X4Ws_b44rwE97v1FauXh9'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://media.discordapp.net/attachments/508946744579457034/886405953598132224/5fb561395c7dc.png',
    },
    {
        'title': 'Rust tutorial',
        'user': {
            'name': 'Hector Pulido',
            'picture': 'https://d1fdloi71mui9q.cloudfront.net/5GIpX9AKTqGK0313X4Ws_b44rwE97v1FauXh9'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://media.discordapp.net/attachments/508946744579457034/886386325249458256/241822843_10227721530000845_1099378808684931821_n.png?width=503&height=632',
    }
]


@login_required
def list_posts(request):
    """List existing posts"""
    context = {
        'posts': posts
    }
    return render(request, 'posts/feed.html', context)
