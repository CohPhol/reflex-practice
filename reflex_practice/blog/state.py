import reflex as rx

from typing import Optional, List
from .model import BlogPost
from sqlmodel import select
from .model import BlogPost

class BlogPostState(rx.State):
    posts: List['BlogPost'] = []
    post: Optional['BlogPost'] = None
    post_content: str = ""

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
            self.post_content = result.content

    def list_entries(self):
        with rx.session() as session:
            posts = session.exec(
                select(BlogPost)
            ).all()
            self.posts = posts

    def create_post(self, form_data: dict):
        with rx.session() as session:
            post = BlogPost(**form_data)
            session.add(post)
            session.commit()
            session.refresh(post)
            self.post = post

    def edit_post(self, post_id:int, updated_data: dict):
        with rx.session() as session:
            post = session.exec(
                select(BlogPost).where(
                    BlogPost.id == self.blog_post_id
                )
            ).one_or_none()

            if post is None:
                return
            for key, value in updated_data.items():
                setattr(post, key, value)
            
            session.add(post)
            session.commit()
            session.refresh(post)
            post.title = updated_data.get()

class BlogCreateFormState(BlogPostState):
    form_data:dict = {}

    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        self.create_post(form_data)

class BlogEditFormState(BlogPostState):
    form_data: dict = {}
    content: str = ""
    
    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        post_id = form_data.pop('post_id')
        updated_data = {**form_data}
        # print(post_id, updated_data)
        self.edit_post(post_id, updated_data)