from app.app import app
from app.routes import Routes

if __name__ == "__main__":
    website = Routes()
    
    for route in website.routes:
        app.add_url_rule(
            route,
            view_func = website.routes[route]['function'],
            methods   = website.routes[route]['methods']
        )

    app.run(**website.config)