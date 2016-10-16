"""kinto_github_token - Github Authentication support for Kinto"""

__version__ = '0.1.0'
__author__ = 'Anh Trinh <anh.trinhtrung@gmail.com>'
__all__ = []

def includeme(config):
    print("I am the kinto_github_token plugin!")

    # Activate end-points.
    config.scan('kinto_github_token.views')
