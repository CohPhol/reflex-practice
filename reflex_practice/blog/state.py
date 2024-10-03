import reflex as rx

from typing import Optional, List
from .model import BlogPost
from sqlmodel import select

class BlogPostState(rx.State):
    posts: List['BlogPost'] = []
    post: Optional['BlogPost'] = None

    def load_posts(self):
        with rx.session() as session:
            result = session.exec(
                select(BlogPost)
            ).all()
            self.posts = result

    # def get_post(self, post_id):
    #     with rx.session() as session:
    #         result = session.exec(
    #             select(BlogPost)
    #         )
    #         self.posts = result