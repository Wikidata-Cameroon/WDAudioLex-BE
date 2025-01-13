import flask
import mwoauth
import toml

config = toml.load("config.toml")
app = flask.Flask(__name__)
# Secret key for session management
app.secret_key = config["secret_key"]


@app.route("/login")
def login():
    """Initiate an OAuth login.

    Call the MediaWiki server to get request secrets and then redirect the
    user to the MediaWiki server to sign the request.
    """
    consumer_token = mwoauth.ConsumerToken(
        config['CONSUMER_KEY'], config['CONSUMER_SECRET'])
    try:
        redirect, request_token = mwoauth.initiate(
            config['OAUTH_MWURI'], consumer_token)
    except Exception:
        app.logger.exception('mwoauth.initiate failed')
        flask.flash(u'OAuth handshake failed.')
        flask.redirect(flask.url_for('index'))
    else:
        flask.session['request_token'] = request_token
        return flask.redirect(redirect)


@app.route("/callback")
def callback():
    """OAuth handshake callback."""
    request_token = flask.session.get('request_token')
    if 'request_token' not in flask.session:
        flask.flash('OAuth callback failed. Are cookies disabled?')
        return flask.redirect(flask.url_for('index'))

    consumer_token = mwoauth.ConsumerToken(
        config['CONSUMER_KEY'], config['CONSUMER_SECRET'])

    try:
        access_token = mwoauth.complete(
            config['OAUTH_MWURI'],
            consumer_token,
            request_token,
            flask.request.query_string)

        identity = mwoauth.identify(
            config['OAUTH_MWURI'], consumer_token, access_token)

    except Exception:
        app.logger.exception('OAuth autnetication failed')
        flask.flash(u'OAuth authentication failed.')

    return flask.redirect(flask.url_for('index'))


@app.route("/")
def index():
    return "Hellow World <a href='/login'><button>Login</button</a>"


if __name__ == "__main__":
    app.run(debug=True)
