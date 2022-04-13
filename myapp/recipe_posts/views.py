#recipeposts/views 

from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import RecipePost
from myapp.recipe_posts.forms import RecipePostForm

recipe_posts = Blueprint('recipe_posts', __name__) # register this in __Init__ py 

# Create a recipe 

@recipe_posts.route('/create', methods=['GET', 'POST'])
@login_required
def create_recipe():
    form = RecipePostForm()
    if form.validate_on_submit():
        recipe_post = RecipePost(title=form.title.data, text=form.text.data, user_id=current_user.id)
        db.session.add(recipe_post)
        db.session.commit()
        flash('Recipe Created')
        print('Recipe post was created')
        return redirect(url_for('core.index'))
    return render_template('create_recipe.html', form=form)


# view a single post
@recipe_posts.route('/<int:recipe_post_id>') #make sure this is an integer 
def recipe_post(recipe_post_id):
    recipe_post = RecipePost.query.get_or_404(recipe_post_id) # this recipe post id is not a string - we are querying for an int 
    return render_template('recipe_post.html', title=recipe_post.title, date=recipe_post.date, post=recipe_post)


# update a post 

@recipe_posts.route('/<int:recipe_post_id>/update',methods=['GET','POST'])
@login_required
def update(recipe_post_id):
    recipe_post = RecipePost.query.get_or_404(recipe_post_id)

    if recipe_post.author != current_user:
        abort(403)

    form = RecipePostForm()


    if form.validate_on_submit():

        recipe_post.title = form.title.data
        recipe_post.text = form.text.data
        db.session.commit()
        flash('Recipe Updated')
        return redirect(url_for('recipe_posts.recipe_post',recipe_post_id=recipe_post.id))

    elif request.method == 'GET':
        form.title.data = recipe_post.title
        form.text.data = recipe_post.text

    return render_template('create_recipe.html',title='Updating',form=form)


# delete post 
@recipe_posts.route('/<int:recipe_post_id>/delete',methods=['GET','POST'])
@login_required
def delete_post(recipe_post_id):

    recipe_post = RecipePost.query.get_or_404(recipe_post_id)
    if recipe_post.author != current_user:
        abort(403)

    db.session.delete(recipe_post)
    db.session.commit()
    flash('Recipe Deleted')
    return redirect(url_for('core.index'))