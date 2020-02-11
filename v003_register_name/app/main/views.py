from flask import render_template, url_for, redirect

from . import main
from .forms import NameForm
from .. import db
from ..models import Name

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
    	name = Name(name=form.name.data)
    	db.session.add(name)
    	db.session.commit()
    	return redirect(url_for('main.index'))
    names = Name.query.all()
    return render_template('index.html', title='Welcome', form=form, names=names)