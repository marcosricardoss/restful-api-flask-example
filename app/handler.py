from flask import jsonify

def register_handlers(app):

    @app.errorhandler(400)
    def handle_invalid_usage(error):        
        output = { "message": str(error) }
        res = jsonify(output)
        res.status_code = 404
        return res
    
    @app.errorhandler(404)
    def handle_invalid_usage(error):        
        output = { "message": str(error) }
        res = jsonify(output)
        res.status_code = 404
        return res           

    @app.errorhandler(TypeError)
    def handle_invalid_usage(error):        
        output = { "message": str(error) }
        res = jsonify(output)
        res.status_code = 400
        return res