from app import db
from app import login_manager
from sqlalchemy import func
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin