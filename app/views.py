from flask import render_template
from app import app, host, port, user, passwd, db
from app.helpers.database import con_db, query_db
from app.helpers.filters import format_currency
import jinja2
from flask import request, url_for


# To create a database connection, add the following
# within your view functions:
# con = con_db(host, port, user, passwd, db)


# ROUTING/VIEW FUNCTIONS
@app.route('/', methods=['GET'])
def index():
    # Create database connection
    con = con_db(host, port, user, passwd, db)
    # Add custom filter to jinja2 env
    jinja2.filters.FILTERS['format_currency'] = format_currency

    var_dict = {
        "home": request.args.get("home"),
        "year_built": request.args.get("year_built", '0'),
        "zip_code": request.args.get("zip_code", '0'),
        "list_price": request.args.get("list_price", '0'),
        "beds": request.args.get("beds", '0'),
        "baths": request.args.get("baths", '0'),
        "sqft": request.args.get("sqft", '0'),
        "dom": request.args.get("dom", '0'),
        "parking": request.args.get("parking", '0'),
        "prediction": request.args.get("prediction", '0'),
        "bike_score": request.args.get("bike_score", '0'),
        "transit_score": request.args.get("transit_score", '0'),
        "walk_score": request.args.get("walk_score", '0'),
        "order_by": request.args.get("order_by", "edu_index"),
        "sort": request.args.get("sort", "DESC")
    }

    # Query the database
    data = query_db(con, var_dict)

    # Add data to dictionary
    var_dict["data"] = data

    return render_template('index.html', settings=var_dict)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500




