from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    #if request.method == 'POST': 
     #   note = request.form.get('note')#Gets the note from the HTML 

 #       if len(note) < 1:
  #          flash('Note is too short!', category='error') 
   #     else:
    #        new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note  
     #       db.session.add(new_note) #adding the note to the database 
      #      db.session.commit()
       #     flash('Note added!', category='success')

    return render_template("dashboard.html", user=current_user)


