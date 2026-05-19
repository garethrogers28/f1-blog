from django import template

register = template.Library()


@register.filter
def cloudinary_transform(url, options):
    """
    Add Cloudinary transformations to an image URL.

    Usage:
        {{ post.featured_image.url|cloudinary_transform:"w_800,..." }}
    """
    if not url:
        return url
    url = str(url)
    # Ensure HTTPS
    if url.startswith('http://'):
        url = url.replace('http://', 'https://', 1)
    # Cloudinary URLs:
    # https://res.cloudinary.com/CLOUD/image/upload/v123/file.jpg
    # We insert transformations after /upload/
    if '/upload/' in url:
        return url.replace('/upload/', f'/upload/{options}/')
    return url
