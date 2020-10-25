from datetime import date

from flask import Blueprint
from flask import request, render_template, redirect, url_for, session

from better_profanity import profanity
from flask_wtf import FlaskForm
from wtforms import TextAreaField, HiddenField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

import CS235FlixSkeleton.adapters.repository as repo
import CS235FlixSkeleton.utilities.utilities as utilities
import CS235FlixSkeleton.news.services as services

from CS235FlixSkeleton.authentication.authentication import login_required


# Configure Blueprint.
news_blueprint = Blueprint(
    'news_bp', __name__)


@news_blueprint.route('/movies_by_page', methods=['GET'])
def movies_by_page():
    target_date = request.args.get('page')
    # Fetch the first and last articles in the series.
    first_movie = services.get_first_movie(repo.repo_instance)
    last_movie = services.get_last_movie(repo.repo_instance)

    if target_date is None:
        # No date query parameter, so return articles from day 1 of the series.
        target_date = first_movie['page']

    # Fetch article(s) for the target date. This call also returns the previous and next dates for articles immediately
    # before and after the target date.
    movies, previous_page, next_page = services.get_movies_by_page(target_date, repo.repo_instance)


    first_movie_url = None
    last_movie_url = None
    next_movie_url = None
    prev_movie_url = None

    if len(movies) > 0:
        # There's at least one article for the target date.
        if previous_page is not None:
            # There are articles on a previous date, so generate URLs for the 'previous' and 'first' navigation buttons.
            prev_movie_url = url_for('news_bp.movies_by_page', page=previous_page)
            first_movie_url = url_for('news_bp.movies_by_page', page=first_movie['page'])

        # There are articles on a subsequent date, so generate URLs for the 'next' and 'last' navigation buttons.
        if next_page is not None:
            next_movie_url = url_for('news_bp.movies_by_page', page=next_page)
            last_movie_url = url_for('news_bp.movies_by_page', page=last_movie['page'])

        # Generate the webpage to display the articles.
        return render_template(
            'news/articles.html',
            title='Movies',
            movies_title=target_date,
            movies=movies,
            first_movie_url=first_movie_url,
            last_movie_url=last_movie_url,
            prev_movie_url=prev_movie_url,
            next_movie_url=next_movie_url,
        )

    # No articles to show, so return the homepage.
    return redirect(url_for('home_bp.home'))


class ProfanityFree:
    def __init__(self, message=None):
        if not message:
            message = u'Field must not contain profanity'
        self.message = message

    def __call__(self, form, field):
        if profanity.contains_profanity(field.data):
            raise ValidationError(self.message)


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', [
        DataRequired(),
        Length(min=4, message='Your comment is too short'),
        ProfanityFree(message='Your comment must not contain profanity')])
    article_id = HiddenField("Article id")
    submit = SubmitField('Submit')