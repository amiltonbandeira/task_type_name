from odoo import models, fields, api

class TypeTask(models.Model):
    _inherit="project.task"

    name_task = fields.Char(string="Task Name", compute='_compute_name_task)


    @api.depends('project_id')
    def _compute_name_task(self):
        if self.project_id:
            self.name_task = self.project_id.name else False
