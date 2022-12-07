from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for

bp = Blueprint('timer', __name__, url_prefix='/timer')


@bp.route('/timer', methods=('GET', 'POST'))
def timer():
    """Load the actual timer to display.

    Checks that a timer has been created.

    """

    # if timer not created, go back to index
    if not session['timer']:
        return redirect(url_for('index'))

    # if no timer loaded then load 
    if 'loaded_timer' not in session:
        session['loaded_timer'] = session['timer'].copy()

    # if timer is finished, remove loaded timer and go back to index
    if not (session['loaded_timer']):
        session.pop('loaded_timer')
        return redirect(url_for('index'))

    loaded_timer = session['loaded_timer'].copy()
    block = loaded_timer.pop(0)
    session['loaded_timer'] = loaded_timer.copy()

    return render_template('blocktimer/timer.html', block=block, timer=loaded_timer)

