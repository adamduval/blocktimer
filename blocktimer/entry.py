from datetime import datetime
from operator import itemgetter

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.exceptions import abort

from blocktimer.auth import login_required
from blocktimer.db import get_db
from blocktimer.helpers import parse_time_block

bp = Blueprint('entry', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():

    #DEBUG
    print('/INDEX')

    # clear loaded timer if returning from timer home button
    if 'loaded_timer' in session:
        session.pop('loaded_timer')

    # Initialize session, ensure endpoint does not clear current stored timer
    if 'timer' not in session:

        #DEBUG
        print('INDEX: timer not in session')
        
        session['timer'] = []
        return render_template('blocktimer/index.html', timer=session['timer'])

    if request.method == 'POST':

        #DEBUG
        print('INDEX: post loop')

        input_time_block = request.form['time_block']
        error = None

        try:
            parsed_time_block = parse_time_block(input_time_block)
            print(parsed_time_block)
            if not parsed_time_block['name']:
                error = "Please enter time block name as well as time"
                flash(error)

        except ValueError:
            error = "Please use text number+m,+s or number+m/number+s  format"
            flash(error)

        if error is None:
            timer = session['timer']
            timer.append(parsed_time_block)
            session['timer'] = timer

        return redirect(url_for('index'))

    else:

        #DEBUG
        print('INDEX: non post loop')
        
        return render_template('blocktimer/index.html', timer=session['timer'])

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')


@bp.route('/logout')
@login_required
def logout():
    session.clear()
    return redirect(url_for('index'))


@bp.route('/load', methods=['GET', 'POST'])
@login_required
def load():    

    print('LOAD')

    if request.method=='GET':
        db = get_db()
            # get list of timer names and dates 0=name, 1=ts, 2=id
        timers = db.execute(
            'SELECT timer.timer_name, timer.created, timer.id FROM timer inner join user on timer.author_id=user.id').fetchall()
            
        return render_template('blocktimer/load.html', timers=timers)

    if request.method=='POST':
        
        print('POST')

        id = request.form['timer_id']
        
        # get time blocks
        db = get_db()
            # 0=block, 1=time, 2=num
        timer = db.execute(
            'SELECT time_block.block, time_block.time, time_block.block_num, timer.timer_name FROM time_block inner join timer on time_block.timer_id=timer.id').fetchall()

        timer_name = db.execute(
            'SELECT timer.timer_name FROM timer where id = ?',(id)).fetchone()[0]
        
        # sort by num and return list of {name:, time:} blocks
        timer_sort = sorted(timer, key=itemgetter(2))
        timer = []
        for block in timer_sort:
            timer.append({'name' : block[0], 'time' :block[1]})

        session['timer'].clear()
        session['timer'] = timer    

        print(timer)
        print(session['timer'])

        return render_template('blocktimer/index.html', timer=timer, timer_name=timer_name)

@bp.route('/save', methods=['GET', 'POST'])
@login_required
def save():

    if request.method=='GET':
        return render_template('blocktimer/save.html', timer=session['timer'])

    if request.method=='POST':
        db = get_db()
        timer_name = (request.form['timer_name'])
        timer = session['timer']
        id = session['user_id']
        error = None

        if not timer_name:
            error = 'Timer name is required'
        elif not timer:
            error = 'No timer to save'

        # save in timer table
        if error is None:
            try:

                # ts = datetime.now() - not needed handles in db
                
                db.execute(
                    'INSERT INTO timer (author_id, timer_name) VALUES (?,?)',
                    (id, timer_name),
                )
                db.commit()

            except db.IntegrityError:
                error = f"User {timer_name} is already used."

        else:
            print('t-save')
            return redirect(url_for("entry.save"))

        # save blocks in time block table

        try:
            # get timer id key
            timer_id = db.execute(
            'SELECT id FROM timer WHERE timer_name = ?', (timer_name,)).fetchone()[0] #TODO understand why:
        
        except db.IntegrityError:
            error = f"User {timer_id} does not exist."

        
        for i, block in  enumerate(session['timer']):
            block_num= i

            db.execute(
                    'INSERT INTO time_block (timer_id, block, time, block_num) VALUES (?,?,?,?)',
                    (timer_id, block['name'],block ['time'], block_num),
                )
            db.commit()

        return render_template('blocktimer/index.html', timer=session['timer'], name=timer_name)


@bp.route('/clear', methods=['GET', 'POST'])
def clear():    
    session.pop('timer')
    return redirect(url_for('index'))
