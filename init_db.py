import sys
from app import create_app, db
from models import Region, WineType, Wine

def init_db():
    """Initialize the database with sample data"""
    app = create_app()
    with app.app_context():
        # Create tables
        db.create_all()
        
        # Check if data already exists
        if Region.query.first() is not None:
            print("Database already contains data. Skipping initialization.")
            return
            
        print("Initializing database with sample data...")
        
        # Add regions
        regions = [
            Region(name='Rioja', country='Spain', 
                  description='One of Spain\'s most renowned wine regions, known for its oak-aged red wines made primarily from Tempranillo.'),
            Region(name='Ribera del Duero', country='Spain',
                  description='Known for producing some of Spain\'s most prestigious red wines from Tempranillo grapes.'),
            Region(name='Priorat', country='Spain',
                  description='A small but prestigious wine region known for powerful red wines made from Garnacha and Cariñena.'),
            Region(name='Chianti', country='Italy',
                  description='Famous Tuscan wine region known for its Sangiovese-based red wines.'),
            Region(name='Piedmont', country='Italy',
                  description='Home to Italy\'s great Barolo and Barbaresco wines, made from the Nebbiolo grape.'),
            Region(name='Sicily', country='Italy',
                  description='The largest Mediterranean island with diverse terroir producing excellent wines from indigenous varieties.')
        ]
        db.session.add_all(regions)
        
        # Add wine types
        wine_types = [
            WineType(name='Red', description='Wines made from red grape varieties, with colors ranging from light ruby to deep purple-black.'),
            WineType(name='White', description='Wines made from green or yellow grape varieties, with colors ranging from pale straw to rich gold.'),
            WineType(name='Rosé', description='Wines with some color from red grape skins, but not enough to qualify as red wine.'),
            WineType(name='Sparkling', description='Wines with significant levels of carbon dioxide, making them fizzy.')
        ]
        db.session.add_all(wine_types)
        
        # Commit to get IDs
        db.session.commit()
        
        # Add sample wines
        wines = [
            Wine(
                name='Reserva Tempranillo', 
                producer='Bodegas Riojanas', 
                vintage=2018, 
                region_id=1,  # Rioja
                wine_type_id=1,  # Red
                description='A classic Rioja Reserva aged for 24 months in oak barrels followed by 12 months in bottle.',
                tasting_notes='Cherry, vanilla, leather, and spice notes with a smooth, elegant finish.',
                price_wholesale=22.50,
                minimum_order=6,
                featured=True,
                image_filename='rioja_reserva.jpg'
            ),
            Wine(
                name='Crianza Ribera', 
                producer='Viñedos del Duero', 
                vintage=2019, 
                region_id=2,  # Ribera del Duero
                wine_type_id=1,  # Red
                description='Aged for 12 months in American and French oak barrels.',
                tasting_notes='Blackberry and cherry flavors with hints of vanilla and toast.',
                price_wholesale=18.75,
                minimum_order=6,
                featured=True,
                image_filename='ribera_crianza.jpg'
            ),
            Wine(
                name='Chianti Classico Riserva', 
                producer='Castello di Toscana', 
                vintage=2017, 
                region_id=4,  # Chianti
                wine_type_id=1,  # Red
                description='A traditional Chianti Classico Riserva made primarily from Sangiovese.',
                tasting_notes='Sour cherry, earthy notes, and dried herbs with firm tannins.',
                price_wholesale=24.00,
                minimum_order=6,
                featured=True,
                image_filename='chianti_riserva.jpg'
            ),
            Wine(
                name='Etna Bianco', 
                producer='Vini Vulcanici', 
                vintage=2021, 
                region_id=6,  # Sicily
                wine_type_id=2,  # White
                description='Made from Carricante grapes grown on the slopes of Mount Etna.',
                tasting_notes='Citrus, green apple, and distinctive mineral notes with refreshing acidity.',
                price_wholesale=19.50,
                minimum_order=6,
                featured=True,
                image_filename='etna_bianco.jpg'
            ),
            Wine(
                name='Barolo', 
                producer='Antica Cantina', 
                vintage=2016, 
                region_id=5,  # Piedmont
                wine_type_id=1,  # Red
                description='A traditional Barolo made from 100% Nebbiolo grapes, aged for 3 years before release.',
                tasting_notes='Rose petals, tar, red cherries, and truffles with firm tannins.',
                price_wholesale=45.00,
                minimum_order=3,
                featured=False,
                image_filename='barolo.jpg'
            ),
            Wine(
                name='Priorat Garnacha Blend', 
                producer='Celler Antic', 
                vintage=2018, 
                region_id=3,  # Priorat
                wine_type_id=1,  # Red
                description='A powerful blend of Garnacha and Cariñena from old vines grown in Priorat\'s distinctive slate soils.',
                tasting_notes='Intense blackberry and plum with mineral notes and a long finish.',
                price_wholesale=32.00,
                minimum_order=6,
                featured=False,
                image_filename='priorat_blend.jpg'
            )
        ]
        db.session.add_all(wines)
        db.session.commit()
        
        print("Database initialized successfully!")

if __name__ == '__main__':
    init_db()