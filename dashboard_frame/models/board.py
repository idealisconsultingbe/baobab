from odoo import api, fields, models
from lxml import etree


class BoardFrame(models.TransientModel):
    _name = 'board.frame'

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super(BoardFrame, self).fields_view_get(view_id, view_type, toolbar, submenu)
        dashboard_view = self.env.ref('dashboard_frame.board_dash_views')
        if 'view_id' in res and res['view_id'] == dashboard_view.id:
            dashboard_url = self.env['ir.config_parameter'].sudo().get_param('dashboard.url')
            if dashboard_url:
                arch = etree.fromstring(res['arch'])
                for iframe in arch.xpath("//iframe"):
                    iframe.set("src", dashboard_url)
                res['arch'] = etree.tostring(arch, encoding='unicode')
        return res
