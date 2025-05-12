import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, TelField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from config import Config
from models import db, Wine, Region, WineType, ContactRequest

csrf = CSRFProtect()

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    business_name = StringField('Business Name', validators=[DataRequired(), Length(max=200)])
    email = EmailField('Email', validators=[DataRequired(), Email(), Length(max=100)])
    phone = TelField('Phone Number', validators=[Length(max=20)])
    message = TextAreaField('Message', validators=[Length(max=1000)])
    submit = SubmitField('Send Request')

def create_app(test_config=None):
    """Create and configure the Flask application"""
    app = Flask(__name__)
    
    if test_config is None:
        app.config.from_object(Config)
    else:
        app.config.from_mapping(test_config)
        
    # Ensure upload folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # Initialize extensions
    db.init_app(app)
    csrf.init_app(app)
    
    @app.route('/')
    def index():
        featured_wines = Wine.query.filter_by(featured=True).limit(4).all()
        return render_template('index.html', featured_wines=featured_wines)
        
    @app.route('/products')
    def products():
        regions = Region.query.all()
        wine_types = WineType.query.all()
        
        # Filter parameters
        region_id = request.args.get('region', type=int)
        wine_type_id = request.args.get('type', type=int)
        
        query = Wine.query
        
        if region_id:
            query = query.filter_by(region_id=region_id)
        if wine_type_id:
            query = query.filter_by(wine_type_id=wine_type_id)
            
        wines = query.order_by(Wine.name).all()
        
        return render_template('products.html', 
                               wines=wines, 
                               regions=regions, 
                               wine_types=wine_types,
                               selected_region=region_id,
                               selected_type=wine_type_id)
    
    @app.route('/about')
    def about():
        return render_template('about.html')
        
    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        form = ContactForm()
        
        if form.validate_on_submit():
            contact_request = ContactRequest(
                name=form.name.data,
                business_name=form.business_name.data,
                email=form.email.data,
                phone=form.phone.data,
                message=form.message.data
            )
            db.session.add(contact_request)
            db.session.commit()
            
            flash('Thank you for your interest! We will contact you soon.', 'success')
            return redirect(url_for('contact'))
            
        return render_template('contact.html', form=form)
        
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404
        
    @app.errorhandler(500)
    def server_error(e):
        return render_template('500.html'), 500
        
    return app
    
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)