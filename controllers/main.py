from odoo import http
from odoo.http import request

class GestionMarchesController(http.Controller):

    @http.route(['/gestion_marches/templates'], type='http', auth="public", website=True)
    def recherche_marche(self, type_marche=None, **kwargs):
        # Rechercher les marchés par type
        domain = []
        if type_marche:
            domain = [('type_marche_id.name', 'ilike', type_marche)]
        
        marches = request.env['gestion_marches.marche'].sudo().search(domain)

        host = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        
        # Rendre la vue avec les résultats de recherche
        return request.render('gestion_marches.templates', {
            'marches': marches,
            'host': host


        })
    

    

   

    
    