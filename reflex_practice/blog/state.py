import reflex as rx

from typing import Optional, List
from .model import BlogPost
from sqlmodel import select
from .model import BlogPost

class BlogPostState(rx.State):
    posts: List['BlogPost'] = []
    post: Optional['BlogPost'] = None

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        data = {}
        for key, value in form_data.items():
            if value == "" or value is None:
                continue
            data[key] = value
        with rx.session() as session:
            db_entry = BlogPost(**data)
            session.add(db_entry)
            session.commit()

    @rx.var
    def blog_post_id(self):
        # print(self.router.page.params)
        return self.router.page.params.get("blog_id", "")

    def get_post_detail(self):
        with rx.session() as session:
            if self.blog_post_id == "":
                self.post = None
                return
            result = session.exec(
                select(BlogPost).where(
                    BlogPost.id == self.blog_post_id
                )
            ).one_or_none()
            self.post = result

    def list_entries(self):
        with rx.session() as session:
            posts = session.exec(
                select(BlogPost)
            ).all()
            self.posts = posts
    # def get_post(self, post_id):
    #     with rx.session() as session:
    #         result = session.exec(
    #             select(BlogPost)
    #         )
    #         self.posts = result